---
type: policy-assembly
title: Coverage Wiki Quickstart
description: Route homeowners questions to the correct authority layer and specialist page. For Coverage B limit increases, verify the issued HO 04 48 attachment and its endorsement Declarations amount rather than assuming the base limit.
tags: [homeowners, coverage-routing, policy-assembly, state-overlays, claims, underwriting]
verified:
  - by: openwiki/0.5.0
    at: 2026-09-13T00:48:02.362Z
sources:
  - id: openwiki-source-f8563069b83f765bb32e6be4
    resource: repo://bulletins/FL/2023-04-roof-age-nonrenewal.md
  - id: openwiki-source-3624f12a121557db250a950b
    resource: repo://bulletins/TX/2021-08-windstorm-deductible.md
  - id: openwiki-source-e81c5a85097780cfed50a7a1
    resource: repo://forms/HO/MS/HO-04-16/2018-09.md
  - id: openwiki-source-9c2b05516073c90ea8ebe398
    resource: repo://forms/HO/MS/HO-04-48/2026-06.md
  - id: openwiki-source-0de2907066d0f023c5c2e68b
    resource: repo://forms/HO/MS/HO-04-81/2018-09.md
  - id: openwiki-source-cd26c30cc942869b52618f95
    resource: repo://forms/HO/MS/HO-04-90/2010-10.md
  - id: openwiki-source-36bcf8e9754ce8cd9b63db52
    resource: repo://forms/HO/MS/HO-04-90/2026-01.md
  - id: openwiki-source-a7812317f4b735061e88f5bb
    resource: repo://forms/HO/MS/HO-23-74/2018-09.md
  - id: openwiki-source-e727058d16eee86c951e380a
    resource: repo://forms/HO/MS/HO-3/2011-05.md
  - id: openwiki-source-f4ebd2ece3eaf490178dfc41
    resource: repo://forms/HO/MS/HO-3/2018-09.md
  - id: openwiki-source-ff7de1315ac46ce4dd65d251
    resource: repo://forms/HO/TX/HO-01-45/2022-01.md
  - id: openwiki-source-243115596013c4ec281c4a90
    resource: repo://guidelines/appetite/fl-homeowners.md
  - id: openwiki-source-da67a262bebb42780999bd2a
    resource: repo://guidelines/appetite/tx-homeowners.md
  - id: openwiki-source-c7690df4255f266075cd43d2
    resource: repo://guidelines/authority/referral-matrix.md
  - id: openwiki-source-fe5cf28f9b15285dd496cba1
    resource: repo://guidelines/claims/water-loss-handling.md
  - id: openwiki-source-23775c3de52f3ab95a13cb8b
    resource: repo://README.md
generated: { by: "openwiki/0.5.0", at: "2026-09-13T00:48:02.362Z" }
---

## Start with the authority layer, not the file tree

This page is the entrypoint for the synthetic homeowners corpus. It is a routing map, not a coverage answer: choose the authority layer first, then follow the specialist page that matches the question. The corpus separates three kinds of authority:

- **Contract language** — the issued policy record, including the selected HO-3 edition, Declarations, and only those endorsements or amendments actually attached.
- **Regulatory overlay** — state bulletins that constrain insurer conduct, filing, notice, deductible configuration, or reporting.
- **Internal guidance** — underwriting and claims procedures that direct staff work but are not policy terms and must not be quoted as such.

If the issued record is incomplete, keep the issue unresolved rather than filling gaps with a later form, a bulletin, or a workflow note.

## What to read for each question

| Question being answered | Start with | Keep separate |
| --- | --- | --- |
| What does this issued policy cover, exclude, require, or pay? | The issued-policy record: policy-written date, state, selected HO-3 edition, complete Declarations, and verified attached endorsements or amendments. | A repository form that is not proven attached, a bulletin, and internal workflow. |
| What may the insurer do for issue, renewal, deductible configuration, filing, notice, or reporting? | The applicable state overlay and its effective-date gate. | Contract wording and internal authority. A bulletin does not prove an attachment. |
| How should staff investigate, reserve rights, refer, document, or bind? | The relevant claims or underwriting guidance after the contract and regulatory layers are identified. | Coverage authority, an insured duty, and customer-facing coverage language. |

**Operating boundary:** internal claims and underwriting guidance are file-management controls. They help staff record source facts, preserve evidence, and route exceptions, but they do not decide coverage or create a policy term.

## Minimum record before a contract answer

Before answering a contract question, collect the policy-written date, policy effective date, state, Declarations, limits, deductible selections, selected HO-3 edition, and every actually attached form and edition. For a Coverage B limit-increase question, obtain the issued HO 04 48 attachment and the amount shown for that endorsement in the Declarations; neither may be inferred from a repository form or premium entry. For water-backup questions, also collect the exact HO 04 90 edition because 2010-10 and 2026-01 have different payment and condition terms. For a claim, add the loss date, alleged cause, property involved, and the facts needed by the potentially applicable provision.

If a required record or attachment is unverified, do not import newer language just because it exists in the repository.

## Base-form selection and form assembly

