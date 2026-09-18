---
type: coverage
title: Windstorm, Hail, and Percentage Deductibles
description: How homeowners and dwelling policies determine whether a covered wind or hail loss is subject to a percentage deductible, including wind-driven rain openings, calculation basis, occurrence rules, other deductibles, and state-specific storm overlays.
tags: [windstorm, hail, deductibles, percentage-deductible, wind-driven-rain, state-overlays]
verified:
  - by: openwiki/0.5.2
    at: 2026-09-18T12:15:46.420Z
sources:
  - id: openwiki-source-18e62e3e0cc23c448e9a7a88
    resource: repo://bulletins/CO/doi-2013-01-hail-deductibles.md
  - id: openwiki-source-ea49da73d188dae27727c39a
    resource: repo://bulletins/CO/doi-2019-05-hail-deductibles.md
  - id: openwiki-source-cf3bdf4919dc01656b85cad5
    resource: repo://bulletins/FL/oir-2022-01-hurricane-deductible.md
  - id: openwiki-source-c682388a7af0924de5ae99dd
    resource: repo://bulletins/LA/ldi-2012-05-hurricane-deductible.md
  - id: openwiki-source-53b0fcac982bbc589328cd99
    resource: repo://bulletins/LA/ldi-2020-07-hurricane-deductible.md
  - id: openwiki-source-38049e374f54d1eb9a15f4ef
    resource: repo://bulletins/TX/b-2021-08-windstorm-deductibles.md
  - id: openwiki-source-3c9f3e7c3b76f6a61601b18d
    resource: repo://forms/DP/FL/DP-01-09/2021-03.md
  - id: openwiki-source-94a64462d39a6acab87c2fe5
    resource: repo://forms/DP/TX/DP-01-45/2022-01.md
  - id: openwiki-source-822f35c9e6943f4967e8b585
    resource: repo://forms/HO/CO/HO-01-05/2022-10.md
  - id: openwiki-source-a8c95d71a2a2351aaf8e360c
    resource: repo://forms/HO/FL/HO-01-09/2023-07.md
  - id: openwiki-source-1fa05a0fd929d1f05f011dff
    resource: repo://forms/HO/LA/HO-01-17/2020-09.md
  - id: openwiki-source-884e0e1bd1dfb4241d618135
    resource: repo://forms/HO/MS/HO-23-77/2014-02.md
  - id: openwiki-source-a831e6cf8f75394917fb0dc8
    resource: repo://forms/HO/MS/HO-23-77/2022-07.md
  - id: openwiki-source-7176aead92778c93cb0441d2
    resource: repo://forms/HO/MS/HO-3/2024-03.md
  - id: openwiki-source-ff7de1315ac46ce4dd65d251
    resource: repo://forms/HO/TX/HO-01-45/2022-01.md
  - id: openwiki-source-a4c7b640218374da69fe20e4
    resource: repo://training/state-deductibles-explained.md
generated: { by: "openwiki/0.5.2", at: "2026-09-18T12:15:46.420Z" }
---

# Windstorm, Hail, and Percentage Deductibles

