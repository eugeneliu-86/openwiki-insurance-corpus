"""Validators V1–V9 over the BUILT FILES. Ph. 02 §6.

Each returns a list of failure strings; empty is a pass. They import the
agent's contracts rather than re-typing a regex, and they read what is on
disk, never the drafts.
"""
from __future__ import annotations

import pathlib
import re
from collections import Counter, defaultdict

import _paths  # noqa: F401
from contracts.corpus_paths import CORPUS_PATH_RE
from ledger.schema import Ledger

from .render import renderings, unslotted_numerals, value_occurrences


def _read(out: pathlib.Path, path: str) -> list[str]:
    return (out / path).read_text().split("\n")


def _section_spans(ledger: Ledger, out: pathlib.Path, doc_id: str) -> dict[str, tuple[int, int]]:
    """section id -> (first line, last line), 1-based, from the headings in the file."""
    doc = ledger.doc(doc_id)
    lines = _read(out, doc.path)
    starts = {}
    for i, l in enumerate(lines, 1):
        if l.startswith("## "):
            for s in doc.sections:
                if l == f"## {s.id} — {s.title}" or l == f"## {s.title}":
                    starts[s.id] = i
    ids = [s.id for s in doc.sections if s.id in starts]
    spans = {}
    for k, sid in enumerate(ids):
        end = starts[ids[k + 1]] - 1 if k + 1 < len(ids) else len(lines)
        spans[sid] = (starts[sid], end)
    return spans


def _norm(s: str) -> str:
    return " ".join(s.split()).lower()


def v1_facts_at_recorded_lines(ledger: Ledger, out: pathlib.Path, placements: dict) -> list[str]:
    errs = []
    for f in ledger.facts:
        pl = placements.get(f.id)
        if not pl:
            errs.append(f"V1 {f.id}: no placement"); continue
        lines = _read(out, f.document if False else ledger.doc(f.document).path)
        line = lines[pl["line_start"] - 1] if pl["line_start"] <= len(lines) else ""
        if not value_occurrences(line, f.value):
            errs.append(f"V1 {f.id}: value not at {pl['path']}:{pl['line_start']}")
        if f.value.kind in ("text", "enum", "boolean"):
            continue  # a phrase value ("replacement cost", "is required") recurs in prose legitimately; the line check above is the rule
        spans = _section_spans(ledger, out, f.document)
        a, b = spans.get(f.section, (1, len(lines)))
        # exactly one line in the section carries THIS fact's rendering (another fact of the same value in the same section is allowed only if it is a different concept)
        # four Additional Coverages limits can all be $500, and a planted misstatement
        # can share a value with a neighbouring fact: one line per planted value whose
        # renderings overlap this one's is the rule
        def collides(other) -> bool:  # another planted value whose text would read as this fact's value
            return any(value_occurrences(r, f.value) for r in renderings(other))
        same_value = [g.id for g in ledger.facts if g.document == f.document and g.section == f.section and collides(g.value)]
        same_value += [c.id for c in ledger.contradictions if c.document == f.document and c.section == f.section and collides(c.wrong_value)]
        hits = [i for i in range(a, b + 1) if value_occurrences(lines[i - 1], f.value)]
        if len(hits) > len(same_value):
            errs.append(f"V1 {f.id}: value appears {len(hits)} times in section {f.section}")
    return errs


def v2_synonyms(ledger: Ledger, out: pathlib.Path) -> list[str]:
    errs = []
    corpus = "\n".join((out / d.path).read_text().lower() for d in ledger.documents if (out / d.path).exists())
    forms_used = defaultdict(set)
    for f in ledger.facts:
        forms_used[f.concept].add(f.surface_form)
    for c in ledger.concepts:
        if not c.synonym_target:
            continue
        present = [x for x in [c.canonical, *c.synonyms] if x.lower() in corpus]
        if len(present) < 2:
            errs.append(f"V2 {c.id}: only {len(present)} forms appear in the corpus")
        if forms_used[c.id] and forms_used[c.id] == {c.canonical}:
            errs.append(f"V2 {c.id}: every fact uses the canonical form")
    return errs


def v3_references(ledger: Ledger, out: pathlib.Path) -> list[str]:
    errs = []
    for r in ledger.references:
        spans = _section_spans(ledger, out, r.src_document)
        lines = _read(out, ledger.doc(r.src_document).path)
        a, b = spans.get(r.src_section, (1, len(lines)))
        text = _norm("\n".join(lines[a - 1:b]))
        if _norm(r.wording) not in text:
            errs.append(f"V3 {r.id}: wording not in {r.src_document}/{r.src_section}")
        if r.dst_section and r.dst_section not in _section_spans(ledger, out, r.dst_document):
            errs.append(f"V3 {r.id}: destination section {r.dst_document}/{r.dst_section} not in file")
    return errs


