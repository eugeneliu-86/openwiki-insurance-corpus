"""Sections -> documents; slots -> values; placements. Ph. 02 §3–§4.

Numbering is code so references resolve and renumberings are exact. Front
matter is exactly FRONT_MATTER_LINES lines so the loader's depth arithmetic
and the assembled file agree about where section one begins. Every slot fill
records the line it landed on, and that record is `placements.json`.
"""
from __future__ import annotations

import json
import pathlib
import re

import _paths  # noqa: F401
from ledger.schema import FRONT_MATTER_LINES, Document, Ledger

from .plan import SectionJob, jobs_for
from .render import render_reference, render_value, value_occurrences
from .tables import table_for

MARKER = re.compile(r"\{\{(fact|def|contra|ref):([^}]+)\}\}")

# ph. 05 E1 — `pdf-text` layout: the text a PDF extractor produces. Wrapped at
# WRAP columns, sub-items on their own lines, a running header and footer every
# PAGE lines. Applied to the assembled single-line document, so drafts and the
# marker-recording pass are untouched; placements are re-mapped to the new lines.
WRAP = 88
PAGE = 55
SUBITEM = re.compile(r"\s(?=(?:[a-z]\.|\(\d{1,2}\)|\([ivx]+\))\s)")
HEADER_RE = re.compile(r"^\S.* · Page \d+ of \d+$")
FOOTER_RE = re.compile(r"^© \d{4} .*permission\.$")


def form_code(doc: Document) -> str:
    parts = doc.path.split("/")
    if doc.type in ("form", "endorsement", "amendatory") and len(parts) >= 5:
        return parts[3]
    return doc.title.split(" — ")[0][:40]


_GLUE = "\ue000"   # private-use stand-in for a space inside a rendered value while wrapping


def wrap_paragraph(text: str, protect: tuple[str, ...] = ()) -> list[str]:
    """One assembled paragraph -> the lines a PDF extractor would give. Phrases in
    `protect` (the document's rendered values) are never split across lines: a
    citation and its anchor need the value on one line."""
    import textwrap
    if not text.strip() or text.startswith(("#", "|", ">", "---")):
        return [text]
    for phrase in sorted(protect, key=len, reverse=True):
        if " " in phrase and phrase in text:
            text = text.replace(phrase, phrase.replace(" ", _GLUE))
    parts = SUBITEM.split(text)
    if len(parts) < 3:
        parts = [text]
    out: list[str] = []
    for i, part in enumerate(parts):
        indent = "  " if i else ""
        out += textwrap.wrap(part.strip(), width=WRAP - len(indent), break_long_words=False, break_on_hyphens=False,
                             initial_indent=indent, subsequent_indent=indent) or [indent.rstrip()]
    return [l.replace(_GLUE, " ") for l in out]


