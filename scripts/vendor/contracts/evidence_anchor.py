"""Verifies an OpenWiki evidence anchor against the file as it is now. No model involved.

An anchor is "repo-lines-v1:sha256:<content hash>:<base64 JSON metadata>". Every
hash is sha256 of the lines joined with LF plus one trailing LF (an empty block
hashes to sha256("")). When the lines at the recorded range no longer hash, the
text may only have moved — as when a supersession marker is inserted above it —
so the verifier looks for the same block elsewhere, the way OpenWiki's resolver
does. Text that actually changed stays `content_changed`: that is staleness.
"""

from __future__ import annotations

import base64
import hashlib
import json
import re
from dataclasses import dataclass
from typing import Literal

RESOURCE_RE = re.compile(r"^repo://([^#]+)#L(\d+)-L(\d+)$")

#: As contracts/corpus_paths.py writes it (a test keeps the two in step). The one insertion
#: the corpus makes inside a document, so the one the verifier can see through.
SUPERSEDED_MARKER_RE = re.compile(r"^> (?:\*\*)?SUPERSEDED(?:\*\*)? by .+")

Verdict = Literal["clean", "content_changed", "range_missing", "unparseable"]


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def block_hash(lines: list[str]) -> str:
    """OpenWiki's formula: LF-joined plus a trailing LF; an empty block (a file boundary) is sha256("")."""
    if not lines:
        return _sha("")
    return _sha("\n".join(lines) + "\n")


@dataclass
class AnchorCheck:
    resource: str
    verdict: Verdict
    detail: str = ""
    #: The text is intact but its surroundings changed. Reported, not a failure.
    context_shifted: bool = False
    #: The text was found intact at other lines; `start`/`end` say where. Quote from there.
    relocated: bool = False
    #: Where the cited text is now, 1-based inclusive. None unless clean.
    start: int | None = None
    end: int | None = None
    #: The supersession marker sits inside the cited range; `start`..`end` include it.
    marker_inside: bool = False

    @property
    def ok(self) -> bool:
        return self.verdict == "clean"

    @property
    def lines(self) -> str | None:
        return f"L{self.start}-L{self.end}" if self.start and self.end else None


def parse_resource(resource: str) -> tuple[str, int, int] | None:
    """`repo://path#L12-L20` -> ("path", 12, 20), or None."""
    match = RESOURCE_RE.match(resource or "")
    if not match:
        return None
    return match.group(1), int(match.group(2)), int(match.group(3))


def verify_anchor(resource: str, version: str, file_lines: list[str]) -> AnchorCheck:
    """Check one evidence pointer against the file as it is now."""
    parsed = parse_resource(resource)
    if parsed is None:
        return AnchorCheck(resource, "unparseable", f"not a repo:// line range: {resource!r}")
    _, start, end = parsed

    try:
        kind, algo, content_hash, encoded = version.split(":", 3)
    except (ValueError, AttributeError):
        return AnchorCheck(resource, "unparseable", f"malformed anchor: {str(version)[:40]!r}")
    if kind != "repo-lines-v1" or algo != "sha256":
        return AnchorCheck(resource, "unparseable", f"unknown anchor scheme {kind}:{algo}")

    try:
        meta = json.loads(base64.b64decode(encoded + "=" * (-len(encoded) % 4)))
    except Exception as exc:  # noqa: BLE001 - every decode failure is one verdict
        return AnchorCheck(resource, "unparseable", f"metadata undecodable: {exc}")

    # The anchor, not the resource string, is authoritative about the block's length:
    # OpenWiki can re-anchor a longer block while keeping the old resource as the id.
    declared = int(meta.get("selectedLineCount") or 0)
    if declared > 0 and declared != end - start + 1:
        end = start + declared - 1
    in_range = 1 <= start <= end <= len(file_lines)
    if in_range and block_hash(file_lines[start - 1 : end]) == content_hash:
        if (start, end) != parsed[1:]:
            return AnchorCheck(
                resource,
                "clean",
                f"the anchor describes {declared} lines from L{start} (the resource says L{parsed[1]}-L{parsed[2]}); intact at L{start}-L{end}",
                context_shifted=_context_shifted(file_lines, start, end, meta),
                relocated=True,
                start=start,
                end=end,
            )
        # Intact where the pointer says. A shifted context is drift, not staleness.
        return AnchorCheck(resource, "clean", context_shifted=_context_shifted(file_lines, start, end, meta), start=start, end=end)

    found = relocate(file_lines, end - start + 1, content_hash, meta)
    if found is not None:
        new_start, new_end = found
        return AnchorCheck(
            resource,
            "clean",
            f"cited text moved from L{start}-L{end} to L{new_start}-L{new_end}; intact",
            context_shifted=_context_shifted(file_lines, new_start, new_end, meta),
            relocated=True,
            start=new_start,
            end=new_end,
        )

    # A supersession marker inserted inside the cited range leaves the text intact around it.
    marker = _marker_block(file_lines)
    if marker is not None:
        m_start, m_len = marker
        stripped = file_lines[:m_start] + file_lines[m_start + m_len :]
        span = None
        if 1 <= start <= end <= len(stripped) and block_hash(stripped[start - 1 : end]) == content_hash:
            span = (start, end)
        else:
            span = relocate(stripped, end - start + 1, content_hash, meta)
        if span is not None and span[0] - 1 < m_start <= span[1] - 1:
            new_start, new_end = span[0], span[1] + m_len
            return AnchorCheck(
                resource,
                "clean",
                f"the supersession marker was inserted inside L{start}-L{end}; the cited text is intact "
                f"around it at L{new_start}-L{new_end}",
                context_shifted=_context_shifted(stripped, span[0], span[1], meta),
                relocated=(new_start, new_end) != (start, end),
                start=new_start,
                end=new_end,
                marker_inside=True,
            )

    if not in_range:
        return AnchorCheck(
            resource,
            "range_missing",
            f"L{start}-L{end} is outside a {len(file_lines)}-line file, and the cited text is nowhere else in it",
        )
    selected = file_lines[start - 1 : end]
    return AnchorCheck(
        resource,
        "content_changed",
        f"L{start}-L{end} no longer hashes to the anchor "
        f"(expected {content_hash[:12]}, got {block_hash(selected)[:12]}), and the cited text is nowhere else in the file",
    )