def v4_edition_diffs(ledger: Ledger, placements: dict) -> list[str]:
    errs = []
    values = {f.id: (f.concept, f.value.key()) for f in ledger.facts}
    for e in ledger.editions:
        if ledger.doc(e.older).type != "form":
            continue
        old = {values[f.id][0]: values[f.id][1] for f in ledger.facts if f.document == e.older}
        new = {values[f.id][0]: values[f.id][1] for f in ledger.facts if f.document == e.newer}
        changed = {c for c in new if c in old and old[c] != new[c]}
        declared = {values[o][0] for o, _ in e.changed}
        if changed != declared:
            errs.append(f"V4 {e.form} {e.older}->{e.newer}: changed {sorted(changed ^ declared)} not as declared")
        if {c for c in new if c not in old} != {values[a][0] for a in e.added}:
            errs.append(f"V4 {e.form}: added set differs")
        if {c for c in old if c not in new} != {values[r][0] for r in e.removed}:
            errs.append(f"V4 {e.form}: removed set differs")
        missing = [fid for pair in e.changed for fid in pair if fid not in placements]
        if missing:
            errs.append(f"V4 {e.form}: unplaced {missing[:3]}")
    return errs


def v5_ambiguity(ledger: Ledger, out: pathlib.Path) -> list[str]:
    errs = []
    texts = {d.id: (out / d.path).read_text().lower() for d in ledger.documents if (out / d.path).exists()}
    qualifying = 0
    for c in ledger.concepts:
        if not c.ambiguous:
            continue
        forms = [x.lower() for x in [c.canonical, *c.synonyms]]
        n_docs = sum(1 for t in texts.values() if any(f in t for f in forms))
        if n_docs >= 25:
            qualifying += 1
        # a question fixes the edition it asks about, so competing answers are
        # contract/regulation documents in the same (line, state, edition)
        by_scope = defaultdict(set)
        for f in ledger.facts:
            if f.concept == c.id and f.authority in ("contract", "regulation"):
                d = ledger.doc(f.document)
                family = d.id.rsplit(".", 1)[0] if d.type in ("endorsement", "amendatory", "bulletin") else d.type
                by_scope[(family, d.line, d.state, d.edition)].add(f.document)
        worst = max((len(v) for v in by_scope.values()), default=0)
        if worst > 3 and n_docs >= 25:
            errs.append(f"V5 {c.id}: {worst} answer-bearing documents in one (line, state) scope")
    if qualifying < 12:
        errs.append(f"V5: only {qualifying} ambiguous concepts appear in >= 25 documents")
    return errs


def v6_depth(placements: dict) -> list[str]:
    deep2 = sum(1 for p in placements.values() if p["line_start"] > 2000)
    deep6 = sum(1 for p in placements.values() if p["line_start"] > 6000)
    errs = []
    if deep2 < 40:
        errs.append(f"V6: {deep2} facts beyond line 2000 (need 40)")
    if deep6 < 15:
        errs.append(f"V6: {deep6} facts beyond line 6000 (need 15)")
    return errs


def _concept_phrases(ledger: Ledger) -> list[str]:
    return [x for c in ledger.concepts for x in [c.canonical, *c.synonyms]]


def v7_distractors(ledger: Ledger, out: pathlib.Path) -> list[str]:
    errs = []
    phrases = _concept_phrases(ledger)
    for d in ledger.documents:
        if not d.distractor:
            continue
        text = (out / d.path).read_text()
        lines = text.split("\n")
        spans = _section_spans(ledger, out, d.id)
        skip = set()
        for s in d.sections:
            if s.kind in ("table", "schedule") and s.id in spans:
                a, b = spans[s.id]; skip.update(range(a, b + 1))
        for c in ledger.contradictions:
            if c.document == d.id:
                skip.add(_placement_line(c.id))
        body = "\n".join(l for i, l in enumerate(lines, 1) if i > 12 and i not in skip and not l.startswith("## "))
        vocab = [ledger.concept(c) for s in d.sections for c in s.distractor_concepts]
        for c in vocab:
            if not any(x.lower() in text.lower() for x in [c.canonical, *c.synonyms]):
                errs.append(f"V7 {d.id}: distractor concept {c.id} not mentioned")
        nums = unslotted_numerals(body, phrases)
        if nums:
            errs.append(f"V7 {d.id}: carries numbers {sorted(set(nums))[:5]}")
    return errs