A windstorm, hail, or percentage deductible is a **contractual allocation of a covered loss**, not a coverage grant. The applicable policy form, attached endorsement, edition, declarations, state amendatory form, and any controlling state requirement must be identified before the claim is adjusted. A superseded edition continues to govern policies written under it; do not blend its percentage, limit basis, occurrence rule, or notice period with a later edition. For example, HO 23 77 (2014-02) is superseded by HO 23 77 (2022-07) for policies effective on or after July 1, 2022, while the earlier edition remains applicable to policies written under it ([2014-02, W.0](repo://forms/HO/MS/HO-23-77/2014-02.md#L1-L9)).

## Coverage gate: what must be covered first

The deductible applies only after the policy establishes **direct physical loss to covered property** caused by windstorm or hail. The 2024-03 HO-3 form covers direct physical loss caused by windstorm and hail, subject to its exclusions and conditions ([HO-3 2024-03, P.37](repo://forms/HO/MS/HO-3/2024-03.md#L625-L633)). The same form preserves important boundaries:

- Rain, snow, sleet, sand, or dust entering a building is covered only when the direct force of wind or hail first damages the building and creates an opening; the deductible does not make otherwise uncovered water damage payable ([HO-3 2024-03, P.38](repo://forms/HO/MS/HO-3/2024-03.md#L631-L634)).
- Roof surfacing cosmetic damage that does not impair the ability to shed water is excluded, while covered direct physical loss that impairs that ability is treated differently ([HO-3 2024-03, P.40-P.41](repo://forms/HO/MS/HO-3/2024-03.md#L635-L639)).
- An endorsement may modify the base policy's deductible or conditions, but it does not automatically restore an exclusion. The 2022-07 HO 23 77 expressly says that it does not provide coverage for property, loss, or damage that the policy does not otherwise cover ([HO 23 77 2022-07, W.0](repo://forms/HO/MS/HO-23-77/2022-07.md#L25-L43)).

Thus, “wind-driven rain claim” is not enough by itself. Establish the opening, the direct physical damage that created it, the resulting covered damage, and the applicable form language. If the loss is excluded, the deductible is not a substitute for coverage.

## Claim decision flow

The practical order is to identify the governing contract, establish coverage and causation, determine the applicable event and limit, then calculate and subtract the deductible. The forms require investigation from the facts and available evidence rather than application based only on a storm label or nearby weather ([HO 01 05 2022-10, T.16 and T.28](repo://forms/HO/CO/HO-01-05/2022-10.md#L89-L91), [L.115](repo://forms/HO/CO/HO-01-05/2022-10.md#L113-L115)).

```mermaid
flowchart TD
    A["Identify policy edition and attached deductible terms"] --> B["Confirm direct physical loss to covered property"]
    B --> C{"Windstorm or hail caused covered loss"}
    C --> D["No: apply other coverage and deductible terms"]
    C --> E["Yes: identify cause sequence and loss event"]
    E --> F["Select applicable limit and percentage basis"]
    F --> G["Apply valuation and coverage terms"]
    G --> H["Subtract percentage deductible before payment"]
    H --> I["Apply remaining limits and payment conditions"]
```

*This flow shows the coverage, causation, calculation, and payment sequence reflected in the cited forms.*

## Calculation and limit basis

A percentage deductible is not normally a percentage of the repair estimate. The controlling form determines the percentage, the applicable limit or insured value, the covered-loss amount to which the deduction is applied, and whether separate limits must be calculated separately.

The common calculation is:

> **Deductible = selected percentage × applicable limit**  
> **Payment before other remaining limits or conditions = covered adjusted loss − deductible, but not less than zero**

The 2014-02 HO 23 77 defines the applicable coverage limit as the limit for the property damaged, calculates the deductible from that limit without reducing it for the loss, and subtracts the deductible from the adjusted loss after applicable terms are applied ([HO 23 77 2014-02, W.3](repo://forms/HO/MS/HO-23-77/2014-02.md#L263-L287), [W.15-W.17](repo://forms/HO/MS/HO-23-77/2014-02.md#L291-L297)). The 2022-07 edition similarly uses the limit immediately before the loss, applies valuation and loss-settlement provisions before determining the net amount, and does not combine separate applicable limits solely to reduce the deductible ([HO 23 77 2022-07, W.2-W.18](repo://forms/HO/MS/HO-23-77/2022-07.md#L301-L325), [W.2-W.18](repo://forms/HO/MS/HO-23-77/2022-07.md#L215-L231)).

**Illustration.** If the controlling terms use a $400,000 applicable limit and a selected 2 percent deductible, the deductible is $8,000. A $30,000 covered adjusted loss leaves $22,000 before any other applicable limit, sublimit, or payment condition. A $6,000 covered loss produces no payment under a form that does not pay when the adjusted loss does not exceed the deductible. This is an arithmetic illustration, not a universal policy result: the actual form controls the limit basis, allocation, and payment order.

When more than one applicable limit is involved, allocate the loss to the property or coverage to which each limit applies. The 2022-07 HO 23 77 requires separate deductible determinations when separate applicable limits apply and forbids combining limits merely to reduce the deduction ([HO 23 77 2022-07, W.10-W.12](repo://forms/HO/MS/HO-23-77/2022-07.md#L175-L181)). A later reduction in the limit after the loss does not retroactively reduce the deductible for that loss event ([same edition, W.10](repo://forms/HO/MS/HO-23-77/2022-07.md#L175-L177)).

## Trigger, causation, and loss-event rules

The deductible trigger is a causal requirement, not merely the presence of wind, hail, rain, or a named storm nearby.

- Windstorm or hail may be the sole cause or may combine with another cause. The deductible applies to the covered portion for which windstorm or hail caused direct physical loss; it does not apply to a portion attributable only to an unrelated or excluded cause ([HO 01 17 Louisiana 2020-09, T.8-T.17](repo://forms/HO/LA/HO-01-17/2020-09.md#L75-L97)).
- Wind-driven rain follows the opening rule. The Louisiana amendatory form applies its deductible to covered rain damage only when windstorm or hail created the opening, and the Texas DP form likewise requires an opening created by windstorm for covered wind-driven rain ([HO 01 17 Louisiana 2020-09, T.4-T.16](repo://forms/HO/LA/HO-01-17/2020-09.md#L61-L91), [DP 01 45 Texas 2022-01, T.20](repo://forms/DP/TX/DP-01-45/2022-01.md#L95-L105)).
- Related damage is generally grouped under the form's occurrence or loss-event rule. HO 23 77 (2022-07) treats related windstorm or hail conditions arising from the same weather event as one occurrence and does not create a second deductible merely because damage is discovered later ([HO 23 77 2022-07, W.10-W.12](repo://forms/HO/MS/HO-23-77/2022-07.md#L315-L325)). Louisiana's 2020-09 form treats related damage from the same event as one occurrence but permits separate weather events to be separate occurrences ([HO 01 17 Louisiana 2020-09, T.18-T.20](repo://forms/HO/LA/HO-01-17/2020-09.md#L95-L99)).
- Texas HO 01 45 (2022-01) applies the deductible to an occurrence involving windstorm or hail and recognizes that wind and hail damage may arise from the same occurrence ([HO 01 45 Texas 2022-01, T.16-T.17](repo://forms/HO/TX/HO-01-45/2022-01.md#L91-L95)).

The claim file should therefore record the alleged event, the physical evidence, the sequence of causes, any covered and noncovered allocation, and the policy provision that makes the event one occurrence or loss event.

## Other deductibles and covered related expenses

The wind or hail deductible does not automatically replace every other deductible, and it must not be duplicated merely because several items or coverages are involved. The controlling form decides whether another deductible applies to a separate cause, remains applicable by its own terms, or is excluded for the same loss.

- The 2022-07 HO 23 77 says not to apply another deductible to the same covered windstorm or hail loss unless its terms require it, while preserving another deductible when its own terms apply ([HO 23 77 2022-07, W.38-W.39](repo://forms/HO/MS/HO-23-77/2022-07.md#L129-L133)).
- Texas HO 01 45 (2022-01) makes the windstorm or hail deductible separate from a deductible for another peril and says the applicable amount is determined from the coverage and cause of loss ([HO 01 45 Texas 2022-01, T.1-T.9](repo://forms/HO/TX/HO-01-45/2022-01.md#L61-L81)). Texas B-2021-08 also prohibits more than one deductible for the same covered loss unless the policy clearly permits it ([Texas Bulletin B-2021-08, B.2.19-B.2.20](repo://bulletins/TX/b-2021-08-windstorm-deductibles.md#L83-L87)).
- Covered emergency measures, temporary or reasonable protective repairs, debris removal, loss of use, and other related expenses remain subject to the deductible when the applicable policy covers them. They do not become covered merely because a deductible applies. HO 23 77 (2022-07) addresses emergency measures and temporary repairs directly ([HO 23 77 2022-07, W.49-W.54](repo://forms/HO/MS/HO-23-77/2022-07.md#L153-L163)); the Louisiana form separately includes covered debris removal, reasonable protective repairs, and covered loss of use ([HO 01 17 Louisiana 2020-09, T.48-T.52](repo://forms/HO/LA/HO-01-17/2020-09.md#L155-L163)).

Apply valuation and coverage conditions before calculating the covered amount, then apply the deductible in the order specified by the controlling form. Do not use emergency work, a supplemental estimate, debris removal, or a separate coverage limit as a device to avoid a deductible that the form applies to the same occurrence.

## Edition-specific contractual ranges and notice rules

These are contractual terms from the identified editions, not a universal industry range.

| Form and edition | Contractual percentage or limit rule | Trigger, basis, and notice rule |
|---|---|---|
| HO 23 77, 2014-02 | Selected percentage is **1% to 5%**. Deductible uses the applicable coverage limit for damaged property. | Applies to each windstorm or hail loss and is separate from another-peril deductible; the older edition remains live for policies written under it ([W.3-W.15](repo://forms/HO/MS/HO-23-77/2014-02.md#L269-L295)). |
| HO 23 77, 2022-07 | Selected percentage is **2% to 10%**. Applicable limit is the limit for damaged property immediately before loss. | Same occurrence or related weather event controls; separate limits are not combined solely to reduce the deduction ([W.3-W.12](repo://forms/HO/MS/HO-23-77/2022-07.md#L305-L323)). |
| Florida DP 01 09, 2021-03 | Windstorm and hail deductible is **2% to 10%** and uses the amount of insurance applicable to damaged property. | Applied to the total covered loss from the same occurrence, not separately to each item. The form requires at least **45 days' notice** before an increase ([DP 01 09 Florida 2021-03, T.1-T.10](repo://forms/DP/FL/DP-01-09/2021-03.md#L61-L85), [T.2 notice](repo://forms/DP/FL/DP-01-09/2021-03.md#L167-L175)). |
| Florida HO 01 09, 2023-07 | Windstorm and hail deductible is **2% to 15%**. | Applies to covered loss and is separate from another deductible; wind-driven rain requires an opening caused by wind. This edition requires **60 days' written notice** before an increase ([HO 01 09 Florida 2023-07, T.1-T.10](repo://forms/HO/FL/HO-01-09/2023-07.md#L57-L77), [T.2 notice](repo://forms/HO/FL/HO-01-09/2023-07.md#L167-L175)). |
| Texas HO 01 45, 2022-01 | Windstorm and hail deductible is **1% to 10%**. | Applies to covered direct physical loss, including resulting covered damage, and uses the applicable limit of liability for the damaged property; the form requires **45 days' notice** before an increase ([HO 01 45 Texas 2022-01, T.1-T.21](repo://forms/HO/TX/HO-01-45/2022-01.md#L61-L103), [T.2 notice](repo://forms/HO/TX/HO-01-45/2022-01.md#L169-L183)). |
| Texas DP 01 45, 2022-01 | Windstorm and hail deductible shown in the Declarations is **1% to 5%**. | Uses the applicable amount of insurance and applies to the total covered loss from the same occurrence; the form requires **30 days' notice** before an increase ([DP 01 45 Texas 2022-01, T.1-T.10](repo://forms/DP/TX/DP-01-45/2022-01.md#L59-L81), [T.2 notice](repo://forms/DP/TX/DP-01-45/2022-01.md#L215-L229)). |
| Colorado HO 01 05, 2022-10 | Windstorm and hail deductible is **1% to 5%**. | HO 01 05 **implements** Colorado Bulletin DOI-2019-05 for the deductible range and applies the deduction to covered loss, including a loss with another cause; its notice provision requires **30 days** before an increase ([HO 01 05 Colorado 2022-10, T.1-T.8](repo://forms/HO/CO/HO-01-05/2022-10.md#L59-L75), [T.2 notice](repo://forms/HO/CO/HO-01-05/2022-10.md#L211-L225)). |
| Louisiana HO 01 17, 2020-09 | Windstorm and hail deductible is **2% to 5%**. | Applies to covered direct physical loss, including covered wind-driven rain through a storm-created opening; related damage is one occurrence. The form requires **30 days' notice** before an increase and defines a named-storm period continuing **72 hours** after designation ends ([HO 01 17 Louisiana 2020-09, T.1-T.20](repo://forms/HO/LA/HO-01-17/2020-09.md#L59-L99), [notice and named storm](repo://forms/HO/LA/HO-01-17/2020-09.md#L211-L273)). |

The Texas HO row and Texas DP row must not be collapsed: they are different contract editions and have different maximums and notice periods. Likewise, the Florida HO and DP forms differ even though both are Florida contracts.

## State overlays: contractual terms versus regulatory constraints

A state bulletin is not the policy's deductible calculation unless the contract or amendatory form makes it so. Treat the sources in two layers:

1. **Contract layer:** read the declarations and attached form or endorsement to determine the deductible, limit basis, trigger, occurrence, and payment order.
2. **Regulatory layer:** check the bulletin for disclosure, filing, recordkeeping, consistency, claims-investigation, and advance-notice constraints. A bulletin may constrain how a deductible is offered or administered without changing the coverage grant.

### Colorado

Colorado Bulletin DOI-2013-01 is superseded by DOI-2019-05 for policies effective on or after May 20, 2019; the earlier bulletin remains relevant to policies written under it ([supersession notice](repo://bulletins/CO/doi-2013-01-hail-deductibles.md#L1-L9)). Under that earlier overlay, a windstorm or hail deductible could not exceed **3% of the applicable property coverage limit**, and the insurer had to disclose the trigger, basis, and relationship to another deductible ([DOI-2013-01, B.2.1-B.2.10](repo://bulletins/CO/doi-2013-01-hail-deductibles.md#L59-L79)).

DOI-2019-05 now constrains the windstorm and hail deductible to no more than **5% of applicable covered loss**, requires the value stated in the policy for the percentage calculation, and requires a **30-day written notice** before an increase in a windstorm deductible ([DOI-2019-05, B.2.1-B.2.9](repo://bulletins/CO/doi-2019-05-hail-deductibles.md#L59-L79), [B.3.1-B.3.3](repo://bulletins/CO/doi-2019-05-hail-deductibles.md#L151-L159)). HO 01 05 (2022-10) implements that bulletin in the contract by setting a 1% to 5% range ([HO 01 05, T.1-T.3](repo://forms/HO/CO/HO-01-05/2022-10.md#L59-L67)).

### Florida

Florida OIR-2022-01 is primarily a disclosure overlay. It requires the disclosure to identify the trigger, separate the hurricane deductible from other deductibles, describe the calculation basis, and state a named-storm minimum of **2%** and hurricane maximum of **10%** ([OIR-2022-01, B.2.1-B.2.10](repo://bulletins/FL/oir-2022-01-hurricane-deductible.md#L59-L81)). The bulletin expressly says that it does **not** establish a minimum Section I deductible or other unrelated policy term ([OIR-2022-01, B.1.12-B.1.14](repo://bulletins/FL/oir-2022-01-hurricane-deductible.md#L35-L41)). Do not therefore replace the Florida HO 01 09 2023-07 contract's 2% to 15% windstorm-and-hail range with the bulletin's 10% statement without first determining whether the policy's deductible is the hurricane or named-storm deductible addressed by the bulletin.

The form remains the contract. Florida HO 01 09 2023-07 requires 60 days' written notice before an increase, while DP 01 09 2021-03 requires 45 days ([HO notice](repo://forms/HO/FL/HO-01-09/2023-07.md#L167-L175), [DP notice](repo://forms/DP/FL/DP-01-09/2021-03.md#L167-L175)). OIR-2022-01 additionally requires records supporting delivery of the disclosure and the disclosure version used ([OIR-2022-01, B.2.12-B.2.21](repo://bulletins/FL/oir-2022-01-hurricane-deductible.md#L81-L101)).

### Texas

Texas Bulletin B-2016-04 is the historical overlay for policies subject to that edition. It required a minimum **1%** windstorm or hail deductible and capped a hurricane deductible at **3%** of applicable insured value ([B-2016-04, B.2.1-B.2.10](repo://bulletins/TX/b-2016-04-windstorm-deductibles.md#L59-L79)). B-2021-08 supplies the later overlay: named-storm windstorm and hail deductibles must be at least **1%**, hurricane deductibles cannot exceed **5%**, and a seacoast-territory windstorm deductible cannot exceed **10%** ([B-2021-08, B.2.1-B.2.6](repo://bulletins/TX/b-2021-08-windstorm-deductibles.md#L47-L59)).

B-2021-08 also requires the insurer to disclose the separate deductible, the trigger, the relationship to another deductible, and the policy value or limit used for calculation. It prohibits more than one deductible for the same covered loss unless the policy clearly permits it and requires claim documentation supporting the application ([B-2021-08, B.2.7-B.2.21](repo://bulletins/TX/b-2021-08-windstorm-deductibles.md#L61-L89)). Its disclosure section requires **30 days' notice** before increasing a windstorm deductible and a **72-hour continuation** after a named-storm designation ends when the policy uses a named-storm period ([B.3.12-B.3.23](repo://bulletins/TX/b-2021-08-windstorm-deductibles.md#L157-L181)). The Texas HO and DP forms provide their own contract notice rules, so use the form edition in force for the policy rather than substituting the bulletin period.

### Louisiana

Louisiana Bulletin LDI-2012-05 is superseded by LDI-2020-07 for policies effective on or after July 15, 2020; the earlier bulletin remains relevant to policies written under it ([supersession notice](repo://bulletins/LA/ldi-2012-05-hurricane-deductible.md#L1-L9)). The 2012 overlay required the hurricane deductible to be disclosed separately and capped a windstorm and hail deductible at **5% of insured value** ([LDI-2012-05, B.2.1-B.2.12](repo://bulletins/LA/ldi-2012-05-hurricane-deductible.md#L47-L71)).

LDI-2020-07 keeps the disclosure and administration focus, caps the hurricane deductible at **5% of applicable covered loss**, requires a **30-day** advance written notice before increasing a windstorm deductible, and requires the named-storm period to continue for **72 hours** after the designation ends ([LDI-2020-07, B.2.7-B.2.16](repo://bulletins/LA/ldi-2020-07-hurricane-deductible.md#L71-L97), [B.3.1-B.3.21](repo://bulletins/LA/ldi-2020-07-hurricane-deductible.md#L179-L221)). Louisiana HO 01 17 (2020-09) implements the operative contract terms, including the same 72-hour named-storm period, while the bulletin constrains notice and disclosure administration ([HO 01 17, T.2-T.3 and T.1-T.7](repo://forms/HO/LA/HO-01-17/2020-09.md#L211-L231), [T.3 named storm](repo://forms/HO/LA/HO-01-17/2020-09.md#L261-L275)).

## Operational checklist

Before applying a windstorm or hail deductible, preserve these decisions in the underwriting or claim record:

1. **Contract identity:** policy line, state, effective date, declarations, attached endorsement or amendatory form, and edition. Confirm whether a later edition supersedes the cited form for this policy.
2. **Coverage:** covered property and direct physical loss. Separate covered wind or hail damage from wear, deterioration, cosmetic roof damage, flood, surface water, or other excluded causes.
3. **Causation:** whether windstorm or hail directly caused the loss, whether it combined with another cause, and whether wind created the opening required for wind-driven rain.
4. **Event basis:** one occurrence or loss event versus separate weather events, including related damage discovered later.
5. **Calculation basis:** selected percentage, applicable limit or insured value, property or coverage allocation, and whether the limit is measured before the loss.
6. **Other deductibles:** whether another deductible applies to a separate cause, whether the contract prevents duplication, and whether a state overlay requires a specific disclosure.
7. **Covered expenses:** emergency measures, temporary repairs, debris removal, loss of use, and supplemental payments only to the extent the policy covers them and the form subjects them to the deductible.
8. **Notice and evidence:** applicable advance-notice period for a deductible increase, storm designation or named-storm period, prompt loss notice, photographs, weather information, inspection access, estimates, and records.

### Training context, not contract authority

The state-deductibles training supplies a plain-language workflow aid: identify the policy, declarations, endorsements, location, cause, timing, and supporting evidence; keep coverage analysis separate from payment calculation; explain the result clearly; and escalate when the record does not support a clear answer ([training objectives](repo://training/state-deductibles-explained.md#L13-L53), [training workflow and escalation](repo://training/state-deductibles-explained.md#L79-L109), [training uncertainty guidance](repo://training/state-deductibles-explained.md#L814-L828)). Use that material to organize intake, file notes, and communications only. It does not establish a percentage, deductible basis, notice period, occurrence rule, or coverage outcome; those come from the governing form, bulletin, and edition identified for the loss.

The final payment explanation should identify the controlling form provision, the covered amount before the deductible, the selected percentage and limit basis, the deductible arithmetic, any occurrence allocation, and any other deductible or limit that affected payment. Regulatory bulletins require clear, consistent explanations and records supporting the factual and contractual basis for applying a storm or hail deductible ([Colorado DOI-2019-05, B.2.9-B.2.10](repo://bulletins/CO/doi-2019-05-hail-deductibles.md#L75-L79), [Texas B-2021-08, B.4.1-B.4.6](repo://bulletins/TX/b-2021-08-windstorm-deductibles.md#L213-L225), [Louisiana LDI-2020-07, B.2.21-B.2.24](repo://bulletins/LA/ldi-2020-07-hurricane-deductible.md#L99-L107)).
