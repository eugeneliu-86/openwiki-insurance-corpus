"""The fact ledger: schema, loader, referential integrity. Corpus expansion ph. 01.

Code owns this; the model never writes to it. Every questionable fact in the
large corpus is a row here before any prose exists, so gold answers are
lookups and the validators (ph. 02 §6) prove the built files match.

Unknown keys are rejected everywhere (`extra="forbid"`), as every contract in
this project does: a typo'd field silently ignored is a fact that never gets
planted and a question with no answer.
"""
from __future__ import annotations

import pathlib
import re
from collections import Counter, defaultdict
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field, model_validator

# The path contract is the agent's, imported, never re-typed (C2).
import _paths  # noqa: F401
from contracts.corpus_paths import CORPUS_PATH_RE  # noqa: E402

DocType = Literal["form", "endorsement", "amendatory", "bulletin", "manual", "guide", "memorandum", "training"]
Line = Literal["HO-3", "HO-5", "HO-4", "HO-6", "DP-3"]
Voice = Literal["iso-form", "regulator", "carrier-manual", "carrier-guide", "filing-memo", "trainer"]
SectionKind = Literal["prose", "provisions", "definitions", "table", "schedule", "faq"]
Authority = Literal["contract", "regulation", "guidance", "interpretation"]
ValueKind = Literal["money", "percent", "days", "business-days", "years", "hours", "date", "text", "enum", "boolean", "count", "horsepower", "feet"]

FRONT_MATTER_LINES = 12   # the assembler's front matter + title + blank; used for depth arithmetic


class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")


class FactValue(Strict):
    kind: ValueKind
    value: str | int | float | bool

    def key(self) -> str:
        return f"{self.kind}:{self.value}"


class Section(Strict):
    id: str
    title: str
    target_lines: int = Field(ge=4)
    kind: SectionKind = "provisions"
    facts: list[str] = []
    references_out: list[str] = []
    distractor_concepts: list[str] = []


class Document(Strict):
    id: str
    path: str
    type: DocType
    title: str
    line: Line | None = None
    state: str | None = None
    edition: str | None = None            # YYYY-MM for forms; issue date YYYY-MM-DD for bulletins
    effective: str | None = None          # YYYY-MM-DD
    supersedes: str | None = None         # document id
    superseded_by: str | None = None      # document id
    voice: Voice
    distractor: bool = False              # R5: carries vocabulary, no facts
    sections: list[Section]

    @property
    def target_lines(self) -> int:
        return FRONT_MATTER_LINES + sum(s.target_lines for s in self.sections)

    def section_starts(self) -> dict[str, int]:
        """Section id -> the line its heading lands on, from the TOC targets."""
        out, line = {}, FRONT_MATTER_LINES + 1
        for s in self.sections:
            out[s.id] = line
            line += s.target_lines
        return out


class Concept(Strict):
    id: str
    canonical: str
    synonyms: list[str] = []
    kind: ValueKind
    ambiguous: bool = False               # R1
    synonym_target: bool = False          # R2: questioned in the synonym split; set by author from voice spread
    group: str
    label: str | None = None              # a short name for questions and propositions when the canonical reads as a definition


class Fact(Strict):
    id: str
    concept: str
    document: str
    section: str
    value: FactValue
    surface_form: str
    phrasing: str | None = None
    depth_target: int | None = None       # R4: plant at or after this line
    authority: Authority


class Definition(Strict):
    id: str
    term: str
    document: str
    section: str
    used_by: list[str] = []               # document ids that use the term without defining it


class Reference(Strict):
    id: str
    chain: str
    src_document: str
    src_section: str
    dst_document: str
    dst_section: str | None = None
    dst_definition: str | None = None
    wording: str

    @model_validator(mode="after")
    def _one_destination(self):
        if (self.dst_section is None) == (self.dst_definition is None):
            raise ValueError(f"reference {self.id}: exactly one of dst_section / dst_definition")
        return self


class EditionDiff(Strict):
    form: str
    older: str                            # document id
    newer: str
    changed: list[tuple[str, str]] = []   # (fact id in older, fact id in newer)
    added: list[str] = []
    removed: list[str] = []
    renumbered: list[tuple[str, str]] = []


class Contradiction(Strict):
    id: str
    fact: str                             # the correct fact
    document: str                         # the document that misstates it
    section: str
    wrong_value: FactValue
    kind: Literal["stale", "overstated", "misattributed", "wrong-edition"]


class HistoryEntry(Strict):
    date: str
    value: FactValue
    document: str


class History(Strict):
    id: str
    concept: str
    entries: list[HistoryEntry]
    current: int


