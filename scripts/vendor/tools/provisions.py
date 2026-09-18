"""The provision layer — graph-expansion phase 01, tier 1.

Every numbered paragraph of every source document is an addressable unit:
document path, section, paragraph id, line range, and a hash of its text. No
model is involved, so the layer covers 100% of the source and nothing in it can
be stale: a provision is the source at the pinned commit.

Two callers share one parser. The refresh workflow commits the index per commit
(`.provisions-index.json`, built by the vendored copy of this module); the agent
reads that file when it exists and otherwise builds the same index in memory
from the corpus it already holds — the two are identical bytes, and a test pins
that. `provisions_for` is the pure core the tool and the evaluator both call, so
an evaluator recomputing "what did expand_section return" cannot disagree with
the tool.

Layout awareness: on `pdf-text` documents (corpus-expansion ph. 05 E1) a
paragraph is wrapped over several lines and a page header/footer may cut
through it. The parser rejoins the paragraph and drops the header/footer lines,
so a provision on those documents is one unit with a multi-line range.
"""

from __future__ import annotations

import hashlib
import json
import re
from typing import Any, Callable

try:
    from langchain.tools import tool
    from langchain_core.tools import ToolException
except ImportError:  # the vendored copy runs in the corpus workflow on stdlib Python: parser and index only
    tool = None

    class ToolException(Exception):  # type: ignore[no-redef]
        pass

from contracts.corpus_paths import SOURCE_PREFIXES

SCHEMA_VERSION = 1
FRONT_MATTER_LINES = 12
WINDOW = 12   # provisions per expand_section call

#: `**B.2**`, `**W.14**`, `**DEF.11**`, `**B.2.6**`, `**L.3.1**`, `**110.A**`, `**4.AB**`, `**210.A.2**`,
#: and the manuals' `**510.1**` / `**8.2**` (graph-expansion ph. 02: 384 numbered paragraphs the ph. 01 pattern missed)
OPENER = re.compile(r"^\*\*([A-Z]{1,3}(?:\.\d+)+|[A-Z]+\.\d+(?:\.\d+)*|\d{1,3}\.[A-Z]{1,2}(?:\.\d+)?|\d{1,3}\.\d{1,2})\*\*")
HEADING = re.compile(r"^## (.+?)(?: — (.*))?$")
SUBHEADING = re.compile(r"^###+ (.+?)\s*$")   # a sub-heading inside a section (the hand-written corpus's "### A. Coverage A")
HEADER_RE = re.compile(r"^\S.* · Page \d+ of \d+$")
FOOTER_RE = re.compile(r"^© \d{4} .*permission\.$")
TABLE_ROW = re.compile(r"^\|")
TABLE_SEP = re.compile(r"^\|\s*:?-+")
CORPUS_PREFIXES = ("/workspace/corpus/", "repo://")


def normalize_document(path: str) -> str:
    p = (path or "").strip()
    for pre in CORPUS_PREFIXES:
        if p.startswith(pre):
            p = p[len(pre):]
            break
    return p.split("#")[0].strip("/")


def is_source(path: str) -> bool:
    return path.startswith(SOURCE_PREFIXES) and path.endswith(".md")


def _section_key(heading_id: str) -> str:
    """'Rule 110' -> 'Rule 110'; kept as written, matched loosely by `_match_section`."""
    return heading_id.strip()


def _compact(section_id: str) -> str:
    """'Table 2' -> 'T2'; 'Rule 110' -> 'R110'; 'I.E' -> 'I.E' — the table-row id prefix."""
    m = re.match(r"^(Table|Rule|Chapter|Part) (\d+)$", section_id)
    return (m.group(1)[0] + m.group(2)) if m else section_id


