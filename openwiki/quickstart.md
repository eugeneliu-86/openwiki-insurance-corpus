---
type: policy-assembly
title: Coverage Wiki Quickstart
description: Route HO-3 fungi and mold questions to the correct HO 04 81 endorsement edition by policy effective date and issued attachment package. Use this map to reach contract, coverage, and claims pages without treating an endorsement, manual, guideline, memorandum, or training source as a base form or coverage conclusion.
tags: [coverage, policy-assembly, HO-3, HO-04-81, fungi, mold, navigation]
verified:
  - by: openwiki/0.6.0
    at: 2026-09-30T04:20:28.270Z
sources:
  - id: openwiki-source-7dd90be03dbdd65accd7c766
    resource: repo://bulletins/CA/cdi-2022-03-earthquake-offer.md
  - id: openwiki-source-cf3bdf4919dc01656b85cad5
    resource: repo://bulletins/FL/oir-2022-01-hurricane-deductible.md
  - id: openwiki-source-3bd145be9dd2d256294b3e9a
    resource: repo://bulletins/NC/ncdoi-2021-06-claims-handling.md
  - id: openwiki-source-d2d0e0eee59ab93741467060
    resource: repo://bulletins/TX/b-2019-02-prompt-payment.md
  - id: openwiki-source-38049e374f54d1eb9a15f4ef
    resource: repo://bulletins/TX/b-2021-08-windstorm-deductibles.md
  - id: openwiki-source-0de2907066d0f023c5c2e68b
    resource: repo://forms/HO/MS/HO-04-81/2018-09.md
  - id: openwiki-source-65c1bab72aeee4cf69ba7892
    resource: repo://forms/HO/MS/HO-04-81/2026-09.md
  - id: openwiki-source-6a71dbfe57881e21b8a0e5ea
    resource: repo://forms/HO/MS/HO-04-90/2027-01.md
  - id: openwiki-source-5802aac0ff04777c19a4717f
    resource: repo://forms/HO/MS/HO-23-74/2025-05.md
  - id: openwiki-source-7176aead92778c93cb0441d2
    resource: repo://forms/HO/MS/HO-3/2024-03.md
  - id: openwiki-source-0d6a76164fce2d196a0998b8
    resource: repo://forms/HO/NY/HO-01-31/2016-04.md
  - id: openwiki-source-1a7fd187295c6f9ef57d73cb
    resource: repo://guidelines/appetite/ca-homeowners.md
  - id: openwiki-source-243115596013c4ec281c4a90
    resource: repo://guidelines/appetite/fl-homeowners.md
  - id: openwiki-source-1a23ac5f105f70e05c6ce688
    resource: repo://guidelines/appetite/la-homeowners.md
  - id: openwiki-source-b4a32c6164f88c97824a6cfb
    resource: repo://guidelines/appetite/nc-homeowners.md
  - id: openwiki-source-ff8a10adb5aaa9d147aa506d
    resource: repo://guidelines/appetite/ny-homeowners.md
  - id: openwiki-source-da67a262bebb42780999bd2a
    resource: repo://guidelines/appetite/tx-homeowners.md
  - id: openwiki-source-e3f8eeadc60c530791e87a00
    resource: repo://guidelines/authority/binding-authority.md
  - id: openwiki-source-b835c3d80d50a5ec159c2c2a
    resource: repo://guidelines/claims/liability-claim-handling.md
  - id: openwiki-source-826017f9c17ff1c446a5e4f6
    resource: repo://guidelines/claims/mold-claim-handling.md
  - id: openwiki-source-98996e9748507677077d5997
    resource: repo://guidelines/claims/roof-claim-handling.md
  - id: openwiki-source-fe5cf28f9b15285dd496cba1
    resource: repo://guidelines/claims/water-loss-handling.md
  - id: openwiki-source-77e27410bda4d59c2b779d5e
    resource: repo://manuals/claims/manual.md
  - id: openwiki-source-add01ee6690ea277c5253419
    resource: repo://manuals/rating/manual.md
  - id: openwiki-source-2b86de67275893a8b33d953b
    resource: repo://manuals/underwriting/manual.md
  - id: openwiki-source-9a9291b2de270f91ca242ea5
    resource: repo://memoranda/HO-3-2024-03.md
  - id: openwiki-source-23775c3de52f3ab95a13cb8b
    resource: repo://README.md
  - id: openwiki-source-d2ea423343a02d2233c77383
    resource: repo://training/attaching-endorsements.md
  - id: openwiki-source-8460fe3c58470ce6ec8d9b51
    resource: repo://training/choosing-the-governing-edition.md
  - id: openwiki-source-a6e7a7f52df2ed58605a3898
    resource: repo://training/guidance-versus-contract.md
generated: { by: "openwiki/0.6.0", at: "2026-09-30T04:20:28.270Z" }
---

# Coverage Wiki Quickstart

