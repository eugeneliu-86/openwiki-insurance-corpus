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
from .render import render_reference, render_value
from .tables import table_for

MARKER = re.compile(r"\{\{(fact|def|contra|ref):([^}]+)\}\}")


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
