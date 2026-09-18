---
type: coverage condition
title: Ordinance or Law Coverage
description: Compares the base-form ordinance-or-law exclusions and built-in code coverage with HO 04 16 editions 2018-09 and 2023-11. Explains the covered-loss trigger, limits, covered and excluded code costs, payment conditions, state-form boundaries, and roof-settlement interaction.
tags: [ordinance or law, building code, HO 04 16, Coverage A, roof settlement, policy conditions]
sources:
  - id: openwiki-source-d7e85cf3e721d2c3c6ee885c
    resource: repo://forms/DP/MS/DP-3/2026-01.md
  - id: openwiki-source-e81c5a85097780cfed50a7a1
    resource: repo://forms/HO/MS/HO-04-16/2018-09.md
  - id: openwiki-source-8128a40005a9dcb88892ab86
    resource: repo://forms/HO/MS/HO-04-16/2023-11.md
  - id: openwiki-source-5802aac0ff04777c19a4717f
    resource: repo://forms/HO/MS/HO-23-74/2025-05.md
  - id: openwiki-source-7176aead92778c93cb0441d2
    resource: repo://forms/HO/MS/HO-3/2024-03.md
  - id: openwiki-source-ea6397bf6ad5bac1c652ab3a
    resource: repo://forms/HO/MS/HO-4/2021-10.md
  - id: openwiki-source-25d651d4a45fc0fd8ab047e2
    resource: repo://forms/HO/MS/HO-5/2022-06.md
  - id: openwiki-source-9a3362ddf208da1fe1570617
    resource: repo://forms/HO/MS/HO-6/2023-02.md
  - id: openwiki-source-fe5cf28f9b15285dd496cba1
    resource: repo://guidelines/claims/water-loss-handling.md
generated: { by: "openwiki/0.5.2", at: "2026-09-18T17:38:15.786Z" }
verified:
  - by: openwiki/0.5.2
    at: 2026-09-18T17:38:15.786Z
---

# Ordinance or Law Coverage

## Scope and controlling relationship