This is a **policy-assembly routing page**, not a coverage opinion or claims procedure. Begin with the issued policy package: line, state, policy-effective date, Declarations, base form, attached endorsements, and applicable state form. The repository path is load-bearing because it carries line, state, form, and edition context ([repository layout](repo://README.md#L13-L31)).

## HO 04 81: select the edition first

For an HO-3 policy, **HO 04 81 edition 2026-09 supersedes edition 2018-09 only for policies written or renewed on or after 2026-10-01**. The older 2018-09 edition remains live for policies written under it and governs losses under those policies, even if reported later ([2026-09 endorsement](repo://forms/HO/MS/HO-04-81/2026-09.md#L1-L7), [2018-09 endorsement](repo://forms/HO/MS/HO-04-81/2018-09.md#L8-L12)). Do not select an edition from the report date, current catalog, or newest repository file.

```mermaid
flowchart TD
    A["HO-3 question"] --> B["Record policy date and issued package"]
    B --> C{"Written or renewed on or after 2026-10-01"}
    C -->|"yes"| D["Candidate HO 04 81 2026-09"]
    C -->|"no"| E["Live HO 04 81 2018-09"]
    D --> F{"Endorsement actually attached"}
    E --> F
    F -->|"no or uncertain"| G["Obtain package or escalate"]
    F -->|"yes"| H["Read HO 04 81 with the governing HO-3"]
    H --> I["Route coverage and handling separately"]
```
*Caption: The policy date selects the candidate edition; the complete issued package confirms whether the endorsement forms part of the contract.*

The date rule is not proof of attachment. An endorsement can be used as contract language only after its complete pages and schedules are matched to the insured, policy term, location, and subject; a listed-but-missing form or attached-but-unlisted form must be reconciled ([attachment workflow](repo://training/attaching-endorsements.md#L65-L87), [policy-assembly entry gate](repo://openwiki/policy-assembly/editions-and-state-attachments.md#L61-L69)). Once attachment is confirmed, read the endorsement with the base HO-3: it controls only where it conflicts within its stated scope, while unchanged policy provisions remain applicable ([2018-09 attachment and preservation](repo://forms/HO/MS/HO-04-81/2018-09.md#L17-L47), [2026-09 scope](repo://forms/HO/MS/HO-04-81/2026-09.md#L3-L7)).

## What changes between the two editions

The 2026-09 form states that its only change from 2018-09 is the aggregate limit: **$25,000 instead of $10,000**; all other provisions are unchanged ([2026-09 change statement](repo://forms/HO/MS/HO-04-81/2026-09.md#L23-L33), [2018-09 limit](repo://forms/HO/MS/HO-04-81/2018-09.md#L161-L169)). This is a routing cue, not a coverage conclusion. The fungi page explains the trigger, exclusions, covered remediation, and the single aggregate; the applicable attached edition controls ([Fungi, Wet or Dry Rot, and Bacteria](/openwiki/coverage/perils/fungi-and-bacteria.md)).

A covered cause must cause direct physical loss before the fungi causes loss; qualifying work is limited to the endorsement’s express terms. Thus a water event, inspection, vendor label, mitigation step, or mold allegation does not by itself establish fungi coverage ([2026-09 coverage terms](repo://forms/HO/MS/HO-04-81/2026-09.md#L9-L21), [2018-09 trigger and work](repo://forms/HO/MS/HO-04-81/2018-09.md#L49-L81)).

## Route by domain

| Need | Open next | Boundary |
| --- | --- | --- |
| Select edition, assemble policy, resolve attachment or precedence | [Editions, Endorsements, and State Attachments](/openwiki/policy-assembly/editions-and-state-attachments.md) | Contract forms and attached endorsements are distinct from bulletins and internal controls. |
| Interpret fungi, wet or dry rot, bacteria, trigger, exclusions, scope, or limit | [Fungi, Wet or Dry Rot, and Bacteria](/openwiki/coverage/perils/fungi-and-bacteria.md) | Apply the attached HO 04 81 edition; do not combine the $10,000 and $25,000 aggregates. |
| Investigate a reported mold or microbial loss | [Mold Claim Handling](/openwiki/claims/guidelines/mold-claim-handling.md) | Handling guidance organizes evidence and escalation; it does not grant or deny coverage. |
| Investigate a water-origin loss | [Water Loss Handling](/openwiki/claims/guidelines/water-loss-handling.md) and [Water Damage](/openwiki/coverage/perils/water-damage.md) | Separate the initiating water cause from the resulting fungi question. |

## Contract versus guidance

Base forms, attached endorsements, and state amendatory forms supply contract wording. Regulator bulletins constrain carrier issuance, disclosure, or administration. Manuals and claims or underwriting guidelines are internal controls. Filing memoranda explain an edition, and training teaches a review method; neither replaces the issued form or creates coverage ([document families](repo://README.md#L15-L27), [authority layers](repo://openwiki/policy-assembly/editions-and-state-attachments.md#L46-L57), [guidance boundary](repo://training/guidance-versus-contract.md#L61-L83)).

Keep these propositions separate:

- **Edition selection:** use the policy-effective date and preserve the 2018-09 edition for policies written under it.
- **Attachment:** verify the complete issued package; a schedule or system label is not the endorsement itself.
- **Coverage:** read the attached endorsement and governing HO-3 together; an endorsement is not a base form and does not expand coverage beyond its express terms.
- **Handling:** use mold and water pages to investigate source, sequence, evidence, mitigation, scope, and escalation. Do not turn handling activity, a manual rule, a memorandum, or training shortcut into a coverage result.

If date, attachment, state form, or policy wording is incomplete or conflicting, hold the interpretation and obtain the issued package or escalate rather than choosing the edition that produces the preferred result ([selection procedure](repo://openwiki/policy-assembly/editions-and-state-attachments.md#L96-L103)).