def _marker_block(file_lines: list[str]) -> tuple[int, int] | None:
    """(start index, length) of the marker block mark_superseded inserts, blank line included; or None."""
    for i, line in enumerate(file_lines):
        if SUPERSEDED_MARKER_RE.match(line):
            end = i
            while end < len(file_lines) and file_lines[end].startswith("> "):
                end += 1
            start = i - 1 if i >= 2 and file_lines[i - 1] == "" and file_lines[i - 2].startswith("# ") else i
            return start, end - start
    return None


def _context_shifted(file_lines: list[str], start: int, end: int, meta: dict) -> bool:
    pre_n = int(meta.get("precedingContextLineCount", 0) or 0)
    post_n = int(meta.get("followingContextLineCount", 0) or 0)
    pre = file_lines[max(0, start - 1 - pre_n) : start - 1]
    post = file_lines[end : end + post_n]
    return (
        block_hash(pre) != meta.get("precedingContextHash")
        or block_hash(post) != meta.get("followingContextHash")
    )


def _context_matches(file_lines: list[str], start: int, end: int, meta: dict) -> bool:
    """OpenWiki's hasMatchingRangeContext: an empty context matches only at the file boundary."""
    pre_n = int(meta.get("precedingContextLineCount", 0) or 0)
    post_n = int(meta.get("followingContextLineCount", 0) or 0)
    if pre_n == 0:
        pre_ok = start == 1
    else:
        pre_ok = start - 1 >= pre_n and block_hash(file_lines[start - 1 - pre_n : start - 1]) == meta.get("precedingContextHash")
    if post_n == 0:
        post_ok = end == len(file_lines)
    else:
        post_ok = end + post_n <= len(file_lines) and block_hash(file_lines[end : end + post_n]) == meta.get("followingContextHash")
    return pre_ok and post_ok


def relocate(file_lines: list[str], length: int, content_hash: str, meta: dict) -> tuple[int, int] | None:
    """The cited block found intact elsewhere, as 1-based (start, end), or None.

    Mirrors OpenWiki's locateUnchangedLineRange: spans whose first and last line
    and content hashes match; several are narrowed by context; still ambiguous is None.
    """
    if length < 1 or length > len(file_lines):
        return None
    first_h = meta.get("firstSelectedLineHash")
    last_h = meta.get("lastSelectedLineHash")
    line_hashes = [block_hash([line]) for line in file_lines]
    matches: list[tuple[int, int]] = []
    for i in range(0, len(file_lines) - length + 1):
        if first_h and line_hashes[i] != first_h:
            continue
        if last_h and line_hashes[i + length - 1] != last_h:
            continue
        if block_hash(file_lines[i : i + length]) == content_hash:
            matches.append((i + 1, i + length))
    if len(matches) == 1:
        return matches[0]
    with_context = [m for m in matches if _context_matches(file_lines, m[0], m[1], meta)]
    return with_context[0] if len(with_context) == 1 else None
