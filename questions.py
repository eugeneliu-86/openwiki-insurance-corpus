"""Derive the large evaluation dataset from the ledger. Corpus expansion ph. 03.

Every question is a template instantiated against ledger objects; every answer,
proposition and citation is looked up in the ledger and in `out/placements.json`.
Nothing in a reference is model-written. The output is the `questions.jsonl`
shape the POC's evaluation harness already consumes (evaluations ph. 03 §2).

    uv run python questions.py --corpus ../openwiki-insurance-corpus \
        --out ../openwiki-insurance-poc/evals/dataset/large

Writes questions.jsonl, stale_edits.json (the six source edits the stale
branch makes) and manifest.json (split counts and the main SHA the corpus
checkout is at). shas.json is written by evals/stale/make.sh after it pushes
the stale branch.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import pathlib
import re
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import _paths  # noqa: F401,E402
from ledger.schema import Concept, Document, Fact, FactValue, Ledger, load  # noqa: E402
from gen.render import render_value, renderings, value_occurrences  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
COUNTS = {"single": 15, "composed": 25, "assembly": 20, "corpus_wide": 10, "disambiguation": 15, "synonym": 15,
          "chain": 15, "deep": 15, "abstain": 8, "stale": 6, "stale_control": 6}
STATE_NAMES = {"FL": "Florida", "TX": "Texas", "CA": "California", "NY": "New York", "LA": "Louisiana", "NC": "North Carolina",
               "CO": "Colorado", "IL": "Illinois"}


# --- helpers ----------------------------------------------------------------------
def h(*parts: str) -> int:
    return int(hashlib.sha256("|".join(parts).encode()).hexdigest(), 16)


def pick(seed: str, options: list):
    return options[h(seed) % len(options)]


class Ctx:
    def __init__(self, ledger: Ledger, placements: dict, corpus: pathlib.Path, claims_index: dict | None):
        self.L = ledger
        self.P = placements
        self.corpus = corpus
        self._text: dict[str, list[str]] = {}
        self.by_concept: dict[str, list[Fact]] = collections.defaultdict(list)
        for f in ledger.facts:
            self.by_concept[f.concept].append(f)
        self.contra_by_fact = {c.fact: c for c in ledger.contradictions}
        self.section_title = {(d.id, s.id): s.title for d in ledger.documents for s in d.sections}
        # claim evidence ranges by document path, for the stale split
        self.claim_ranges: dict[str, list[tuple[int, int]]] = collections.defaultdict(list)
        for c in (claims_index or {}).get("claims", []):
            for e in c.get("evidence", []):
                if e.get("document") and e.get("start") is not None:
                    self.claim_ranges[e["document"]].append((e["start"], e["end"]))

    # text
    def lines(self, doc: Document) -> list[str]:
        if doc.id not in self._text:
            self._text[doc.id] = (self.corpus / doc.path).read_text().split("\n")
        return self._text[doc.id]

    def gold_lines(self, fid: str) -> str:
        pl = self.P[fid]
        return "\n".join(self.lines(self.L.doc(self.L.fact(fid).document))[pl["line_start"] - 1: pl["line_end"]])

    # rendering
    def cite(self, key: str) -> str:
        pl = self.P[key]
        return f"repo://{pl['path']}#L{pl['line_start']}-L{pl['line_end']}"

    @staticmethod
    def words(value: FactValue) -> str:
        return renderings(value)[0]

    def concept(self, f: Fact) -> Concept:
        return self.L.concept(f.concept)

    def doc(self, f: Fact) -> Document:
        return self.L.doc(f.document)

    @staticmethod
    def name(con: Concept) -> str:
        return con.label or con.canonical

    def prop(self, f: Fact, value: FactValue | None = None) -> str:
        v = value or f.value
        return f"under {self.doc(f).title}, the {self.name(self.concept(f))} is {self.words(v)}"

    def wrong_prop(self, f: Fact, value: FactValue) -> str:
        return f"the {self.name(self.concept(f))} is {self.words(value)}"

    def sec_title(self, f: Fact) -> str:
        return self.section_title.get((f.document, f.section), f.section)

    def sec_label(self, doc: Document, sec: str) -> str:
        """How the built document names the section: manual chapters carry their number
        in the title ("Rule 110 — …", "Chapter 3 — …", "Part 1 — …", "Table 2 — …")."""
        if doc.type == "manual":
            title = self.section_title.get((doc.id, sec), sec)
            return title.split(" — ")[0]
        return sec

    @staticmethod
    def edition_label(doc: Document) -> str | None:
        if doc.type not in ("form", "endorsement", "amendatory") or not doc.edition:
            return None
        return f"{doc.path.split('/')[3]} {doc.edition}"

    def editions(self, facts: list[Fact]) -> list[str]:
        out = []
        for f in facts:
            lab = self.edition_label(self.doc(f))
            if lab and lab not in out:
                out.append(lab)
        return out

    def guidance(self, facts: list[Fact]) -> list[dict]:
        out = []
        for f in facts:
            d = self.doc(f)
            if d.type == "guide":
                g = {"document": d.path, "provision": f.section}
                if g not in out:
                    out.append(g)
        return out

    def neighbours(self, f: Fact, k: int = 2, same_family: bool | None = None, relied: list[Fact] | None = None) -> list[str]:
        """Wrong-answer propositions: the concept's value in other documents, when that
        value differs and its rendering is not on the gold lines (a correct answer that
        quotes the gold line must not trip it). `relied` are the other facts the answer
        must state; their values are never wrong answers."""
        gold = "\n".join(self.gold_lines(g.id) for g in [f, *(relied or [])])
        out, seen = [], {g.value.key() for g in [f, *(relied or [])]}
        cands = [g for g in self.by_concept[f.concept] if g.document != f.document]
        cands.sort(key=lambda g: h(f.id, g.id))
        if same_family is not None:
            fam = self.doc(f).path.split("/")[3] if self.doc(f).type in ("form", "endorsement", "amendatory") else None
            cands = [g for g in cands if (self.doc(g).path.split("/")[3] == fam if self.doc(g).type in ("form", "endorsement", "amendatory") else False) == same_family] or cands
        for g in cands:
            if g.value.key() in seen or value_occurrences(gold, g.value):
                continue
            seen.add(g.value.key())
            out.append(self.wrong_prop(f, g.value))
            if len(out) >= k:
                break
        return out


def spread(cands: list, n: int, keys, seed: str) -> list:
    """Pick n candidates favouring unseen values of each key (concept, document…),
    deterministic in `seed`."""
    cands = sorted(cands, key=lambda c: h(seed, str(c)))
    out, seen = [], [set() for _ in keys]
    while len(out) < n and cands:
        best = max(cands, key=lambda c: sum(1 for i, k in enumerate(keys) if k(c) not in seen[i]))
        out.append(best); cands.remove(best)
        for i, k in enumerate(keys):
            seen[i].add(k(best))
    return out


def example(id_: str, split: str, question: str, *, position: str, must_state: list[str], must_not: list[str],
            gold: list[str], guidance: list[dict] | None = None, editions: list[str] | None = None,
            unresolved: dict | None = None, gold_list: list[dict] | None = None, sha_ref: str = "main") -> dict:
    return {"id": id_, "split": split, "sha_ref": sha_ref, "question": question,
            "reference": {"position": position, "must_state": must_state, "must_not_state": must_not,
                          "gold_citations": gold, "gold_guidance": guidance or [], "editions": editions or [],
                          "expect_unresolved": unresolved, "gold_list": gold_list}}


NUMERIC = ("money", "percent", "days", "business-days", "years", "hours", "count", "feet", "horsepower")


def contract_facts(c: Ctx) -> list[Fact]:
    return [f for f in c.L.facts if f.authority == "contract" and f.value.kind in NUMERIC and f.id in c.P]


# --- templates ----------------------------------------------------------------------
def t_single(c: Ctx) -> list[dict]:
    facts = spread(contract_facts(c), COUNTS["single"], [lambda f: f.concept, lambda f: f.document, lambda f: c.doc(f).type], "single")
    out = []
    for i, f in enumerate(facts, 1):
        d, con = c.doc(f), c.concept(f)
        q = pick(f.id, [
            f"Under {d.title}, what is the {f.surface_form}?",
            f"What does {d.title} set as the {c.name(con)}?",
            f"In {d.title}, section {f.section} ({c.sec_title(f)}): what is the {f.surface_form}?",
            f"Tell me the {f.surface_form} under {d.title}, with the provision that sets it.",
        ])
        out.append(example(f"single-{i:02d}", "single", q, position=f"{c.words(f.value).capitalize()} ({d.title}, {f.section}).",
                           must_state=[c.prop(f)], must_not=c.neighbours(f, 2), gold=[c.cite(f.id)], editions=c.editions([f])))
    return out


def t_composed(c: Ctx) -> list[dict]:
    out = []
    # edition differences: the same concept in two editions of one form
    pairs = [(o, n, e) for e in c.L.editions for o, n in e.changed if o in c.P and n in c.P]
    pairs = spread(pairs, 15, [lambda p: p[2].form, lambda p: c.L.fact(p[0]).concept], "composed-edition")
    for i, (o, n, e) in enumerate(pairs, 1):
        fo, fn = c.L.fact(o), c.L.fact(n)
        do, dn = c.doc(fo), c.doc(fn)
        q = pick(o, [
            f"How did the {c.name(c.concept(fn))} change between {do.title} and {dn.title}?",
            f"Compare the {fn.surface_form} under {do.title} with the {dn.title} edition. Which governs a policy written today?",
            f"A policy was written under {do.title} and renewed onto {dn.title}. What was the {fn.surface_form} before and after?",
        ])
        # a wrong-edition misstatement quotes the other edition's value, which this
        # question must state, so only misstatements with a third value are wrong answers
        relied_values = {fo.value.key(), fn.value.key()}
        avoid = [c.wrong_prop(f, c.contra_by_fact[f.id].wrong_value) for f in (fo, fn)
                 if f.id in c.contra_by_fact and c.contra_by_fact[f.id].wrong_value.key() not in relied_values]
        avoid = avoid or c.neighbours(fn, 1, same_family=False, relied=[fo]) or [c.wrong_prop(fn, bump(fn.value))]
        out.append(example(f"composed-{i:02d}", "composed", q,
                           position=f"{c.words(fo.value)} under {do.title}; {c.words(fn.value)} under {dn.title}, which governs policies effective on or after {dn.effective or dn.edition}.",
                           must_state=[c.prop(fo), c.prop(fn)], must_not=avoid, gold=[c.cite(o), c.cite(n)], editions=c.editions([fo, fn])))
    # a misstatement in interpretive material against the controlling text
    # the composed split's reference carries editions, so the misstated fact must sit in a
    # form, endorsement or amendatory edition (a bulletin or manual has none)
    contras = [k for k in c.L.contradictions if k.fact in c.P and c.doc(c.L.fact(k.fact)).type in ("form", "endorsement", "amendatory")]
    contras = spread(contras, 10, [lambda k: c.L.fact(k.fact).concept, lambda k: k.document], "composed-contra")
    for i, k in enumerate(contras, 16):
        f = c.L.fact(k.fact); d, dk = c.doc(f), c.L.doc(k.document)
        q = pick(k.id, [
            f"{dk.title} says the {f.surface_form} is {c.words(k.wrong_value)}. What does {d.title} actually provide, and which controls?",
            f"An adjuster relying on {dk.title} quotes {c.words(k.wrong_value)} for the {c.name(c.concept(f))}. Is that right under {d.title}?",
            f"Reconcile {dk.title} with {d.title} on the {c.name(c.concept(f))}.",
        ])
        out.append(example(f"composed-{i:02d}", "composed", q,
                           position=f"{d.title} controls: {c.words(f.value)}. {dk.title} misstates it as {c.words(k.wrong_value)}.",
                           must_state=[c.prop(f), f"{d.title} controls over {dk.title}"],
                           must_not=[c.wrong_prop(f, k.wrong_value)], gold=[c.cite(f.id)], editions=c.editions([f])))
    return out


def t_assembly(c: Ctx) -> list[dict]:
    comps = [k for k in c.L.compositions if all(f in c.P for f in k.facts)]
    comps = spread(comps, COUNTS["assembly"], [lambda k: k.scenario.split(":")[0], lambda k: len(k.facts)], "assembly")
    out = []
    for i, k in enumerate(comps, 1):
        facts = [c.L.fact(f) for f in k.facts]
        q = pick(k.id, [
            f"{k.scenario}. Give the governing value for each point with the provision that sets it.",
            f"Work this file: {k.scenario}. Which provisions apply and what does each one set?",
            f"{k.scenario}. Assemble the answer from the form, the endorsement, the state form and our guidance.",
        ])
        relied_values = {f.value.key() for f in facts}
        avoid = [c.wrong_prop(f, c.contra_by_fact[f.id].wrong_value) for f in facts
                 if f.id in c.contra_by_fact and c.contra_by_fact[f.id].wrong_value.key() not in relied_values]
        avoid = avoid or c.neighbours(facts[1], 1, relied=facts)
        out.append(example(f"assembly-{i:02d}", "assembly", q,
                           position="; ".join(f"{c.doc(f).title} {f.section}: {c.words(f.value)}" for f in facts) + ".",
                           must_state=[c.prop(f) for f in facts], must_not=avoid, gold=[c.cite(f.id) for f in facts],
                           guidance=c.guidance(facts), editions=c.editions(facts)))
    return out


def t_corpus_wide(c: Ctx) -> list[dict]:
    cands = [con for con in c.L.concepts if len(c.by_concept[con.id]) >= 6 and all(f.id in c.P for f in c.by_concept[con.id])]
    cands = spread(cands, COUNTS["corpus_wide"], [lambda k: k.group, lambda k: k.kind], "corpus_wide")
    distractor_docs = [d for d in c.L.documents if d.distractor]
    out = []
    for i, con in enumerate(cands, 1):
        facts = c.by_concept[con.id]
        gold_list, seen = [], set()
        for f in facts:
            d = c.doc(f)
            key = (d.path, f.section)
            if key not in seen:
                seen.add(key); gold_list.append({"document": d.path, "provision": c.sec_label(d, f.section)})
        mention = [d for d in distractor_docs if any(con.id in s.distractor_concepts for s in d.sections)]
        avoid = [f"{d.title} sets a value for the {c.name(con)}" for d in mention[:2]]
        avoid = avoid or [f"the {c.name(con)} is the same in every document that sets it"]
        q = pick(con.id, [
            f"List every document and provision in the corpus that sets a {c.name(con)}, with the value each gives.",
            f"Where in the corpus is the {c.name(con)} set? Name each document and provision and its value.",
            f"Enumerate all provisions across forms, endorsements, state forms, bulletins and guidance that state the {c.name(con)}.",
        ])
        out.append(example(f"corpus-wide-{i:02d}", "corpus_wide", q,
                           position=f"{len(gold_list)} provisions in {len({c.doc(f).id for f in facts})} documents set the {c.name(con)}.",
                           must_state=[], must_not=avoid, gold=[], gold_list=gold_list))
    return out


def t_disambiguation(c: Ctx) -> list[dict]:
    cands = [f for f in c.L.facts if c.concept(f).ambiguous and f.id in c.P and c.doc(f).type in ("form", "endorsement", "amendatory", "bulletin")]
    facts = spread(cands, COUNTS["disambiguation"], [lambda f: f.concept, lambda f: f.document, lambda f: c.doc(f).state or c.doc(f).line], "disambiguation")
    out = []
    for i, f in enumerate(facts, 1):
        d, con = c.doc(f), c.concept(f)
        others = len({g.document for g in c.by_concept[con.id]})
        q = pick(f.id, [
            f"Under {d.title}, what is the {f.surface_form}?",
            f"What does {d.title} set as the {f.surface_form}? Other documents set their own; I want this one.",
            f"For a policy governed by {d.title}, what {c.name(con)} applies?",
        ])
        out.append(example(f"disambiguation-{i:02d}", "disambiguation", q,
                           position=f"{c.words(f.value).capitalize()} ({d.title}, {f.section}); {others} documents set this concept and most give a different value.",
                           must_state=[c.prop(f)], must_not=c.neighbours(f, 3), gold=[c.cite(f.id)], editions=c.editions([f])))
    return out


def t_synonym(c: Ctx) -> list[dict]:
    cands = []
    for f in c.L.facts:
        con = c.concept(f)
        if not con.synonym_target or f.id not in c.P or f.value.kind not in NUMERIC:
            continue
        text = "\n".join(c.lines(c.doc(f))).lower()
        forms = [s for s in [con.canonical, *con.synonyms] if s.lower() != f.surface_form.lower() and s.lower() not in text]
        if forms:
            cands.append((f, forms))
    picked = spread(cands, COUNTS["synonym"], [lambda p: p[0].concept, lambda p: p[0].document], "synonym")
    out = []
    for i, (f, forms) in enumerate(picked, 1):
        d, con = c.doc(f), c.concept(f)
        s = pick(f.id + "form", forms)
        q = pick(f.id, [
            f"Under {d.title}, what is the {s}?",
            f"What {s} applies under {d.title}?",
            f"I need the {s} for {d.title}. What is it and where is it set?",
        ])
        out.append(example(f"synonym-{i:02d}", "synonym", q,
                           position=f"{c.words(f.value).capitalize()}; {d.title} calls it the {f.surface_form} ({f.section}).",
                           must_state=[c.prop(f), f"{d.title} refers to this as the {f.surface_form}"],
                           must_not=c.neighbours(f, 2), gold=[c.cite(f.id)], editions=c.editions([f])))
    return out


def t_chain(c: Ctx) -> list[dict]:
    chains: dict[str, list] = collections.defaultdict(list)
    for r in c.L.references:
        chains[r.chain].append(r)
    cands = []
    for cid, hops in chains.items():
        hops = sorted(hops, key=lambda r: int(r.id.rsplit(".", 1)[1]))
        end = hops[-1]
        if end.dst_definition or not all(f"ref:{r.id}" in c.P for r in hops):
            continue
        end_facts = [f for f in c.L.facts if f.document == end.dst_document and f.section == end.dst_section and f.id in c.P and f.value.kind in NUMERIC]
        if not end_facts:
            continue
        earlier_docs = {hops[0].src_document, *(r.dst_document for r in hops[:-1])}
        earlier_concepts = {f.concept for f in c.L.facts if f.document in earlier_docs}
        on_subject = [f for f in end_facts if f.concept in earlier_concepts] or end_facts
        manual_hop = any(c.L.doc(r.dst_document).type == "manual" for r in hops)
        cands.append((cid, hops, sorted(on_subject, key=lambda f: h(cid, f.id))[0], manual_hop))
    cands.sort(key=lambda t: (not t[3], -len(t[1])))
    picked = cands[:COUNTS["chain"]]
    out = []
    for i, (cid, hops, f_end, _) in enumerate(picked, 1):
        src = c.L.doc(hops[0].src_document); src_sec = c.section_title.get((src.id, hops[0].src_section), hops[0].src_section)
        d_end = c.doc(f_end); via = c.L.doc(hops[0].dst_document).title
        # several chains leave the same provision (one per state), so the first hop's
        # destination is named to keep the questions distinct
        q = pick(cid, [
            f"{src.title}, {hops[0].src_section} ({src_sec}) defers to {via} (\"{hops[0].wording}\"). Follow that chain to its end: what {c.name(c.concept(f_end))} applies, and where is it set?",
            f"Starting from {src.title} {hops[0].src_section} and its pointer to {via}, follow each cross-reference until you reach the provision that actually sets the {c.name(c.concept(f_end))}. What is it?",
            f"Trace the reference chain that begins at {src.title} {hops[0].src_section}, passes through {via}, and give the {f_end.surface_form} the final provision sets.",
        ])
        out.append(example(f"chain-{i:02d}", "chain", q,
                           position=f"{len(hops)} hops ending at {d_end.title} {c.sec_label(d_end, f_end.section)}: {c.words(f_end.value)}.",
                           must_state=[c.prop(f_end)], must_not=c.neighbours(f_end, 1),
                           gold=[c.cite(f"ref:{r.id}") for r in hops] + [c.cite(f_end.id)], guidance=c.guidance([f_end]), editions=c.editions([f_end])))
    return out


def t_deep(c: Ctx) -> list[dict]:
    cands = [f for f in c.L.facts if f.id in c.P and c.P[f.id]["line_start"] > 2000 and f.value.kind in NUMERIC]
    facts = spread(cands, COUNTS["deep"], [lambda f: f.document, lambda f: f.concept, lambda f: c.P[f.id]["line_start"] // 2000], "deep")
    out = []
    for i, f in enumerate(facts, 1):
        d = c.doc(f); rule = c.sec_label(d, f.section)
        q = pick(f.id, [
            f"In the {d.title}, what {c.name(c.concept(f))} does {rule} ({c.sec_title(f)}) set?",
            f"Under {rule} of the {d.title}, what is the {f.surface_form}?",
            f"The {d.title} addresses {c.sec_title(f).lower()} in {rule}. What {f.surface_form} does it state?",
        ])
        out.append(example(f"deep-{i:02d}", "deep", q, position=f"{c.words(f.value).capitalize()} ({d.title}, {rule}, line {c.P[f.id]['line_start']}).",
                           must_state=[c.prop(f)], must_not=c.neighbours(f, 2), gold=[c.cite(f.id)], guidance=c.guidance([f])))
    return out


def t_abstain(c: Ctx) -> list[dict]:
    out = []
    pairs = [(d, s.distractor_concepts[j]) for d in c.L.documents if d.distractor for s in d.sections for j in range(len(s.distractor_concepts))]
    pairs = spread(pairs, 6, [lambda p: p[0].id, lambda p: p[1]], "abstain")
    for i, (d, cid) in enumerate(pairs, 1):
        con = c.L.concept(cid); real = sorted(c.by_concept[cid], key=lambda f: h(d.id, f.id))[0]
        q = pick(d.id + cid, [
            f"What {c.name(con)} does {d.title} set?",
            f"According to {d.title}, what is the {c.name(con)}?",
            f"Quote the {c.name(con)} from {d.title}.",
        ])
        out.append(example(f"abstain-{i:02d}", "abstain", q,
                           position=f"{d.title} discusses the concept but sets no value; the value is set elsewhere and must not be attributed to it.",
                           must_state=[], must_not=[f"{d.title} sets the {c.name(con)} at {c.words(real.value)}"], gold=[],
                           unresolved={"reason": ["no_governing_provision", "outside_corpus", "missing_document"], "document": d.path}))
    # a (line, state) amendatory form the corpus does not hold
    have = {(d.line, d.state) for d in c.L.documents if d.type == "amendatory"}
    lines = sorted({d.line for d in c.L.documents if d.type == "form"})
    missing = [(ln, st) for ln in lines for st in STATE_NAMES if (ln, st) not in have]
    for i, (ln, st) in enumerate(spread(missing, 2, [lambda p: p[0], lambda p: p[1]], "abstain-missing"), 7):
        con = c.L.concept("cancellation-notice-other-days")
        other = sorted([f for f in c.by_concept[con.id] if c.doc(f).type == "amendatory"], key=lambda f: h(ln, st, f.id))[0]
        q = f"What {c.name(con)} does the {STATE_NAMES[st]} amendatory endorsement to {ln} require?"
        out.append(example(f"abstain-{i:02d}", "abstain", q,
                           position=f"The corpus holds no {STATE_NAMES[st]} amendatory endorsement for {ln}.",
                           must_state=[], must_not=[f"the {STATE_NAMES[st]} amendatory endorsement to {ln} sets {c.words(other.value)}"], gold=[],
                           unresolved={"reason": ["outside_corpus", "missing_document"]}))
    return out


def bump(v: FactValue) -> FactValue:
    n = int(v.value)
    if v.kind == "money":
        new = n + max(500, (n // 2) // 500 * 500)
    elif v.kind == "percent":
        new = n + 5
    else:
        new = n + (10 if n >= 30 else 5)
    return FactValue(kind=v.kind, value=new)


def t_stale(c: Ctx) -> tuple[list[dict], list[dict]]:
    cands = []
    for f in contract_facts(c):
        d = c.doc(f); pl = c.P[f.id]
        if pl["line_start"] != pl["line_end"] or f.value.kind not in ("money", "percent", "days"):
            continue
        line = c.lines(d)[pl["line_start"] - 1]
        old = render_value(f.value, d.voice)
        if line.count(old) != 1 or value_occurrences(line, f.value) != 1:
            continue
        if not any(s <= pl["line_start"] <= e for s, e in c.claim_ranges.get(d.path, [])):
            continue  # nothing compiled cites this line, so nothing could go stale
        cands.append(f)
    facts = spread(cands, COUNTS["stale"], [lambda f: f.document, lambda f: f.concept, lambda f: c.doc(f).type], "stale")
    stale, control, edits = [], [], []
    for i, f in enumerate(facts, 1):
        d = c.doc(f); pl = c.P[f.id]; new = bump(f.value)
        old_text, new_text = render_value(f.value, d.voice), render_value(new, d.voice)
        q = pick(f.id, [
            f"Under {d.title}, what is the {f.surface_form}?",
            f"What {c.name(c.concept(f))} does {d.title} set in {f.section}?",
        ])
        lines_ = f"L{pl['line_start']}-L{pl['line_end']}"
        stale.append(example(f"stale-{i:02d}", "stale", q, sha_ref="stale",
                             position=f"The source now says {c.words(new)}; the compiled wiki still reflects {c.words(f.value)} and must be flagged stale.",
                             must_state=[c.prop(f, new)], must_not=[c.prop(f)], gold=[c.cite(f.id)], editions=c.editions([f]),
                             unresolved={"reason": "stale_claim", "document": d.path, "lines": lines_, "old_text": old_text, "new_text": new_text,
                                         "required_for": ["wiki", "wiki_graph"]}))
        control.append(example(f"stale-control-{i:02d}", "stale_control", q,
                               position=f"{c.words(f.value).capitalize()} ({d.title}, {f.section}).",
                               must_state=[c.prop(f)], must_not=[c.prop(f, new)], gold=[c.cite(f.id)], editions=c.editions([f])))
        edits.append({"path": d.path, "line": pl["line_start"], "old": old_text, "new": new_text, "fact": f.id})
    return stale + control, edits


# --- main -------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", required=True, help="corpus checkout at the main SHA the questions pin")
    ap.add_argument("--out", required=True, help="directory for questions.jsonl, stale_edits.json, manifest.json")
    ap.add_argument("--ledger", default=str(HERE / "ledger" / "data"))
    ap.add_argument("--placements", default=str(HERE / "out" / "placements.json"))
    a = ap.parse_args()

    corpus = pathlib.Path(a.corpus)
    sha = subprocess.run(["git", "-C", str(corpus), "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
    dirty = subprocess.run(["git", "-C", str(corpus), "status", "--porcelain", "--", "forms", "bulletins", "guidelines", "manuals", "memoranda", "training"],
                           capture_output=True, text=True).stdout.strip()
    if dirty:
        print("corpus checkout has uncommitted source changes; questions would pin a SHA that does not match", file=sys.stderr)
        return 1
    ledger = load(pathlib.Path(a.ledger))
    placements = json.load(open(a.placements))
    ci_path = corpus / ".claims-index.json"
    claims_index = json.load(open(ci_path)) if ci_path.exists() else None
    c = Ctx(ledger, placements, corpus, claims_index)

    examples: list[dict] = []
    for t in (t_single, t_composed, t_assembly, t_corpus_wide, t_disambiguation, t_synonym, t_chain, t_deep, t_abstain):
        examples += t(c)
    stale_examples, edits = t_stale(c)
    examples += stale_examples

    counts = collections.Counter(e["split"] for e in examples)
    short = {k: (v, counts.get(k, 0)) for k, v in COUNTS.items() if counts.get(k, 0) != v}
    seen: dict[tuple[str, str], str] = {}
    for e in examples:
        key = (e["question"], e["sha_ref"])
        if key in seen:
            print(f"duplicate question: {e['id']} repeats {seen[key]}", file=sys.stderr)
            return 1
        seen[key] = e["id"]

    out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)
    (out / "questions.jsonl").write_text("".join(json.dumps(e, ensure_ascii=False) + "\n" for e in examples))
    (out / "stale_edits.json").write_text(json.dumps(edits, indent=1))
    (out / "manifest.json").write_text(json.dumps({"main": sha, "counts": dict(counts), "splits": list(COUNTS)}, indent=1))
    print(f"wrote {len(examples)} examples -> {out}")
    for k, v in COUNTS.items():
        print(f"  {k:16} {counts.get(k, 0):3}{'' if counts.get(k, 0) == v else f'  (wanted {v})'}")
    if short:
        print("split counts short of the spec:", short, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
