#!/usr/bin/env python3
"""Build .graph-edges.json from the working tree (graph-expansion ph. 02).

The edges the corpus states — claim → provision, provision → referenced section,
edition → edition, amendatory → base form, index → page — plus node labels.
Deterministic, no model: a pure function of the tree, the claims index and the
provisions index. Imports the vendored agent module so the committed artifact
and the one the agent builds in memory are the same bytes.
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "vendor"))

from tools.claims_index import _scan_sidecars  # noqa: E402
from tools.corpus_local import _load  # noqa: E402
from tools.edges import build_edges, dumps  # noqa: E402


def main() -> int:
    root = pathlib.Path.cwd()
    sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
    corpus = _load(root, sha, None)
    pindex = json.loads((root / ".provisions-index.json").read_text())
    art = build_edges(corpus, sha, pindex, _scan_sidecars(corpus))
    (root / ".graph-edges.json").write_text(dumps(art))
    print(f"wrote .graph-edges.json: {art['counts']}; {len(art['unresolved'])} unresolved reference(s); {len(art['labels'])} labels "
          f"(vendored from poc {(HERE / 'vendor' / 'VENDORED_FROM').read_text().strip()[:12]})", file=sys.stderr)
    for u in art["unresolved"][:20]:
        print(f"  unresolved: {u['from']}: {u['text']} — {u['why']}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
