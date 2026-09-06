---
type: property claim conditions reference
title: Section I Claim Conditions, Payment, and Deductibles
description: Select the issued HO-3 edition and attached state or coverage endorsements before applying Section I notice, preservation, proof-of-loss, suit, payment, and deductible provisions. This reference separates base-form duties from Texas timing and wind-hail rules and from water and roof deductible overlays.
tags: [homeowners, property-claims, section-i, deductibles, proof-of-loss, texas]
sources:
  - id: openwiki-source-f8563069b83f765bb32e6be4
    resource: repo://bulletins/FL/2023-04-roof-age-nonrenewal.md
  - id: openwiki-source-3624f12a121557db250a950b
    resource: repo://bulletins/TX/2021-08-windstorm-deductible.md
  - id: openwiki-source-cd26c30cc942869b52618f95
    resource: repo://forms/HO/MS/HO-04-90/2010-10.md
  - id: openwiki-source-e727058d16eee86c951e380a
    resource: repo://forms/HO/MS/HO-3/2011-05.md
  - id: openwiki-source-f4ebd2ece3eaf490178dfc41
    resource: repo://forms/HO/MS/HO-3/2018-09.md
  - id: openwiki-source-ff7de1315ac46ce4dd65d251
    resource: repo://forms/HO/TX/HO-01-45/2022-01.md
generated: { by: "openwiki/0.5.0", at: "2026-09-05T20:29:02.779Z" }
---

## Purpose and control boundary

This page is the Section I handling sequence for the synthetic homeowners forms: what an insured must do after loss, when a proof-of-loss deadline and payment trigger arise, and which deductible path applies. It is not a coverage grant or a substitute for the issued policy. Begin with the policy record—written date, effective date, state, declarations, and attached endorsements—rather than importing terms from a later edition or a regulatory bulletin.

