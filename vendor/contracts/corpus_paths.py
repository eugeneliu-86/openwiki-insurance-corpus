"""Corpus path conventions — enforces C2 and C5 of 00-contracts.md.

This module is the single source of truth for which paths exist in the corpus
and who may write them. The ingest API and the refresh workflow both import from
here. A component with its own regex is reimplementing one person's reading of
the contract, which is how the two drift.

Note on naming: `validate_source_write` is called by the ingest API, which is the
only writer of source documents. The agent has no write path at all (C5), so
there is deliberately no agent-facing write validator.
"""

from __future__ import annotations

import re
from typing import Final

# --- C2: layout ------------------------------------------------------------

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

#: Corpus expansion (docs/specs/corpus-expansion/00 §3): three more source
#: families. A manual is one long document per function; a memorandum
#: explains one form edition; training is carrier-authored interpretation.
#: {line} in FORM_PATH_RE was already any two capitals, so HO-5, HO-4, HO-6
#: and DP-3 needed nothing.
MANUAL_PATH_RE: Final = re.compile(r"^manuals/(?:underwriting|rating|claims)/[a-z0-9][a-z0-9\-]*\.md$")
MEMORANDUM_PATH_RE: Final = re.compile(r"^memoranda/[A-Z0-9][A-Z0-9\-]*-\d{4}-\d{2}\.md$")
TRAINING_PATH_RE: Final = re.compile(r"^training/[a-z0-9][a-z0-9\-]*\.md$")

#: C5: the ingest API's write domain is exactly the union of the source families.
CORPUS_PATH_RE: Final = re.compile(
    "|".join(f"(?:{r.pattern})" for r in (FORM_PATH_RE, BULLETIN_PATH_RE, GUIDELINE_PATH_RE,
                                          MANUAL_PATH_RE, MEMORANDUM_PATH_RE, TRAINING_PATH_RE))
)

#: The source-document prefixes, in one place. `variant.py`, `git_ops.py` and
#: `tools/corpus.py` import this rather than carrying their own tuple (C2: a
#: tool with its own list is reimplementing someone's reading of the contract).
SOURCE_PREFIXES: Final = ("forms/", "bulletins/", "guidelines/", "manuals/", "memoranda/", "training/")

#: C5: paths the refresh workflow owns. The agent may never write these.
WORKFLOW_OWNED_PREFIXES: Final = ("openwiki/",)
WORKFLOW_OWNED_FILES: Final = (".compile-state.json",)

#: C2: human-owned, never rewritten by either writer.
HUMAN_OWNED_FILES: Final = ("openwiki/INSTRUCTIONS.md", ".openwikiignore")


class CorpusPathError(ValueError):
    """A path falls outside the caller's write domain."""


def validate_source_write(path: str) -> str:
    """Return `path` if the ingest API may write it, else raise.

    Rejects rather than normalizes. A path the agent got wrong is a signal that
    the ingest metadata is wrong, and silently correcting it hides that.
    """
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


def validate_workflow_write(paths: list[str]) -> None:
    """Raise if the refresh workflow is about to commit outside its domain (C5)."""
    stray = [
        p
        for p in paths
        if not (p in WORKFLOW_OWNED_FILES or p.startswith(WORKFLOW_OWNED_PREFIXES))
        or p in HUMAN_OWNED_FILES
    ]
    if stray:
        raise CorpusPathError(f"refresh workflow would write outside its domain: {stray}")


def is_form_path(path: str) -> bool:
    return bool(FORM_PATH_RE.match(path))


def parse_form_path(path: str) -> dict[str, str]:
    """Split a form path into its components. Assumes `is_form_path(path)`."""
    _, line, state, form, edition_md = path.split("/")
    return {"line": line, "state": state, "form": form, "edition": edition_md[:-3]}


def validate_is_text(content: str | bytes) -> str:
    """Return `content` decoded as UTF-8 text, else raise (C8).

    Path shape alone is not enough: a file named `2022-03.md` containing raw PDF
    bytes satisfies every path rule we have, and OpenWiki would compile grounded
    claims against binary garbage. This is the only thing standing between a
    failed extraction and a wiki that certifies nonsense.
    """
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


# --- C5: supersession is an explicit act ----------------------------------

#: The marker the ingest API prepends to a superseded edition. One spelling,
#: because three things read it: OpenWiki (via the corpus brief), the agent's
#: policy-assembly skill, and the UI. It is what makes the old file's BYTES
#: change, which is the only signal OpenWiki acts on — a new edition alone
#: leaves every claim citing the old one clean.
#: Accepts the corpus's hand-written spelling ("> SUPERSEDED by") and the
#: bold form an earlier contract draft used. A detector that missed the existing
#: marker on HO-3 2011-05 would let the API stack a second one onto an
#: already-superseded edition.
SUPERSEDED_MARKER_RE: Final = re.compile(r"^> (?:\*\*)?SUPERSEDED(?:\*\*)? by .+", re.M)


def supersession_marker(form: str, edition: str, effective: str) -> str:
    """The block prepended under the title of the edition being replaced.

    Spelled exactly as the marker already present on forms/HO/MS/HO-3/2011-05.md,
    which OpenWiki compiled against and the corpus brief describes. The wording
    matters: the second line is what tells a reader — and the policy-assembly
    skill — that a superseded edition is still live knowledge.
    """
    return (
        f"> SUPERSEDED by {form} edition {edition} for policies written on or after {effective}.\n"
        f"> This edition remains in force for policies written under it and governs the adjustment of any\n"
        f"> loss occurring under such a policy, regardless of when that loss is reported.\n"
    )


def is_superseded(content: str) -> bool:
    return bool(SUPERSEDED_MARKER_RE.search(content))


def mark_superseded(content: str, form: str, edition: str, effective: str) -> str:
    """Return `content` with the marker inserted directly after the title line.

    Idempotent: a file already carrying a marker is returned unchanged, so a
    retried confirm cannot stack two markers and change the bytes twice.
    Everything else in the file is untouched — no operative text, no section
    numbering, no whitespace elsewhere — so relocation anchors below the
    insertion survive and only the header lines shift.
    """
    if is_superseded(content):
        return content
    lines = content.split("\n")
    if not lines or not lines[0].startswith("# "):
        raise CorpusPathError("cannot mark superseded: the document does not start with a title line")
    marker = supersession_marker(form, edition, effective).rstrip("\n")
    return "\n".join([lines[0], "", marker, *lines[1:]])


# Deprecated alias kept so an early draft importing the old name fails loudly
# rather than silently validating nothing.
def validate_agent_write(path: str) -> str:  # noqa: D103
    raise CorpusPathError(
        "validate_agent_write no longer exists: the agent has no write path (C5). "
        "The ingest API calls validate_source_write instead."
    )
