---
type: coverage
title: Personal Property Limits, Special Limits, and Scheduling
description: Compares Coverage C limits and special sublimits across the supplied HO-3, HO-4, HO-5, and HO-6 editions, then explains how business-property, scheduled-property, special-personal-property, credit-card, forgery, and identity-fraud endorsements modify those limits. Use the policy edition, declarations, attached schedule, and applicable deductible together when evaluating a personal-property loss.
tags: [Coverage C, personal property, special limits, business property, scheduled property, identity fraud]
verified:
  - by: openwiki/0.5.2
    at: 2026-09-18T05:47:51.376Z
sources:
  - id: openwiki-source-140687b379118f9f7520b12c
    resource: repo://forms/HO/MS/HO-04-12/2018-09.md
  - id: openwiki-source-cc338df9f298d0367fa0ce1a
    resource: repo://forms/HO/MS/HO-04-53/2013-06.md
  - id: openwiki-source-f85056bbe235cf6a4fc2c4bd
    resource: repo://forms/HO/MS/HO-04-55/2017-01.md
  - id: openwiki-source-9317c9df787e726c2de69887
    resource: repo://forms/HO/MS/HO-04-61/2012-02.md
  - id: openwiki-source-88c622c73b9f6c05a612e286
    resource: repo://forms/HO/MS/HO-04-61/2020-11.md
  - id: openwiki-source-9679ec1f8a738a9848624d0a
    resource: repo://forms/HO/MS/HO-04-65/2018-09.md
  - id: openwiki-source-93641f89ccf305903a2b34b6
    resource: repo://forms/HO/MS/HO-05-24/2018-09.md
  - id: openwiki-source-7176aead92778c93cb0441d2
    resource: repo://forms/HO/MS/HO-3/2024-03.md
  - id: openwiki-source-ea6397bf6ad5bac1c652ab3a
    resource: repo://forms/HO/MS/HO-4/2021-10.md
  - id: openwiki-source-25d651d4a45fc0fd8ab047e2
    resource: repo://forms/HO/MS/HO-5/2022-06.md
  - id: openwiki-source-9a3362ddf208da1fe1570617
    resource: repo://forms/HO/MS/HO-6/2023-02.md
  - id: openwiki-source-4f6faf651be34a4d6948eebe
    resource: repo://training/customer-faq-homeowners.md
generated: { by: "openwiki/0.5.2", at: "2026-09-18T05:47:51.376Z" }
---

# Personal Property Limits, Special Limits, and Scheduling

## Decision order

Coverage C decisions are made in layers. First identify the policy line and edition. Then classify the property and cause of loss, apply the base Coverage C limit and any category sublimit, and only then apply an attached endorsement or schedule. A limit modification does not by itself restore excluded property or an excluded cause of loss; the endorsement must expressly restore coverage to do that.

```mermaid
flowchart TD
    A["Identify policy line and edition"] --> B["Classify property and cause of loss"]
    B --> C{"Business property?"}
    C -->|"Yes"| D["Apply base business limit or HO 04 12"]
    C -->|"No"| E{"Scheduled item?"}
    D --> E
    E -->|"Yes"| F["Verify attached Schedule and item limit"]
    E -->|"No"| G{"Special category?"}
    F --> H["Apply scheduled-property deductible"]
    G -->|"Yes"| I["Apply base or HO 04 65 special limit"]
    G -->|"No"| J["Apply Coverage C limit"]
    I --> K["Apply applicable policy deductible"]
    J --> K
    K --> L["Check exclusions, conditions, and other insurance"]
    H --> L
```

*This flow shows how classification, scheduling, sublimits, deductibles, and exclusions interact; an available limit is not a coverage grant.*

## Base Coverage C positions by form edition

### HO-3 2024-03

