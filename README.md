# Corpus generator (orphan branch `generator`)

This branch holds the fact ledger, the hybrid generator and the validators
that build the corpus on `main`. It is an orphan branch on purpose: nothing
here is ever in `main`'s tree, so no commit the agent fetches contains the
ledger — which is the answer key to every evaluation question.

Specs: `docs/specs/corpus-expansion/` in the POC repo (openwiki-insurance-poc).

```bash
uv sync
uv run python -m ledger.author                 # regenerate ledger/data/*.yaml and print the requirement report
uv run pytest                                  # loader, renderer, drafter checks, a fake-drafted slice through V1-V9
uv run python build.py --out /tmp/corpus --fake                       # whole corpus, deterministic filler, no model
uv run --env-file ../openwiki-insurance-poc/agent/.env python build.py --out ../openwiki-insurance-corpus   # real drafts into a main worktree
```

Layout: `ledger/` (schema, author, report, data), `gen/` (plan, voices, draft,
render, tables, assemble, validate), `build.py`, `tests/`, `vendor/contracts/`
(the two POC contracts this needs, at the commit in `vendor/VENDORED_FROM`).

Never commit `out/placements.json` or `.draft-cache/` to `main`.