The HO-3 edition is selected from the policy-written date, not the loss date. HO-3 2011-05 remains controlling for policies written under it, while HO-3 2018-09 applies to policies written on or after 2018-09-01. That selection changes the available provisions, so the base form must be chosen before any endorsement analysis.

Use [Governing Form Editions and Policy Assembly](/openwiki/coverage/policy-editions-and-governing-forms.md) whenever the form set, attachment, compatibility, or Texas amendment is uncertain. Its assembly sequence is:

1. Select the HO-3 edition from the policy-written date.
2. Verify the Declarations and actual attachments; “if attached” is not proof of attachment. For HO 04 48, obtain the endorsement's declared amount as well as the issued attachment.
3. Apply an attached, in-scope state amendment only at the conflict it identifies.
4. Analyze the applicable grant and exclusions before any narrow write-back, then apply settlement, limits, deductible, and conditions.

## Fast routes by topic

| Topic | Route to |
| --- | --- |
| Dwelling scope, replacement-cost baseline, or the 80-percent condition | [Coverage A — Dwelling](/openwiki/coverage/coverage-a/dwelling.md) |
| Wind/hail roof surfacing, ACV schedule, roof age/material, or deductible sequence | [Coverage A — Roof Surfacing Settlement](/openwiki/coverage/coverage-a/roof-settlement.md) |
| Detached structures, fence or utility connections, rental use, the base 10% additional limit, or an asserted Coverage B limit increase | [Coverage B — Other Structures](/openwiki/coverage/coverage-b/other-structures.md) |
| Personal property, worldwide scope, special limits, or settlement treatment | [Coverage C — Personal Property](/openwiki/coverage/coverage-c/personal-property.md) |
| Additional living expense, uninhabitability, duration, or fungi-related loss of use | [Coverage D — Loss of Use](/openwiki/coverage/coverage-d/loss-of-use.md) |
| Liability, defense, medical payments, business activity, or insured-owned/rented property | [Coverage E and F — Liability and Medical Payments](/openwiki/coverage/coverage-e-f/liability-and-medical-payments.md) |
| Cause of loss, direct physical loss, named peril, or a general exclusion | [Section I Property Perils and General Exclusions](/openwiki/coverage/property/perils-and-general-exclusions.md) |
| Notice, protection, inventory, proof of loss, payment, action limit, or ordinary deductible | [Section I Claim Conditions, Payment, and Deductibles](/openwiki/coverage/property/claim-conditions-and-deductibles.md) |
| Flood, surface water, backup, sump event, internal discharge, seepage, or the 2010-10 / 2026-01 water-backup terms | [Water Damage Exclusions and Water Backup Write-Back](/openwiki/coverage/property/water-damage-and-backup.md) |
| Mold, fungi, wet/dry rot, bacteria, mitigation, aggregate, or water-related fungi result | [Fungi, Rot, and Bacteria Limited Coverage](/openwiki/coverage/property/fungi-rot-and-bacteria.md) |
| Code-required repair, demolition, increased construction cost, or undamaged roof portions | [Ordinance or Law Coverage and Undamaged Roof Portions](/openwiki/coverage/property/ordinance-or-law.md) |
| Roof-loss investigation, estimate review, ordinance handoff, state check, escalation, or closure record | [Roof Loss Claims Handling](/openwiki/operations/claims-roof-loss-handling.md) |
| Water-loss intake, source investigation, reservation of rights, referral, accounting, or completion record | [Water Loss Claims Handling](/openwiki/operations/claims-water-loss-handling.md) |
| Florida roof age, inspection, ACV-schedule offer, nonrenewal, deductible overlap, or reporting | [Florida Roof Age, ACV Schedule, and Nonrenewal Overlay](/openwiki/state-overlays/florida.md) |
| Texas wind/hail deductible, disclosure, filing, allocation, named storm, residual market, or claim timing | [Texas Windstorm and Hail Deductible Overlay](/openwiki/state-overlays/texas.md) |
| Enterprise authority tier, referral, hard stop, endorsement route, or audit record | [Referral and Binding Authority](/openwiki/underwriting/referral-and-binding-authority.md) |
| Florida eligibility, roof/nonrenewal workflow, optional endorsement configuration, or authority route | [Florida Homeowners Appetite](/openwiki/underwriting/florida-appetite.md) |
| Texas eligibility, coastal/roof controls, water-backup configuration, wind/hail routing, or authority route | [Texas Homeowners Appetite](/openwiki/underwriting/texas-appetite.md) |

## Coverage B limit-increase routing: HO 04 48

Route any question about an other-structures limit increase to [Coverage B — Other Structures](/openwiki/coverage/coverage-b/other-structures.md), then use [Governing Form Editions and Policy Assembly](/openwiki/coverage/policy-editions-and-governing-forms.md) to assemble the policy. This is a routing and record-collection step, not a coverage determination.

