---
type: policy-assembly
title: Coverage Wiki Quickstart
description: Route homeowners coverage and operational questions involving HO 04 90 2026-01 by policy effective date, issued attachments, water cause, claims handling, underwriting controls, and state overlays. Use this map to keep contract wording distinct from internal guidance.
tags: [coverage, policy-assembly, claims, underwriting, water-backup, state-overlays, navigation]
verified:
  - by: openwiki/0.6.1
    at: 2026-10-02T17:06:49.327Z
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
generated: { by: "openwiki/0.6.1", at: "2026-10-02T17:06:49.327Z" }
---

# Coverage Wiki Quickstart

This is a task-routing map, not a substitute for the issued policy, declarations, attached endorsement, state form, applicable law, or internal procedure. Forms and bulletins are frozen authority; manuals and guidelines are living operational guidance, while memoranda and training explain rather than create coverage ([repository document families](repo://README.md#L15-L23), [authority boundary](repo://README.md#L35-L41)).

## Start with the issued package

For any water question, record the line, state, policy-effective date, policy period, declarations, base form, complete endorsement package, and state attachments before interpreting the loss. A repository file, quote, schedule entry, or system label does not establish that an endorsement was issued or attached. The evidence path is load-bearing because it carries line, state, form, and edition context ([repository path model](repo://README.md#L26-L31)).

```mermaid
flowchart TD
  Q["Water coverage or operations question"] --> P["Record line, state, effective date, declarations"]
  P --> E["Select base and endorsement editions"]
  E --> A{"HO 04 90 2026-01 actually attached?"}
  A -->|"no"| H["Use the applicable earlier edition or base form; hold if package is missing"]
  A -->|"yes"| W["Read HO-3, HO 04 90, declarations, and state form together"]
  H --> C["Establish water source and covered property"]
  W --> C
  C --> R["Route to coverage, claims, underwriting, and state controls"]
```

### Edition gate: HO 04 90 2026-01

HO 04 90 2026-01 is a multistate endorsement that attaches to HO-3, modifies Section I—Exclusions A.3, and replaces 2010-10 for policies written on or after **2026-01-01** ([edition metadata](repo://forms/HO/MS/HO-04-90/2026-01.md#L1-L4)). That date selects a candidate edition; it does **not** mean the endorsement applies merely because the topic is water loss. Confirm the actual attachment and complete issued wording. For the assembly decision and the 2027-01 supersession boundary, use [Policy Editions and State Attachments](policy-assembly/editions-and-state-attachments.md).

When the 2026-01 endorsement is attached, it covers direct physical loss to Coverage A, B, and C property from sewer or drain backup or sump, sump-pump, or related-equipment overflow or discharge, including an event resulting from mechanical breakdown ([endorsement grant](repo://forms/HO/MS/HO-04-90/2026-01.md#L6-L11)). Its default maximum is **$10,000 for all endorsement loss in one policy period**, subject to a higher declarations limit, and a separate **$1,000 deductible applies to each loss** ([limit and deductible](repo://forms/HO/MS/HO-04-90/2026-01.md#L13-L23)). Flood, surface water, storm surge, body-of-water overflow, and below-ground water remain excluded; the endorsement also contains a known-maintenance condition and a backwater-valve condition for finished below-grade areas ([preserved exclusions and conditions](repo://forms/HO/MS/HO-04-90/2026-01.md#L25-L47)). These are contract terms, not underwriting thresholds.

## Route by work product

| Need | Open first | What to establish |
| --- | --- | --- |
| Edition, attachment, declarations, or state assembly | [Policy Editions and State Attachments](policy-assembly/editions-and-state-attachments.md) | Effective-date interval, base form, attached endorsement, declarations, and state form; do not backdate later wording. |
| Water cause and coverage boundaries | [Water Backup and Sump Discharge](coverage/perils/water-backup.md) | Sewer/drain reverse flow versus sump discharge, flood, surface water, groundwater, seepage, source repair, covered property, limit, deductible, and valuation. |
| Reported or pending loss | [Water Loss Handling](claims/guidelines/water-loss-handling.md) | Safe mitigation, evidence preservation, source and path, direct physical damage, exact attached wording, exclusions, scope, payment, and escalation. Guidance does not create coverage. |
| Attachment, deductible, eligibility, or referral | [Endorsements and Deductibles](underwriting/manual/endorsements-and-deductibles.md) | Whether the carrier may attach or select terms, required evidence and authority, and reconciliation of rating, declarations, and issued package. Internal rules are not policy terms. |
| Base homeowners form | [HO-3 Form Editions](coverage/forms/ho-3.md) | The applicable HO-3 edition, Section I exclusions, covered property, settlement, and declarations before applying a write-back. |
| State-specific contract or operations | [Policy Editions and State Attachments](policy-assembly/editions-and-state-attachments.md) and the applicable state overlay | Amendatory form and bulletin requirements separately from the multistate endorsement and internal guidance. |

## Water-loss triage

<!-- openwiki: broken internal link [claims/guidelines/water-loss-handling.md#L12-L16] heading anchor "L12-L16" does not exist in "claims/guidelines/water-loss-handling.md". Fix the href or restore the target, then delete this comment. -->
<!-- openwiki: broken internal link [claims/guidelines/water-loss-handling.md#L43-L54] heading anchor "L43-L54" does not exist in "claims/guidelines/water-loss-handling.md". Fix the href or restore the target, then delete this comment. -->
Do not infer “backup” from standing water or a claimant’s label. Establish the source, first appearance, migration path, duration, affected property, failed component, maintenance history, weather/runoff, and direct physical damage. Separate mitigation, source repair, permanent repair, valuation, and coverage; an inspection, estimate, mitigation authorization, reserve, or partial payment is not acceptance of the whole claim ([claims workflow](claims/guidelines/water-loss-handling.md#L12-L16), [investigation evidence](claims/guidelines/water-loss-handling.md#L43-L54)).

<!-- openwiki: broken internal link [claims/guidelines/water-loss-handling.md#L56-L69] heading anchor "L56-L69" does not exist in "claims/guidelines/water-loss-handling.md". Fix the href or restore the target, then delete this comment. -->
For an attached 2026-01 endorsement, consult the exact endorsement with the HO-3 and declarations: the grant is limited to stated Coverage A/B/C property, and the preserved flood, surface-water, below-ground-water, maintenance, and below-grade backflow requirements still require factual investigation ([water-loss contract consultation](claims/guidelines/water-loss-handling.md#L56-L69)).

## State and guidance boundary

<!-- openwiki: broken internal link [policy-assembly/editions-and-state-attachments.md#L63-L72] heading anchor "L63-L72" does not exist in "policy-assembly/editions-and-state-attachments.md". Fix the href or restore the target, then delete this comment. -->
State amendatory forms modify or supplement the contract for the matters they address. Bulletins constrain disclosure, issuance, rating, claims administration, or other carrier conduct; they do not silently add an endorsement limit or deductible. Underwriting and claims manuals control eligibility, evidence, referrals, investigation, and authority; they do not grant, restrict, waive, or interpret coverage ([state-layer roles](policy-assembly/editions-and-state-attachments.md#L63-L72)). Where the state page is absent or records conflict, hold the affected action and escalate rather than choosing the broader or newest wording.

<!-- openwiki: broken internal link [coverage/perils/water-backup.md#L206-L214] heading anchor "L206-L214" does not exist in "coverage/perils/water-backup.md". Fix the href or restore the target, then delete this comment. -->
For Illinois water-backup work, route to the Illinois overlay and verify its disclosure and claims controls separately from the contract. The focused coverage page explains that an overlay disclosure does not replace the edition-specific attached endorsement ([Illinois overlay discussion](coverage/perils/water-backup.md#L206-L214)).

## Final check

Before publishing a position or issuing a package, verify: (1) effective date and governing editions; (2) complete, legible, correctly matched attachments; (3) declarations limits and deductibles; (4) water source, covered property, exclusions, and valuation; (5) state form and bulletin; and (6) the distinct operational owner for claims, underwriting, authority, or rating. Cite the acting document and describe whether it **supersedes**, **writes back**, **preserves**, **modifies**, **implements**, or **constrains** another source ([relationship conventions](repo://README.md#L92-L95)).
