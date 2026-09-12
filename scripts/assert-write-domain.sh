#!/usr/bin/env bash
# The refresh workflow may write openwiki/**, .compile-state.json and
# .claims-index.json, and NOTHING else (C5). The scaffold this replaced staged
# AGENTS.md, CLAUDE.md and its own workflow file. Run after `git add`.
set -euo pipefail
stray=$(git diff --cached --name-only | grep -vE '^(openwiki/|\.compile-state\.json$|\.claims-index\.json$)' || true)
# The human-owned brief is inside openwiki/ but is never the workflow's to change.
brief=$(git diff --cached --name-only | grep -x 'openwiki/INSTRUCTIONS.md' || true)
if [ -n "$stray$brief" ]; then
  echo "FATAL: refresh workflow would commit outside its write domain:" >&2
  printf '  %s\n' $stray $brief >&2
  exit 1
fi
echo "write domain ok: $(git diff --cached --name-only | wc -l | tr -d ' ') paths, all inside openwiki/ + state files" >&2