The supplied Mississippi base forms start from an exclusion or limitation rather than an automatic code-upgrade grant. HO-3 2024-03 excludes loss caused by enforcement of an ordinance, law, or governmental requirement in its perils section ([HO-3 P.7](repo://forms/HO/MS/HO-3/2024-03.md#L475-L487)). DP-3 2026-01 likewise excludes enforcement loss and compliance costs in P.41 and repeats the exclusion in X.2 ([DP-3 P.41](repo://forms/DP/MS/DP-3/2026-01.md#L1390-L1397), [DP-3 X.2](repo://forms/DP/MS/DP-3/2026-01.md#L1436-L1445)). HO 04 16 is an attached endorsement that changes the insurance for loss arising from enforcement: the 2018 edition says it modifies the policy and controls a conflict, and the 2023 edition says it changes the insurance and controls for ordinance-or-law coverage ([HO 04 16 2018 W.0](repo://forms/HO/MS/HO-04-16/2018-09.md#L13-L23), [HO 04 16 2023 preamble](repo://forms/HO/MS/HO-04-16/2023-11.md#L16-L21), [HO 04 16 2023 conflict rule](repo://forms/HO/MS/HO-04-16/2023-11.md#L64-L66)). HO 04 16 therefore cannot be assumed to amend a DP-3 unless that policy actually attaches an applicable endorsement.

The endorsement is not a general betterment allowance. It responds only within the applicable form or endorsement, covered property, covered cause, governmental requirement, limit, valuation, deductible, and proof conditions. A code recommendation, voluntary upgrade, excluded underlying cause, or cost for property outside the grant remains outside this coverage.

```mermaid
flowchart TD
    start["Reported code-related cost"] --> physical{"Direct physical loss to covered property?"}
    physical -->|"No"| noPhysical["No ordinance-or-law code-cost coverage"]
    physical -->|"Yes"| peril{"Loss caused by a covered peril?"}
    peril -->|"No"| noPeril["Underlying loss remains excluded"]
    peril -->|"Yes"| enforcement{"Applicable requirement enforced by governmental authority?"}
    enforcement -->|"No"| noEnforcement["No payment for advisory or voluntary compliance"]
    enforcement -->|"Yes"| work{"Required work and cost tied to the covered loss?"}
    work -->|"No"| noWork["Unrelated, prior-condition, or elective cost excluded"]
    work -->|"Yes"| covered["Evaluate demolition, debris, and increased construction cost"]
    covered --> limit["Apply edition limit, deductible, valuation, and proof conditions"]
```

*Caption: Decision gates for ordinance-or-law code costs; the flow summarizes the cited form requirements and does not replace the operative policy or endorsement.*

## Base-form landscape

The built-in arrangements differ materially. The percentages below are the wording of the supplied edition, not a conclusion that a particular policy's declarations or attachments provide the referenced Coverage A.

| Form and edition | Base exclusion or limitation | Built-in ordinance-or-law provision in the supplied edition |
| --- | --- | --- |
| DP-3 2026-01 | P.41 and X.2 exclude enforcement loss and compliance costs. | The supplied 2026-01 Additional Coverages section provides debris, mitigation, tree, and related provisions but no listed ordinance-or-law grant; do not carry the older DP-3 2012-11 or 2020-08 percentage into this edition ([DP-3 E.1-E.4](repo://forms/DP/MS/DP-3/2026-01.md#L834-L857), [DP-3 P.41/X.2](repo://forms/DP/MS/DP-3/2026-01.md#L1394-L1397)). |
| HO-3 2024-03 | A.27 limits increased ordinance-or-law costs unless otherwise provided; P.7 excludes enforcement loss. | E.18 provides increased compliance cost at **15% of the amount of insurance applying to the dwelling**; E.19 separately addresses required demolition and reconstruction ([HO-3 A.27](repo://forms/HO/MS/HO-3/2024-03.md#L149-L153), [HO-3 E.18-E.19](repo://forms/HO/MS/HO-3/2024-03.md#L439-L445)). |
| HO-4 2021-10 | Coverage A is expressly not provided. B.19 and D.16 preserve separate building/loss-of-use boundaries for ordinance-related costs. | E.45-E.48 state a **10% of Coverage A** provision and related demolition, reconstruction, and permit wording, even though the same form says Coverage A is not provided ([HO-4 A.1-A.3](repo://forms/HO/MS/HO-4/2021-10.md#L71-L77), [HO-4 B.19](repo://forms/HO/MS/HO-4/2021-10.md#L161-L167), [HO-4 E.45-E.48](repo://forms/HO/MS/HO-4/2021-10.md#L439-L453)). Treat that literal dependency as an issue to reconcile from the issued policy and attachments; do not invent a Coverage A limit. |
| HO-5 2022-06 | P.4 and X.1 contain enforcement exclusions, subject to the form's Additional Coverages wording. | E.31-E.35 provide **15% of the applicable amount of Coverage A**, required demolition/clearing, increased compliant work, and a repair-or-replace/documentation condition ([HO-5 E.31-E.35](repo://forms/HO/MS/HO-5/2022-06.md#L487-L495), [HO-5 P.4/X.1](repo://forms/HO/MS/HO-5/2022-06.md#L575-L581), [HO-5 X.1](repo://forms/HO/MS/HO-5/2022-06.md#L711-L717)). The source does not say to treat that percentage as a separate amount in addition to Coverage A. |
| HO-6 2023-02 | X.1 excludes enforcement loss unless an ordinance-or-law endorsement is attached. | E.40 provides **additional coverage of 15% of Coverage A** for enforcement costs; E.41 limits undamaged-property removal and excludes unrelated correction and failure-to-comply costs ([HO-6 E.40-E.41](repo://forms/HO/MS/HO-6/2023-02.md#L440-L446), [HO-6 X.1](repo://forms/HO/MS/HO-6/2023-02.md#L668-L674)). |

These are form-structure comparisons, not automatic coverage decisions. Confirm the policy line, declarations, attached endorsements, effective edition, and any state-mandated modification. All supplied form sources here are Mississippi editions; another state's operative wording may change the result.

## HO 04 16 trigger and covered work

Both HO 04 16 editions require a covered physical-loss path before code costs can be considered:

1. **Covered direct physical loss first.** The 2018 edition requires direct physical loss to covered property caused by a peril insured against and says code-only loss is not covered ([2018 W.0](repo://forms/HO/MS/HO-04-16/2018-09.md#L21-L31)). The 2023 edition requires direct physical loss caused by a covered peril during the policy period ([2023 W.1-W.4](repo://forms/HO/MS/HO-04-16/2023-11.md#L70-L87)).
2. **A legally applicable requirement.** The requirement must regulate repair, construction, demolition, reconstruction, replacement, occupancy, or use as stated by the edition, be in force, and be enforced by the governmental authority having jurisdiction. A recommendation, anticipated future requirement, private preference, or voluntary compliance is insufficient ([2018 W.7-W.9](repo://forms/HO/MS/HO-04-16/2018-09.md#L27-L35), [2018 W.64-W.65](repo://forms/HO/MS/HO-04-16/2018-09.md#L181-L187), [2023 W.2](repo://forms/HO/MS/HO-04-16/2023-11.md#L76-L83), [2023 W.54](repo://forms/HO/MS/HO-04-16/2023-11.md#L303-L306)).
3. **A required and attributable cost.** The insured must identify the required work and show that the cost results from the covered loss. Both editions exclude pre-loss or unrelated conditions, elective betterment, and costs that would have arisen without the enforcement ([2018 W.8-W.10](repo://forms/HO/MS/HO-04-16/2018-09.md#L27-L35), [2023 W.15-W.18](repo://forms/HO/MS/HO-04-16/2023-11.md#L133-L149)).

Once those gates are met, the endorsements address three principal categories:

- **Undamaged portion:** loss in value or required removal/demolition of an undamaged portion when the ordinance or law requires it because of the covered loss ([2018 W.1-W.4](repo://forms/HO/MS/HO-04-16/2018-09.md#L55-L65), [2023 W.5-W.7](repo://forms/HO/MS/HO-04-16/2023-11.md#L89-L100)).
- **Demolition and debris:** reasonable required demolition and resulting debris removal, subject to the edition's property and cost wording ([2018 W.4, W.10-W.11](repo://forms/HO/MS/HO-04-16/2018-09.md#L61-L77), [2023 W.7](repo://forms/HO/MS/HO-04-16/2023-11.md#L97-L100)).
- **Increased construction cost:** the incremental cost to repair, rebuild, or replace covered property so the work complies; ordinary repair cost and elective improvement are not the code increment ([2018 W.5-W.6](repo://forms/HO/MS/HO-04-16/2018-09.md#L63-L69), [2023 W.11-W.13](repo://forms/HO/MS/HO-04-16/2023-11.md#L114-L127)).

The 2018 edition expressly lists required changes to foundations, framing, walls, roofs, wiring, plumbing, heating, cooling, fixtures, accessibility, fire protection, safety, structural, utility, sanitation, drainage, and energy-conservation features, along with permits, plan review, inspection, and necessary architectural, engineering, or design services ([2018 W.14-W.19](repo://forms/HO/MS/HO-04-16/2018-09.md#L81-L93)). The 2023 edition requires professional services to be directly required by the applicable ordinance or law and excludes services used to dispute or appeal it ([2023 W.56-W.57](repo://forms/HO/MS/HO-04-16/2023-11.md#L1022-L1029)). Neither list makes an otherwise uncovered cause, property, or cost payable.

## Edition comparison

### 2018-09

The 2018-09 edition is superseded for policies effective on or after November 1, 2023, but remains relevant to policies written under it ([2018 notice](repo://forms/HO/MS/HO-04-16/2018-09.md#L8-L9)). Its stated ordinance-or-law limit is **10% of Coverage A** and applies to the total amounts payable under that coverage ([2018 Limit of Liability](repo://forms/HO/MS/HO-04-16/2018-09.md#L213-L221)). The cited limit provision does not say that the 10% is a separate amount in addition to Coverage A; use its actual wording with the policy's other terms.

The 2018 edition permits payment as work progresses or after work is completed when supported by evidence of incurred covered costs. It also permits withholding increased-construction-cost payment until the building is repaired, rebuilt, or constructed and the insured supplies evidence that the completed work complies ([2018 W.17-W.18](repo://forms/HO/MS/HO-04-16/2018-09.md#L47-L51), [2018 W.42-W.45](repo://forms/HO/MS/HO-04-16/2018-09.md#L137-L145)).

### 2023-11

The 2023-11 edition states a **25%** maximum for ordinance-or-law coverage. It applies to Coverage A property only to the extent the policy otherwise insures it ([2023 W.1-W.2, Limit of Liability](repo://forms/HO/MS/HO-04-16/2023-11.md#L356-L366)). One limit applies to the total covered costs under the provision regardless of the number of ordinances or laws; it is not a separate amount per requirement ([2023 W.6-W.8](repo://forms/HO/MS/HO-04-16/2023-11.md#L381-L394)). The endorsement permits covered ordinance-or-law costs in addition to direct-physical-loss amounts, but the same cost cannot be paid twice and all such costs remain subject to the single limit ([2023 W.21-W.22 and W.42](repo://forms/HO/MS/HO-04-16/2023-11.md#L455-L463), [2023 W.42](repo://forms/HO/MS/HO-04-16/2023-11.md#L560-L566)).

The 2023 edition requires the covered building to be repaired or replaced for increased construction cost, requires the work at the same residence premises unless the ordinance or law prohibits that location, and limits payment to reasonable costs actually incurred ([2023 W.13-W.14](repo://forms/HO/MS/HO-04-16/2023-11.md#L125-L131), [2023 W.33-W.35](repo://forms/HO/MS/HO-04-16/2023-11.md#L207-L221), [2023 W.64](repo://forms/HO/MS/HO-04-16/2023-11.md#L348-L350)). It also requires separation of ordinary repair cost from the compliance increment and excludes costs recovered or recoverable from another source ([2023 W.19-W.22](repo://forms/HO/MS/HO-04-16/2023-11.md#L440-L463), [2023 W.49](repo://forms/HO/MS/HO-04-16/2023-11.md#L596-L598)).

Both editions retain important boundaries: no code-only loss without covered physical damage, no excluded underlying cause, no land-use or pollutant compliance cost under this coverage, no fines or penalties, no loss of use or income, and no elective improvement or betterment ([2018 W.20-W.30](repo://forms/HO/MS/HO-04-16/2018-09.md#L95-L117), [2023 W.15-W.30](repo://forms/HO/MS/HO-04-16/2023-11.md#L133-L202)). The 2023 text also excludes voluntary standards and costs that are not enforced against the covered work ([2023 W.54](repo://forms/HO/MS/HO-04-16/2023-11.md#L303-L306), [2023 W.31-W.32](repo://forms/HO/MS/HO-04-16/2023-11.md#L505-L514)).

## Deductible, proof, and payment controls

The deductible applies after covered ordinance-or-law loss is determined in both editions. The 2018 wording applies it only to otherwise covered loss, after valuation and applicable exclusions; it does not create coverage ([2018 W.1-W.9, Deductible](repo://forms/HO/MS/HO-04-16/2018-09.md#L295-L313)). The 2023 wording applies it to covered enforcement loss after determining coverage and excluding non-attributable amounts ([2023 W.1-W.4, Deductible](repo://forms/HO/MS/HO-04-16/2023-11.md#L614-L636)). The policy deductible and any mandatory state treatment still control.

Operationally, preserve the governmental notice, order, citation, permit, inspection material, plan, estimate, contract, invoice, and proof of payment needed to identify the requirement and separate compliance cost from ordinary repair, prior-condition correction, or betterment. The 2018 edition requires prompt notice, preservation, inspection access, cost records, and evidence of performed work ([2018 W.33-W.44](repo://forms/HO/MS/HO-04-16/2018-09.md#L121-L143)). The 2023 edition requires notice, records, access, plans and specifications, permits, and evidence of incurred compliant work ([2023 W.36-W.47](repo://forms/HO/MS/HO-04-16/2023-11.md#L223-L274), [2023 W.63-W.64](repo://forms/HO/MS/HO-04-16/2023-11.md#L344-L350)). These duties support adjustment and payment; they do not independently create coverage.

## State and form interactions

The sources supplied for this page are Mississippi form editions. Read them with the declarations, attached endorsements, and any applicable state-mandated modification. DP-3 2026-01 says that a provision required by applicable law controls over a conflicting policy term while the remaining term continues to the extent permitted by law ([DP-3 AGR.11-AGR.13](repo://forms/DP/MS/DP-3/2026-01.md#L52-L60)). That is a conflict rule, not a universal list of code costs a state requires an insurer to cover.

Do not use the water-loss handling guide to decide insurability. It is expressly operational and noncontractual and says that the applicable policy, endorsements, definitions, exclusions, conditions, and valuation terms govern ([water-loss guidance H.0.1-H.0.2](repo://guidelines/claims/water-loss-handling.md#L13-L21), [water-loss guidance H.0.11-H.0.17](repo://guidelines/claims/water-loss-handling.md#L33-L47)). The operative form, endorsement, declarations, and applicable law remain the authority.

The HO 04 16 percentage is tied to Coverage A or to the amount of insurance applying to the dwelling. The 2023 endorsement says it applies to Coverage A only to the extent the policy provides that coverage and does not expand otherwise uninsured property ([2023 W.1-W.2](repo://forms/HO/MS/HO-04-16/2023-11.md#L356-L366)); it also limits application to property for which Coverage A insurance is provided ([2023 W.50](repo://forms/HO/MS/HO-04-16/2023-11.md#L600-L603)). Therefore, confirm that the policy actually insures the building under Coverage A before applying the percentage. The HO-4 boundary is material because its form says Coverage A is not provided even while its Additional Coverages section contains a Coverage-A reference ([HO-4 A.1-A.3](repo://forms/HO/MS/HO-4/2021-10.md#L71-L77), [HO-4 E.45](repo://forms/HO/MS/HO-4/2021-10.md#L445-L451)).

## Roof-loss interaction

Ordinance-or-law coverage and roof settlement answer different questions:

- **Cause and coverage:** the roof must first have covered direct physical loss, and the code requirement must result from that loss. A roof condition caused only by age or deterioration, or a code recommendation without enforcement, does not satisfy the ordinance-or-law trigger ([2023 W.3](repo://forms/HO/MS/HO-04-16/2023-11.md#L81-L87), [2023 W.15-W.18](repo://forms/HO/MS/HO-04-16/2023-11.md#L133-L149)).
- **HO-3 settlement:** the HO-3 2024-03 form settles roof surfacing on the basis applicable to the dwelling; its Coverage A settlement provisions use replacement cost when the 80% condition is met and otherwise address actual-cash-value settlement ([HO-3 A.10-A.13](repo://forms/HO/MS/HO-3/2024-03.md#L117-L123)). This is separate from the code-cost increment.
- **DP-3 2026-01 settlement:** unlike the HO-3 wording, the current DP-3 says roof surfacing is settled on an actual-cash-value basis unless an actual-cash-value roof schedule endorsement is attached ([DP-3 A.2](repo://forms/DP/MS/DP-3/2026-01.md#L161-L166)). Do not carry an HO-3 replacement-cost statement into this DP-3 edition.
- **Roof schedule effect:** HO 23 74 2025-05 settles roof surfacing at actual cash value when the damaged roof surfacing is at least 12 years old, whether or not it is repaired or replaced ([HO 23 74 W.1-W.4](repo://forms/HO/MS/HO-23-74/2025-05.md#L88-L105)). That changes valuation of the damaged roof surfacing; it does not itself create or remove ordinance-or-law coverage. The endorsement also includes reasonable building-requirement costs only when they are covered under the policy and the insured establishes that the requirement applies to the covered repair ([HO 23 74 W.27-W.28](repo://forms/HO/MS/HO-23-74/2025-05.md#L202-L208)).
- **Code-cost separation:** when HO 04 16 is attached, its own trigger, limit, repair-or-replacement rules, deductible, and proof requirements govern the ordinance-or-law increment. In particular, 2023-11 requires repair or replacement for increased construction cost even though HO 23 74 may settle damaged roof surfacing at actual cash value without requiring replacement ([2023 W.11-W.14](repo://forms/HO/MS/HO-04-16/2023-11.md#L114-L131)).

Accordingly, a roof estimate should keep at least three amounts distinguishable: covered physical roof damage under the applicable roof settlement basis, ordinary repair or replacement cost, and the incremental cost required by an enforced ordinance or law. The code-cost limit applies only to the supported code-related amount after the underlying loss and every applicable form, endorsement, deductible, and proof condition are satisfied.