def v8_contradictions(ledger: Ledger, out: pathlib.Path, placements: dict) -> list[str]:
    errs = []
    for c in ledger.contradictions:
        pl = placements.get(c.id)
        if not pl:
            errs.append(f"V8 {c.id}: not placed"); continue
        line = _read(out, ledger.doc(c.document).path)[pl["line_start"] - 1]
        if not value_occurrences(line, c.wrong_value):
            errs.append(f"V8 {c.id}: wrong value not at its line")
        if c.fact not in placements:
            errs.append(f"V8 {c.id}: the true fact {c.fact} is not placed")
    return errs


def v9_inventory(ledger: Ledger, out: pathlib.Path) -> list[str]:
    errs = []
    total = 0
    long_docs = 0
    phrases = _concept_phrases(ledger)
    for d in ledger.documents:
        if not CORPUS_PATH_RE.match(d.path):
            errs.append(f"V9 {d.id}: path fails CORPUS_PATH_RE")
        p = out / d.path
        if not p.exists():
            errs.append(f"V9 {d.id}: missing file"); continue
        text = p.read_text()
        n = text.count("\n")
        total += n
        long_docs += n >= 5000
        if "{{" in text:
            errs.append(f"V9 {d.id}: a slot marker survived")
        if not 0.7 * d.target_lines <= n <= 1.4 * d.target_lines:
            errs.append(f"V9 {d.id}: {n} lines, target {d.target_lines}")
        # numerals outside table sections and outside fact/contradiction lines
        spans = _section_spans(ledger, out, d.id)
        lines = text.split("\n")
        allowed_lines = set()
        for s in d.sections:
            if s.kind in ("table", "schedule") and s.id in spans:
                a, b = spans[s.id]; allowed_lines.update(range(a, b + 1))
        for f in ledger.facts:
            if f.document == d.id:
                allowed_lines.add(_placement_line(f.id))
        for c in ledger.contradictions:
            if c.document == d.id:
                allowed_lines.add(_placement_line(c.id))
        for key, pl in _PLACEMENTS.items():  # code-rendered references may carry an edition date
            if key.startswith("ref:") and pl["path"] == d.path:
                allowed_lines.add(pl["line_start"])
        for i, l in enumerate(lines, 1):
            if i <= 12 or i in allowed_lines or l.startswith("## ") or l.startswith("> SUPERSEDED"):
                continue
            hits = unslotted_numerals(l, phrases)
            if hits:
                errs.append(f"V9 {d.id}:{i}: numerals outside slots {hits[:3]}")
                if len(errs) > 60:
                    return errs
    n_docs = len(ledger.documents)
    if n_docs < 100:
        errs.append(f"V9: {n_docs} documents")
    if total / max(1, n_docs) < 1000:
        errs.append(f"V9: average {total / n_docs:.0f} lines")
    if long_docs < 3:
        errs.append(f"V9: {long_docs} documents >= 5000 lines")
    return errs


class _Sub:
    """The ledger restricted to a slice of documents, for a partial build.
    Lookups (doc/fact/concept) still see the whole ledger so references to
    absent documents resolve; the lists are filtered."""

    def __init__(self, ledger: Ledger, only: set[str]):
        self._l = ledger
        self.documents = [d for d in ledger.documents if d.id in only]
        self.facts = [f for f in ledger.facts if f.document in only]
        self.contradictions = [c for c in ledger.contradictions if c.document in only]
        self.references = [r for r in ledger.references if r.src_document in only and r.dst_document in only]
        self.editions = [e for e in ledger.editions if e.older in only and e.newer in only]
        self.concepts = ledger.concepts
        self.definitions = ledger.definitions

    def doc(self, i): return self._l.doc(i)
    def fact(self, i): return self._l.fact(i)
    def concept(self, i): return self._l.concept(i)


_PLACEMENTS: dict = {}


def _placement_line(ident: str) -> int:
    return _PLACEMENTS.get(ident, {}).get("line_start", -1)


def run_all(ledger: Ledger, out: pathlib.Path, placements: dict, only_documents: set[str] | None = None) -> dict[str, list[str]]:
    """Every validator; a partial build (a slice) skips the corpus-wide counts."""
    global _PLACEMENTS
    _PLACEMENTS = placements
    if only_documents:
        ledger = _Sub(ledger, only_documents)
    results = {
        "V1": v1_facts_at_recorded_lines(ledger, out, placements),
        "V3": v3_references(ledger, out),
        "V4": v4_edition_diffs(ledger, placements),
        "V7": v7_distractors(ledger, out),
        "V8": v8_contradictions(ledger, out, placements),
    }
    if not only_documents:
        results["V2"] = v2_synonyms(ledger, out)
        results["V5"] = v5_ambiguity(ledger, out)
        results["V6"] = v6_depth(placements)
        results["V9"] = v9_inventory(ledger, out)
    else:
        results["V9"] = [e for e in v9_inventory(ledger, out) if not e.startswith("V9:")]
    return results
