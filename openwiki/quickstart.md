---
type: routing-guide
title: Coverage Wiki Quickstart
description: Route homeowners contract, regulatory, claims, and underwriting questions to the correct authority layer and specialist page. Start with the issued-policy record, then keep contractual terms, regulatory controls, and internal guidance separate.
tags: [homeowners, coverage-routing, policy-assembly, state-overlays, claims, underwriting]
verified:
  - by: openwiki/0.5.0
    at: 2026-09-09T17:00:59.484Z
sources:
  - id: openwiki-source-f8563069b83f765bb32e6be4
    resource: repo://bulletins/FL/2023-04-roof-age-nonrenewal.md
  - id: openwiki-source-3624f12a121557db250a950b
    resource: repo://bulletins/TX/2021-08-windstorm-deductible.md
  - id: openwiki-source-e81c5a85097780cfed50a7a1
    resource: repo://forms/HO/MS/HO-04-16/2018-09.md
  - id: openwiki-source-0de2907066d0f023c5c2e68b
    resource: repo://forms/HO/MS/HO-04-81/2018-09.md
  - id: openwiki-source-cd26c30cc942869b52618f95
    resource: repo://forms/HO/MS/HO-04-90/2010-10.md
  - id: openwiki-source-a7812317f4b735061e88f5bb
    resource: repo://forms/HO/MS/HO-23-74/2018-09.md
  - id: openwiki-source-e727058d16eee86c951e380a
    resource: repo://forms/HO/MS/HO-3/2011-05.md
  - id: openwiki-source-f4ebd2ece3eaf490178dfc41
    resource: repo://forms/HO/MS/HO-3/2018-09.md
  - id: openwiki-source-ff7de1315ac46ce4dd65d251
    resource: repo://forms/HO/TX/HO-01-45/2022-01.md
  - id: openwiki-source-c7690df4255f266075cd43d2
    resource: repo://guidelines/authority/referral-matrix.md
  - id: openwiki-source-fe5cf28f9b15285dd496cba1
    resource: repo://guidelines/claims/water-loss-handling.md
  - id: openwiki-source-23775c3de52f3ab95a13cb8b
    resource: repo://README.md
generated: { by: "openwiki/0.5.0", at: "2026-09-09T17:00:59.484Z" }
---

## Choose the authority layer first