def parse_document(path: str, lines: list[str]) -> tuple[list[dict], list[dict]]:
    """(provisions, sections) for one file. Pure."""
    pdf = any(HEADER_RE.match(l) for l in lines[FRONT_MATTER_LINES:FRONT_MATTER_LINES + 8])
    provisions: list[dict] = []
    sections: list[dict] = []
    cur: dict | None = None
    sec_id, sec_title, sec_start = "", "", FRONT_MATTER_LINES + 1
    sub = ""
    unnumbered = 0
    table_rows = 0
    in_table_header = False

    def close(end: int) -> None:
        nonlocal cur
        if cur is not None:
            cur["end"] = end
            text = [l for l in lines[cur["start"] - 1:end] if not (pdf and (HEADER_RE.match(l) or FOOTER_RE.match(l)))]
            cur["content_hash"] = hashlib.sha256(("\n".join(text) + "\n").encode()).hexdigest()
            provisions.append(cur)
            cur = None

    def close_section(end: int) -> None:
        if sec_id:
            sections.append({"id": sec_id, "title": sec_title, "start": sec_start, "end": end,
                             "provisions": sum(1 for p in provisions if p["section"] == sec_id)})

    last_nonblank = FRONT_MATTER_LINES
    for i, raw in enumerate(lines[FRONT_MATTER_LINES:], start=FRONT_MATTER_LINES + 1):
        line = raw.rstrip("\n")
        if pdf and (HEADER_RE.match(line) or FOOTER_RE.match(line)):
            continue   # a page boundary is not a paragraph boundary
        m = HEADING.match(line)
        if m:
            close(last_nonblank); close_section(i - 1)
            sec_id, sec_title, sec_start = _section_key(m.group(1)), (m.group(2) or "").strip(), i
            sub = ""; unnumbered = 0; table_rows = 0; in_table_header = False
            last_nonblank = i
            continue
        sm = SUBHEADING.match(line)
        if sm:
            close(last_nonblank)
            sub = sm.group(1).split(".")[0].split(" ")[0]   # "A. Coverage A — Dwelling" -> "A"
            last_nonblank = i
            continue
        if not line.strip():
            close(last_nonblank)
            in_table_header = False
            continue
        last_nonblank = i
        if TABLE_ROW.match(line):
            close(i - 1)
            if TABLE_SEP.match(line):
                in_table_header = False
                continue
            if table_rows == 0 and not in_table_header and (i + 1 <= len(lines) and TABLE_SEP.match(lines[i])):
                in_table_header = True   # the header row: the next line is the separator
                continue
            table_rows += 1
            pid = f"{_compact(sec_id)}.r{table_rows}"
            provisions.append({"id": f"{path}#{pid}", "document": path, "section": sec_id, "paragraph": pid, "start": i, "end": i,
                               "content_hash": hashlib.sha256((line + "\n").encode()).hexdigest(), "kind": "row"})
            continue
        om = OPENER.match(line)
        if om:
            close(i - 1)
            pid = om.group(1)
            cur = {"id": f"{path}#{pid}", "document": path, "section": sec_id, "paragraph": pid, "start": i, "end": i, "kind": "provision", "sub": sub}
            continue
        if cur is None:
            unnumbered += 1
            pid = f"{sec_id}.p{unnumbered}" if sec_id else f"p{unnumbered}"
            cur = {"id": f"{path}#{pid}", "document": path, "section": sec_id, "paragraph": pid, "start": i, "end": i, "kind": "paragraph"}
        # a continuation line (soft break, wrapped line, sub-item) extends the open unit
    close(last_nonblank); close_section(len(lines))

    # ids unique within the document. A repeated paragraph id is prefixed with its
    # sub-heading when there is one, else its section; a residual repeat gets an
    # ordinal. The generated corpus never repeats; the hand-written one does.
    def dedupe(key) -> None:
        counts: dict[str, int] = {}
        for p in provisions:
            counts[p["paragraph"]] = counts.get(p["paragraph"], 0) + 1
        for p in provisions:
            if counts[p["paragraph"]] > 1:
                p["paragraph"] = key(p)
    dedupe(lambda p: f"{p['sub']}/{p['paragraph']}" if p.get("sub") else f"{p['section']}/{p['paragraph']}")
    dedupe(lambda p: f"{p['section']}/{p['paragraph']}" if not p["paragraph"].startswith(p["section"] + "/") else p["paragraph"])
    seen: dict[str, int] = {}
    for p in provisions:
        seen[p["paragraph"]] = seen.get(p["paragraph"], 0) + 1
        if seen[p["paragraph"]] > 1:
            p["paragraph"] = f"{p['paragraph']}~{seen[p['paragraph']]}"
    for p in provisions:
        p["id"] = f"{path}#{p['paragraph']}"
        p["layout"] = "pdf-text" if pdf else "single-line"
        p.pop("sub", None)
    assert len({p["id"] for p in provisions}) == len(provisions)
    return provisions, sections


def build_provisions_index(corpus, sha: str) -> dict[str, Any]:
    """The whole index for a corpus at `sha`. Pure over the corpus reader."""
    provisions: list[dict] = []
    sections: dict[str, list[dict]] = {}
    for path in sorted(corpus.paths(suffix=".md")):
        if not is_source(path):
            continue
        p, s = parse_document(path, corpus.lines(path))
        provisions += p
        sections[path] = s
    return {"schema_version": SCHEMA_VERSION, "corpus_sha": sha, "provisions": provisions, "sections": sections}