<!-- openwiki: broken internal link [/openwiki/coverage/policy-editions-and-governing-forms] file "/openwiki/coverage/policy-editions-and-governing-forms" does not exist. Fix the href or restore the target, then delete this comment. -->
The base-form selection is a hard control. **HO-3 2011-05** governs policies written from 2011-05-01 through 2018-08-31 and remains controlling for their losses even when reported later. **HO-3 2018-09** governs policies written on or after 2018-09-01. Therefore, the 2018 inventory, loss-payment, and S.5 deductible language does **not** supply an omitted term for a 2011 policy. See [Governing Form Editions and Policy Assembly](/openwiki/coverage/policy-editions-and-governing-forms) for the selection and attachment controls. [2011 applicability](repo://forms/HO/MS/HO-3/2011-05.md#L1-L7) · [2018 applicability](repo://forms/HO/MS/HO-3/2018-09.md#L1-L4)

State amendments and coverage endorsements are additional, conditional layers. An endorsement must be part of the issued policy; a bulletin may establish a regulatory constraint but does not by itself prove attachment. Where attached, the Texas amendatory endorsement expressly governs over a conflicting base-form provision. [Texas attachment and conflict rule](repo://forms/HO/TX/HO-01-45/2022-01.md#L1-L4) · [Texas filing rule](repo://bulletins/TX/2021-08-windstorm-deductible.md#L35-L37)

### Routing map

<!-- openwiki: broken internal link [/openwiki/coverage/property/water-damage-and-backup] file "/openwiki/coverage/property/water-damage-and-backup" does not exist. Fix the href or restore the target, then delete this comment. -->
- **Coverage and water source:** decide whether the loss is covered before applying the handling conditions. For sewer/drain backup and sump events, use [Water Damage and Backup](/openwiki/coverage/property/water-damage-and-backup) and the issued HO 04 90 endorsement.
<!-- openwiki: broken internal link [/openwiki/coverage/coverage-a/roof-settlement] file "/openwiki/coverage/coverage-a/roof-settlement" does not exist. Fix the href or restore the target, then delete this comment. -->
<!-- openwiki: broken internal link [/openwiki/state-overlays/florida] file "/openwiki/state-overlays/florida" does not exist. Fix the href or restore the target, then delete this comment. -->
- **Roof settlement and roof deductibles:** use [Roof Settlement](/openwiki/coverage/coverage-a/roof-settlement) for the separate 2018 roof-surfacing settlement path and attached roof endorsements. Florida-specific roof terms belong in the [Florida overlay](/openwiki/state-overlays/florida).
<!-- openwiki: broken internal link [/openwiki/state-overlays/texas] file "/openwiki/state-overlays/texas" does not exist. Fix the href or restore the target, then delete this comment. -->
- **Texas amendment:** use the [Texas overlay](/openwiki/state-overlays/texas) when HO 01 45 is attached and temporally applicable. It changes deductible application and adds its own action and prompt-payment language.
<!-- openwiki: broken internal link [/openwiki/operations/claims-water-loss-handling] file "/openwiki/operations/claims-water-loss-handling" does not exist. Fix the href or restore the target, then delete this comment. -->
- **Operational handling:** use [Water-Loss Handling](/openwiki/operations/claims-water-loss-handling) for intake, mitigation, vendor, and documentation workflow; this page states the policy-condition controls that workflow must preserve.

## Claim lifecycle and required file record

```mermaid
flowchart TD
    Intake["Report a property loss"] --> Record["Collect issued policy record and loss facts"]
    Record --> Edition{"Select written-date HO-3 edition"}
    Edition --> Old["2011-05 conditions"]
    Edition --> New["2018-09 conditions"]
    Old --> Layers["Verify declarations and attached endorsements"]
    New --> Layers
    Layers --> State{"Applicable Texas amendment attached"}
    State -- Yes --> Texas["Apply Texas conflicting terms and timing"]
    State -- No --> Coverage["Confirm coverage and loss cause"]
    Texas --> Coverage
    Coverage --> Duties["Record notice mitigation inventory and requested proof"]
    Duties --> Deductible["Choose one applicable deductible path"]
    Deductible --> Resolution["Agreement appraisal or judgment and payment review"]
```

*The handling sequence selects the issued base form first, overlays only verified attached terms, then records compliance and chooses the applicable deductible before payment review.* [HO-3 2011-05, applicability and conditions](repo://forms/HO/MS/HO-3/2011-05.md#L3-L7) · [HO-3 2018-09, conditions](repo://forms/HO/MS/HO-3/2018-09.md#L101-L112) · [HO 01 45, conflict rule](repo://forms/HO/TX/HO-01-45/2022-01.md#L1-L4)

At first notice of loss, preserve an auditable record of the policy-written date, policy effective date, selected HO-3 edition, declarations limits and deductible values, state, verified attachment and edition of each endorsement, reported cause and loss date, notice recipient and date, mitigation steps, property inventory, insurer proof-of-loss request, and proof delivery date. These facts are the entrypoints for the provisions below: the base forms make duties and deductibles depend on the policy/declarations, the proof deadline depends on an insurer request, and Texas has a distinct endorsement effective-date trigger. [2011 conditions](repo://forms/HO/MS/HO-3/2011-05.md#L83-L92) · [2018 conditions](repo://forms/HO/MS/HO-3/2018-09.md#L101-L112) · [Texas effective-date trigger](repo://forms/HO/TX/HO-01-45/2022-01.md#L1-L4)

## Insured duties by controlling HO-3 edition

| Control | HO-3 2011-05 | HO-3 2018-09 | Handling consequence |
| --- | --- | --- | --- |
| **Prompt notice** | S.1 requires prompt notice to the insurer or its agent. | S.1 retains prompt notice to the insurer or its agent. | Log who received notice and when; neither form gives a fixed number of days for “prompt.” |
| **Protect and preserve** | S.1 requires protection from further damage. | S.1 requires protection from further damage. | Capture reasonable emergency mitigation and the condition of property before and after it. The neglect exclusion separately bars loss caused by failure to use all reasonable means to save and preserve property at and after loss. |
| **Inventory** | S.1 does not state an inventory requirement. | S.1 adds preparation of an inventory of damaged personal property. | Require and retain the inventory only under the 2018 wording (or another verified policy term); do not manufacture it as a 2011 S.1 duty. |
| **Sworn proof of loss** | S.2 requires a signed, sworn proof within 60 days **after the insurer requests it**. | S.2 has the same request-triggered 60-day requirement. | The request date starts the stated clock. Record the request, the requested materials, delivery, and any cure communications. |
| **Action limitation** | S.3 requires full compliance with Section I conditions and suit within two years after loss. | S.4 imposes the same two-year limitation and compliance condition. | Record the loss date and governing wording; the section number changes by edition. |

The table follows 2011-05 S.1-S.3 and 2018-09 S.1-S.4. The preservation control is reinforced by each edition's neglect exclusion; it does not justify treating every post-loss expense or every later deterioration as automatically covered. [2011 conditions and neglect exclusion](repo://forms/HO/MS/HO-3/2011-05.md#L71-L75) [2011 conditions](repo://forms/HO/MS/HO-3/2011-05.md#L83-L90) · [2018 conditions and neglect exclusion](repo://forms/HO/MS/HO-3/2018-09.md#L83-L87) [2018 conditions](repo://forms/HO/MS/HO-3/2018-09.md#L101-L109)

## Adjustment and payment checkpoints

Only **HO-3 2018-09 S.3** supplies the base-form loss-payment sequence in these sources: the insurer adjusts losses with the insured and pays the insured unless another payee is named; payment is due 60 days after receipt of proof of loss **and** written agreement, an appraisal award, or a court judgment. Treat those as conjunctive resolution checkpoints, not a universal 60-day deadline running from notice alone. The 2011-05 Section I conditions stop at its S.4 deductible provision and do not contain that 2018 S.3 payment clause. [2018 S.3](repo://forms/HO/MS/HO-3/2018-09.md#L107-L108) · [2011 S.1-S.4](repo://forms/HO/MS/HO-3/2011-05.md#L83-L92)

For an applicable **Texas HO 01 45** endorsement, keep the following changes separate from that base-form payment trigger:

- **Action period:** T.4 says the form's S.4 action period is extended from two years to **two years and one day** after loss.
- **Carrier prompt-payment milestones:** T.5 requires acknowledgement within 15 days; a written approval or denial within 15 business days after receiving all reasonably requested items; and payment within five business days after approval notice.

The endorsement does not describe T.5 as a rewrite of 2018 S.3. Track both the selected base payment clause and the applicable Texas milestones instead of relabeling either one. Also perform a compatibility check: T.4 expressly names an **S.4 action** provision, which matches 2018-09, whereas 2011-05 places its action limitation in S.3 and uses S.4 for the deductible. Do not silently transpose the Texas cross-reference onto a 2011 policy; resolve it from the issued policy record. [Texas T.4-T.5](repo://forms/HO/TX/HO-01-45/2022-01.md#L21-L27) · [2018 S.3-S.4](repo://forms/HO/MS/HO-3/2018-09.md#L107-L110) · [2011 S.3-S.4](repo://forms/HO/MS/HO-3/2011-05.md#L87-L92)

## Deductible decision rules

Start with the Declarations and the coverage path. A deductible is not an extra loss category: apply the controlling provision to the portion of loss for which it speaks, and do not stack the ordinary deductible with an alternate deductible where the form or bulletin selects one deductible.

### Base-form ordinary deductible

- Under **2011-05 S.4**, the deductible shown in the Declarations applies to each Section I loss.
- Under **2018-09 S.5**, the Declarations deductible also applies to each Section I loss, subject to a separate windstorm/hail deductible required by a state amendatory endorsement. Where both could apply under S.5, the form says only the larger is deducted.

The declaration value must be taken from the issued policy; neither base form fixes a dollar amount. [2011 S.4](repo://forms/HO/MS/HO-3/2011-05.md#L89-L92) · [2018 S.5](repo://forms/HO/MS/HO-3/2018-09.md#L109-L112)

### Water-backup alternate deductible

If **HO 04 90 (2010-10)** is attached, it changes the water-backup coverage path: it provides stated A/B/C coverage for sewer/drain backup or sump-related discharge or overflow, subject to its terms. For each loss under the endorsement, its separate **$500 deductible** applies and the Section I Declarations deductible **does not** apply. This is a replacement path, not two deductibles. Confirm attachment, the endorsement's policy-period sublimit or any higher declared limit, the source of water, and its maintenance condition before applying this result. [HO 04 90 W.1-W.5](repo://forms/HO/MS/HO-04-90/2010-10.md#L5-L25) · [2018 water-backup attachment condition](repo://forms/HO/MS/HO-3/2018-09.md#L69-L77)

### Texas windstorm and hail deductible

For a Texas policy with HO 01 45 attached and effective on or after 2022-01-01, T.1 implements Texas Bulletin B-2021-08. Read the endorsement and bulletin together: the contractual clause applies a separate windstorm/hail deductible and the bulletin supplies the regulatory disclosure, application, and filing constraints. The endorsement states the percentage of Coverage A, generally from 1% through 5%, with a 10% ceiling in stated seacoast territories; the bulletin also permits a flat-dollar alternative no lower than the all-other-perils deductible. [HO 01 45 T.1 and T.6](repo://forms/HO/TX/HO-01-45/2022-01.md#L5-L11) [HO 01 45 T.6](repo://forms/HO/TX/HO-01-45/2022-01.md#L29-L31) · [Bulletin B.2](repo://bulletins/TX/2021-08-windstorm-deductible.md#L9-L13)

The no-stacking and allocation controls are explicit in both sources:

1. A windstorm/hail loss receives **only** the windstorm/hail deductible; do not also deduct the all-other-perils amount.
2. For one occurrence involving wind/hail and another covered peril, use a deductible for each respective portion only when damages can be separately determined.
3. If those damages cannot be separately determined, apply only the **larger single deductible** to the entire loss.
4. A higher wind/hail percentage at renewal is ineffective for that renewal term without the required 30-day written notice; the prior percentage remains applicable.

The bulletin additionally requires Declarations disclosure in specified form and approved or deemed-approved filing of the amendatory endorsement and rate rule before application. Those regulatory facts support review and configuration controls, but they are not evidence that a particular policy has HO 01 45 attached. [HO 01 45 T.1-T.2](repo://forms/HO/TX/HO-01-45/2022-01.md#L5-L15) · [Bulletin B.3-B.4](repo://bulletins/TX/2021-08-windstorm-deductible.md#L15-L25) · [Bulletin B.7](repo://bulletins/TX/2021-08-windstorm-deductible.md#L35-L37)

When the declarations specify a per-named-storm Texas deductible, the named-storm period starts when the National Hurricane Center names the storm and ends 72 hours after its designation is discontinued; all wind/hail loss during that period is one occurrence for deductible purposes. If wind/hail is excluded because the insured obtained that coverage through the Texas Windstorm Insurance Association and the required exclusion endorsement and acknowledgement are in place, T.1 does not apply. [HO 01 45 T.3 and T.7](repo://forms/HO/TX/HO-01-45/2022-01.md#L17-L19) [HO 01 45 T.7](repo://forms/HO/TX/HO-01-45/2022-01.md#L33-L37)

### Florida roof and hurricane routing

<!-- openwiki: broken internal link [/openwiki/state-overlays/florida] file "/openwiki/state-overlays/florida" does not exist. Fix the href or restore the target, then delete this comment. -->
For Florida residential policies issued or renewed with an effective date on or after 2023-07-01, the roof-age bulletin allows a separate roof deductible only when the insured is offered a policy without it at a filed and approved rate and the premium difference is disclosed in writing at offer. It prohibits an ACV roof schedule for a roof under ten years old at the policy effective date. A hurricane deductible remains otherwise permitted, but a hurricane deductible and a separate roof deductible may not both be applied to the same loss: deduct only the larger. Apply these controls through the [Florida overlay](/openwiki/state-overlays/florida) alongside the selected base form and any issued roof endorsement. [Florida applicability and roof terms](repo://bulletins/FL/2023-04-roof-age-nonrenewal.md#L1-L3) [Florida roof deductible and settlement](repo://bulletins/FL/2023-04-roof-age-nonrenewal.md#L21-L25) · [Florida hurricane rule](repo://bulletins/FL/2023-04-roof-age-nonrenewal.md#L31-L33)

## Focused review scenarios

Use these as file-review tests before communicating a condition, deadline, payment expectation, or net-loss estimate:

1. **Late-reported older policy:** Select 2011-05 from the written date; verify that the file does not use the 2018 inventory or S.3 payment language.
2. **Proof-of-loss clock:** Confirm a documented insurer request, then calculate 60 days from that request rather than from the loss report.
3. **Post-loss deterioration:** Preserve photographs, emergency invoices, and mitigation notes; evaluate the S.1 protection duty together with the neglect exclusion rather than presuming avoidable damage is part of the original loss.
4. **Attached water-backup loss:** Verify HO 04 90 and its conditions; apply its $500 deductible and exclude the ordinary Section I deductible from that endorsement loss.
5. **Texas mixed-peril occurrence:** Determine whether wind/hail and other covered damage can be allocated. If not, use only the larger deductible; also test endorsement attachment, effective date, declaration disclosure, and any renewal-increase notice.
6. **Texas deadlines:** Record receipt, completion of reasonably requested items, written decision, approval notice, payment, and the action deadline separately. Do not mistake the 15-day and five-business-day endorsement milestones for the 2018 S.3 proof-plus-resolution payment condition.
7. **Florida roof/hurricane loss:** Confirm the applicable bulletin period and roof product terms; never deduct both a separate roof deductible and hurricane deductible from the same loss.

The invariant across these scenarios is: **select the issued form, verify the overlay, document the trigger, and apply the single deductible rule that the controlling language selects.**
