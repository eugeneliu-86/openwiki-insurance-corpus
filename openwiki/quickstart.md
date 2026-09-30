---
type: policy-assembly
title: Coverage Wiki Quickstart
description: Route a water-backup question through line, state, policy-effective date, declarations, and attachment evidence before selecting the governing HO 04 90 edition. Then follow the water-backup coverage guide and the claims or assembly route without treating a current form as universally applicable.
tags: [coverage, policy-assembly, water-backup, claims, state-overlays, navigation]
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
  - id: openwiki-source-cd26c30cc942869b52618f95
    resource: repo://forms/HO/MS/HO-04-90/2010-10.md
  - id: openwiki-source-36bcf8e9754ce8cd9b63db52
    resource: repo://forms/HO/MS/HO-04-90/2026-01.md
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
generated: { by: "openwiki/0.6.0", at: "2026-09-30T16:48:38.942Z" }
verified:
  - by: openwiki/0.6.0
    at: 2026-09-30T16:48:38.942Z
---

# Coverage Wiki Quickstart

This is a routing map, not a substitute for the issued policy, endorsement, state form, claims procedure, or internal guidance. Contract wording comes from the issued base form and attached endorsements; bulletins, memoranda, training, manuals, and appetite guidance constrain or explain operations but do not create coverage ([source roles](repo://README.md#L15-L27), [guidance boundary](repo://training/guidance-versus-contract.md#L61-L83)).

## Required path

```mermaid
flowchart TD
    question["Water backup question"] --> line["1. Identify line"]
    line --> state["2. Identify state"]
    state --> date["3. Confirm policy effective date"]
    date --> declarations["4. Read declarations"]
    declarations --> attach["5. Verify complete attachments"]
    attach --> edition["6. Select governing HO 04 90 edition"]
    edition --> coverage["7. Follow water backup coverage"]
    coverage --> route{"Separate operational route"}
    route --> claims["Claims handling"]
    route --> assembly["Policy assembly and state attachments"]
```
*Caption: Preserve the line, state, date, declarations, and attachment sequence before interpreting coverage or routing operations.*

## Water-backup entrypoint

Start with [Water Backup and Sump Overflow](/openwiki/coverage/perils/water-backup.md) after confirming the policy package. It explains the water path, direct physical loss, edition-specific exclusions and conditions, and the form-versus-memorandum authority boundary.

For HO 04 90, use the policy-effective date only to identify the candidate interval, then independently prove that the exact endorsement is attached. The repository does not make a newer file universally applicable, and a later edition does not rewrite an older policy ([assembly gate](repo://openwiki/policy-assembly/editions-and-state-attachments.md#L15-L19), [edition selection](repo://openwiki/policy-assembly/editions-and-state-attachments.md#L51-L61)).

| Candidate edition | Routing cue | Do not skip |
| --- | --- | --- |
| **2010-10** | Effective 2010-10-01; retain it for an earlier policy when it is the issued endorsement. Its cited limit is $5,000 and deductible $500. | Confirm the endorsement is attached; do not substitute a newer specimen ([form](repo://forms/HO/MS/HO-04-90/2010-10.md#L1-L9), [limit](repo://forms/HO/MS/HO-04-90/2010-10.md#L107-L113), [deductible](repo://forms/HO/MS/HO-04-90/2010-10.md#L157-L167)). |
| **2026-01** | Replaces 2010-10 for policies written on or after 2026-01-01. It states a $10,000 per-policy-period sublimit, unless a higher endorsement limit is shown in the Declarations, and a separate $1,000 deductible. | For finished below-grade area, verify an installed and operable backwater valve or equivalent device; test the maintenance condition and preserved flood and below-ground-water exclusions ([form](repo://forms/HO/MS/HO-04-90/2026-01.md#L1-L4), [limits](repo://forms/HO/MS/HO-04-90/2026-01.md#L13-L33), [controls](repo://forms/HO/MS/HO-04-90/2026-01.md#L35-L47)). |
| **2027-01** | Effective 2027-01-01; use it only when the issued package attaches it. It states a $10,000 limit and $1,000 deductible. | Read its own conditions and exclusions with the base policy; attachment makes it part of the policy and unmodified terms remain applicable ([form](repo://forms/HO/MS/HO-04-90/2027-01.md#L14-L60), [limit and deductible](repo://forms/HO/MS/HO-04-90/2027-01.md#L254-L271), [deductible](repo://forms/HO/MS/HO-04-90/2027-01.md#L391-L412)). |

If the date, declarations, schedule, attachment record, or form copy conflicts, hold the coverage conclusion and obtain the complete issued package. Do not infer attachment from a system label or edition date ([attachment workflow](repo://training/attaching-endorsements.md#L65-L87)).

## Route after the contract check

- **Coverage interpretation:** Use [Water Backup and Sump Overflow](/openwiki/coverage/perils/water-backup.md), then [HO-3 form editions](/openwiki/coverage/forms/ho-3.md) for the base exclusion and applicable policy terms.
- **Assembly, edition, or state attachment:** Use [Editions, Endorsements, and State Attachments](/openwiki/policy-assembly/editions-and-state-attachments.md). A state form implements state contract wording; a bulletin constrains administration; neither replaces the issued endorsement ([authority rules](repo://openwiki/policy-assembly/editions-and-state-attachments.md#L38-L49)).
- **Claim investigation and mitigation:** Use [Water loss handling](/openwiki/claims/guidelines/water-loss-handling.md) after the contract route. Keep cause, coverage, scope, valuation, payment authority, and recovery as separate work products ([claims manual](repo://manuals/claims/manual.md#L13-L19)).

## Final check

Before publishing a position, confirm: line and state; policy-effective date; declarations; base form; exact attached HO 04 90 edition; water path and direct physical loss; edition-specific limit, deductible, exclusions, and conditions; applicable state wording; and the separate claims or operational guidance. Escalate unresolved attachment, causation, authority, regulatory, or evidence issues rather than guessing.