def pdf_text_layout(ledger: Ledger, doc: Document, lines: list[str], placements: dict[str, dict]) -> tuple[list[str], dict[str, dict]]:
    """Re-lay `lines` (single-line assembly) as pdf-text; re-map `placements`
    (which point at single-line numbers) to paragraph ranges and a `value_line`."""
    fm, body = lines[:FRONT_MATTER_LINES], lines[FRONT_MATTER_LINES:]
    protect = tuple(v for k, v in renderings_for(ledger, doc).items() if not k.startswith("ref:"))
    # 1. wrap, remembering old line -> new (start, end) relative to the body
    wrapped: list[str] = []
    span: dict[int, tuple[int, int]] = {}
    for i, raw in enumerate(body, start=FRONT_MATTER_LINES + 1):
        new = wrap_paragraph(raw, protect)
        span[i] = (len(wrapped), len(wrapped) + len(new) - 1)
        wrapped += new
    # 2. paginate: a header opens and a footer closes every PAGE lines of the body
    code = form_code(doc)
    edition = doc.edition or doc.effective or ""
    year = (doc.effective or doc.edition or "2024")[:4]
    footer = f"© {year} Sample Mutual Insurance Company. Includes copyrighted material of Insurance Services Office, Inc., with its permission."
    per_page = PAGE - 2
    n_pages = max(1, -(-len(wrapped) // per_page))
    paged: list[str] = []
    pos: dict[int, int] = {}   # wrapped index -> final body index
    for page in range(n_pages):
        paged.append(f"{code}" + (f" · Edition {edition}" if edition else "") + f" · Page {page + 1} of {n_pages}")
        chunk = wrapped[page * per_page:(page + 1) * per_page]
        for j, l in enumerate(chunk):
            pos[page * per_page + j] = len(paged)
            paged.append(l)
        paged.append(footer)
    final = fm + paged
    # 3. placements: old single line -> the paragraph's new range and the line carrying the value
    facts = {f.id: f for f in ledger.facts}
    contras = {c.id: c for c in ledger.contradictions}
    remapped: dict[str, dict] = {}
    for key, pl in placements.items():
        if pl["path"] != doc.path:
            remapped[key] = pl; continue
        a, b = span[pl["line_start"]]
        start, end = FRONT_MATTER_LINES + pos[a] + 1, FRONT_MATTER_LINES + pos[b] + 1
        value_line = start
        val = facts[key].value if key in facts else (contras[key].wrong_value if key in contras else None)
        if val is not None:
            for ln in range(start, end + 1):
                if value_occurrences(final[ln - 1], val):
                    value_line = ln; break
        remapped[key] = {**pl, "line_start": start, "line_end": end, "value_line": value_line}
    return final, remapped


def front_matter(ledger: Ledger, doc: Document) -> list[str]:
    fm = ["---", f"type: {doc.type}", f'title: "{doc.title}"']
    if doc.line:
        fm.append(f"line: {doc.line}")
    if doc.state:
        fm.append(f"state: {doc.state}")
    if doc.edition:
        fm.append(f"edition: {doc.edition}")
    if doc.effective:
        fm.append(f"effective: {doc.effective}")
    fm.append("---")
    fm.append(f"# {doc.title}")
    if doc.superseded_by:
        sup = ledger.doc(doc.superseded_by)
        fm.append(f"> SUPERSEDED by {sup.title} for policies effective on or after {sup.effective or sup.edition}. This edition remains in force for policies written under it.")
    else:
        fm.append("")
    while len(fm) < FRONT_MATTER_LINES:
        fm.append("")
    return fm[:FRONT_MATTER_LINES]


def heading(doc: Document, sec_id: str, title: str) -> str:
    if doc.type in ("form", "endorsement", "amendatory", "bulletin", "guide", "memorandum", "training"):
        return f"## {sec_id} — {title}" if not title.startswith(sec_id) else f"## {title}"
    return f"## {title}"  # manual chapters carry their number in the title


def fill(ledger: Ledger, doc: Document, sec_id: str, text: str, renders: dict[str, str]) -> str:
    def sub(m: re.Match) -> str:
        kind, ident = m.group(1), m.group(2)
        key = f"{kind}:{ident}"
        if key not in renders:
            raise KeyError(f"{doc.id}/{sec_id}: no rendering for {key}")
        return renders[key]
    return MARKER.sub(sub, text)


def renderings_for(ledger: Ledger, doc: Document) -> dict[str, str]:
    r: dict[str, str] = {}
    for f in ledger.facts:
        if f.document == doc.id:
            r[f"fact:{f.id}"] = render_value(f.value, doc.voice)
    for c in ledger.contradictions:
        if c.document == doc.id:
            r[f"contra:{c.id}"] = render_value(c.wrong_value, doc.voice)
    for d in ledger.definitions:
        if d.document == doc.id:
            r[f"def:{d.id}"] = d.term
    titles = {(d.id, s.id): s.title for d in ledger.documents for s in d.sections}
    for ref in ledger.references:
        if ref.src_document == doc.id:
            dst = ledger.doc(ref.dst_document)
            r[f"ref:{ref.id}"] = render_reference(ref, doc, dst, titles.get((dst.id, ref.dst_section)) if ref.dst_section else None)
    return r


def assemble(ledger: Ledger, doc: Document, drafts: dict[tuple[str, str], str]) -> tuple[str, dict[str, dict]]:
    """(file text, placements) for one document. Placements map fact ids and
    contradiction ids to {path, line_start, line_end}."""
    renders = renderings_for(ledger, doc)
    lines = front_matter(ledger, doc)
    placements: dict[str, dict] = {}
    for sec in doc.sections:
        lines.append(heading(doc, sec.id, sec.title))
        lines.append("")
        body = drafts[(doc.id, sec.id)] if sec.kind not in ("table", "schedule") else drafts[(doc.id, sec.id)] + "\n\n" + table_for(ledger, doc, sec, sec.target_lines)
        # record which line each marker lands on BEFORE filling
        for offset, raw in enumerate(body.split("\n")):
            for m in MARKER.finditer(raw):
                kind, ident = m.group(1), m.group(2)
                if kind in ("fact", "contra"):
                    placements[ident] = {"path": doc.path, "line_start": len(lines) + offset + 1, "line_end": len(lines) + offset + 1, "section": sec.id}
                elif kind == "ref":
                    # references are code-rendered and may carry an edition date; recorded so V9 can allow the line
                    placements[f"ref:{ident}"] = {"path": doc.path, "line_start": len(lines) + offset + 1, "line_end": len(lines) + offset + 1, "section": sec.id}
        filled = fill(ledger, doc, sec.id, body, renders)
        lines += filled.split("\n")
        lines.append("")
    if doc.layout == "pdf-text":
        lines, placements = pdf_text_layout(ledger, doc, lines, placements)
    text = "\n".join(lines).rstrip("\n") + "\n"
    if "{{" in text:
        raise ValueError(f"{doc.id}: a marker survived assembly")
    return text, placements


def build_documents(ledger: Ledger, docs: list[Document], drafts: dict[tuple[str, str], str], out: pathlib.Path) -> dict[str, dict]:
    placements: dict[str, dict] = {}
    for doc in docs:
        text, pl = assemble(ledger, doc, drafts)
        target = out / doc.path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text)
        placements.update(pl)
    return placements


def write_placements(placements: dict[str, dict], path: pathlib.Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(dict(sorted(placements.items())), indent=1))
