---
type: policy-assembly
title: Coverage Wiki Quickstart
description: Start here to route a homeowners coverage, regulatory, claims, or underwriting question to the controlling policy assembly or specialized reference. It separates issued contract terms, regulator requirements, and internal guidance so no layer is used as authority for another.
tags: [homeowners, policy-assembly, coverage-routing, state-overlays, claims, underwriting]
verified:
  - by: openwiki/0.5.0
    at: 2026-09-05T21:30:30.144Z
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
generated: { by: "openwiki/0.5.0", at: "2026-09-05T21:30:30.144Z" }
---

## Start with the authority layer

This wiki documents a synthetic insurance corpus, not a real carrier product, ISO form, or legal advice. Forms and regulator bulletins are frozen authority; a new edition is a new file and does not revise an already issued policy. Internal guidelines are living operational material. [Corpus scope and source lifecycle](repo://README.md#L3-L18) · [Frozen authority and living guidance](repo://README.md#L28-L36)

| Question | Controlling source | Do not use as a substitute |
| --- | --- | --- |
| What does an issued policy cover, exclude, require, or pay? | The policy-specific assembly: selected HO-3 edition, Declarations, and compatible endorsements or state amendments actually attached. | A later form, a repository copy of an unattached form, a bulletin, or an internal workflow. |
| What constrains issuance, renewal, notice, deductible setup, or other insurer conduct? | The applicable regulator bulletin, with the issued policy retained separately for contractual terms. | An appetite guide or a referral approval. A bulletin does not attach an endorsement. |
| How should staff investigate, document, refer, reserve rights, or bind? | The relevant internal claims or underwriting guidance after the contract and regulatory layers are identified. | Coverage authority, policy language, an insured duty, or customer-facing coverage wording. |

**Invariant:** internal guidance cannot grant, restrict, or prove coverage. A state appetite guide may be more restrictive than enterprise guidance but cannot grant broader authority, and referral cannot approve a filing or bulletin violation. [Referral-matrix precedence and hard stop](repo://guidelines/authority/referral-matrix.md#L1-L11) [Referral-matrix regulatory hard stop](repo://guidelines/authority/referral-matrix.md#L33-L40)

## Assemble the issued policy before answering a coverage question

Preserve the policy-written date, policy effective date, state, complete Declarations, limits and deductible selections, selected HO-3 edition, and every actually attached endorsement or amendment and its edition. For a claim, also preserve loss date, alleged cause, property, and facts needed to test the relevant provision. The policy-written date selects the base form: HO-3 2011-05 remains in force for policies written under it, including a later-reported loss; HO-3 2018-09 applies prospectively to policies written on or after 2018-09-01. [HO-3 2011-05 continuing force](repo://forms/HO/MS/HO-3/2011-05.md#L1-L7) · [HO-3 2018-09 applicability](repo://forms/HO/MS/HO-3/2018-09.md#L1-L4)

Use [Governing Form Editions and Policy Assembly](/openwiki/coverage/policy-editions-and-governing-forms.md) whenever the issued form set is unknown, a form is asserted to be attached, the policy predates 2018-09, or a Texas amendment may apply. The safe order is:

1. Select the HO-3 edition by **policy-written date**.
2. Verify Declarations and actual attachments; “if attached” is a condition, not evidence of attachment.
3. Apply an attached state amendment within its own effective-date scope and conflict rule.
4. Analyze the selected coverage grant and exclusions, then any narrow write-back, settlement, limits, deductible, and conditions.

For example, HO 01 45 is a Texas amendment that attaches to HO-3, is effective for policies with an effective date on or after 2022-01-01, and governs when it conflicts with the form to which it attaches. Its effective-date gate does not replace the base HO-3 written-date selection or prove attachment. [HO 01 45 applicability and conflict rule](repo://forms/HO/TX/HO-01-45/2022-01.md#L1-L4) · [Policy-assembly sequence](repo://openwiki/coverage/policy-editions-and-governing-forms.md#L45-L76)

## Route a contract question

Use the assembly page first if any policy-record fact is unresolved. Then use the most specific substantive page below; that page remains subject to the issued form set.

| If the question concerns… | Go to | Routing boundary |
| --- | --- | --- |
| Governing edition, Declarations, attachments, or a Texas amendment | [Governing Form Editions and Policy Assembly](/openwiki/coverage/policy-editions-and-governing-forms.md) | Establish the contract before importing a later edition or endorsement. |
| Dwelling property, ordinary replacement-cost baseline, or 80-percent condition | [Coverage A — Dwelling](/openwiki/coverage/coverage-a/dwelling.md) | Route wind/hail roof surfacing to its distinct settlement path. |
| Wind/hail roof surfacing, ACV schedule, roof age/material, or deductible sequence | [Coverage A — Roof Surfacing Settlement](/openwiki/coverage/coverage-a/roof-settlement.md) | Separate covered loss, surfacing scope, HO 23 74 attachment, settlement, and code-driven work. |
| Detached structures, a fence/utility connection, rental use, or the extra Coverage B limit | [Coverage B — Other Structures](/openwiki/coverage/coverage-b/other-structures.md) | Apply the selected edition; the 2018 rental/private-garage boundary is not automatically an older-policy term. |
| Contents, worldwide property, special limits, or ACV/replacement-cost treatment | [Coverage C — Personal Property](/openwiki/coverage/coverage-c/personal-property.md) | Water and fungi require their own source and attachment analysis. |
| Additional living expense or uninhabitability after a covered loss | [Coverage D — Loss of Use](/openwiki/coverage/coverage-d/loss-of-use.md) | Test the covered-loss gate, limit, duration, and fungi interaction. |
| Liability, defense, medical payments, business activity, or insured-owned/rented property | [Coverage E and F — Liability and Medical Payments](/openwiki/coverage/coverage-e-f/liability-and-medical-payments.md) | Use Section II, not a Section I property endorsement, as the starting point. |
| Section I cause of loss or a general exclusion | [Section I Property Perils and General Exclusions](/openwiki/coverage/property/perils-and-general-exclusions.md) | For 2018-09, distinguish A/B direct-physical-loss and C named-peril gates before exclusions and write-backs. |
| Notice, protection, inventory, proof of loss, payment timing, action limitation, or an ordinary deductible | [Section I Claim Conditions, Payment, and Deductibles](/openwiki/coverage/property/claim-conditions-and-deductibles.md) | Apply a controlling attached state amendment or state overlay separately. |

### Route a water, fungi, ordinance, or roof write-back correctly

An endorsement is not a general replacement for the base policy. First establish the base coverage and exclusion result, then apply only the attached endorsement's stated exception, limit, deductible, condition, and settlement terms.

| Fact pattern | Go to | Critical separation |
| --- | --- | --- |
| Flood, surface water, groundwater, backup, sump event, internal discharge, seepage, or water-backup payment terms | [Water Damage Exclusions and Water Backup Write-Back](/openwiki/coverage/property/water-damage-and-backup.md) | HO 04 90 modifies A.3 for its stated sewer/drain-backup and sump events when attached; flood/surface-water and subsurface-water exclusions remain. [HO 04 90 W.1 and W.4](repo://forms/HO/MS/HO-04-90/2010-10.md#L5-L8) [HO 04 90 W.4](repo://forms/HO/MS/HO-04-90/2010-10.md#L17-L21) |
| Fungi, mold, wet/dry rot, bacteria, mitigation, or the fungi aggregate | [Fungi, Rot, and Bacteria Limited Coverage](/openwiki/coverage/property/fungi-rot-and-bacteria.md) | HO 04 81 is a separate limited Section I write-back: the condition must result from a covered underlying peril during the policy period, and its underlying water restrictions remain. [HO 04 81 M.1-M.2](repo://forms/HO/MS/HO-04-81/2018-09.md#L5-L17) |
| Code-required demolition, increased construction cost, or undamaged roof portions | [Ordinance or Law Coverage and Undamaged Roof Portions](/openwiki/coverage/property/ordinance-or-law.md) | HO 04 16 modifies D.1; its ordinance path is distinct from damaged-property and roof-schedule settlement. [HO 04 16 O.1-O.3](repo://forms/HO/MS/HO-04-16/2018-09.md#L5-L19) |
| Wind/hail roof surfacing plus code-required undamaged work | [Coverage A — Roof Surfacing Settlement](/openwiki/coverage/coverage-a/roof-settlement.md) and [Ordinance or Law Coverage and Undamaged Roof Portions](/openwiki/coverage/property/ordinance-or-law.md) | HO 23 74 changes A.4 settlement for roof surfacing only; it does not itself pay ordinance-required undamaged surfacing. [HO 23 74 R.1-R.2](repo://forms/HO/MS/HO-23-74/2018-09.md#L5-L15) [HO 23 74 R.6](repo://forms/HO/MS/HO-23-74/2018-09.md#L37-L41) |

## Add the state overlay without confusing it with the contract

Use a state-overlay page whenever state rules may affect issuance, renewal, deductible configuration, notice, claim timing, or a roof decision. Retain the distinction: a bulletin can impose regulatory requirements, but it does not add an amendment or endorsement to a particular policy.

- **Florida:** [Florida Roof Age, ACV Schedule, and Nonrenewal Overlay](/openwiki/state-overlays/florida.md) applies OIR-2023-04 to in-scope Florida personal residential policies issued or renewed with an effective date on or after 2023-07-01. It covers roof-age and inspection controls, roof-deductible/ACV-schedule offers, nonrenewal, deductible nonstacking, and county reporting; it does not determine issued roof-settlement terms. [OIR-2023-04 applicability and scope](repo://bulletins/FL/2023-04-roof-age-nonrenewal.md#L1-L37)
- **Texas:** [Texas Windstorm and Hail Deductible Overlay](/openwiki/state-overlays/texas.md) separates Bulletin B-2021-08 from HO 01 45. The bulletin applies to Texas residential property policies delivered or issued for delivery with effective dates on or after 2022-01-01 and supplies regulatory deductible, disclosure, nonstacking, and filing controls; contract wording still requires the issued-policy attachment check. [B-2021-08 applicability and loss rule](repo://bulletins/TX/2021-08-windstorm-deductible.md#L1-L7) [B-2021-08 loss rule and filing](repo://bulletins/TX/2021-08-windstorm-deductible.md#L15-L37)

## Use internal guidance only for operations and authority

These pages make work reproducible; they do not establish coverage or replace a bulletin.

| Need | Internal guidance page | Use after identifying |
| --- | --- | --- |
| Water-loss intake, source/duration investigation, referral, reservation of rights, and closing record | [Water Loss Claims Handling](/openwiki/operations/claims-water-loss-handling.md) | The issued policy and water/write-back paths. The underlying guidance directs staff to establish and document the water source before evaluating damage, but it is not policy language and must not be quoted to an insured or claimant. [Guidance status and source-first direction](repo://guidelines/claims/water-loss-handling.md#L1-L11) |
| Roof-loss fact development, age/material documentation, calculation review, ordinance handoff, state check, and escalation | [Roof Loss Claims Handling](/openwiki/operations/claims-roof-loss-handling.md) | The contract analysis in roof settlement and ordinance pages, plus the relevant overlay. |
| Enterprise authority tier, referral, hard stop, endorsement route, and audit record | [Referral and Binding Authority](/openwiki/underwriting/referral-and-binding-authority.md) | State guide, issued-form dependencies, and applicable bulletin. Referral and management approval are escalation paths; out-of-appetite or filing/bulletin-conflicting risks must not be bound. [Referral outcomes](repo://guidelines/authority/referral-matrix.md#L7-L10) [Non-clearable conditions](repo://guidelines/authority/referral-matrix.md#L33-L40) |
| Florida eligibility, roof/nonrenewal controls, water-backup/mold configuration, and authority route | [Florida Homeowners Appetite](/openwiki/underwriting/florida-appetite.md) | Florida overlay requirements and issued-policy facts. |
| Texas eligibility, coastal/roof controls, water-backup configuration, wind/hail routing, and authority route | [Texas Homeowners Appetite](/openwiki/underwriting/texas-appetite.md) | Texas overlay requirements and issued-policy facts. |

## Final routing controls

Before a coverage conclusion, payment calculation, binding decision, referral disposition, or insured-facing communication, verify these focused controls:

1. **Assembly test:** Can the file show the written date, effective date, state, Declarations, selected base edition, and each actual attachment? If not, obtain the issued-policy record rather than substituting repository text.
2. **Authority test:** Is the conclusion identified as contract, regulatory, or internal guidance? Do not cite internal guidance as coverage authority or treat a bulletin as proof of attachment.
3. **Scope test:** Have peril/source, property, exclusion, write-back, settlement, limit, deductible, and condition been kept in their stated order? Do not let a settlement endorsement become the initial coverage grant.
4. **State test:** Has the relevant state overlay been checked for its own applicability gate and then kept separate from policy terms?
5. **Operations test:** Does the internal record identify factual evidence, referral/approval, calculation, notice, or escalation without converting the workflow into an insured obligation?

If a gate cannot be established, leave the affected coverage or authority issue unresolved. Do not cure the gap by importing a newer form, assuming an endorsement is attached, or treating an internal instruction as contract language.
