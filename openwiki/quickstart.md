---
type: routing-guide
title: Coverage Wiki Quickstart
description: Route homeowners contract, regulatory, claims, and underwriting questions to the correct authority layer and specialist page. Start with the issued-policy record and keep contract terms, regulatory controls, and internal guidance separate.
tags: [homeowners, coverage-routing, policy-assembly, state-overlays, claims, underwriting]
verified:
  - by: openwiki/0.5.0
    at: 2026-09-13T02:16:51.029Z
sources:
  - id: openwiki-source-f8563069b83f765bb32e6be4
    resource: repo://bulletins/FL/2023-04-roof-age-nonrenewal.md
  - id: openwiki-source-3624f12a121557db250a950b
    resource: repo://bulletins/TX/2021-08-windstorm-deductible.md
  - id: openwiki-source-cd26c30cc942869b52618f95
    resource: repo://forms/HO/MS/HO-04-90/2010-10.md
  - id: openwiki-source-6a71dbfe57881e21b8a0e5ea
    resource: repo://forms/HO/MS/HO-04-90/2027-01.md
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
generated: { by: "openwiki/0.5.0", at: "2026-09-13T02:16:51.029Z" }
---

## Start with the authority layer

This wiki describes a synthetic insurance corpus, not a real carrier product, ISO form, or legal advice. Forms and bulletins are frozen authority: a new edition is a new file, while a superseded edition continues to govern policies written under it. Internal guidelines are living material and are not policy language. [Corpus scope](repo://README.md#L3-L9) · [Authority lifecycle](repo://README.md#L28-L36)

| Question | Start with | Do not treat as authority for the answer |
| --- | --- | --- |
| **What does an issued policy cover, exclude, require, or pay?** | The issued-policy record: selected HO-3 edition, Declarations, and each verified attached endorsement/amendment. | An unattached repository form, bulletin, or internal workflow. |
| **What may the insurer do at issue, renewal, notice, deductible configuration, filing, or reporting?** | The applicable state bulletin after its scope and effective-date test. | Contract wording or internal authority. A bulletin does not establish attachment. |
| **How should staff investigate, reserve rights, refer, document, or bind?** | Claims or underwriting guidance after contract and regulatory layers are identified. | Coverage authority, an insured duty, or customer-facing coverage wording. |

**Internal-guidance boundary:** The water-loss guide directs staff to establish and document the water source before evaluating damage; it is not part of a policy and must not be quoted to an insured or claimant. [Water Loss Claim Handling Guidance, status and C.1](repo://guidelines/claims/water-loss-handling.md#L1-L11)

## Policy-assembly entrypoint

Collect the policy-written date, policy effective date, state, full Declarations, limits, deductible selections, selected HO-3 edition, and every actually attached form with its edition. For a claim, also preserve the loss date, alleged cause, property involved, and facts required by potentially applicable provisions. If a record or attachment is unverified, leave that issue unresolved; do not import a later form.

**HO-3 2018-09** supersedes **HO-3 2011-05** for policies written on or after 2018-09-01. **HO-3 2011-05** remains governing for policies written under it, including later-reported losses. [HO-3 2018-09, applicability](repo://forms/HO/MS/HO-3/2018-09.md#L1-L4) · [HO-3 2011-05, continuing force](repo://forms/HO/MS/HO-3/2011-05.md#L1-L7)

Select **HO 04 90** independently from the base form. **HO 04 90 2010-10** remains governing for policies written under it, including later-reported losses. **HO 04 90 2027-01** replaces edition 2026-01 for policies written on or after 2027-01-01; verify the exact issued attachment rather than substituting it for 2010-10. [HO 04 90 2010-10, status](repo://forms/HO/MS/HO-04-90/2010-10.md#L1-L7) · [HO 04 90 2027-01, status](repo://forms/HO/MS/HO-04-90/2027-01.md#L1-L4)

Use [Governing Form Editions and Policy Assembly](/openwiki/coverage/policy-editions-and-governing-forms.md) when form selection, attachment, compatibility, or a Texas amendment is uncertain. Its operational sequence is: select the written-date HO-3 edition; verify Declarations and attachments; apply an attached in-scope state amendment at its stated conflict; then analyze grant, exclusion, narrow write-back, settlement, limits, deductible, and conditions. **HO 01 45 2022-01** attaches to HO-3, is effective for policies effective on or after 2022-01-01, and governs a conflict with the attached form; that gate neither selects an HO-3 edition nor proves individual attachment. [HO 01 45, scope and conflict rule](repo://forms/HO/TX/HO-01-45/2022-01.md#L1-L4)

### HO 04 90 edition checkpoint

| Verified attached edition | Contract terms to route to the water page |
| --- | --- |
| **HO 04 90 2010-10** | W.1–W.6: default $5,000 policy-period sublimit within Coverage A/B/C limits, separate $500 deductible, known pre-loss maintenance condition, and Coverage C ACV settlement unless its endorsement Declarations state otherwise. [2010-10 W.2–W.6](repo://forms/HO/MS/HO-04-90/2010-10.md#L13-L33) |
| **HO 04 90 2027-01** | W.1–W.7: default $10,000 policy-period sublimit within Coverage A/B/C limits, separate $1,000 deductible, the same maintenance condition, a finished-below-grade operable backflow-device condition, and Coverage C ACV settlement unless its endorsement Declarations state otherwise. [2027-01 W.2–W.7](repo://forms/HO/MS/HO-04-90/2027-01.md#L13-L55) |
| **Edition or attachment unverified** | Do not choose either edition’s limit, deductible, condition, or settlement rule. Obtain the issued endorsement and Declarations. |

For **HO 04 90 2010-10**, W.1 writes back HO-3 Section I Exclusions A.3 for the stated sewer/drain-backup and sump-event direct-property-loss route. For **HO 04 90 2027-01**, W.1 writes back the same target and route. Each edition’s W.4 preserves A.1 and A.2, so neither route is flood/surface-water or subsurface-water coverage. [2010-10 W.1 and W.4](repo://forms/HO/MS/HO-04-90/2010-10.md#L7-L11) · [2010-10 W.4](repo://forms/HO/MS/HO-04-90/2010-10.md#L21-L25) · [2027-01 W.1 and W.4](repo://forms/HO/MS/HO-04-90/2027-01.md#L3-L11) · [2027-01 W.4](repo://forms/HO/MS/HO-04-90/2027-01.md#L25-L33) · [HO-3 2018-09 A.1–A.3](repo://forms/HO/MS/HO-3/2018-09.md#L69-L77)

## Task-routing map

A route is an entrypoint, not a coverage result or proof of attachment.

| Domain | Route when the question concerns | Specialist page |
| --- | --- | --- |
| **Policy assembly** | Written date, governing edition, Declarations, attachment, compatibility, or Texas amendment | [Governing Form Editions and Policy Assembly](/openwiki/coverage/policy-editions-and-governing-forms.md) |
| **Coverage A–D / Section II** | Dwelling, roof settlement, other structures, personal property, loss of use, liability, or medical payments | [Coverage index](/openwiki/coverage/) |
| **Section I gates** | Cause of loss, direct physical loss, named peril, general exclusion, claim condition, payment, or deductible | [Property coverage](/openwiki/coverage/property/) |
| **Water and fungi** | Flood, surface/subsurface water, backup, sump event, internal discharge, seepage, water-backup terms, or resulting fungi | [Water Damage Exclusions and Water Backup Write-Back](/openwiki/coverage/property/water-damage-and-backup.md) · [Fungi, Rot, and Bacteria](/openwiki/coverage/property/fungi-rot-and-bacteria.md) |
| **Claims operations** | Water-loss intake, source/duration evidence, referral, reservation of rights, payment accounting, or completion record | [Water Loss Claims Handling](/openwiki/operations/claims-water-loss-handling.md) |
| **Florida regulatory and underwriting work** | Florida roof/nonrenewal requirements, eligibility, water-backup configuration, or authority | [Florida overlay](/openwiki/state-overlays/florida.md) · [Florida Homeowners Appetite](/openwiki/underwriting/florida-appetite.md) |
| **Texas regulatory and underwriting work** | Texas wind/hail requirements, eligibility, water-backup configuration, or authority | [Texas overlay](/openwiki/state-overlays/texas.md) · [Texas Homeowners Appetite](/openwiki/underwriting/texas-appetite.md) |
| **Enterprise authority** | Referral tier, hard stop, endorsement authority, or audit record | [Referral and Binding Authority](/openwiki/underwriting/referral-and-binding-authority.md) |

For **HO-3 2018-09**, Coverage A/B use the direct-physical-loss grant subject to exclusions, while Coverage C also requires a P.2 listed peril. Route a coverage question through those gates before treating a settlement term or endorsement limit as a grant. [HO-3 2018-09 P.1–P.2 and water exclusions](repo://forms/HO/MS/HO-3/2018-09.md#L59-L77)

## State and operational handoffs

- **Florida regulatory requirement:** OIR-2023-04 applies to Florida personal residential property policies issued or renewed with an effective date on or after 2023-07-01 and controls the stated roof-age, inspection, offer, nonrenewal, deductible-overlap, and reporting matters. It does not determine an issued policy’s roof-settlement wording. [OIR-2023-04, scope and controls](repo://bulletins/FL/2023-04-roof-age-nonrenewal.md#L1-L37)
- **Texas regulatory requirement:** B-2021-08 applies to Texas residential property policies delivered or issued for delivery with an effective date on or after 2022-01-01 and establishes the stated separate windstorm/hail deductible configuration, disclosure, loss-application, and filing requirements. [B-2021-08, scope and requirements](repo://bulletins/TX/2021-08-windstorm-deductible.md#L1-L37)
- **Internal underwriting guidance:** A state appetite guide may impose tighter authority than the enterprise referral matrix but cannot grant broader authority. Referral and management approval escalate a decision; they cannot clear an out-of-appetite risk or filing/bulletin conflict. [Referral matrix, authority boundary](repo://guidelines/authority/referral-matrix.md#L1-L11) · [Referral matrix, non-clearable conditions](repo://guidelines/authority/referral-matrix.md#L33-L40)

## Final controls

Before a coverage conclusion, payment calculation, binding decision, referral disposition, or insured-facing communication, confirm:

1. **Assembly:** The issued record establishes dates, state, Declarations, base edition, and each attachment.
2. **Authority:** The result is expressly identified as contract, regulatory requirement, or internal guidance.
3. **Sequence:** Analysis retains the cause/property gate, exclusion, narrow write-back, settlement, limit, deductible, and condition in their stated order.
4. **Edition:** A superseded edition remains governing knowledge for policies written under it; do not move 2027-01 HO 04 90 terms onto a 2010-10 policy.
5. **Operations:** The file records facts, authority, calculations, notices, referrals, and escalations without turning internal workflow into an insured obligation.

If a gate cannot be established, do not cure the gap with a later form, an assumed endorsement, a bulletin, or an internal instruction.
