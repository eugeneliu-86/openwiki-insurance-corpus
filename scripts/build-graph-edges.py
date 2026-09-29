#!/usr/bin/env python3
"""Build .graph-edges.json from the working tree.

The edges the corpus states (claim → provision, provision → referenced section,
edition → edition, amendatory → base form, index → page) plus node labels.
Deterministic, and built with the agent's vendored module.
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "vendor"))

from corpus.claims import scan_sidecars  # noqa: E402
from corpus.edges import build_edges, dumps  # noqa: E402
from corpus.loader import load_corpus  # noqa: E402


def main() -> int:
    root = pathlib.Path.cwd()
    sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
    corpus = load_corpus(root, sha, None)
    pindex = json.loads((root / ".provisions-index.json").read_text())
    art = build_edges(corpus, sha, pindex, scan_sidecars(corpus))
    (root / ".graph-edges.json").write_text(dumps(art))
    print(f"wrote .graph-edges.json: {art['counts']}; {len(art['unresolved'])} unresolved reference(s); {len(art['labels'])} labels "
          f"(vendored from poc {(HERE / 'vendor' / 'VENDORED_FROM').read_text().strip()[:12]})", file=sys.stderr)
    for u in art["unresolved"][:20]:
        print(f"  unresolved: {u['from']}: {u['text']} — {u['why']}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
