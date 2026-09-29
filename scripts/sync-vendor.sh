#!/usr/bin/env bash
# Copy the agent's corpus modules from the poc repo into scripts/vendor/.
#
# Vendored because the poc repo is private: the workflow cannot clone it
# without a credential. VENDORED_FROM records the poc commit, and the poc's
# agent/tests/test_vendored_copy.py fails as soon as the copies differ.
#
#   scripts/sync-vendor.sh [path-to-poc-repo]
set -euo pipefail
POC="${1:-../openwiki-insurance-poc}"
here="$(cd "$(dirname "$0")" && pwd)"
rm -rf "$here/vendor/contracts" "$here/vendor/corpus" "$here/vendor/tools"
for rel in contracts/__init__.py contracts/corpus_manifest.py contracts/corpus_paths.py \
           contracts/evidence_anchor.py contracts/relation_types.py \
           corpus/__init__.py corpus/snapshot/__init__.py corpus/snapshot/loader.py \
           corpus/indexes/__init__.py corpus/indexes/claims.py corpus/indexes/edges.py corpus/indexes/provisions.py; do
  mkdir -p "$here/vendor/$(dirname "$rel")"
  cp "$POC/agent/$rel" "$here/vendor/$rel"
done
git -C "$POC" rev-parse HEAD > "$here/vendor/VENDORED_FROM"
echo "vendored from poc $(cat "$here/vendor/VENDORED_FROM")"