class Composition(Strict):
    """R8: a named set of facts a correct answer must combine, spanning >= 4 documents."""
    id: str
    facts: list[str]
    scenario: str


class Ledger(Strict):
    documents: list[Document]
    concepts: list[Concept]
    facts: list[Fact]
    definitions: list[Definition] = []
    references: list[Reference] = []
    editions: list[EditionDiff] = []
    contradictions: list[Contradiction] = []
    histories: list[History] = []
    compositions: list[Composition] = []

    # --- indexes ---------------------------------------------------------------
    def doc(self, doc_id: str) -> Document:
        return self._docs[doc_id]

    def fact(self, fact_id: str) -> Fact:
        return self._facts[fact_id]

    def concept(self, cid: str) -> Concept:
        return self._concepts[cid]

    @model_validator(mode="after")
    def _index_and_check(self):
        object.__setattr__(self, "_docs", {d.id: d for d in self.documents})
        object.__setattr__(self, "_facts", {f.id: f for f in self.facts})
        object.__setattr__(self, "_concepts", {c.id: c for c in self.concepts})
        object.__setattr__(self, "_defs", {d.id: d for d in self.definitions})
        errors = list(self._integrity())
        if errors:
            raise ValueError("ledger integrity:\n  " + "\n  ".join(errors[:40]) + (f"\n  … {len(errors) - 40} more" if len(errors) > 40 else ""))
        return self

    def _integrity(self):
        docs, facts, concepts, defs = self._docs, self._facts, self._concepts, self._defs
        for name, items in (("document", self.documents), ("fact", self.facts), ("concept", self.concepts),
                            ("definition", self.definitions), ("reference", self.references),
                            ("contradiction", self.contradictions), ("history", self.histories), ("composition", self.compositions)):
            dup = [k for k, n in Counter(x.id for x in items).items() if n > 1]
            if dup:
                yield f"duplicate {name} ids: {dup[:5]}"
        sections: dict[tuple[str, str], Section] = {}
        for d in self.documents:
            if not CORPUS_PATH_RE.match(d.path):
                yield f"{d.id}: path {d.path!r} does not match CORPUS_PATH_RE"
            if d.type in ("form", "endorsement", "amendatory") and not d.edition:
                yield f"{d.id}: a {d.type} needs an edition"
            for s in d.sections:
                if (d.id, s.id) in sections:
                    yield f"{d.id}: duplicate section id {s.id}"
                sections[(d.id, s.id)] = s
                for cid in s.distractor_concepts:
                    if cid not in concepts:
                        yield f"{d.id}/{s.id}: unknown distractor concept {cid}"
            if d.supersedes and d.supersedes not in docs:
                yield f"{d.id}: supersedes unknown {d.supersedes}"
            if d.superseded_by and d.superseded_by not in docs:
                yield f"{d.id}: superseded_by unknown {d.superseded_by}"
        planted: dict[str, tuple[str, str]] = {}
        for d in self.documents:
            for s in d.sections:
                for fid in s.facts:
                    if fid not in facts:
                        yield f"{d.id}/{s.id}: plants unknown fact {fid}"
                        continue
                    if fid in planted:
                        yield f"fact {fid} planted twice: {planted[fid]} and {(d.id, s.id)}"
                    planted[fid] = (d.id, s.id)
        for f in self.facts:
            if f.concept not in concepts:
                yield f"fact {f.id}: unknown concept {f.concept}"
            elif concepts[f.concept].kind != f.value.kind:
                yield f"fact {f.id}: value kind {f.value.kind} != concept kind {concepts[f.concept].kind}"
            if f.document not in docs:
                yield f"fact {f.id}: unknown document {f.document}"
            elif (f.document, f.section) not in sections:
                yield f"fact {f.id}: unknown section {f.document}/{f.section}"
            if f.id not in planted:
                yield f"fact {f.id} is planted nowhere"
            elif planted[f.id] != (f.document, f.section):
                yield f"fact {f.id}: planted in {planted[f.id]} but declares {(f.document, f.section)}"
            if f.concept in concepts:
                c = concepts[f.concept]
                if f.surface_form != c.canonical and f.surface_form not in c.synonyms:
                    yield f"fact {f.id}: surface form {f.surface_form!r} is not a form of {c.id}"
            if f.document in docs and docs[f.document].distractor:
                yield f"fact {f.id}: planted in distractor document {f.document}"
            if f.depth_target is not None and f.document in docs and (f.document, f.section) in sections:
                start = docs[f.document].section_starts()[f.section]
                if start < f.depth_target:
                    yield f"fact {f.id}: depth_target {f.depth_target} but section {f.section} starts at line {start} — the TOC cannot meet it"
        for dfn in self.definitions:
            if (dfn.document, dfn.section) not in sections:
                yield f"definition {dfn.id}: unknown section {dfn.document}/{dfn.section}"
            for u in dfn.used_by:
                if u not in docs:
                    yield f"definition {dfn.id}: used_by unknown document {u}"
        for r in self.references:
            if (r.src_document, r.src_section) not in sections:
                yield f"reference {r.id}: unknown source {r.src_document}/{r.src_section}"
            if r.dst_document not in docs:
                yield f"reference {r.id}: unknown destination document {r.dst_document}"
            elif r.dst_section is not None and (r.dst_document, r.dst_section) not in sections:
                yield f"reference {r.id}: unknown destination section {r.dst_document}/{r.dst_section}"
            if r.dst_definition is not None and r.dst_definition not in defs:
                yield f"reference {r.id}: unknown definition {r.dst_definition}"
            if (r.src_document, r.src_section) in sections and r.id not in sections[(r.src_document, r.src_section)].references_out:
                yield f"reference {r.id}: not listed in {r.src_document}/{r.src_section}.references_out"
        for e in self.editions:
            for side in (e.older, e.newer):
                if side not in docs:
                    yield f"edition diff {e.form}: unknown document {side}"
            for old, new in e.changed:
                if old in facts and facts[old].document != e.older:
                    yield f"edition diff {e.form}: {old} is not in {e.older}"
                if new in facts and facts[new].document != e.newer:
                    yield f"edition diff {e.form}: {new} is not in {e.newer}"
                if old in facts and new in facts:
                    if facts[old].concept != facts[new].concept:
                        yield f"edition diff {e.form}: {old} and {new} are different concepts"
                    if facts[old].value == facts[new].value:
                        yield f"edition diff {e.form}: {old} -> {new} does not change the value"
            for fid in e.added:
                if fid in facts and facts[fid].document != e.newer:
                    yield f"edition diff {e.form}: added {fid} is not in {e.newer}"
            for fid in e.removed:
                if fid in facts and facts[fid].document != e.older:
                    yield f"edition diff {e.form}: removed {fid} is not in {e.older}"
        for c in self.contradictions:
            if c.fact not in facts:
                yield f"contradiction {c.id}: unknown fact {c.fact}"
            if (c.document, c.section) not in sections:
                yield f"contradiction {c.id}: unknown section {c.document}/{c.section}"
            elif c.fact in facts:
                if facts[c.fact].document == c.document:
                    yield f"contradiction {c.id}: misstating document is the fact's own"
                if c.wrong_value == facts[c.fact].value:
                    yield f"contradiction {c.id}: wrong value equals the fact's value"
        for h in self.histories:
            if h.concept not in concepts:
                yield f"history {h.id}: unknown concept {h.concept}"
            if not (0 <= h.current < len(h.entries)):
                yield f"history {h.id}: current index out of range"
            for e in h.entries:
                if e.document not in docs:
                    yield f"history {h.id}: unknown document {e.document}"
        for comp in self.compositions:
            missing = [f for f in comp.facts if f not in facts]
            if missing:
                yield f"composition {comp.id}: unknown facts {missing[:3]}"
            else:
                if len({facts[f].document for f in comp.facts}) < 4:
                    yield f"composition {comp.id}: spans fewer than 4 documents"
        # R10 density: outside distractors and the rating manual, no run of 300 lines without a fact.
        for d in self.documents:
            if d.distractor or d.id == "manual.rating":
                continue
            gap = FRONT_MATTER_LINES
            for s in d.sections:
                if s.facts or s.kind == "table":
                    gap = 0
                gap += s.target_lines
                if gap > 300 + s.target_lines and not s.facts:
                    yield f"{d.id}: {gap} lines without a fact ending at section {s.id} (R10)"
                    gap = 0


def load(directory: str | pathlib.Path) -> Ledger:
    """Load every YAML file in `directory` into one Ledger. File names are the
    field names (documents.yaml -> documents, …)."""
    directory = pathlib.Path(directory)
    data: dict[str, list] = {}
    for f in sorted(directory.glob("*.yaml")):
        data[f.stem] = yaml.safe_load(f.read_text()) or []
    return Ledger.model_validate(data)


def dump(ledger: Ledger, directory: str | pathlib.Path) -> None:
    directory = pathlib.Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    for field in ("documents", "concepts", "facts", "definitions", "references", "editions", "contradictions", "histories", "compositions"):
        items = [x.model_dump(mode="json", exclude_defaults=True) for x in getattr(ledger, field)]
        (directory / f"{field}.yaml").write_text(yaml.safe_dump(items, sort_keys=False, allow_unicode=True, width=120))
