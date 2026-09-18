# OpenWiki Insurance Corpus

A synthetic homeowners insurance corpus, used as the primary source layer for the OpenWiki
insurance POC. The current tree is the generated corpus (calibration slice first, then the full
~110 documents); the original sixteen hand-written documents are tagged `small-corpus-v1`. The proposal that motivates it lives in the sibling `openwiki-insurance-poc` repo
under `docs/poc-proposal.md`.

Nothing here is a real carrier's product, a real ISO form, or legal advice. Form numbers
deliberately resemble industry conventions so the corpus reads realistically, but all operative
language is invented.

## Layout

```
forms/{lob}/{state}/{form}/{edition}.md    frozen authority — never edited in place
bulletins/{state}/{id}.md                  frozen authority — regulator-issued
guidelines/{area}/{name}.md                living guidance — edited in place, continuously
manuals/{function}/{name}.md               living guidance — underwriting, claims, rating manuals
memoranda/{form}-{edition}.md              interpretation — filing memoranda on an edition change
training/{name}.md                         interpretation — training modules and customer FAQs
openwiki/INSTRUCTIONS.md                   the brief OpenWiki reads; never rewritten by a run
demo/                                      staged changes, ignored by OpenWiki
```

`{state}` is a two-letter code, or `MS` for multistate forms that apply everywhere unless a state
amendatory form overrides them.

The path is load-bearing. OpenWiki claims carry no domain attributes — the sidecar schema is
strict — so the evidence path is the only channel through which line of business, state, form,
and edition reach the retrieval layer.

## The two halves

**Frozen authority** (`forms/`, `bulletins/`) is never edited once issued. A revision is a *new
file* at a new edition. The prior edition stays exactly as it was, because it continues to govern
every policy written under it — a 2011 policy is still adjudicated against the 2011 form in 2026.

**Living guidance** (`guidelines/`, `manuals/`) is the carrier's own internal material. It is revised in
place, section by section, and changes far more often than forms do. This is the only half where
OpenWiki's relocation anchors ever fire.

## Conventions

**One paragraph per line. Never hard-wrap.** OpenWiki hashes evidence per line and uses three
lines of surrounding context to relocate a citation when text moves. Hard-wrapped legal text
produces many short, near-identical lines, which defeats that and yields false "unresolved"
flags. Long lines are correct here even though they look wrong in a narrow editor.

**Number every section, and keep numbering stable within an edition.** Claims cite sections by
name in their statement and by line range in their evidence; stable numbering is what makes a
citation legible to a human reviewer.

**Mark supersession explicitly.** When a new edition is issued, append a `> SUPERSEDED by ...`
block directly under the superseded file's title. OpenWiki detects byte changes, not semantic
supersession — this marker is what turns "a newer authority exists" into a signal it can act on.
Add only the marker; never alter operative text in a superseded file.

**Keep the worktree clean.** Any untracked file makes OpenWiki's no-op check bail to a full model
run. Commit or ignore everything before running `--update`.

## Running OpenWiki

```sh
openwiki --init      # first build; writes openwiki/ and openwiki/.claims/
openwiki --update    # incremental; a clean run is a proven no-op with zero model calls
openwiki visualize   # interactive graph over the generated wiki
```

## Current contents

The tree is generated from a fact ledger by the generator on this repo's orphan `generator`
branch (`git switch generator`; see its README). Every limit, period, percentage and cross-reference
in these documents was placed deliberately, and the ledger is the answer key for the evaluation
dataset in the sibling POC repo. The ledger and its placements are never committed to `main`, because
the retrieval agent reads this whole tree.

| Family | Documents | Notes |
| --- | --- | --- |
| `forms/` | HO-3 (2018-09, 2024-03), HO-6 (2023-02), seven endorsements in two editions each where paired, five state amendatory forms | ISO-style numbered provisions |
| `bulletins/` | TX ×3, FL ×2, IL ×1 | two superseded pairs |
| `guidelines/` | TX appetite, water-loss handling, referral matrix | living guidance |
| `manuals/` | underwriting manual (~10,000 lines) | rule-numbered chapters |
| `memoranda/` | HO-3 2024-03 filing memorandum | what changed and why |
| `training/` | water losses 101, roof claims, customer FAQ | interpretation; the FAQ carries no numbers |

Documents are cross-wired by design: endorsements write back or preserve base-form exclusions,
amendatory forms implement bulletins, guidelines and manual rules constrain when forms attach, and
memoranda and training restate positions the forms establish. That web is what makes a coverage
question resolve across several documents, and what a chunk-based retriever cannot follow.
