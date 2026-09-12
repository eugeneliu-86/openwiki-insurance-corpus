#!/usr/bin/env bash
# Claims delta and .compile-state.json — enforces C4 of 00-contracts.md.
#
# The delta is SET ARITHMETIC over sidecar claim ids, captured before and after
# the compile. It depends on nothing OpenWiki prints, so a change to its console
# output cannot break it. Claim ids are stable across regeneration (97% carried
# over two forced rebuilds of an unchanged tree), so `carried` is a real signal.
#
#   claim-diff.sh snapshot <out-file>
#   claim-diff.sh emit <before> <after>                 # prints the claims block
#   claim-diff.sh write-state <before> <after> <outcome> <run-url> <attempt> <prev-compiled-from>
set -euo pipefail

claim_ids() {
  [ -d openwiki/.claims ] || return 0
  find openwiki/.claims -name '*.json' -exec jq -r '.claims[].id' {} + | sort -u
}

emit_claims() {
  local before="$1" after="$2"
  local added retracted carried total
  added=$(comm -13 "$before" "$after" | wc -l | tr -d ' ')
  retracted=$(comm -23 "$before" "$after" | wc -l | tr -d ' ')
  carried=$(comm -12 "$before" "$after" | wc -l | tr -d ' ')
  total=$(wc -l < "$after" | tr -d ' ')
  # C4 invariant. A mismatch means the sidecars were read mid-write or one
  # failed to parse, and the state file must not be published.
  if [ "$(( added + carried ))" -ne "$total" ]; then
    echo "FATAL: added($added) + carried($carried) != total($total)" >&2
    exit 1
  fi
  jq -n --argjson total "$total" --argjson added "$added" \
        --argjson retracted "$retracted" --argjson carried "$carried" \
        '{total: $total, added: $added, retracted: $retracted, carried: $carried}'
}

case "${1:-}" in
  snapshot)
    out="${2:?usage: claim-diff.sh snapshot <out-file>}"
    claim_ids > "$out"
    echo "captured $(wc -l < "$out" | tr -d ' ') claim ids -> $out" >&2
    ;;

  emit)
    emit_claims "${2:?before}" "${3:?after}"
    ;;

  write-state)
    before="${2:?before}"; after="${3:?after}"; outcome="${4:?outcome}"
    run_url="${5:?run-url}"; attempt="${6:?attempt}"; prev="${7:-}"; mode="${8:-normal}"
    head="$(git rev-parse HEAD)"

    if [ ! -f openwiki/.last-update.json ]; then
      # `failed` is OURS: the process died before OpenWiki wrote its metadata,
      # so there is no gitHead to assert against and the output may not exist.
      # `claims` is OMITTED, not zeroed — zero added and zero retracted is a
      # true statement about a no-op run and a false one about a run that
      # never happened.
      jq -n --arg head "$head" --arg at "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
            --argjson attempts "$attempt" --arg url "$run_url" \
            '{schema_version: 1, compiled_from: $head, status: "failed", compiled_at: $at,
              attempts: $attempts, workflow_run_url: $url, changed_sources: []}' \
        > .compile-state.json
      echo "compile FAILED before writing metadata; state recorded" >&2
      exit 0
    fi

    ow_head="$(jq -r .gitHead openwiki/.last-update.json)"
    ow_status="$(jq -r .status openwiki/.last-update.json)"
    # C4: compiled_from is ASSERTED equal to what OpenWiki recorded, not copied
    # hopefully. A mismatch means the compile ran against a different tree than
    # the one being committed, and every downstream answer would be pinned to a
    # commit that does not contain what it claims.
    if [ "$ow_head" != "$head" ]; then
      echo "FATAL: OpenWiki documented $ow_head but HEAD is $head" >&2
      exit 1
    fi
    case "$ow_status" in complete|interrupted) ;; *) ow_status="complete" ;; esac
    # An interrupted OpenWiki run exits non-zero and leaves status=interrupted.
    # A non-zero exit WITH metadata written and status=complete is still a
    # failure of the step — surface it rather than launder it as complete.
    if [ "$outcome" = "failure" ] && [ "$ow_status" = "complete" ]; then
      ow_status="interrupted"
    fi

    changed="[]"
    if [ -n "$prev" ] && git cat-file -e "$prev^{commit}" 2>/dev/null; then
      changed=$(git diff --name-only "$prev" "$head" -- forms bulletins guidelines | jq -R . | jq -s 'unique')
    fi

    jq -n --arg head "$head" --arg status "$ow_status" \
          --arg at "$(date -u +%Y-%m-%dT%H:%M:%SZ)" --argjson attempts "$attempt" \
          --arg url "$run_url" --argjson claims "$(emit_claims "$before" "$after")" \
          --argjson changed "$changed" --arg mode "$mode" \
          '{schema_version: 1, compiled_from: $head, status: $status, compiled_at: $at,
            attempts: $attempts, workflow_run_url: $url, claims: $claims, changed_sources: $changed,
            compile_mode: $mode}' \
      > .compile-state.json

    # C4 tier 2: validate BEFORE the commit, so an invalid file is never pushed.
    python3 scripts/validate-compile-state.py .compile-state.json
    echo "wrote .compile-state.json: $(jq -c '{status, claims}' .compile-state.json)" >&2
    ;;

  *)
    echo "usage: claim-diff.sh {snapshot <out>|emit <before> <after>|write-state ...}" >&2
    exit 2
    ;;
esac