def dumps(index: dict[str, Any]) -> str:
    return json.dumps(index, indent=1, sort_keys=False, ensure_ascii=False) + "\n"


# --- lookups -----------------------------------------------------------------------
def _match_section(index: dict, document: str, section: str | None, line: int | None) -> dict | None:
    secs = index["sections"].get(document) or []
    if line is not None:
        return next((s for s in secs if s["start"] <= line <= s["end"]), None)
    if not section:
        return None
    want = section.strip()
    norm = lambda s: re.sub(r"[^a-z0-9.]", "", s.lower())
    for s in secs:
        if s["id"] == want or norm(s["id"]) == norm(want) or norm(_compact(s["id"])) == norm(want):
            return s
    for s in secs:   # 'R110' / '110' for 'Rule 110'; a heading-title fragment
        if norm(want) in (norm(s["id"]), norm(_compact(s["id"]))) or (len(want) >= 5 and want.lower() in s["title"].lower()):
            return s
    m = re.fullmatch(r"[A-Za-z]?(\d{1,3})", want)
    if m:
        return next((s for s in secs if re.fullmatch(rf"(Rule|Chapter|Part|Table) {m.group(1)}", s["id"])), None)
    return None


def section_of(index: dict, document: str, line: int) -> str | None:
    s = _match_section(index, normalize_document(document), None, line)
    return s["id"] if s else None


def text_of(corpus, p: dict) -> str:
    lines = corpus.lines(p["document"])[p["start"] - 1:p["end"]]
    if p.get("layout") == "pdf-text":
        lines = [l for l in lines if not (HEADER_RE.match(l) or FOOTER_RE.match(l))]
    return "\n".join(l.rstrip() for l in lines).strip()


def provisions_for(index: dict, corpus, document: str, section: str | None = None, paragraph: str | None = None,
                   offset: int = 0, limit: int = WINDOW) -> dict[str, Any]:
    """One section's provisions, verbatim, in document order, windowed. Pure.

    Raises ToolException for a document outside the source prefixes or a section
    that cannot be resolved, naming the sections the document does have."""
    doc = normalize_document(document)
    if not is_source(doc):
        raise ToolException(f"{document!r} is not a source document; expand_section reads under {', '.join(SOURCE_PREFIXES)}")
    if doc not in index["sections"]:
        raise ToolException(f"{doc} is not in the corpus at this commit")
    if offset < 0:
        raise ToolException(f"offset must be 0 or more, got {offset!r}")
    by_doc = [p for p in index["provisions"] if p["document"] == doc]
    if paragraph:
        want = paragraph.strip().strip("*")
        hits = [p for p in by_doc if p["paragraph"] == want or p["paragraph"].endswith("/" + want)]
        if not hits:
            raise ToolException(f"{doc} has no paragraph {paragraph!r}")
        sec = _match_section(index, doc, None, hits[0]["start"])
        items = hits
    else:
        line = None
        if section and re.fullmatch(r"L?\d+", section.strip()):
            line = int(section.strip().lstrip("L")); section = None
        sec = _match_section(index, doc, section, line)
        if sec is None:
            have = ", ".join(s["id"] for s in index["sections"][doc][:40])
            raise ToolException(f"{doc}: cannot resolve section {section!r}. Sections: {have}")
        items = [p for p in by_doc if p["section"] == sec["id"]]
    total = len(items)
    window = items[offset:offset + limit]
    out = [{"id": p["id"], "paragraph": p["paragraph"], "start": p["start"], "end": p["end"], "text": text_of(corpus, p)} for p in window]
    truncated = total > offset + limit
    note = (f"Provisions {offset + 1}-{offset + len(out)} of {total} in {doc} § {sec['id'] if sec else '?'}"
            + (f" — {sec['title']}" if sec and sec.get("title") else "") + ". Verbatim source text. "
            "To cite one, put its id in the citation's `resource` and leave `quote` empty: the pointer and quote are filled in after you answer. "
            + (f"More: call again with offset={offset + limit}." if truncated else ""))
    return {"document": doc, "section": ({"id": sec["id"], "title": sec["title"], "start": sec["start"], "end": sec["end"], "provisions": total} if sec else None),
            "provisions": out, "count": total, "next_offset": (offset + limit) if truncated else None, "note": note}


