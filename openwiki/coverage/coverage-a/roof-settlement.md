---
type: coverage
title: Coverage A — Roof Surfacing Settlement
description: Explains the attached HO 23 74 windstorm-or-hail roof-surfacing settlement route under HO-3 2018-09, including scope separation, the material-and-age schedule, the pre-deductible floor, and deductible selection. It also distinguishes the independent HO 04 16 ordinance-or-law path and Florida, Texas, and internal handling controls.
tags: [homeowners, coverage-a, roof-surfacing, actual-cash-value, deductibles, ordinance-or-law]
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
  - id: openwiki-source-a7812317f4b735061e88f5bb
    resource: repo://forms/HO/MS/HO-23-74/2018-09.md
  - id: openwiki-source-f4ebd2ece3eaf490178dfc41
    resource: repo://forms/HO/MS/HO-3/2018-09.md
  - id: openwiki-source-ff7de1315ac46ce4dd65d251
    resource: repo://forms/HO/TX/HO-01-45/2022-01.md
  - id: openwiki-source-98996e9748507677077d5997
    resource: repo://guidelines/claims/roof-claim-handling.md
generated: { by: "openwiki/0.5.0", at: "2026-09-09T17:00:59.484Z" }
---


## Scope and controlling documents

This reference is a **contract-analysis sequence** for a Coverage A roof loss under **HO-3 Homeowners 3 — Special Form, edition 2018-09**. That base form is multistate and applies to policies written on or after 2018-09-01. It insures Coverage A property against direct physical loss unless a Section I exclusion applies; it does not make every roof condition a covered loss. In particular, the base form excludes loss caused by deterioration, wear and tear, rot, and several specified conditions affecting roofs. Determine coverage, the issued edition, the Declarations, and attached endorsements before calculating settlement. [HO-3 2018-09, heading and P.1](repo://forms/HO/MS/HO-3/2018-09.md#L1-L3) · [HO-3 2018-09, C.2](repo://forms/HO/MS/HO-3/2018-09.md#L83-L89)

The relevant layers are cumulative only where they are actually part of the issued policy:

| Layer | Role in the decision | Do not assume |
| --- | --- | --- |
| HO-3 2018-09 | Establishes Coverage A, covered-loss gateway, replacement-cost baseline, A.4 roof routing, Section I exclusions, and base deductible rule. | That roof damage is covered merely because it is reported or because settlement language exists. |
| HO 23 74, edition 2018-09 | A separately attached multistate endorsement that modifies A.4 and supplies an ACV schedule **only for roof surfacing** damaged by windstorm or hail. | That it applies because the roof is old, an estimate depreciates a roof, or underwriting normally requires it. |
| HO 04 16, edition 2018-09 | A separately attached ordinance-or-law endorsement that can restore specified code-driven costs excluded by the base form. | That it is attached whenever HO 23 74 is attached, or that it pays damaged-property settlement. |
| State amendatory form and Declarations | Can determine the applicable deductible and change the base form where it conflicts. | That the nationwide S.5 default or a prior policy's deductible controls. |

The attachment check is an invariant. A.4 routes windstorm- or hail-caused roof-surfacing loss to a schedule only when that endorsement is attached. HO 23 74 identifies itself as an endorsement that attaches to HO-3 and modifies A.4; HO 04 16 separately identifies itself as an endorsement that attaches to HO-3 and modifies Exclusion D.1. Verify each independently in the issued policy: attachment of one does not establish attachment of the other. [HO-3 2018-09, A.4 and D.1](repo://forms/HO/MS/HO-3/2018-09.md#L31-L34) [D.1](repo://forms/HO/MS/HO-3/2018-09.md#L91-L94) · [HO 23 74 2018-09, attachment](repo://forms/HO/MS/HO-23-74/2018-09.md#L1-L4) · [HO 04 16 2018-09, attachment](repo://forms/HO/MS/HO-04-16/2018-09.md#L1-L4)

For adjacent analysis, use [Coverage A — Dwelling](dwelling.md) for the issued-edition and A.3 baseline, [Section I Claim Conditions, Payment, and Deductibles](../property/claim-conditions-and-deductibles.md) for the broader deductible and condition rules, and [Ordinance or Law Coverage and Undamaged Roof Portions](../property/ordinance-or-law.md) for the code-cost path. [Roof Loss Claims Handling](../../operations/claims-roof-loss-handling.md) is the internal operating procedure; it does not replace this issued-form analysis.

## Settlement control flow

HO-3 A.3 supplies the ordinary Coverage A settlement baseline: **“Losses to the dwelling are settled at replacement cost, subject to the roof surfacing provisions in A.4 and to the applicable deductible, provided the dwelling is insured to at least eighty percent of its replacement cost at the time of loss.”** Replacement cost is like-kind-and-quality repair or replacement without depreciation at the time of loss. Actual cash value (ACV) is the corresponding cost less depreciation based on age, condition, and remaining useful life immediately before loss. [HO-3 2018-09, Definitions 1–2](repo://forms/HO/MS/HO-3/2018-09.md#L9-L14) · [HO-3 2018-09, A.3](repo://forms/HO/MS/HO-3/2018-09.md#L25-L33)

A.4 is a limited routing rule, not a general roof exclusion: **“Loss to roof surfacing caused by windstorm or hail is settled at replacement cost unless an actual cash value roof schedule endorsement is attached to this policy, in which case that endorsement governs settlement for the roof surfacing only. All other components of the dwelling continue to be settled under A.3.”** Thus an attached HO 23 74 changes the settlement basis only after three facts align: the loss is covered, the damaged item is roof surfacing, and windstorm or hail caused that surfacing loss. [HO-3 2018-09, A.3–A.4](repo://forms/HO/MS/HO-3/2018-09.md#L31-L34) · [HO 23 74 2018-09, R.1–R.2](repo://forms/HO/MS/HO-23-74/2018-09.md#L5-L15)

```mermaid
flowchart TD
    Start["Identify issued HO-3 2018-09 policy and attachments"] --> Coverage["Establish covered direct physical loss"]
    Coverage --> Scope{"Damaged item is roof surfacing"}
    Scope -- No --> Base["Settle dwelling component under A.3"]
    Scope -- Yes --> Peril{"Windstorm or hail caused the loss"}
    Peril -- No --> Base
    Peril -- Yes --> ScheduleAttached{"HO 23 74 is attached"}
    ScheduleAttached -- No --> Base
    ScheduleAttached -- Yes --> Separate["Separate surfacing estimate and determine material and age"]
    Separate --> Rate["Apply R.3 percentage and R.4 minimum before deductible"]
    Rate --> Deductible["Apply deductible selected under issued policy"]
    Base --> Deductible
    Deductible --> Code{"Undamaged work required by ordinance or law"}
    Code -- No --> Outcome["Document settlement result"]
    Code -- Yes --> OrdinanceAttached{"HO 04 16 is attached"}
    OrdinanceAttached -- No --> Outcome
    OrdinanceAttached -- Yes --> Ordinance["Settle eligible incurred increased cost after damaged-property settlement"]
    Ordinance --> Outcome
```

*The flow routes covered components to the baseline or attached roof schedule, then keeps ordinance-driven undamaged work on its separate path.*

This decision flow is grounded in HO-3 A.3–A.4 and Exclusion D.1, HO 23 74 R.1–R.6, and HO 04 16 O.1–O.6. [HO-3 2018-09, A.3–A.4 and D.1](repo://forms/HO/MS/HO-3/2018-09.md#L25-L34) [D.1](repo://forms/HO/MS/HO-3/2018-09.md#L91-L94) · [HO 23 74 2018-09, R.1–R.6](repo://forms/HO/MS/HO-23-74/2018-09.md#L5-L40) · [HO 04 16 2018-09, O.1–O.6](repo://forms/HO/MS/HO-04-16/2018-09.md#L5-L37)

### Routing outcomes

| Claim fact pattern after coverage is established | Settlement path |
| --- | --- |
| A dwelling component that is not roof surfacing | HO-3 A.3 replacement cost, subject to the 80-percent condition and applicable deductible. |
| Roof surfacing damaged by a covered peril other than windstorm or hail | HO-3 A.3 replacement cost. HO 23 74 expressly does not apply to this loss. |
| Windstorm or hail damage to roof surfacing, with no attached HO 23 74 | HO-3 A.4 replacement cost under the A.3 baseline. |
| Windstorm or hail damage to roof surfacing, with attached HO 23 74 | HO 23 74 ACV schedule, its minimum-payment rule, then the applicable deductible. |

This table describes **settlement after coverage**, not a coverage grant. For any qualifying non-wind/hail peril, the HO-3 A.3 baseline remains controlling: HO 23 74 R.2 says the surfacing loss is replacement cost and “this endorsement does not apply to that loss.” [HO-3 2018-09, A.3–A.4](repo://forms/HO/MS/HO-3/2018-09.md#L31-L34) · [HO 23 74 2018-09, R.2](repo://forms/HO/MS/HO-23-74/2018-09.md#L11-L16)

## What counts as roof surfacing

Do not price the entire roof as one scheduled item. Under attached HO 23 74 R.1, roof surfacing means **“shingles, tiles, shakes, metal panels, membrane, and the underlayment and flashing directly beneath them.”** It does **not** include the roof deck, trusses, rafters, sheathing, or interior finish. The endorsement preserves the HO-3 A.3 replacement-cost settlement for every dwelling component other than roof surfacing. [HO-3 2018-09, A.3–A.4](repo://forms/HO/MS/HO-3/2018-09.md#L31-L34) · [HO 23 74 2018-09, R.1](repo://forms/HO/MS/HO-23-74/2018-09.md#L5-L10)

A defensible estimate consequently has at least two buckets when both are damaged:

1. **Scheduled surfacing:** the R.1 materials, valued under R.2–R.4 only if the windstorm/hail and attachment gates are met.
2. **Other dwelling components:** deck, framing, sheathing, and interior finish, valued under HO-3 A.3 rather than depreciated under the roof schedule.

This separation is a settlement-scope requirement; it does not transform an excluded condition into covered damage. It also allows different settlement bases in one physical roof loss without treating the attached endorsement as applicable to structural or interior work. [HO-3 2018-09, P.1 and A.3–A.4](repo://forms/HO/MS/HO-3/2018-09.md#L31-L34) [P.1](repo://forms/HO/MS/HO-3/2018-09.md#L59-L63) · [HO 23 74 2018-09, R.1–R.2](repo://forms/HO/MS/HO-23-74/2018-09.md#L5-L15)

## HO 23 74 calculation: material, age, floor, then deductible

For an attached **HO 23 74 edition 2018-09**, the A.4 exception routes windstorm- or hail-caused surfacing loss to R.2: **“Loss to roof surfacing caused by windstorm or hail is settled at actual cash value, determined by applying the depreciation schedule in R.3 to the replacement cost of the roof surfacing at the time of loss, less the applicable deductible.”** The schedule percentage is therefore applied to the replacement cost of the eligible surfacing, not to non-surfacing work. [HO-3 2018-09, A.3–A.4](repo://forms/HO/MS/HO-3/2018-09.md#L31-L34) · [HO 23 74 2018-09, R.1–R.2](repo://forms/HO/MS/HO-23-74/2018-09.md#L5-L15)

### R.3 schedule

| Roof-surfacing material | Age at date of loss | Payable percentage of surfacing replacement cost |
| --- | --- | --- |
| Composition shingle | Under 5 years / 5–9 / 10–14 / 15–19 / 20 or more | 100% / 80% / 60% / 40% / 25% |
| Architectural shingle, metal, or tile | Under 10 years / 10–19 / 20–29 / 30 or more | 100% / 80% / 60% / 40% |
| Wood shake | Under 5 years / 5–9 / 10 or more | 100% / 70% / 40% |

The age input is not merely the apparent age or a rating-system value. R.5 uses the documented date of original installation or most recent **full** replacement, whichever is later. Without that documentation, age is presumed to be the dwelling's age. A partial repair does not reset roof age; a full replacement of one slope resets age for that slope only. A multi-slope loss can therefore require separately documented ages and separately priced surfacing. [HO 23 74 2018-09, R.3 and R.5](repo://forms/HO/MS/HO-23-74/2018-09.md#L17-L35)

R.4 sets a pre-deductible payment floor: **“In no event will the payable amount for roof surfacing be less than twenty-five percent of the replacement cost of that surfacing, before application of the deductible.”** Operationally, first calculate the R.3 schedule amount; if it is lower than 25% of eligible surfacing replacement cost, raise it to that floor; only then apply the deductible that governs the loss. The floor does not eliminate or cap the deductible. [HO-3 2018-09, A.3–A.4 and S.5](repo://forms/HO/MS/HO-3/2018-09.md#L31-L34) [S.5](repo://forms/HO/MS/HO-3/2018-09.md#L101-L112) · [HO 23 74 2018-09, R.2–R.4](repo://forms/HO/MS/HO-23-74/2018-09.md#L11-L30)

For an eligible surfacing estimate with replacement cost `RC`, schedule rate `r`, and applicable deductible `D`, the ordering can be represented as:

`scheduled pre-deductible amount = max(RC × r, RC × 25%)`

`settlement after deductible = scheduled pre-deductible amount − D`

This is an ordering aid, not a substitute for the Declarations, policy limits, coverage decision, or any governing state amendatory form.

## Deductible selection is a policy-and-state step

The HO-3 2018-09 default says that the Declarations deductible applies to each Section I loss. It then recognizes a separate windstorm-or-hail deductible where a state amendatory endorsement requires one and directs that, where both apply, “**only the larger is deducted.**” Apply this deductible after the HO 23 74 R.4 floor when the schedule applies. [HO-3 2018-09, S.5](repo://forms/HO/MS/HO-3/2018-09.md#L101-L112) · [HO 23 74 2018-09, R.2 and R.4](repo://forms/HO/MS/HO-23-74/2018-09.md#L11-L30)

A state endorsement can replace that default for the conflict it names. For a Texas HO-3 2018-09 policy, **only if HO 01 45 edition 2022-01 is attached and applicable**, T.1 expressly amends S.5 and implements Texas Department of Insurance Bulletin B-2021-08. Its contractual selection rule is more specific than S.5: windstorm- or hail-caused loss receives only the separately stated windstorm-and-hail deductible, not the all-other-perils deductible. T.1 states that deductible as a Coverage A percentage—normally 1%–5%, with its stated seacoast maximum—and supplies the mixed-peril allocation rule. The bulletin independently regulates the same deductible's permissible configuration, application, disclosure, and filing; it does not supply an unissued contract term. [HO-3 2018-09, S.5](repo://forms/HO/MS/HO-3/2018-09.md#L101-L112) · [HO 01 45 2022-01, introductory provision and T.1](repo://forms/HO/TX/HO-01-45/2022-01.md#L1-L11) · [Texas Bulletin B-2021-08, B.1–B.4 and B.7](repo://bulletins/TX/2021-08-windstorm-deductible.md#L5-L25) [B.7](repo://bulletins/TX/2021-08-windstorm-deductible.md#L35-L37)

The practical entrypoint is the issued Declarations plus all attached state forms, not the roof schedule alone. Confirm the loss peril, state, policy effective date, and endorsement attachment before choosing `D`.

## Code-required undamaged work: a distinct endorsement path

The base form excludes the increased cost of construction, demolition, or repair required by an ordinance or law unless an ordinance-or-law endorsement is attached. **HO 23 74 R.6 preserves that HO-3 D.1 exclusion as a separate boundary:** code-required replacement of undamaged roof surfacing is subject to D.1 and is not a roof-schedule benefit. Do not use R.6 as an ordinance-or-law write-back, and do not use the schedule to set the limit for this work. [HO-3 2018-09, D.1](repo://forms/HO/MS/HO-3/2018-09.md#L91-L94) · [HO 23 74 2018-09, R.6](repo://forms/HO/MS/HO-23-74/2018-09.md#L37-L41)

**Separately, when HO 04 16 edition 2018-09 is attached**, O.1 writes back HO-3 D.1 for eligible increased cost: it covers incurred increased cost to repair, rebuild, or demolish damaged dwelling property because of an in-force ordinance or law, provided the underlying loss is covered. O.3 specifically covers code-required replacement of undamaged roof surfacing needed to repair the damaged portion. This is the independent potential payment path for the R.6 work, not a revision of the roof schedule. That benefit is subject to all of these separately controlling constraints:

- O.2 limits payment to 10% of the Coverage A limit unless a higher percentage is shown; the amount is additional insurance and does not reduce Coverage A or B.
- O.5 requires completion as soon as reasonably possible and no later than two years after loss unless the insurer agrees in writing to extend the period.
- O.6 applies the endorsement only **after** the damaged-property loss is settled under the applicable Section I settlement provisions and only to increased cost actually incurred.
- O.4 preserves specified exclusions, including pre-loss compliance obligations.

[HO-3 2018-09, D.1](repo://forms/HO/MS/HO-3/2018-09.md#L91-L94) · [HO 04 16 2018-09, O.1–O.4](repo://forms/HO/MS/HO-04-16/2018-09.md#L5-L27) · [HO 04 16 2018-09, O.5–O.6](repo://forms/HO/MS/HO-04-16/2018-09.md#L29-L37)

Accordingly, state the relationship precisely: **R.6 leaves code-required undamaged surfacing in the HO-3 D.1 exclusion; an independently attached HO 04 16 may then cover the additional incurred cost under O.1/O.3, within O.2 and after damaged-property settlement.** This conclusion requires the separate endorsement and its conditions; R.6 is not itself the write-back. [HO-3 2018-09, D.1](repo://forms/HO/MS/HO-3/2018-09.md#L91-L94) · [HO 23 74 2018-09, R.6](repo://forms/HO/MS/HO-23-74/2018-09.md#L37-L41) · [HO 04 16 2018-09, O.1–O.3 and O.6](repo://forms/HO/MS/HO-04-16/2018-09.md#L5-L19) [O.6](repo://forms/HO/MS/HO-04-16/2018-09.md#L33-L37)

## Florida bulletin: regulatory and underwriting constraints, not settlement wording

Florida OIR Bulletin OIR-2023-04 applies to Florida personal residential property policies issued or renewed with effective dates on or after 2023-07-01. F.4 regulates the offer and permitted application of a separate roof deductible or ACV roof schedule; F.6 limits deductible overlap on a loss. Neither provision changes the A.4/R.1–R.4 settlement terms of an issued policy or itself attaches HO 23 74 or HO 04 16. Treat this as a state control alongside—not a substitute for—the issued forms and Declarations. [OIR-2023-04, applicability, F.4, and F.6](repo://bulletins/FL/2023-04-roof-age-nonrenewal.md#L1-L3) [F.4](repo://bulletins/FL/2023-04-roof-age-nonrenewal.md#L21-L25) [F.6](repo://bulletins/FL/2023-04-roof-age-nonrenewal.md#L31-L33) · [HO-3 2018-09, A.4](repo://forms/HO/MS/HO-3/2018-09.md#L31-L34) · [HO 23 74 2018-09, R.1–R.4](repo://forms/HO/MS/HO-23-74/2018-09.md#L5-L30)

For policy issuance and renewal, the bulletin provides these controls:

- An insurer may not refuse to issue or renew solely because of roof age when a qualifying inspection within the preceding 12 months establishes at least five years of remaining useful life. A roof-condition decline must state the specific deficiency rather than roof age alone.
- At age 15 or older, the insurer may require an inspection at its expense. It must accept a qualifying inspection by a state-licensed inspector and cannot require a second inspection at the insured's expense in the same policy period.
- The insurer may offer a separate roof deductible or ACV roof schedule only if it also offers a policy without that provision at a filed and approved rate and discloses the premium difference in writing at offer. It **“may not apply an actual cash value roof settlement schedule to a roof less than ten years of age at the effective date of the policy.”**
- A roof-condition nonrenewal requires at least 120 days' written notice, a specific reason, and the relied-on inspection report.

[OIR-2023-04, F.2–F.5](repo://bulletins/FL/2023-04-roof-age-nonrenewal.md#L9-L29)

For a Florida loss where a hurricane deductible and separate roof deductible would both apply, F.6 forbids stacking them: only the larger is deducted. This state rule must be kept separate from HO-3 S.5's general state-endorsement routing and from the HO 23 74 ACV calculation. The bulletin also requires annual county-level reporting of roof-condition nonrenewals; that is an insurer compliance obligation, not a claim-payment component. [OIR-2023-04, F.6–F.7](repo://bulletins/FL/2023-04-roof-age-nonrenewal.md#L31-L37)

## Contract decision versus claim operations

Internal roof-claim guidance is not policy language and is not to be quoted to an insured or claimant. Its role is to make the contract decision reproducible: establish and document peril before pricing, obtain installation/full-replacement evidence, inspect to confirm material, split surfacing from decking and interior work, and retain the calculation inputs. It also directs referral for a disputed age with more than a $10,000 payment effect, a public adjuster or counsel, more than one slope age, or a claimed code upgrade without an ordinance endorsement. These are operating controls, not independent coverage grants, denials, or replacements for the issued forms. [Roof Claim Handling Guidance, status and K.1–K.4](repo://guidelines/claims/roof-claim-handling.md#L1-L33) · [Roof Claim Handling Guidance, K.5–K.7](repo://guidelines/claims/roof-claim-handling.md#L35-L49)

A focused file review should be able to answer, in order:

1. Which base-form edition, Declarations deductible, state form, HO 23 74, and HO 04 16 were in force on the date of loss?
2. What direct physical loss and peril were established, and do any exclusions apply?
3. Which estimate lines are R.1 surfacing and which remain A.3 dwelling components?
4. For scheduled surfacing, what inspection supports material, and what document supports the original-installation or full-replacement date for each slope?
5. Is the R.3 percentage correct, is the R.4 25% pre-deductible floor preserved, and is the deductible selected from the issued policy rather than assumed?
6. If undamaged work is claimed, what in-force ordinance requires it, is HO 04 16 attached, and have O.2, O.5, and O.6 been satisfied?

The insured's general Section I duties remain relevant regardless of settlement path: prompt notice, protection against further damage, and a signed sworn proof of loss within 60 days after request. The base form makes loss payable 60 days after receipt of proof of loss plus written agreement, appraisal award, or court judgment. [HO-3 2018-09, S.1–S.3](repo://forms/HO/MS/HO-3/2018-09.md#L101-L108)
