#!/usr/bin/env python3
"""Build .claims-index.json from the sidecars in the working tree.

Runs after the compile and before the commit, using the agent's own vendored
modules, so the committed index and the one the agent builds are the same.
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "vendor"))

from corpus.claims import ClaimsIndex, scan_sidecars, to_committed  # noqa: E402
from corpus.loader import load_corpus  # noqa: E402


def main() -> int:
    root = pathlib.Path.cwd()
    sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
    corpus = load_corpus(root, sha, None)     # the agent's loader, so line numbers agree with the anchors
    index = ClaimsIndex(corpus_sha=sha, claims=scan_sidecars(corpus))
    data = to_committed(index, corpus)
    (root / ".claims-index.json").write_text(json.dumps(data, indent=1, sort_keys=False) + "\n")
    print(
        f"wrote .claims-index.json: {data['claim_count']} claims, "
        f"{data['evidence_count']} pointers, {len(data['resources'])} resources, "
        f"{len(data['relations'])} relation edges (vendored from poc "
        f"{(HERE / 'vendor' / 'VENDORED_FROM').read_text().strip()[:12]})",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