HO-3 2024-03 covers personal property owned or used by an insured anywhere in the world. The Coverage C limit is **50% of Coverage A**. Property of a guest or residence employee can be covered at the residence premises at the insured’s request, but the employee-property coverage does not increase Coverage C. Covered property still must suffer direct physical loss from a covered peril. [HO-3 2024-03 C.1–C.8](repo://forms/HO/MS/HO-3/2024-03.md#L221-L235)

The base HO-3 special limits are: **$300** for money, bank notes, bullion, coins, medals, and precious metals; **$2,000** for theft of jewelry, watches, and precious stones; **$3,000** for theft of firearms and related equipment; **$1,500** for watercraft including trailers; **$3,000** for theft of silverware and similar plated ware; **$3,000** for business property on the residence premises; and **$1,500** for electronic apparatus in a motor vehicle. Each special limit is within, not additional to, Coverage C. [HO-3 2024-03 C.9–C.18](repo://forms/HO/MS/HO-3/2024-03.md#L237-L255)

The base HO-3 also provides separate additional-insurance coverage of **$1,500** for credit-card, fund-transfer-card, and forgery loss. It does not cover card loss arising from a resident relative or entrusted person, or from business activity. This is not a Coverage C sublimit; it is separate Coverage E insurance. [HO-3 2024-03 E.17–E.22](repo://forms/HO/MS/HO-3/2024-03.md#L445-L455)

### HO-4 2021-10

HO-4 2021-10 covers an insured’s personal property at and away from the residence premises, including property temporarily removed when the cause is covered. The supplied Coverage C section does **not** state a Coverage C percentage or dollar amount; use the applicable limit shown by the policy and declarations rather than importing the HO-3 or HO-5 50% rule. It specifically excludes business property away from the residence premises unless another Coverage C provision supplies coverage. [HO-4 2021-10 C.1–C.14](repo://forms/HO/MS/HO-4/2021-10.md#L219-L245)

Its stated special limits are **$1,500** for electronic apparatus in a motor vehicle, **$250** for money and precious metals, **$2,000** for theft of jewelry, watches, and precious stones, **$2,500** for theft of firearms, **$1,500** for watercraft including trailers, **$2,500** for theft of silverware, and **$3,000** for business property on the residence premises. The special limits are part of the applicable Coverage C limit. [HO-4 2021-10 C.15–C.22](repo://forms/HO/MS/HO-4/2021-10.md#L245-L263)

HO-4 also provides separate additional-insurance coverage of **$1,000** for credit-card, fund-transfer-card, and forgery loss. The form excludes business use and specified voluntary or dishonest use; this coverage is not a Coverage C sublimit. [HO-4 2021-10 E.17–E.23](repo://forms/HO/MS/HO-4/2021-10.md#L465-L477)

### HO-5 2022-06

HO-5 2022-06 covers personal property anywhere in the world, including property of others in an insured’s care and certain guest, residence-employee, and student property. The Coverage C limit is **50% of Coverage A**, applies regardless of the number of insureds, locations, items, or claims, and is reduced by payments. [HO-5 2022-06 C.1–C.10](repo://forms/HO/MS/HO-5/2022-06.md#L253-L271)

The HO-5 special limits are: **$300** for money, bank notes, bullion, precious metals, and stored-value cards; **$3,000** for theft of jewelry, watches, and precious or semiprecious stones; **$3,500** for theft of firearms and related equipment; **$2,000** for watercraft including trailer and accessories; **$5,000** for theft of silverware, goldware, pewterware, platinumware, and plated articles; **$5,000** for business property on the residence premises; and **$2,000** for electronic apparatus in a motor vehicle. Acquired property remains subject to the Coverage C limit and special limits. [HO-5 2022-06 C.8–C.18](repo://forms/HO/MS/HO-5/2022-06.md#L267-L287)

HO-5 separately provides **$2,500** of additional-insurance coverage for credit-card, fund-transfer-card, forgery, and counterfeit-paper-currency loss. Business use and certain use by resident relatives or entrusted persons remain excluded. [HO-5 2022-06 E.24–E.30](repo://forms/HO/MS/HO-5/2022-06.md#L509-L521)

### HO-6 2023-02

HO-6 2023-02 covers personal property at or away from the residence premises, including certain guest, residence-employee, student, and temporarily occupied-residence property. It states that acquired property is subject to the applicable Coverage C limit, but the supplied Coverage C section does **not** state a percentage or dollar amount for that limit. Use the applicable policy/declarations limit; do not import the HO-3 or HO-5 50% rule. [HO-6 2023-02 C.1–C.10](repo://forms/HO/MS/HO-6/2023-02.md#L186-L204)

The HO-6 special limits are: **$250** for money, bank notes, bullion, gold other than goldware, silver other than silverware, platinum, coins, medals, and precious metals; **$2,000** for theft of jewelry, watches, and precious or semiprecious stones; **$2,500** for theft of firearms and related equipment; **$1,500** for watercraft including trailers and equipment; **$2,500** for theft of silverware and specified plated ware; **$3,000** for business property on the residence premises; and **$1,500** for electronic apparatus in a motor vehicle. Special limits apply before the applicable deductible and do not increase Coverage C. [HO-6 2023-02 C.26–C.35](repo://forms/HO/MS/HO-6/2023-02.md#L236-L256)

HO-6’s separate Coverage E protection for credit-card, fund-transfer-card, forgery, and counterfeit-money loss is **$1,000** and does not reduce Coverage C. The form excludes business use and requires prompt notice and reasonable protective steps. [HO-6 2023-02 E.11–E.20](repo://forms/HO/MS/HO-6/2023-02.md#L390-L408)

## Endorsements that modify Coverage C decisions

### HO 04 12 2018-09 — increased business-property limit

HO 04 12 (2018-09) modifies business-property coverage. It defines business property as property used in a trade, profession, occupation, or other activity for economic gain and covers qualifying business property owned or used by an insured, including property temporarily removed from the residence premises, subject to the endorsement’s terms. The endorsement does not create coverage for an otherwise excluded property or cause of loss. [HO 04 12 W.0–W.1](repo://forms/HO/MS/HO-04-12/2018-09.md#L15-L39) · [HO 04 12 W.1.1–W.1.12](repo://forms/HO/MS/HO-04-12/2018-09.md#L57-L81)

For business property on the **Residence Premises**, HO 04 12 sets a collective **$10,000** maximum for all business property. The amount is not increased by separate items, ownership, buildings, rooms, storage areas, or different business uses. The endorsement’s limit section does not state a separate dollar limit for property away from the residence premises; away-from-premises coverage remains subject to the endorsement and the underlying policy, including its theft and other limitations. [HO 04 12 W.2.1–W.2.9 and W.2.18–W.2.21](repo://forms/HO/MS/HO-04-12/2018-09.md#L171-L213) · [HO 04 12 W.1.3–W.1.5](repo://forms/HO/MS/HO-04-12/2018-09.md#L61-L69) · [HO 04 12 W.4.29–W.4.35](repo://forms/HO/MS/HO-04-12/2018-09.md#L385-L399)

The applicable policy deductible still applies to the total covered business-property loss from an occurrence. The endorsement gives no numeric deductible; it applies the policy’s applicable deductible before payment, including to covered emergency measures and whether the loss is settled at actual cash value or replacement cost. [HO 04 12 W.3.1–W.3.20](repo://forms/HO/MS/HO-04-12/2018-09.md#L269-L309)

### HO 04 65 2018-09 — increased Coverage C special limits

HO 04 65 (2018-09) **modifies** only the Coverage C special limits it expressly increases. It first requires the loss and property to be covered, then replaces the otherwise applicable category special limit; it does not alter exclusions, the cause of loss, the valuation method, or the property interest required for coverage. [HO 04 65 W.1.1–W.1.15](repo://forms/HO/MS/HO-04-65/2018-09.md#L45-L75)

The endorsement’s increased theft limits are **$5,000** for jewelry, watches, and precious stones; **$6,500** for firearms; and **$10,000** for silverware. Each limit is collective for covered theft loss in its category from the same occurrence, regardless of the number of items or insureds. The applicable policy deductible remains in force; the endorsement does not state a numeric deductible. [HO 04 65 W.2.1–W.2.9](repo://forms/HO/MS/HO-04-65/2018-09.md#L157-L177) · [HO 04 65 W.2.14–W.2.18](repo://forms/HO/MS/HO-04-65/2018-09.md#L183-L193) · [HO 04 65 W.3.1–W.3.10 and W.3.32](repo://forms/HO/MS/HO-04-65/2018-09.md#L263-L283) · [HO 04 65 W.3.32](repo://forms/HO/MS/HO-04-65/2018-09.md#L323-L327)

### HO 04 61 — scheduled personal property

Scheduled-property coverage is item-specific, not a general increase to Coverage C. The attached Schedule identifies the property, description, and applicable limit; property not described is not scheduled, and similar property is not pulled into coverage by resemblance. Changes are effective only when made part of the Schedule by the insurer. [HO 04 61 2012-02 W.0](repo://forms/HO/MS/HO-04-61/2012-02.md#L13-L49)

**2012-02 edition.** This edition is superseded by the 2020-11 edition for policies effective on or after November 1, 2020, but remains in force for policies written under it. It covers described scheduled property for direct physical loss anywhere in the world, including while worn, used, transported, stored, or temporarily in another person’s possession. It expressly covers theft, disappearance, accidental breakage, and accidental damage, subject to the endorsement’s exclusions. [HO 04 61 2012-02 preamble and W.1](repo://forms/HO/MS/HO-04-61/2012-02.md#L8-L9) · [HO 04 61 2012-02 W.1.1–W.1.12](repo://forms/HO/MS/HO-04-61/2012-02.md#L51-L75)

The 2012-02 Schedule limit is the most payable for the scheduled item or group and is not additional insurance. The scheduled-property deductible is **$0**; the form describes separate- or same-occurrence handling, but a zero deductible produces no deductible reduction. [HO 04 61 2012-02 W.2.1–W.2.8](repo://forms/HO/MS/HO-04-61/2012-02.md#L209-L225) · [HO 04 61 2012-02 W.3.1–W.3.12](repo://forms/HO/MS/HO-04-61/2012-02.md#L315-L339)

**2020-11 edition.** The current supplied edition requires an insured to have an ownership interest or legal responsibility and an insurable interest at the time of loss. It covers described property at or away from the residence, including while worn, used, stored, transported, displayed, or temporarily entrusted; it also covers theft, mysterious disappearance, breakage, and accidental damage when the endorsement’s requirements are met. Property acquired after the Schedule is issued is not covered unless the insurer agrees to add it. [HO 04 61 2020-11 W.0](repo://forms/HO/MS/HO-04-61/2020-11.md#L13-L53) · [HO 04 61 2020-11 W.1.1–W.1.10](repo://forms/HO/MS/HO-04-61/2020-11.md#L55-L75)

The 2020-11 Schedule’s applicable limit is the maximum for the described property and does not increase because of repair cost, scarcity, sentimental value, location, possession by another person, or another recovery. Its deductible is **$250 per covered loss**, applied to the total scheduled-property loss from the same event rather than separately merely because items are separately described. The endorsement requires prompt notice of material changes in ownership, location, condition, or use, and additions or removals take effect only when recorded in the Schedule. [HO 04 61 2020-11 W.2.1–W.2.23](repo://forms/HO/MS/HO-04-61/2020-11.md#L213-L261) · [HO 04 61 2020-11 W.3.1–W.3.13 and W.3.26–W.3.31](repo://forms/HO/MS/HO-04-61/2020-11.md#L291-L319) · [HO 04 61 2020-11 W.3.26–W.3.31](repo://forms/HO/MS/HO-04-61/2020-11.md#L343-L353)

### HO 05 24 2018-09 — special personal property coverage

HO 05 24 (2018-09) **modifies** the peril treatment for eligible personal property: it covers direct physical loss caused by a peril not otherwise excluded or limited, while retaining policy exclusions and conditions. It is not scheduled-property coverage and does not give a blanket limit separate from the policy; the applicable Coverage C limit and deductible continue to govern unless the form expressly changes them. [HO 05 24 W.0](repo://forms/HO/MS/HO-05-24/2018-09.md#L13-L35) · [HO 05 24 W.1.1–W.1.16](repo://forms/HO/MS/HO-05-24/2018-09.md#L41-L73)

This form keeps a **$2,500** theft limit for jewelry, watches, and precious stones. It excludes property held for sale, buildings and construction materials, most business property away from the residence premises except property an insured personally carries or uses, and other listed property categories. Its general limit is the applicable policy Coverage C limit; the form’s deductible section supplies no numeric amount and applies the policy deductible to each covered occurrence. [HO 05 24 W.1.17–W.1.28](repo://forms/HO/MS/HO-05-24/2018-09.md#L75-L97) · [HO 05 24 W.2.1–W.2.18](repo://forms/HO/MS/HO-05-24/2018-09.md#L141-L177) · [HO 05 24 W.3.1–W.3.10](repo://forms/HO/MS/HO-05-24/2018-09.md#L209-L229)

### HO 04 53 2013-06 — credit card, fund transfer card, and forgery

HO 04 53 (2013-06) **modifies** the separate credit-card, fund-transfer-card, forgery, and counterfeit-money coverage. It covers direct financial loss from theft or unauthorized use of qualifying cards and access information, unauthorized transfers, forgery or alteration of checks and negotiable instruments, and good-faith acceptance of counterfeit paper currency, subject to its exclusions and recovery conditions. [HO 04 53 W.1.1–W.1.32](repo://forms/HO/MS/HO-04-53/2013-06.md#L57-L121)

The endorsement limit is **$10,000** for all covered loss under that coverage, collectively for all insureds, cards, accounts, instruments, transactions, and related acts. It treats related theft, unauthorized use, forgery, alteration, or counterfeit-currency acts as one occurrence for the limit. The deductible is expressly **not applicable** to covered loss under this endorsement. [HO 04 53 W.2.1–W.2.15 and W.2.36–W.2.38](repo://forms/HO/MS/HO-04-53/2013-06.md#L171-L203) · [HO 04 53 W.3.1–W.3.11](repo://forms/HO/MS/HO-04-53/2013-06.md#L249-L271)

This endorsement does not turn Coverage C into card or forgery coverage. It excludes, among other things, insured or entrusted-person acts, business activity, voluntary parting after deceit, and loss reimbursed by an issuer or another source. [HO 04 53 W.1.40–W.1.52](repo://forms/HO/MS/HO-04-53/2013-06.md#L137-L161)

### HO 04 55 2017-01 — identity-fraud expenses

HO 04 55 (2017-01) provides a separate identity-fraud-expense coverage, not reimbursement for the stolen money, property, securities, income, unauthorized charges, or debt itself. A covered expense must be reasonable, necessary, actually incurred by an insured, and directly caused by identity fraud; examples include reports, records, replacement identification, account restoration, fraud alerts, approved identity-restoration services, certain legal fees with prior consent, and lost wages supported by records. The event must occur during the policy period and the expense may be incurred afterward if the endorsement’s requirements are met. [HO 04 55 W.0](repo://forms/HO/MS/HO-04-55/2017-01.md#L13-L53) · [HO 04 55 W.1.1–W.1.32](repo://forms/HO/MS/HO-04-55/2017-01.md#L55-L119)

The identity-fraud-expense limit is **$15,000**. The endorsement’s deductible section says the applicable deductible is subtracted from a covered loss, but it states no numeric deductible; use the deductible applicable under the policy. The insured must give prompt notice, preserve records, mitigate further expense, pursue available reimbursement, and obtain consent before seeking legal-fee or court-cost reimbursement. [HO 04 55 W.2.1–W.2.12](repo://forms/HO/MS/HO-04-55/2017-01.md#L213-L237) · [HO 04 55 W.3.1–W.3.18](repo://forms/HO/MS/HO-04-55/2017-01.md#L289-L325) · [HO 04 55 W.1.49–W.1.60](repo://forms/HO/MS/HO-04-55/2017-01.md#L153-L175)

## Claim-handling controls

For any personal-property claim, confirm the exact base-form edition, Coverage C limit shown in the policy, applicable category sublimit, attached endorsements, schedule description and limit, cause of loss, deductible, and other insurance before calculating payment. A special or scheduled limit caps covered loss; it does not establish that the property or peril is covered. The base forms require prompt notice, protection from further damage, retention or inspection of damaged property when reasonably possible, and records supporting ownership, condition, value, and loss. [HO-3 2024-03 C.19–C.30](repo://forms/HO/MS/HO-3/2024-03.md#L257-L279) · [Customer FAQ L.2.13–L.2.18](repo://training/customer-faq-homeowners.md#L109-L131)

Training reinforces the operational expectation to explain limits and deductibles without promising full payment, ask what happened and what property was damaged, preserve records, and refer an unclear or claim-specific question for review. It is guidance, not authority for a limit or deductible; the form edition and attached endorsement control the number. [Customer FAQ L.1.6–L.1.12](repo://training/customer-faq-homeowners.md#L25-L37) · [Customer FAQ L.2.6–L.2.8](repo://training/customer-faq-homeowners.md#L81-L91) · [Customer FAQ L.2.52–L.2.59](repo://training/customer-faq-homeowners.md#L265-L295)
