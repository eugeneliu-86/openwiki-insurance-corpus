"""Deterministic verification of an OpenWiki relocation anchor. Contract C7/C11.

Every formula here was reverse-engineered against the live corpus rather than
read out of OpenWiki's source, and all 630 evidence pointers reproduce exactly:

    version = "repo-lines-v1:sha256:<content_hash>:<base64 json metadata>"

    content_hash          = sha256("\\n".join(selected_lines) + "\\n")
    firstSelectedLineHash = sha256(first_selected_line + "\\n")
    lastSelectedLineHash  = sha256(last_selected_line  + "\\n")
    precedingContextHash  = sha256("\\n".join(3 lines before) + "\\n")
    followingContextHash  = sha256("\\n".join(3 lines after)  + "\\n")

Note the trailing newline in every case — joining with LF alone does NOT
reproduce the hash, which is the one detail that makes this worth writing down.

This is the grounding check we can run ourselves, with no model involved.
OpenWiki's own preflight does more: it uses the line and context hashes to
RELOCATE text that moved, and that stays OpenWiki's job. What this gives is the
cheaper and more important half — does the cited text still say what the claim
was built on?
"""

from __future__ import annotations

import base64
import hashlib
import json
import re
from dataclasses import dataclass
from typing import Literal

RESOURCE_RE = re.compile(r"^repo://([^#]+)#L(\d+)-L(\d+)$")

Verdict = Literal["clean", "content_changed", "range_missing", "unparseable"]


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def block_hash(lines: list[str]) -> str:
    """OpenWiki's formula: join with LF, then append one trailing LF.

    An EMPTY block hashes to sha256("") — not sha256("\n"). This matters at
    file boundaries: a citation starting at line 1 has no preceding context, and
    OpenWiki records precedingContextLineCount 0 with the empty-string digest
    e3b0c442... Getting this wrong made 162 of 630 pointers (26%) report
    context_shifted, every one of them at a boundary and none of them real.
    """
    if not lines:
        return _sha("")
    return _sha("\n".join(lines) + "\n")


@dataclass
class AnchorCheck:
    resource: str
    verdict: Verdict
    detail: str = ""
    #: Selected text is intact but its surroundings changed, so the line numbers
    #: are drifting. Reported, deliberately NOT a failure — see verify_anchor.
    context_shifted: bool = False

    @property
    def ok(self) -> bool:
        return self.verdict == "clean"


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
        # Padding is stripped in the stored form; restore it before decoding.
        meta = json.loads(base64.b64decode(encoded + "=" * (-len(encoded) % 4)))
    except Exception as exc:  # noqa: BLE001 - every decode failure is one verdict
        return AnchorCheck(resource, "unparseable", f"metadata undecodable: {exc}")

    if start < 1 or end < start or end > len(file_lines):
        return AnchorCheck(
            resource,
            "range_missing",
            f"L{start}-L{end} is outside a {len(file_lines)}-line file",
        )

    selected = file_lines[start - 1 : end]
    if block_hash(selected) != content_hash:
        return AnchorCheck(
            resource,
            "content_changed",
            f"L{start}-L{end} no longer hashes to the anchor "
            f"(expected {content_hash[:12]}, got {block_hash(selected)[:12]})",
        )

    # Selected text intact. Context tells us whether it MOVED.
    #
    # A shift is not staleness. If the text still hashes, the claim is still
    # grounded in the language it was built on, even at new line numbers.
    # Treating a shift as a failure would flag every claim in any file where
    # someone added a heading — the exact false alarm relocation anchors exist
    # to prevent.
    pre_n = int(meta.get("precedingContextLineCount", 0) or 0)
    post_n = int(meta.get("followingContextLineCount", 0) or 0)
    pre = file_lines[max(0, start - 1 - pre_n) : start - 1]
    post = file_lines[end : end + post_n]
    shifted = (
        block_hash(pre) != meta.get("precedingContextHash")
        or block_hash(post) != meta.get("followingContextHash")
    )
    return AnchorCheck(resource, "clean", context_shifted=shifted)
