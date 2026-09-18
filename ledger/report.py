"""Requirement report: R1–R10 of corpus-expansion/00 §2, computed from the
ledger alone (what can be known before prose exists). Prints
requirement → count → pass/fail and exits non-zero on any failure.

    uv run python -m ledger.report [ledger-dir]
"""
from __future__ import annotations

import sys
from collections import Counter, defaultdict

from .schema import FRONT_MATTER_LINES, Ledger, load

REQUIREMENTS = {
    "R1 ambiguous concepts (>=12, each in >=25 documents)": 12,
    "R2 synonym concepts (>=20 with >=3 forms, >=2 forms used by facts)": 20,
    "R3a chains depth 2 (>=15)": 15,
    "R3b chains depth 3 (>=8)": 8,
    "R3c chains crossing documents (>=6)": 6,
    "R3d chains with a manual hop beyond line 3000 (>=4)": 4,
    "R4a facts beyond line 2000 (>=40)": 40,
    "R4b facts beyond line 6000 (>=15)": 15,
    "R5 distractor documents (>=10)": 10,
    "R6a form edition pairs with 15-25 changes (all)": None,
    "R6b renumberings (>=5)": 5,
    "R7a contradictions (>=10)": 10,
    "R7b superseded bulletins (>=6)": 6,
    "R8 compositions spanning >=4 documents (>=20)": 20,
    "R9 dated histories (>=12)": 12,
    "inventory: documents (>=100)": 100,
    "inventory: average target lines (>=1000)": 1000,
    "inventory: documents >=5000 lines (>=3)": 3,
    "inventory: facts (>=900)": 900,
}


def appearances(ledger: Ledger) -> dict[str, set[str]]:
    """concept -> documents where it appears, by fact or by distractor mention."""
    out: dict[str, set[str]] = defaultdict(set)
    for f in ledger.facts:
        out[f.concept].add(f.document)
    for d in ledger.documents:
        for s in d.sections:
            for c in s.distractor_concepts:
                out[c].add(d.id)
    return out


def chain_stats(ledger: Ledger):
    chains: dict[str, list] = defaultdict(list)
    for r in ledger.references:
        chains[r.chain].append(r)
    d2 = d3 = cross = manual_deep = 0
    for refs in chains.values():
        depth = len(refs)
        if depth == 2:
            d2 += 1
        if depth >= 3:
            d3 += 1
        if any(r.src_document != r.dst_document for r in refs):
            cross += 1
        for r in refs:
            dst = ledger.doc(r.dst_document)
            if dst.type == "manual" and r.dst_section and dst.section_starts().get(r.dst_section, 0) > 3000:
                manual_deep += 1
                break
    return d2, d3, cross, manual_deep