# --- the agent's copy of the index -------------------------------------------------
_INDEXES: dict[str, dict] = {}
INDEX_SOURCE: dict[str, str] = {}


async def ensure_provisions(sha: str, blobs: dict[str, str] | None = None) -> dict[str, Any]:
    """The committed `.provisions-index.json` at `sha` when it exists and matches;
    otherwise the same index built here from the local corpus."""
    idx = _INDEXES.get(sha)
    if idx is None:
        from tools.corpus_local import ensure_local_corpus

        corpus = await ensure_local_corpus(sha, blobs)
        try:
            idx = json.loads("\n".join(corpus.lines(".provisions-index.json")))
            if idx.get("schema_version") != SCHEMA_VERSION or not matches_tree(idx, corpus):
                raise ValueError("provisions index does not describe this tree")
            INDEX_SOURCE[sha] = "committed"
        except (FileNotFoundError, ValueError, json.JSONDecodeError):
            idx = build_provisions_index(corpus, sha)
            INDEX_SOURCE[sha] = "built"
        _INDEXES[sha] = idx
    return idx


def matches_tree(index: dict, corpus, sample: int = 64) -> bool:
    """Does the committed index describe this tree? The workflow builds the index at
    the source commit and commits it with the wiki, so its `corpus_sha` is always one
    commit behind the SHA the agent pins; the SHA is not the test. The test is the
    content: every source document accounted for, and a deterministic sample of
    provisions (first, last and evenly spaced) whose text still hashes as recorded."""
    ps = index.get("provisions") or []
    docs = {p for p in corpus.paths(suffix=".md") if is_source(p)}
    if set(index.get("sections") or {}) != docs or not ps:
        return False
    step = max(1, len(ps) // sample)
    for p in ps[::step] + [ps[-1]]:
        try:
            lines = corpus.lines(p["document"])
        except FileNotFoundError:
            return False
        if p["end"] > len(lines):
            return False
        text = lines[p["start"] - 1:p["end"]]
        if p.get("layout") == "pdf-text":
            text = [l for l in text if not (HEADER_RE.match(l) or FOOTER_RE.match(l))]
        if hashlib.sha256(("\n".join(text) + "\n").encode()).hexdigest() != p["content_hash"]:
            return False
    return True


def by_id(index: dict, provision_id: str) -> dict | None:
    return next((p for p in index["provisions"] if p["id"] == provision_id), None)


def is_provision_id(resource: str) -> bool:
    return isinstance(resource, str) and "#" in resource and not resource.startswith(("repo://", "claim_")) and is_source(resource.split("#")[0])


async def _expand_section(document: str, section: str | None = None, paragraph: str | None = None, offset: int = 0) -> dict:
    """Read one section of a source document as its numbered provisions,
    verbatim, each with an id you can cite — without reading the whole file.

    Use it when a claim's window does not carry the fact you need: a claim tells
    you the document and section it rests on; this returns everything that
    section says, in order, twelve provisions at a time.

    To cite a provision, put its id (e.g. forms/HO/MS/HO-04-90/2027-01.md#W.2)
    in the citation's `resource` and leave `quote` empty; the line pointer and
    verbatim quote are filled in from the index after you answer.

    Args:
        document: The source document, as a path (forms/HO/MS/HO-3/2024-03.md), a
            repo:// pointer, or the /workspace/corpus/... path grep showed you.
        section: A section id (W.2, I.E, B.3), a manual rule (Rule 110 or 110), a
            heading fragment, or a line number inside the section. Omit when
            passing `paragraph`.
        paragraph: One paragraph id (W.14, 110.A, DEF.11) to fetch just that provision.
        offset: Provisions to skip; pass the `next_offset` a previous call returned.
    """
    from tools.claims import _pinned
    from tools.corpus_local import ensure_local_corpus

    sha, blobs = _pinned()
    index = await ensure_provisions(sha, blobs)
    corpus = await ensure_local_corpus(sha, blobs)
    return {"corpus_sha": sha, **provisions_for(index, corpus, document, section, paragraph, offset)}


#: The agent's tool; absent when langchain is not installed (the vendored copy).
expand_section = tool("expand_section", parse_docstring=True)(_expand_section) if tool is not None else None


def section_lookup(index: dict) -> Callable[[str, int], str | None]:
    """A (document, line) -> section id function for the traversal's compact claims."""
    return lambda document, line: section_of(index, document, line)