This wiki describes a synthetic insurance corpus, not a real carrier product, ISO form, or legal advice. Forms and regulator bulletins are frozen authority; internal guidelines are living material. A new form edition is a new file, while a policy written under an earlier edition continues to use that edition. [Corpus scope and source lifecycle](repo://README.md#L3-L18) · [Frozen and living authority](repo://README.md#L28-L36)

| Question being answered | Start with | Keep separate |
| --- | --- | --- |
| What does this issued policy cover, exclude, require, or pay? | The issued-policy record: selected HO-3 edition, complete Declarations, and verified attached endorsements or amendments. | A repository form that is not proven attached, a bulletin, and internal workflow. |
| What may the insurer do for issue, renewal, notice, deductible configuration, filing, or reporting? | The applicable state bulletin and its scope/effective-date test. | Contract wording and internal authority. A bulletin does not prove an attachment. |
| How should staff investigate, reserve rights, refer, document, or bind? | The relevant claims or underwriting guidance after the contract and regulatory layers are identified. | Coverage authority, an insured duty, and customer-facing coverage language. |

**Operating boundary:** Internal claims guidance is not part of a policy and must not be quoted to an insured or claimant. It directs staff to establish and document a water source before evaluating damage; that operational sequence does not decide coverage. [Water Loss Claim Handling Guidance, status and source-first direction](repo://guidelines/claims/water-loss-handling.md#L1-L11)

## Minimum record before a contract answer

Collect the policy-written date, policy effective date, state, full Declarations, limits, deductible selections, selected HO-3 edition, and every actually attached form and edition. For a claim, also collect the loss date, alleged cause, property involved, and facts needed by the potentially applicable provision. If a required record or attachment is unverified, leave the affected issue unresolved rather than importing a later form or assuming attachment.

For base-form selection, **HO-3 2018-09 applicability statement supersedes HO-3 2011-05 supersession statement** for policies written on or after 2018-09-01; HO-3 2011-05 remains in force for policies written under it, regardless of when a loss is reported. [HO-3 2018-09, applicability and supersession](repo://forms/HO/MS/HO-3/2018-09.md#L1-L4) · [HO-3 2011-05, supersession marker and continuing force](repo://forms/HO/MS/HO-3/2011-05.md#L1-L7)

Use [Governing Form Editions and Policy Assembly](/openwiki/coverage/policy-editions-and-governing-forms.md) whenever the form set, attachment, edition compatibility, or Texas amendment is uncertain. Its assembly sequence is:

1. Select the HO-3 edition from the policy-written date.
2. Verify the Declarations and actual attachments; “if attached” is not proof of attachment.
3. Apply an attached, in-scope state amendment at the conflict it identifies.
4. Analyze the applicable grant and exclusions before a narrow write-back, then apply settlement, limits, deductible, and conditions.

For example, HO 01 45 attaches to HO-3, applies to policies effective on or after 2022-01-01, and governs where it conflicts with the attached form. Its effective-date scope does not select the HO-3 edition or establish attachment to an individual policy. [HO 01 45, scope and conflict rule](repo://forms/HO/TX/HO-01-45/2022-01.md#L1-L4)

## Task-routing map

Use the table as the hierarchy entrypoint. The destination pages hold the detailed analysis; a route does not establish a coverage result or an attachment.

| Domain | Route when the question is about | Specialist page |
| --- | --- | --- |
| **Quickstart** | A question has not yet been classified as contract, regulatory, claims, or underwriting work | [Coverage Wiki Quickstart](/openwiki/quickstart.md) |
| **Policy assembly** | Written date, governing edition, Declarations, attachment, compatibility, or Texas amendment | [Governing Form Editions and Policy Assembly](/openwiki/coverage/policy-editions-and-governing-forms.md) |
| **Coverage A** | Dwelling scope, replacement-cost baseline, or the 80-percent condition | [Coverage A — Dwelling](/openwiki/coverage/coverage-a/dwelling.md) |
| **Coverage A** | Wind/hail roof surfacing, ACV schedule, roof age/material, or deductible sequence | [Coverage A — Roof Surfacing Settlement](/openwiki/coverage/coverage-a/roof-settlement.md) |
| **Coverage B** | Detached structures, fence or utility connections, rental use, or the additional limit | [Coverage B — Other Structures](/openwiki/coverage/coverage-b/other-structures.md) |
| **Coverage C** | Personal property, worldwide scope, special limits, or settlement treatment | [Coverage C — Personal Property](/openwiki/coverage/coverage-c/personal-property.md) |
| **Coverage D** | Additional living expense, uninhabitability, duration, or a fungi-related loss-of-use question | [Coverage D — Loss of Use](/openwiki/coverage/coverage-d/loss-of-use.md) |
| **Section II** | Liability, defense, medical payments, business activity, or insured-owned/rented property | [Coverage E and F — Liability and Medical Payments](/openwiki/coverage/coverage-e-f/liability-and-medical-payments.md) |
| **Section I gates** | Cause of loss, direct physical loss, named peril, or a general exclusion | [Section I Property Perils and General Exclusions](/openwiki/coverage/property/perils-and-general-exclusions.md) |
| **Claim conditions** | Notice, protection, inventory, proof of loss, payment, action limitation, or ordinary deductible | [Section I Claim Conditions, Payment, and Deductibles](/openwiki/coverage/property/claim-conditions-and-deductibles.md) |
| **Water** | Flood, surface water, groundwater, backup, sump event, internal discharge, seepage, or water-backup terms | [Water Damage Exclusions and Water Backup Write-Back](/openwiki/coverage/property/water-damage-and-backup.md) |
| **Fungi** | Mold, fungi, wet/dry rot, bacteria, mitigation, aggregate, or a water-related fungi result | [Fungi, Rot, and Bacteria Limited Coverage](/openwiki/coverage/property/fungi-rot-and-bacteria.md) |
| **Ordinance** | Code-required repair, demolition, increased construction cost, or undamaged roof portions | [Ordinance or Law Coverage and Undamaged Roof Portions](/openwiki/coverage/property/ordinance-or-law.md) |
| **Claims operations** | Roof-loss fact development, estimate review, ordinance handoff, state check, escalation, or closure record | [Roof Loss Claims Handling](/openwiki/operations/claims-roof-loss-handling.md) |
| **Claims operations** | Water-loss intake, source/duration investigation, referral, reservation of rights, accounting, or completion record | [Water Loss Claims Handling](/openwiki/operations/claims-water-loss-handling.md) |
| **Florida overlay** | Florida roof age, inspection, ACV-schedule offer, nonrenewal, deductible overlap, or reporting | [Florida Roof Age, ACV Schedule, and Nonrenewal Overlay](/openwiki/state-overlays/florida.md) |
| **Texas overlay** | Texas wind/hail deductible, disclosure, filing, mixed-peril allocation, named storm, residual market, or claim timing | [Texas Windstorm and Hail Deductible Overlay](/openwiki/state-overlays/texas.md) |
| **Underwriting** | Enterprise authority tier, referral, hard stop, endorsement route, or audit record | [Referral and Binding Authority](/openwiki/underwriting/referral-and-binding-authority.md) |
| **Underwriting** | Florida eligibility, roof/nonrenewal workflow, optional endorsement configuration, or authority route | [Florida Homeowners Appetite](/openwiki/underwriting/florida-appetite.md) |
| **Underwriting** | Texas eligibility, coastal/roof controls, water-backup configuration, wind/hail routing, or authority route | [Texas Homeowners Appetite](/openwiki/underwriting/texas-appetite.md) |

For HO-3 2018-09, Coverage A and B use the direct-physical-loss grant subject to Section I exclusions; Coverage C also requires a P.2 listed peril. Route a coverage question through those gates before treating a settlement term or endorsement limit as a coverage grant. [HO-3 2018-09, P.1-P.2 and water exclusions](repo://forms/HO/MS/HO-3/2018-09.md#L59-L77)

## Attachment relationship ledger

The following statements are directional contract relationships. Apply them only after confirming the selected base edition and the actual attachment in the issued policy.

| Directed relationship | Routing consequence |
| --- | --- |
| **HO 04 90 W.1 writes back HO-3 2018-09 Section I Exclusions A.3.** [HO 04 90 W.1](repo://forms/HO/MS/HO-04-90/2010-10.md#L5-L8) · [HO-3 2018-09 A.3](repo://forms/HO/MS/HO-3/2018-09.md#L69-L77) | Route the stated sewer/drain-backup and sump events to the water page. |
| **HO 04 90 W.4 preserves HO-3 2018-09 Section I Exclusions A.1 and A.2.** [HO 04 90 W.4](repo://forms/HO/MS/HO-04-90/2010-10.md#L17-L21) · [HO-3 2018-09 A.1-A.2](repo://forms/HO/MS/HO-3/2018-09.md#L69-L74) | Do not treat the backup route as flood, surface-water, or subsurface-water coverage. |
| **HO 04 81 M.1 writes back HO-3 2018-09 Section I Exclusions C.2.** [HO 04 81 M.1](repo://forms/HO/MS/HO-04-81/2018-09.md#L5-L10) · [HO-3 2018-09 C.2](repo://forms/HO/MS/HO-3/2018-09.md#L83-L89) | Route resulting fungi, rot, or bacteria to its separate attachment, underlying-event, aggregate, and mitigation analysis. |
| **HO 04 16 O.1 writes back HO-3 2018-09 Section I Exclusions D.1.** [HO 04 16 O.1](repo://forms/HO/MS/HO-04-16/2018-09.md#L5-L9) · [HO-3 2018-09 D.1](repo://forms/HO/MS/HO-3/2018-09.md#L91-L94) | Route eligible ordinance-driven increased cost to the ordinance page; it is distinct from damaged-property settlement. |
| **HO 23 74 R.1-R.2 modifies HO-3 2018-09 Section I A.4.** [HO 23 74 R.1-R.2](repo://forms/HO/MS/HO-23-74/2018-09.md#L5-L15) · [HO-3 2018-09 A.4](repo://forms/HO/MS/HO-3/2018-09.md#L31-L34) | Route only windstorm/hail roof-surfacing settlement to the roof page; other components and other covered perils remain on their base-form path. |
| **HO 23 74 R.6 preserves HO-3 2018-09 Section I Exclusions D.1.** [HO 23 74 R.6](repo://forms/HO/MS/HO-23-74/2018-09.md#L37-L41) · [HO-3 2018-09 D.1](repo://forms/HO/MS/HO-3/2018-09.md#L91-L94) | Route code-required undamaged roof surfacing to the ordinance page, not to the roof schedule as an independent payment path. |
| **HO 01 45 T.1 modifies HO-3 2018-09 Section I Conditions S.5.** [HO 01 45 T.1](repo://forms/HO/TX/HO-01-45/2022-01.md#L5-L11) · [HO-3 2018-09 S.5](repo://forms/HO/MS/HO-3/2018-09.md#L109-L112) | For an attached, compatible Texas amendment, route wind/hail deductible selection to the Texas overlay. |
| **HO 01 45 T.1 implements Texas Bulletin B-2021-08 B.3.** [HO 01 45 T.1](repo://forms/HO/TX/HO-01-45/2022-01.md#L7-L11) · [Texas Bulletin B-2021-08 B.3](repo://bulletins/TX/2021-08-windstorm-deductible.md#L15-L19) | Keep the issued amendment's contract result distinct from the bulletin's insurer-conduct requirement. |

## State and operational handoffs

- **Florida:** OIR-2023-04 applies to Florida personal residential property policies issued or renewed with an effective date on or after 2023-07-01. It controls roof-age, inspection, offer, nonrenewal, deductible-overlap, and reporting requirements; it does not determine an individual policy's issued roof-settlement wording. [OIR-2023-04, scope and controls](repo://bulletins/FL/2023-04-roof-age-nonrenewal.md#L1-L37)
- **Texas:** B-2021-08 applies to Texas residential property policies delivered or issued for delivery with an effective date on or after 2022-01-01. It establishes regulatory requirements for separate windstorm/hail deductible configuration, disclosure, loss application, and filing. [B-2021-08, scope and requirements](repo://bulletins/TX/2021-08-windstorm-deductible.md#L1-L37)
- **Underwriting:** A state appetite guide may impose tighter authority than the enterprise referral matrix but may not grant broader authority. Referral and management approval are escalation mechanisms, while out-of-appetite risks and filing/bulletin conflicts cannot be cleared by referral or bound. [Referral matrix, state-guide boundary and tiers](repo://guidelines/authority/referral-matrix.md#L1-L11) · [Referral matrix, non-clearable conditions](repo://guidelines/authority/referral-matrix.md#L33-L40)

## Final controls

Before a coverage conclusion, payment calculation, binding decision, referral disposition, or insured-facing communication, confirm:

1. **Assembly:** the issued record establishes dates, state, Declarations, base edition, and each attachment.
2. **Authority:** the conclusion is identified as contract, regulatory, or internal guidance.
3. **Sequence:** the analysis retains the cause/property gate, exclusion, narrow write-back, settlement, limit, deductible, and condition in their stated order.
4. **State:** the relevant overlay has passed its own scope test and remains separate from issued contract terms.
5. **Operations:** the file records facts, authority, calculations, notices, referrals, and escalations without converting internal workflow into an insured obligation.

If a gate cannot be established, do not cure the gap with a later form, an assumed endorsement, a bulletin, or an internal instruction.
