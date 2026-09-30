"""Where things live in the corpus, and who may write them.

The single source of truth for corpus layout: the ingest API and the refresh
workflow import from here rather than keeping their own patterns. The ingest API
is the only writer of source documents; the agent has no write path.
"""

from __future__ import annotations

import re
from typing import Final

#: forms/{line}/{state}/{form}/{edition}.md
#: {state} is a USPS code or MS for multistate. {edition} is YYYY-MM.
FORM_PATH_RE: Final = re.compile(
    r"^forms/[A-Z]{2}/(?:[A-Z]{2}|MS)/[A-Z0-9][A-Z0-9 \-]*/\d{4}-\d{2}\.md$"
)

#: bulletins/{state}/{bulletin-id}.md
BULLETIN_PATH_RE: Final = re.compile(r"^bulletins/[A-Z]{2}/[a-z0-9][a-z0-9\-]*\.md$")

#: guidelines/{appetite|claims|authority}/{topic}.md
GUIDELINE_PATH_RE: Final = re.compile(
    r"^guidelines/(?:appetite|claims|authority)/[a-z0-9][a-z0-9\-]*\.md$"
)

#: manuals/{underwriting|rating|claims}/{name}.md, memoranda/{FORM}-{YYYY-MM}.md, training/{topic}.md
MANUAL_PATH_RE: Final = re.compile(r"^manuals/(?:underwriting|rating|claims)/[a-z0-9][a-z0-9\-]*\.md$")
MEMORANDUM_PATH_RE: Final = re.compile(r"^memoranda/[A-Z0-9][A-Z0-9\-]*-\d{4}-\d{2}\.md$")
TRAINING_PATH_RE: Final = re.compile(r"^training/[a-z0-9][a-z0-9\-]*\.md$")

#: The ingest API's write domain: the union of the source families.
CORPUS_PATH_RE: Final = re.compile(
    "|".join(f"(?:{r.pattern})" for r in (FORM_PATH_RE, BULLETIN_PATH_RE, GUIDELINE_PATH_RE,
                                          MANUAL_PATH_RE, MEMORANDUM_PATH_RE, TRAINING_PATH_RE))
)

SOURCE_PREFIXES: Final = ("forms/", "bulletins/", "guidelines/", "manuals/", "memoranda/", "training/")

#: Written only by the refresh workflow.
WORKFLOW_OWNED_PREFIXES: Final = ("openwiki/",)
WORKFLOW_OWNED_FILES: Final = (".compile-state.json",)

#: Written by people only.
HUMAN_OWNED_FILES: Final = ("openwiki/INSTRUCTIONS.md", ".openwikiignore")


class CorpusPathError(ValueError):
    """A path falls outside the caller's write domain."""


def validate_source_write(path: str) -> str:
    """`path` if the ingest API may write it, else raise. Rejects rather than normalises."""
    if path != path.strip() or path.startswith("/") or ".." in path.split("/"):
        raise CorpusPathError(f"path is not a clean repo-relative path: {path!r}")
    if path in HUMAN_OWNED_FILES:
        raise CorpusPathError(f"{path} is human-owned and must not be written by the API")
    if path in WORKFLOW_OWNED_FILES or path.startswith(WORKFLOW_OWNED_PREFIXES):
        raise CorpusPathError(f"{path} belongs to the refresh workflow, not the ingest API")
    if not CORPUS_PATH_RE.match(path):
        raise CorpusPathError(
            f"{path} matches no corpus convention. Expected one of:\n"
            "  forms/{line}/{state}/{form}/{YYYY-MM}.md\n"
            "  bulletins/{state}/{bulletin-id}.md\n"
            "  guidelines/{appetite|claims|authority}/{topic}.md"
        )
    return path


def is_form_path(path: str) -> bool:
    return bool(FORM_PATH_RE.match(path))


def parse_form_path(path: str) -> dict[str, str]:
    """Split a form path into its components. Assumes `is_form_path(path)`."""
    _, line, state, form, edition_md = path.split("/")
    return {"line": line, "state": state, "form": form, "edition": edition_md[:-3]}


def validate_is_text(content: str | bytes) -> str:
    """`content` as UTF-8 text, else raise: a .md file of PDF bytes would compile into nonsense claims."""
    if isinstance(content, bytes):
        if content[:5] == b"%PDF-":
            raise CorpusPathError("content is a PDF, not extracted text")
        try:
            content = content.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise CorpusPathError(f"content is not valid UTF-8: {exc}") from exc
    if "\x00" in content:
        raise CorpusPathError("content contains NUL bytes; extraction produced binary")
    if not content.strip():
        raise CorpusPathError("content is empty")
    return content


#: The marker the ingest API puts on a superseded edition. Changing the old file's
#: bytes is what makes OpenWiki revisit claims citing it. Also matches the bold form.
SUPERSEDED_MARKER_RE: Final = re.compile(r"^> (?:\*\*)?SUPERSEDED(?:\*\*)? by .+", re.M)


def supersession_marker(form: str, edition: str, effective: str) -> str:
    """The block inserted under the title of the replaced edition. It says the edition is still in force."""
    return (
        f"> SUPERSEDED by {form} edition {edition} for policies written on or after {effective}.\n"
        f"> This edition remains in force for policies written under it and governs the adjustment of any\n"
        f"> loss occurring under such a policy, regardless of when that loss is reported.\n"
    )


def is_superseded(content: str) -> bool:
    return bool(SUPERSEDED_MARKER_RE.search(content))


def mark_superseded(content: str, form: str, edition: str, effective: str) -> str:
    """`content` with the marker inserted after the title line. Idempotent; nothing else changes."""
    if is_superseded(content):
        return content
    lines = content.split("\n")
    title = _title_index(lines)
    if title is None:
        raise CorpusPathError("cannot mark superseded: no `# ` title line at the top of the document (after any front matter)")
    marker = supersession_marker(form, edition, effective).rstrip("\n")
    return "\n".join([*lines[: title + 1], "", marker, *lines[title + 1:]])


def _title_index(lines: list[str]) -> int | None:
    """The line index of the document's `# ` title: the first line, or the first after a YAML front-matter block."""
    i = 0
    if lines and lines[0].strip() == "---":
        close = next((j for j in range(1, len(lines)) if lines[j].strip() == "---"), None)
        if close is None:
            return None
        i = close + 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    return i if i < len(lines) and lines[i].startswith("# ") else None

