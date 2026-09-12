#!/usr/bin/env python3
"""Build .claims-index.json (C11) from the sidecars in the working tree.

Runs in the workflow AFTER the compile and BEFORE the commit, so it reads the
working tree — the new sidecars are not committed yet. It imports the vendored
phase 02 modules rather than reimplementing interval arithmetic and the synonym
map: a second implementation would disagree with the first on exactly the hard
cases, and would inherit none of the tests that pin them.
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "vendor"))

from tools.claims_index import ClaimsIndex, _scan_sidecars, to_committed  # noqa: E402
from tools.corpus_local import _load  # noqa: E402


def main() -> int:
    root = pathlib.Path.cwd()
    sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
    # The production loader over the working tree: same LF-only split rule the
    # tools use, so line numbers in the index agree with the anchors.
    corpus = _load(root, sha, None)
    index = ClaimsIndex(corpus_sha=sha, claims=_scan_sidecars(corpus))
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
