"""Build the corpus from the ledger. Ph. 02 §1, §7.

    uv run --env-file ../agent/.env python build.py --out ../../openwiki-insurance-corpus   # a clone of THE corpus repo
    uv run python build.py --out /tmp/corpus --fake                 # no model: deterministic filler, for pipeline checks
    uv run python build.py --out /tmp/slice --documents form.ho3.2024-03 manual.underwriting … --fake
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys
import time

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import _paths  # noqa: E402,F401
from gen import assemble, draft, plan, validate  # noqa: E402
from ledger import author  # noqa: E402
from ledger.schema import load  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True, help="directory to write the corpus tree into: a local clone of openwiki-insurance-corpus (the same repo the small corpus lives in)")
    ap.add_argument("--ledger", default=str(HERE / "ledger" / "data"))
    ap.add_argument("--documents", nargs="*", default=None, help="document ids to build (default: all)")
    ap.add_argument("--fake", action="store_true", help="deterministic filler instead of the model")
    ap.add_argument("--no-cache", action="store_true")
    ap.add_argument("--concurrency", type=int, default=8)
    ap.add_argument("--no-validate", action="store_true")
    args = ap.parse_args(argv)

    ledger = load(args.ledger) if pathlib.Path(args.ledger).exists() else author.author()
    docs = ledger.documents if not args.documents else [ledger.doc(d) for d in args.documents]
    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    jobs = [j for d in docs for j in plan.jobs_for(ledger, d)]
    print(f"{len(docs)} documents, {len(jobs)} sections, {sum(1 for j in jobs for _ in j.slots)} slots; drafter={'fake' if args.fake else draft.MODEL}")
    t0 = time.time()
    drafter = draft.fake_drafter if args.fake else draft.real_drafter
    drafts = draft.draft_all(jobs, drafter=drafter, concurrency=args.concurrency, cache=not args.no_cache)
    print(f"drafted in {time.time() - t0:.0f}s")

    placements = assemble.build_documents(ledger, docs, drafts, out)
    pl_path = HERE / "out" / "placements.json"
    assemble.write_placements(placements, pl_path)
    (HERE / "out" / "manifest.json").write_text(json.dumps({j.document + "/" + j.section: j.hash() for j in jobs}, indent=1))
    lines = sum((out / d.path).read_text().count("\n") for d in docs)
    print(f"wrote {len(docs)} files, {lines} lines, {len(placements)} placements -> {out}")

    if args.no_validate:
        return 0
    results = validate.run_all(ledger, out, placements, only_documents={d.id for d in docs} if args.documents else None)
    failed = 0
    for v, errs in sorted(results.items()):
        print(f"{v}: {'PASS' if not errs else f'{len(errs)} problems'}")
        for e in errs[:12]:
            print("   " + e)
        failed += len(errs)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
