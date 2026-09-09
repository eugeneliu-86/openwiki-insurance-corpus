---
type: Coverage knowledge brief
title: Coverage Wiki Instructions
description: Guidance for building and maintaining a grounded coverage wiki over a homeowners policy corpus, for use by underwriters, claims adjusters, and the agents that assist them.
tags: [insurance, coverage, underwriting, claims, policy-forms]
---

A coverage knowledge wiki for this homeowners policy corpus. The audience is an underwriter or a claims adjuster who needs to answer a coverage question correctly and defensibly, and the agents that assist them.

## What to organize by

Organize by coverage part first (Coverage A dwelling, B other structures, C personal property, D loss of use, E liability, F medical payments), then by peril or subject within it, then by state overlay. Give exclusions and their write-backs their own pages where the interaction is material — water damage and roof settlement both warrant dedicated pages.

Give the carrier's internal underwriting guidance its own top-level area, separate from contract language. Guidance is not part of any policy and must never be presented as though it were. Where guidance depends on a form provision, say so explicitly and cite both.

## Page types

Every page must declare a `type` in its front matter, chosen from exactly this list and written verbatim in lower case. Do not invent new values, do not add qualifiers, and do not describe the page in the type field.

- `coverage` — what the contract covers, excludes, or writes back, and on what settlement basis. Use this for every page derived primarily from a policy form or endorsement.
- `underwriting-guidance` — the carrier's own rules about which risks it will write, at what limit, and at what authority level.
- `claims-guidance` — the carrier's own rules about how a loss is investigated, adjudicated, and settled.
- `state-overlay` — a requirement imposed by a state regulator, and the amendatory form that implements it.
- `policy-assembly` — how editions, endorsements, and state overlays combine to produce the terms governing a particular policy.

The type carries the distinction between contract language, internal guidance, and regulatory constraint. That distinction is the most important thing a reader needs and the only one the type field is for, so keep it clean. A page that could plausibly take two types takes the one matching the document it is primarily derived from.

Section index pages do not declare a type.

## What counts as a material proposition

Document what changes an underwriting decision, a claim decision, or an operational expectation. Specifically: what a coverage part covers and excludes; the exact conditions under which an exclusion is written back by an endorsement; sublimits, deductibles, and how they interact; loss settlement basis and when it changes; the edition and state variations that govern a given policy; referral triggers and authority levels; and the notice, proof, and time-limit conditions an insured must satisfy.

Do not document that a section exists, that a form has a number, or that a definition is present. Apply this test: if the proposition were false, would it change how a reader underwrites a risk, adjudicates a claim, or advises an insured? If not, leave it out.

## Grounding rules

Every material proposition must cite the exact section of the exact document that establishes it. Prefer a narrow line range over a whole file.

Never paraphrase policy language in a way that changes its legal meaning. Where a coverage outcome turns on a specific phrase — "sudden and accidental", "directly or indirectly", "whether or not driven by wind" — quote that phrase verbatim in the prose rather than restating it.

When a proposition depends on more than one document, cite all of them. A coverage position that composes a base form exclusion with an endorsement write-back is one proposition supported by two pieces of evidence, not two propositions.

## Document relationships

Most material propositions in this corpus compose two documents: an exclusion in
one and an endorsement, amendatory form, bulletin, or internal rule that acts on
it. When a proposition composes documents this way, state the relationship
explicitly, with a direction and one of the verbs below used verbatim.

Name the **acting** document first, with its provision, then the verb, then the
document and provision it acts on. The acting document is always the grammatical
subject. Write "HO 04 90 W.2 writes back HO-3 Section I A.3", never "HO-3
Section I A.3 is written back by HO 04 90".

Use exactly one of these verbs, in lower case, spelled as shown:

- `supersedes` — a later edition replaces an earlier one for policies written
  after its effective date.
- `writes back` — an endorsement restores coverage that an exclusion in another
  document removed. Use this only where coverage is actually restored.
- `preserves` — a document expressly leaves another document's exclusion or limit
  intact. Use this where a reader might otherwise assume the exclusion was
  written back.
- `modifies` — changes a limit, sublimit, deductible, settlement basis, or
  condition without restoring excluded coverage.
- `implements` — a state amendatory form carries out a requirement imposed by a
  regulator's bulletin.
- `constrains` — internal guidance or a regulatory requirement limits when or how
  a form may be attached or applied. A constraint never changes what the contract
  means, only what the carrier may do.

Where one document both writes back an exclusion and preserves a neighbouring
one, those are two propositions, not one. HO 04 90 writes back Section I A.3 and
preserves Section I A.1 and A.2; document both, because a reader who knows only
the first will misread a flood loss.

A proposition that relates two documents must cite both. Cite the acting
provision and the provision acted on, not one standing for the other.

## Editions and supersession

Every coverage statement must say which edition it describes. The edition in force when a policy was written governs that policy for its life, so a superseded edition is still live knowledge and must not be deleted or rewritten as though the current edition had always applied.

Where a file carries a `SUPERSEDED by` marker, document both editions and state plainly which policies each one governs.

## What not to do

Do not write architecture, component, or data-flow documentation. This is not a software system. There are no modules, responsibilities, interfaces, or extension points here — there are contracts, coverages, exclusions, endorsements, and internal rules.

Do not state a coverage position without citing the controlling text. Do not treat internal guidance as authority over contract language. Do not resolve an ambiguity in the forms by inventing an answer; document the ambiguity and cite the competing provisions.
