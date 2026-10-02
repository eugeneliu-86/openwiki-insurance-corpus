#!/usr/bin/env bash
# Undo the ingests a compile just covered, right after it lands: one [skip ci]
# commit restoring their source documents and the compiled outputs to the tree
# before the first of them, as the poc's Reset button does. The wiki is already
# compiled against that tree, so nothing needs recompiling.
#
#   scripts/reset-ingests.sh <previous compiled_from>
#
# Refuses (exits 0, resets nothing) when a source document outside the ingests
# changed in the range: undoing the ingests underneath it would leave the wiki
# compiled against neither tree. The reset commit names each ingest id (from the
# ingest commits' Ingest-Id trailer) so the poc's API can mark them reset.
set -euo pipefail

prev="${1:-}"
SOURCES=(forms bulletins guidelines manuals memoranda training)
OUTPUTS=(openwiki .compile-state.json .claims-index.json .provisions-index.json .graph-edges.json)
HUMAN_OWNED='^openwiki/INSTRUCTIONS\.md$'

range="HEAD"
if [ -n "$prev" ] && git cat-file -e "$prev^{commit}" 2>/dev/null; then range="$prev..HEAD"; fi
ingests=$(git log --reverse --format=%H --grep='^ingest: ' "$range" -- "${SOURCES[@]}")
if [ -z "$ingests" ]; then echo "no ingest in this compile; nothing to reset"; exit 0; fi

first=$(head -1 <<<"$ingests")
pre=$(git rev-parse "$first^")
mine=$(for c in $ingests; do git diff-tree --no-commit-id --name-only -r "$c"; done | sort -u)
changed=$(git diff --name-only "$pre" HEAD -- "${SOURCES[@]}" | sort -u)
others=$(comm -23 <(printf '%s\n' "$changed") <(printf '%s\n' "$mine") | sed '/^$/d')
if [ -n "$others" ]; then
  echo "not resetting: source documents outside the ingests changed since ${pre:0:12}:"
  printf '  %s\n' $others
  exit 0
fi

restore=$({ printf '%s\n' "$changed"; git diff --name-only "$pre" HEAD -- "${OUTPUTS[@]}"; } | sed '/^$/d' | grep -Ev "$HUMAN_OWNED" | sort -u)
while read -r p; do
  if git cat-file -e "$pre:$p" 2>/dev/null; then git checkout -q "$pre" -- "$p"; else git rm -q -- "$p"; fi
done <<<"$restore"

ids=$(for c in $ingests; do git log -1 --format=%B "$c" | sed -n 's/^Ingest-Id:[[:space:]]*//p'; done | paste -sd' ' -)
git commit -q -m "reset: restore ${pre:0:12} after ingest ${ids:-(no id)} [skip ci]" \
  -m "undoes $(wc -l <<<"$ingests" | tr -d ' ') ingest commit(s), first ${first:0:12}; restores $(wc -l <<<"$restore" | tr -d ' ') paths to their bytes at ${pre:0:12}"

# A commit that landed meanwhile: a source change means the reset no longer
# applies cleanly to what is there, so stop; anything else, replay on top.
for attempt in 1 2 3; do
  if git push --quiet; then echo "reset landed: $(git rev-parse --short HEAD) restores ${pre:0:12} after ${ids:-the ingests}"; exit 0; fi
  git fetch --quiet origin main
  if [ -n "$(git diff --name-only HEAD~1 origin/main -- "${SOURCES[@]}")" ]; then
    echo "not resetting: a newer push changed source documents" >&2; exit 0
  fi
  git rebase --quiet origin/main || { git rebase --abort; break; }
done
echo "could not land the reset after 3 attempts" >&2
exit 1