def counts(ledger: Ledger) -> dict[str, tuple[float, bool, str]]:
    app = appearances(ledger)
    r1 = [c.id for c in ledger.concepts if c.ambiguous and len(app[c.id]) >= 25]
    r1_short = [f"{c.id}({len(app[c.id])})" for c in ledger.concepts if c.ambiguous and len(app[c.id]) < 25]
    forms_used: dict[str, set[str]] = defaultdict(set)
    for f in ledger.facts:
        forms_used[f.concept].add(f.surface_form)
    r2 = [c.id for c in ledger.concepts if c.synonym_target and len(forms_used[c.id]) >= 2]
    d2, d3, cross, mdeep = chain_stats(ledger)
    starts = {d.id: d.section_starts() for d in ledger.documents}
    deep2000 = sum(1 for f in ledger.facts if starts[f.document][f.section] > 2000)
    deep6000 = sum(1 for f in ledger.facts if starts[f.document][f.section] > 6000)
    distractors = [d.id for d in ledger.documents if d.distractor]
    # R6 is about full policy-form editions. Endorsement and amendatory
    # revisions are recorded as diffs too (questions use them) but are small.
    pair_ok = [(e.older, len(e.changed) + len(e.added) + len(e.removed)) for e in ledger.editions if ledger.doc(e.older).type == "form"]
    bad_pairs = [f"{o}({n})" for o, n in pair_ok if not 15 <= n <= 25]
    renum = sum(len(e.renumbered) for e in ledger.editions)
    superseded = sum(1 for d in ledger.documents if d.type == "bulletin" and d.superseded_by)
    comps = [c.id for c in ledger.compositions if len({ledger.fact(f).document for f in c.facts}) >= 4]
    n_docs = len(ledger.documents)
    avg = sum(d.target_lines for d in ledger.documents) / max(1, n_docs)
    long_docs = [d.id for d in ledger.documents if d.target_lines >= 5000]
    out = {
        "R1 ambiguous concepts (>=12, each in >=25 documents)": (len(r1), len(r1) >= 12, f"short: {r1_short}" if r1_short else ""),
        "R2 synonym concepts (>=20 with >=3 forms, >=2 forms used by facts)": (len(r2), len(r2) >= 20, ""),
        "R3a chains depth 2 (>=15)": (d2, d2 >= 15, ""),
        "R3b chains depth 3 (>=8)": (d3, d3 >= 8, ""),
        "R3c chains crossing documents (>=6)": (cross, cross >= 6, ""),
        "R3d chains with a manual hop beyond line 3000 (>=4)": (mdeep, mdeep >= 4, ""),
        "R4a facts beyond line 2000 (>=40)": (deep2000, deep2000 >= 40, ""),
        "R4b facts beyond line 6000 (>=15)": (deep6000, deep6000 >= 15, ""),
        "R5 distractor documents (>=10)": (len(distractors), len(distractors) >= 10, ""),
        "R6a form edition pairs with 15-25 changes (all)": (len(pair_ok) - len(bad_pairs), not bad_pairs and bool(pair_ok), f"out of range: {bad_pairs}" if bad_pairs else f"{len(pair_ok)} pairs"),
        "R6b renumberings (>=5)": (renum, renum >= 5, ""),
        "R7a contradictions (>=10)": (len(ledger.contradictions), len(ledger.contradictions) >= 10, ""),
        "R7b superseded bulletins (>=6)": (superseded, superseded >= 6, ""),
        "R8 compositions spanning >=4 documents (>=20)": (len(comps), len(comps) >= 20, ""),
        "R9 dated histories (>=12)": (len(ledger.histories), len(ledger.histories) >= 12, ""),
        "inventory: documents (>=100)": (n_docs, n_docs >= 100, ""),
        "inventory: average target lines (>=1000)": (round(avg), avg >= 1000, f"total {sum(d.target_lines for d in ledger.documents)}"),
        "inventory: documents >=5000 lines (>=3)": (len(long_docs), len(long_docs) >= 3, ", ".join(long_docs)),
        "inventory: facts (>=900)": (len(ledger.facts), len(ledger.facts) >= 900, f"{len(ledger.concepts)} concepts, {len(ledger.definitions)} definitions, {len(ledger.references)} references"),
    }
    return out


def by_type(ledger: Ledger) -> list[tuple[str, int, int, int]]:
    rows = defaultdict(lambda: [0, 0, 0])
    nfacts = Counter(f.document for f in ledger.facts)
    for d in ledger.documents:
        rows[d.type][0] += 1
        rows[d.type][1] += d.target_lines
        rows[d.type][2] += nfacts[d.id]
    return [(t, n, lines, facts) for t, (n, lines, facts) in sorted(rows.items())]


def main(argv: list[str]) -> int:
    ledger = load(argv[1] if len(argv) > 1 else "ledger/data")
    ok_all = True
    print(f"{'requirement':70s} {'count':>6s}  status")
    for req, (n, ok, note) in counts(ledger).items():
        ok_all &= ok
        print(f"{req:70s} {n:>6}  {'PASS' if ok else 'FAIL'}  {note}")
    print()
    print(f"{'type':12s} {'docs':>5s} {'lines':>7s} {'facts':>6s}")
    for t, n, lines, facts in by_type(ledger):
        print(f"{t:12s} {n:>5d} {lines:>7d} {facts:>6d}")
    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
