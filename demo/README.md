# Demo staging

Nothing in this folder is part of the initial corpus. These files are introduced *during* the
demo to trigger a real `openwiki --update` and show the change-propagation loop working.

Do not move them into `corpus/` before running `openwiki --init`.

## Step 3 — supersession and blast radius

1. Copy `HO-3/2022-03.md` to `corpus/forms/HO/MS/HO-3/2022-03.md`.
2. Copy `HO-04-95/2022-03.md` to `corpus/forms/HO/MS/HO-04-95/2022-03.md`.
3. Append the supersession block from `supersession-marker.md` to the top of
   `corpus/forms/HO/MS/HO-3/2018-09.md`, directly under the title. Change nothing else in that
   file.
4. Run `openwiki --update`.

What to expect: every claim citing the 2018-09 form flags `stale` because that file's bytes
changed. The Texas appetite guide and the claims-handling guidance both cite 2018-09 sections,
so the pages covering them are force-queued for review even though those guidance files were not
touched. That is the blast radius.

What should *not* happen: claims citing the 2011-05 edition must stay clean. That edition was
already marked superseded and was not touched, and it still governs the policies written under
it.

## Step 5 — relocation on a living document

Edit `corpus/guidelines/appetite/tx-homeowners.md` in place: change the roof age threshold in
G.2 from fifteen years to ten years, and separately insert a new paragraph into G.1 above it.

Run `openwiki --update`. The claim about the roof age threshold should flag `stale`. Claims about
G.3 water backup and G.5 prior losses should *not* flag, even though the inserted paragraph
shifted their line numbers. That is the relocation anchors working.