The unendorsed **HO-3 2018-09 B.2** supplies a Coverage B limit equal to 10% of Coverage A and calls it additional insurance. **HO 04 48 (2026-06) OS.1** instead replaces B.2 with the amount shown for that endorsement in the Declarations, with a minimum of 10% of Coverage A; that amount is also additional insurance. The endorsement says it attaches to **HO-3 2018-09** and modifies B.2 only. [HO-3 2018-09 B.2](repo://forms/HO/MS/HO-3/2018-09.md#L35-L41) · [HO 04 48, heading and OS.1](repo://forms/HO/MS/HO-04-48/2026-06.md#L1-L11)

Use this control sequence:

1. Establish the policy-written date and select the base HO-3 edition.
2. For a 2018-09 base form, verify that the issued-policy record actually attaches HO 04 48 (2026-06); repository availability, an assertion, or an endorsement premium is not proof of attachment.
3. Obtain the amount shown for HO 04 48 in the issued endorsement Declarations. If the attachment or declared amount is missing, leave the asserted increased-limit issue unresolved; do not assume either the base 10% amount or an increase.
4. If both controls are satisfied, apply OS.1 only to Coverage B B.2. Retain the property/rental tests in B.1 and B.3, the Section I direct-physical-loss grant and exclusions, and all conditions.

HO 04 48 is neither automatic nor portable to **HO-3 2011-05**: its stated target is HO-3 2018-09. It does not alter B.1 or B.3, another Section I property coverage, an exclusion, or a condition; rental treatment therefore remains under B.3. [HO 04 48 OS.2](repo://forms/HO/MS/HO-04-48/2026-06.md#L13-L17) · [HO-3 2018-09 B.1–B.3](repo://forms/HO/MS/HO-3/2018-09.md#L35-L41) · [HO-3 2018-09 P.1](repo://forms/HO/MS/HO-3/2018-09.md#L59-L63)

## HO 04 90 water-backup routing

HO 04 90 is attachment-dependent and edition-specific. The endorsement writes back the sewer/drain-backup and sump-event exclusion in A.3 only when it is actually attached, and the issued endorsement edition must be selected independently from the HO-3 base-form edition.

| Verified attached HO 04 90 | Contract route after source and property analysis | Do not retrofit |
| --- | --- | --- |
| **2010-10** | Use W.1 for the stated sewer/drain-backup and sump-event route, then apply W.4 retained exclusions, W.5 maintenance condition, W.2’s $5,000 default policy-period sublimit unless the endorsement Declarations show more, W.3’s separate $500 deductible, and W.6 settlement. | Do not apply 2026-01’s $10,000 default sublimit, $1,000 deductible, backflow-prevention condition, or W.7 numbering. |
| **2026-01** | Use W.1, W.4, and W.5, then apply W.2’s $10,000 default policy-period sublimit unless the endorsement Declarations show more, W.3’s separate $1,000 deductible, W.6 when triggered, and W.7 settlement. | Do not quote legacy W.6 as the settlement rule. |
| **Attachment, edition, or written date unverified** | Obtain the issued endorsement and Declarations; leave the endorsement coverage and payment issue unresolved. | Do not select an edition from a report date, current guide, or repository availability. |

The sublimit in either edition is within, not additional to, the applicable A/B/C limits, and the separate deductible displaces the Section I Declarations deductible for a covered endorsement loss. In 2026-01 only, a residence premises with a finished area below grade must have had an installed and operable backwater valve or equivalent backflow-prevention device on the serving sewer line at the time of loss.

For the source analysis, property-specific settlement, and resulting-fungi path, use [Water Damage Exclusions and Water Backup Write-Back](/openwiki/coverage/property/water-damage-and-backup.md).

## State and operations handoffs

- **Florida:** OIR-2023-04 applies to Florida personal residential property policies issued or renewed with an effective date on or after 2023-07-01. It controls roof-age, inspection, offer, nonrenewal, deductible-overlap, and reporting requirements; it does not determine an individual policy's issued roof-settlement wording.
- **Texas:** B-2021-08 applies to Texas residential property policies delivered or issued for delivery with an effective date on or after 2022-01-01. It establishes regulatory requirements for separate windstorm/hail deductible configuration, disclosure, loss application, and filing.
- **Underwriting:** A state appetite guide may narrow authority more than the enterprise referral matrix, but it may not broaden it. Referral and management approval are escalation mechanisms, while out-of-appetite risks and filing or bulletin conflicts cannot be cleared by referral or bound.

## Final controls

Before a coverage conclusion, payment calculation, binding decision, referral disposition, or insured-facing communication, confirm:

1. **Assembly:** the issued record establishes dates, state, Declarations, base edition, and each attachment.
2. **Authority:** the conclusion is identified as contract, regulatory, or internal guidance.
3. **Sequence:** the analysis retains the cause/property gate, exclusion, narrow write-back, settlement, limit, deductible, and condition in their stated order.
4. **State:** the relevant overlay has passed its own scope test and remains separate from issued contract terms.
5. **Operations:** the file records facts, authority, calculations, notices, referrals, and escalations without converting internal workflow into an insured obligation.

If a gate cannot be established, do not cure the gap with a later form, an assumed endorsement, a bulletin, or an internal instruction.
