"""Ledger -> SectionJobs. Ph. 02 §1.

A SectionJob is everything the drafter needs and nothing it must not have: the
voice, the section's title and kind and target length, the slots in order
(with surface forms and phrasing constraints, never values), the references to
make, the distractor concepts to mention, and a little continuity context.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass, field

import _paths  # noqa: F401
from ledger.schema import Document, Ledger, Section

from .render import surface

PROMPT_VERSION = "2026-09-18.1"


@dataclass
class Slot:
    marker: str          # {{fact:ID}} / {{def:ID}} / {{contra:ID}}
    kind: str            # fact | definition | contradiction
    concept_name: str    # surface form the document uses
    concept_desc: str    # canonical description, for the drafter's understanding
    value_kind: str      # money | percent | days | … (so the sentence fits the slot)
    phrasing: str | None = None


@dataclass
class RefSlot:
    marker: str          # {{ref:ID}}
    wording: str         # the phrase the ledger prescribes
    destination: str     # human description of where it points


@dataclass
class SectionJob:
    document: str
    section: str
    title: str
    kind: str
    voice: str
    target_lines: int
    numbering_prefix: str
    slots: list[Slot] = field(default_factory=list)
    refs: list[RefSlot] = field(default_factory=list)
    distractors: list[str] = field(default_factory=list)
    document_title: str = ""
    document_context: str = ""
    previous_tail: str = ""     # a few lines of the previous section, filled at draft time

    def hash(self) -> str:
        d = asdict(self)
        d.pop("previous_tail", None)
        payload = json.dumps(d, sort_keys=True) + "\n" + PROMPT_VERSION
        return hashlib.sha256(payload.encode()).hexdigest()


def numbering_prefix(doc: Document, sec: Section) -> str:
    if doc.type in ("form", "endorsement", "amendatory"):
        parts = sec.id.split(".")
        return parts[-1] if parts[-1].isalpha() else parts[0]
    if doc.type == "bulletin":
        return sec.id
    if doc.type == "manual":
        return sec.id.lstrip("RCP") if sec.id[0] in "RCP" else sec.id
    return sec.id


def jobs_for(ledger: Ledger, doc: Document) -> list[SectionJob]:
    facts_by_section = {}
    for f in ledger.facts:
        if f.document == doc.id:
            facts_by_section.setdefault(f.section, []).append(f)
    defs_by_section = {}
    for d in ledger.definitions:
        if d.document == doc.id:
            defs_by_section.setdefault(d.section, []).append(d)
    contras_by_section = {}
    for c in ledger.contradictions:
        if c.document == doc.id:
            contras_by_section.setdefault(c.section, []).append(c)
    refs_by_id = {r.id: r for r in ledger.references}
    context = f"{doc.title}. " + (f"Line of business {doc.line}. " if doc.line else "") + (f"State: {doc.state}. " if doc.state else "") + (f"Edition {doc.edition}. " if doc.edition else "")
    out = []
    for sec in doc.sections:
        job = SectionJob(document=doc.id, section=sec.id, title=sec.title, kind=sec.kind, voice=doc.voice, target_lines=sec.target_lines,
                         numbering_prefix=numbering_prefix(doc, sec), document_title=doc.title, document_context=context)
        if sec.kind in ("table", "schedule"):
            # tables.py emits the fact markers itself; the drafter writes only the introduction
            out.append(job)
            continue
        for f in facts_by_section.get(sec.id, []):
            c = ledger.concept(f.concept)
            job.slots.append(Slot(marker=f"{{{{fact:{f.id}}}}}", kind="fact", concept_name=f.surface_form, concept_desc=c.canonical, value_kind=f.value.kind, phrasing=f.phrasing))
        for c in contras_by_section.get(sec.id, []):
            fact = ledger.fact(c.fact); concept = ledger.concept(fact.concept)
            job.slots.append(Slot(marker=f"{{{{contra:{c.id}}}}}", kind="fact", concept_name=surface(concept, doc.voice), concept_desc=concept.canonical, value_kind=c.wrong_value.kind))
        for d in defs_by_section.get(sec.id, []):
            job.slots.append(Slot(marker=f"{{{{def:{d.id}}}}}", kind="definition", concept_name=d.term, concept_desc=f'the defined term "{d.term}"', value_kind="text"))
        if sec.kind == "definitions" and not any(sl.kind == "definition" for sl in job.slots):
            # nothing to define here: a "Definitions" section that only explains how the
            # attached form's terms apply is prose, and asking for a glossary of nothing fails
            job.kind = "prose"
        for rid in sec.references_out:
            r = refs_by_id[rid]
            dst = ledger.doc(r.dst_document)
            where = f"{dst.title}" + (f", section {r.dst_section}" if r.dst_section else ", its Definitions")
            job.refs.append(RefSlot(marker=f"{{{{ref:{rid}}}}}", wording=r.wording, destination=where))
        for i, cid in enumerate(sec.distractor_concepts):
            salt = int(hashlib.sha256(f"{doc.id}/{sec.id}".encode()).hexdigest(), 16)  # stable across processes
            job.distractors.append(surface(ledger.concept(cid), doc.voice, salt=(salt + i) % 4))
        out.append(job)
    return out
