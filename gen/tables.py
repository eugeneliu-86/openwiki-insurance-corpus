"""Code-generated tables and schedules. Ph. 02 §3.

The rating manual is almost entirely this: thousands of near-identical rows,
which is what a rating manual is and is distractor mass by design. Rows are
seeded by section id so the same ledger yields the same table.
"""
from __future__ import annotations

import hashlib
import random

import _paths  # noqa: F401
from ledger.schema import Document, Ledger, Section


TERRITORIES = [f"{n:03d}" for n in range(1, 61)]
CONSTRUCTION = ["Frame", "Masonry Veneer", "Masonry", "Superior"]
PC = list(range(1, 11))


def _rng(seed: str) -> random.Random:
    return random.Random(int(hashlib.sha256(seed.encode()).hexdigest(), 16) % (2**32))


def table_for(ledger: Ledger, doc: Document, sec: Section, target_lines: int) -> str:
    """Markdown for a table section: the planted facts as sentences first (so
    they have a line), then rows to fill the target length."""
    rng = _rng(f"{doc.id}/{sec.id}")
    lines: list[str] = []
    for fid in sec.facts:
        f = ledger.fact(fid)
        # a marker, not a value: assembly fills it and records the placement like any slot
        lines.append(f"The {f.surface_form} used throughout this part is {{{{fact:{fid}}}}}.")
        lines.append("")
    for cid in sec.distractor_concepts:
        c = ledger.concept(cid)
        lines.append(f"Where a row refers to the {c.synonyms[0] if c.synonyms else c.canonical}, apply the factor to the premium developed before that adjustment.")
        lines.append("")
    title = sec.title.lower()
    if "base rate" in title:
        lines += ["| Territory | Construction | Protection Class | Base Rate |", "|---|---|---|---|"]
        rows = max(10, target_lines - len(lines) - 2)
        for i in range(rows):
            lines.append(f"| {TERRITORIES[i % len(TERRITORIES)]} | {CONSTRUCTION[(i // len(TERRITORIES)) % 4]} | {PC[(i // 7) % 10]} | ${rng.randint(180, 2400):,} |")
    elif "endorsement premium" in title:
        lines += ["| Endorsement | Option | Premium Basis | Charge |", "|---|---|---|---|"]
        ends = [d for d in ledger.documents if d.type == "endorsement"]
        rows = max(10, target_lines - len(lines) - 2)
        for i in range(rows):
            e = ends[i % len(ends)]
            lines.append(f"| {e.title.split(' (')[0]} | Option {chr(65 + (i // len(ends)) % 6)} | {'flat' if i % 3 else 'per $1,000 of limit'} | ${rng.randint(8, 420):,} |")
    elif "increased limits" in title:
        lines += ["| Coverage | Increment | Factor |", "|---|---|---|"]
        rows = max(10, target_lines - len(lines) - 2)
        for i in range(rows):
            lines.append(f"| {'Coverage ' + 'ABCDEF'[i % 6]} | +${(i % 40 + 1) * 1000:,} | {1 + rng.randint(1, 900) / 1000:.3f} |")
    else:
        lines += ["| Item | Condition | Factor |", "|---|---|---|"]
        rows = max(8, target_lines - len(lines) - 2)
        for i in range(rows):
            lines.append(f"| Item {i + 1} | {rng.choice(['applies', 'does not apply', 'applies with inspection', 'applies in coastal territories'])} | {rng.randint(70, 130) / 100:.2f} |")
    return "\n".join(lines)
