#!/usr/bin/env python3
"""Build .provisions-index.json from the working tree (graph-expansion ph. 01, tier 1).

Every numbered paragraph of every source document, with its section, line
range and text hash. Deterministic, no model: a pure function of the tree at
HEAD, so it runs on every refresh whether or not the compile changed anything.
Imports the vendored agent module so the committed index and the one the agent
builds in memory are the same bytes.
"""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "vendor"))

from tools.corpus_local import _load  # noqa: E402
from tools.provisions import build_provisions_index, dumps  # noqa: E402


def main() -> int:
    root = pathlib.Path.cwd()
    sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
    corpus = _load(root, sha, None)
    index = build_provisions_index(corpus, sha)
    (root / ".provisions-index.json").write_text(dumps(index))
    n_docs = len(index["sections"])
    print(f"wrote .provisions-index.json: {len(index['provisions'])} provisions in {n_docs} documents (vendored from poc "
          f"{(HERE / 'vendor' / 'VENDORED_FROM').read_text().strip()[:12]})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
