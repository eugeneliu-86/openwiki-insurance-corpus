# Supersession marker

Insert the block below into `forms/HO/MS/HO-3/2018-09.md`, on the line directly after the title
and before the "Multistate. Effective for..." line. Change nothing else in that file — no
operative text, no section numbering, no whitespace elsewhere.

```markdown
> SUPERSEDED by HO-3 edition 2022-03 for policies written on or after 2022-03-01.
> This edition remains in force for policies written under it and governs the adjustment of any
> loss occurring under such a policy, regardless of when that loss is reported.
```

The result should match the marker already present at the top of
`forms/HO/MS/HO-3/2011-05.md`, which was superseded by the 2018-09 edition.

## Why this is the whole trick

OpenWiki detects that the bytes of a cited file changed. It has no concept of one document
superseding another. Without this marker the 2018-09 file is untouched when the 2022-03 edition
lands, every claim citing it stays clean, and the Texas appetite guide goes on citing a
superseded form with nothing anywhere flagging it.

Adding three lines to the header changes that file's bytes, which flags every claim citing it,
which force-queues every page reasoning about that edition. That is how a semantic event —
supersession — gets converted into the only signal the tool can act on.
