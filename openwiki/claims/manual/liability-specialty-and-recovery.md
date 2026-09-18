---
type: claims-guidance
title: "Claims Manual: Liability, Specialty Property, and Recovery"
description: "Cross-system handling guidance for liability, condominium and loss-assessment, scheduled-property, subrogation, salvage, and referral decisions. Use the applicable policy or endorsement for coverage and insured-interest conclusions, and the claims manual for investigation, authority, documentation, and closure controls."
tags: [claims, liability, condominium, scheduled-property, subrogation, salvage, referrals]
verified:
  - by: openwiki/0.5.2
    at: 2026-09-18T12:15:46.420Z
sources:
  - id: openwiki-source-ca7a750da91cc1e96f01bfb9
    resource: repo://forms/HO/MS/HO-04-35/2023-02.md
  - id: openwiki-source-9317c9df787e726c2de69887
    resource: repo://forms/HO/MS/HO-04-61/2012-02.md
  - id: openwiki-source-7176aead92778c93cb0441d2
    resource: repo://forms/HO/MS/HO-3/2024-03.md
  - id: openwiki-source-9a3362ddf208da1fe1570617
    resource: repo://forms/HO/MS/HO-6/2023-02.md
  - id: openwiki-source-b835c3d80d50a5ec159c2c2a
    resource: repo://guidelines/claims/liability-claim-handling.md
  - id: openwiki-source-77e27410bda4d59c2b779d5e
    resource: repo://manuals/claims/manual.md
  - id: openwiki-source-2cf1b29512817bd0bdda6254
    resource: repo://training/condo-master-policy-gap.md
generated: { by: "openwiki/0.5.2", at: "2026-09-18T12:15:46.420Z" }
---

# Claims Manual: Liability, Specialty Property, and Recovery

## Scope and control rule

This page organizes related claim paths; it does not replace the controlling form, endorsement, declarations, or governing condominium documents. The claims manual governs internal workflow, authority, investigation, documentation, referral, and closure. Coverage conclusions must be made from the policy or endorsement in force for the reported event. The liability guidance is interpretive only: it supports investigation but does not create, expand, or restrict coverage ([claims manual, Chapter 1](repo://manuals/claims/manual.md#L15-L73); [liability guidance](repo://guidelines/claims/liability-claim-handling.md#L13-L41)).

Keep these questions separate throughout the file:

- **Liability:** Is there an occurrence, alleged bodily injury or property damage, insured status, defense or indemnity issue, or a liability exclusion requiring review?
- **Condominium:** Which party owns or controls each damaged interest, and what does the declaration, master policy, unit-owner form, or assessment endorsement require?
- **Scheduled property:** Does the claimed item match the schedule, and are ownership, identity, condition, value, custody, and salvage established?
- **Recovery:** Could an outside person or organization have caused or contributed to covered damage, and have evidence and recovery rights been protected?
- **Authority:** What may the assigned handler communicate, approve, pay, settle, release, or close, and what must be referred?

An estimate measures claimed damage; it is not a coverage decision. Record coverage analysis separately from cause, scope, valuation, payment, and authority analysis.

## End-to-end handoff

<!-- openwiki: mermaid parse failed and this diagram was converted to a text fence so it does not break rendering. Fix the diagram source and restore the mermaid fence. Parser error: Parse error on line 4: ...nce"] C -> D{ "Primary handling pat... Expecting 'SQE', 'DOUBLECIRCLEEND', 'PE', '-)', 'STADIUMEND', 'SUBROUTINEEND', 'PIPE', 'CYLINDEREND', 'DIAMOND_STOP', 'TAGEND', 'TRAPEND', 'INVTRAPEND', 'UNICODE_TEXT', 'TEXT', 'TAGSTART', got 'STR' -->
```text
flowchart TD
    A["Notice or occurrence received"] --> B["Open file and verify identity policy location and authority"]
    B --> C["Protect people property and evidence"]
    C --> D{ "Primary handling path" }
    D -->|Liability| L["Investigate occurrence injury damage insured status and defense needs"]
    D -->|Condominium| Cn["Separate unit common association and assessment interests"]
    D -->|Scheduled| S["Match item schedule ownership condition value and custody"]
    D -->|Property with possible third party| R["Preserve evidence and refer recovery review"]
    L --> V["Apply policy or endorsement and identify coverage issues"]
    Cn --> V
    S --> V
    R --> V
    V --> E{ "Referral or authority trigger?" }
    E -->|Yes| H["Suspend the affected commitment and obtain direction"]
    E -->|No| H2["Continue within delegated authority"]
    H --> P["Evaluate scope value payment and recovery together"]
    H2 --> P
    P --> Q["Document disposition and unresolved issues"]
    Q --> Z["Close only when investigation payment authority recovery and communications are complete"]
```

*Caption: Claim intake branches into liability, condominium, scheduled-property, and recovery work, then reunites at coverage, authority, payment, and closure controls.*

### Intake and common controls

Open a file for any communication asserting damage, loss, or a request for benefits; capture the source, reported date, location, parties, affected interest, and unverified facts. Acknowledge receipt without promising coverage or payment. Confirm the reporting party and every representative’s authority before disclosing claim information or accepting payment directions. Identify occupancy, access restrictions, other insurance, warranties, repairs already started, emergency vendors, and possible responsible parties ([claims manual, Chapter 2](repo://manuals/claims/manual.md#L389-L467)).

Direct reasonable protective action and emergency mitigation, but do not direct permanent repairs beyond the assigned authority. Ask that damaged property and material evidence be preserved when safe and practical. Arrange prompt inspection when cause, scope, ownership, or value could change. Preserve original photographs, recordings, messages, reports, statements, invoices, estimates, and communications; keep a chronological activity record. Investigation, inspection, an estimate, an advance, or a reservation of rights does not by itself accept or resolve coverage ([claims manual, Chapter 1](repo://manuals/claims/manual.md#L63-L103); [claims manual, Chapter 2](repo://manuals/claims/manual.md#L441-L463)).

## Liability claims

### Investigation path

Open a liability claim on notice of an occurrence and promptly identify the claimant, insured, date, location, alleged conduct, bodily injury, property damage, witnesses, and available physical or electronic evidence. Separate allegations from verified facts and alleged fault from confirmed fault. Inspect damaged property when it will assist liability or damages evaluation, and obtain repair information that can be compared with the reported occurrence ([claims manual, Chapter 8](repo://manuals/claims/manual.md#L2527-L2621)).

Use the applicable liability form to assess, rather than assume, the following:

1. whether the alleged harm is bodily injury or property damage;
2. whether it arose from an occurrence during the policy period and in the applicable territory;
3. whether the person or entity is an insured for the alleged conduct;
4. whether a duty to defend or indemnify is implicated; and
5. whether exclusions, contractual assumptions, property in the insured’s ownership or control, business or professional activity, vehicle or watercraft use, intentional conduct, pollution, abuse, or another exclusion changes the handling path.

The current HO-3 Coverage E grant pays damages for which an insured is legally liable because of bodily injury or property damage caused by an occurrence and provides a defense for a covered claim or suit; the form also requires prompt occurrence notice, forwarding of legal papers, cooperation, and consent before voluntary payment, assumption of obligation, or expense ([HO-3 2024-03, Coverage E](repo://forms/HO/MS/HO-3/2024-03.md#L1023-L1071)). The current HO-6 contains its own Coverage E grant and exclusions, so do not carry an HO-3 conclusion into an HO-6 file without checking the issued form ([HO-6 2023-02, Coverage E](repo://forms/HO/MS/HO-6/2023-02.md#L1000-L1050)).

A liability investigation is not permission to admit fault, promise payment, settle, or give legal advice. Refer serious injury, fatality, intentional or criminal conduct, governmental involvement, professional-services, employment, environmental, structural-failure, product, completed-work, or complex liability allegations before a material disposition. Preserve the scene and evidence and document the referral and authority direction ([claims manual, Chapter 8](repo://manuals/claims/manual.md#L2587-L2681); [liability guidance](repo://guidelines/claims/liability-claim-handling.md#L129-L171)).

### Liability/property boundary

Do not use property settlement concepts—roof age, property deductible, coinsurance, or an estimate—to determine a third party’s negligence, causation, or damages. The liability guidance specifically requires a separate liability analysis even when property information is useful background ([liability guidance](repo://guidelines/claims/liability-claim-handling.md#L229-L255)). If the same event creates both first-party property damage and a third-party allegation, maintain distinct coverage, damage, and recovery records while coordinating facts.

## Condominium, association, and loss-assessment claims

### Classify the interest before the repair

At intake identify whether each item is individual unit property, an interior finish or improvement, common or limited common property, an association-owned asset, a shared building system, personal property, liability damage, or an assessment. Identify the association, unit owner or tenant, property manager, party controlling access, and party authorized to receive payment. Inspect beyond the first visible room when water, smoke, or system damage can cross walls, floors, ceilings, units, or common areas. Maintain separate scopes and records for unit-owner, association, and vendor submissions; remove duplicated items before payment ([claims manual, Chapter 14](repo://manuals/claims/manual.md#L4727-L4851); [condominium training](repo://training/condo-master-policy-gap.md#L59-L139)).

Ownership, repair responsibility, and insurance responsibility are not interchangeable. Compare the declaration, master policy, unit-owner policy, endorsements, repair history, association decisions, and inspection evidence. Do not treat an association’s repair choice, maintenance rule, contractor invoice, or decision not to file a master-policy claim as a coverage conclusion. When the declaration and master policy appear inconsistent, document the conflict and refer it rather than resolving it by assumption ([condominium training](repo://training/condo-master-policy-gap.md#L133-L195)).

For a water loss, identify the source and route before applying a coverage position. Separate damage to the failed part from resulting damage, and distinguish plumbing discharge, repeated leakage, surface water, sewer or drain backup, sump conditions, roof opening, and outside water entry. Preserve source-area evidence before emergency work or repair changes it. The claims manual requires the same discipline for shared plumbing, electrical, heating, cooling, and drainage systems ([claims manual, Chapter 3](repo://manuals/claims/manual.md#L711-L765); [claims manual, Chapter 14](repo://manuals/claims/manual.md#L4757-L4821)).

### Loss assessment decision path

A loss-assessment demand is not automatically covered because an association issued it or because the underlying event damaged common property. Obtain the assessment notice, governing documents, association and master-policy information, meeting or allocation records when relevant, repair scope, cause evidence, payment or deductible information, and records showing the amount legally chargeable to the insured. Separate covered direct physical loss or covered liability from maintenance, reserve funding, improvement, code or regulatory costs, fines, penalties, interest, contract-only obligations, excluded causes, and charges allocated to another member ([HO 04 35, coverage and exclusions](repo://forms/HO/MS/HO-04-35/2023-02.md#L41-L137); [claims manual, Chapter 14](repo://manuals/claims/manual.md#L4865-L4881)).

The base forms have limited loss-assessment provisions. The current HO-3 provides assessment coverage when the assessment results from direct loss to association property caused by a peril insured against under Coverage A, with a **$2,000** maximum and the applicable deductible ([HO-3 2024-03](repo://forms/HO/MS/HO-3/2024-03.md#L449-L463)). The current HO-6 states a **$2,000** maximum for loss assessment and separately describes assessment conditions and exclusions ([HO-6 2023-02](repo://forms/HO/MS/HO-6/2023-02.md#L408-L420); [HO-6 2023-02](repo://forms/HO/MS/HO-6/2023-02.md#L1250-L1282)).

When attached, HO 04 35 provides broader loss-assessment coverage, but it remains conditional: the assessment must be legally chargeable to the insured, arise from covered direct physical loss to collective property or covered liability, and be properly allocated. The endorsement includes covered master-policy deductible assessments and sets a **$25,000** maximum; it does not cover ordinary maintenance, wear, improvements, many excluded causes, invalid or voluntary assessments, or amounts available from other insurance or recovery. Apply its deductible and recovery provisions only after confirming that the assessment itself qualifies ([HO 04 35, coverage](repo://forms/HO/MS/HO-04-35/2023-02.md#L41-L137); [HO 04 35, limit and deductible](repo://forms/HO/MS/HO-04-35/2023-02.md#L141-L241); [HO 04 35, remaining exclusions](repo://forms/HO/MS/HO-04-35/2023-02.md#L245-L365)).

For an assessment claim, do not authorize the insured to voluntarily pay, assume the obligation, settle, or release a responsible party without the required consent and recovery review. Record the legal basis, allocation, cause, applicable limit and deductible, other recoveries, payment recipient, and any disputed or unresolved component. If the assessment combines covered and excluded charges, separate the components rather than paying the combined demand.

## Scheduled and high-value property

At intake, separate scheduled items from unscheduled personal property. Match every claimed item to the schedule description, markings, inscriptions, serial number, appraisal, or other unique identifier. Establish the insured’s ownership or financial interest, location and use at loss, pre-loss condition, cause, value, repairability, custody, and residual value. Do not treat a repair estimate as proof of pre-loss value; use a qualified evaluator when identification, authentication, provenance, restoration, or valuation requires specialized knowledge ([claims manual, Chapter 17](repo://manuals/claims/manual.md#L5783-L5849)).

The scheduled-property wording requires the description to distinguish the item from like property, requires records supporting ownership and value, and requires preservation and inspection before repair, restoration, disposal, sale, or replacement. It excludes unexplained or mysterious disappearance unless the schedule provides otherwise, and it addresses dishonest acts, voluntary parting, deterioration, restoration consent, transfer of salvage, and recovery of a found item ([scheduled-property form, special requirements](repo://forms/HO/MS/HO-04-61/2012-02.md#L743-L829)). The applicable limit is the most payable for the scheduled item or group; it is not extra insurance, and payment remains limited by the insured’s financial interest and the applicable valuation terms ([scheduled-property form, limits](repo://forms/HO/MS/HO-04-61/2012-02.md#L209-L269)). Verify the actual issued schedule and endorsement before relying on this path.

For theft, preserve the law-enforcement report and evidence of possession, access, discovery, and item identity. For antiques, fine art, collectibles, jewelry, or unique property, control custody and vendor transfers, assess restoration before replacement, document provenance and market evidence, and refer authenticity or repeated-loss concerns. Do not release or dispose of high-value damaged property while inspection, appraisal, subrogation, or salvage review remains open ([claims manual, Chapter 17](repo://manuals/claims/manual.md#L5871-L5981)).

## Subrogation, contribution, and salvage

Open a recovery review as soon as facts indicate that a contractor, manufacturer, utility, property manager, neighboring owner, vendor, operator, tenant, association, or other outside party caused or contributed to covered damage. Notify the subrogation unit within **10 days** after identifying a recoverable loss. Preserve the insured’s and carrier’s recovery rights: do not authorize a release, waiver, unapproved settlement, return of a potentially defective product, destructive testing, repair, cleaning, dismantling, or disposal before the review and evidence-preservation steps are complete ([claims manual, Chapter 18](repo://manuals/claims/manual.md#L5985-L6007); [claims manual, Chapter 18](repo://manuals/claims/manual.md#L6159-L6271)).

Capture the insured’s account, responsible-party identities and contacts, chronology, scene and source photographs, witness information, video or access records, contracts, work orders, invoices, warranties, mitigation records, prior repairs, and relevant communications. Refer water, fire, electrical, product, contractor, vehicle, utility, shared-system, common-area, and neighboring-property losses when another party may be responsible. Continue ordinary adjustment of the insured’s covered loss while recovery is evaluated unless the subrogation unit directs otherwise.

Treat salvage as both an evidence and value control. Retain material damaged property for the manual’s **60-day** salvage-inspection period when inspection may be needed; segregate and protect it from weather, contamination, theft, commingling, and further damage; record custody and vendor transfers; and do not dispose of it until subrogation review is complete or release authority is documented ([claims manual, Chapter 18](repo://manuals/claims/manual.md#L6123-L6163)). The applicable form may separately permit taking title or requiring transfer after payment, so payment, ownership, salvage, and recovery disposition must be reconciled rather than assumed ([HO-3 2024-03, personal property and recovery duties](repo://forms/HO/MS/HO-3/2024-03.md#L257-L309); [HO 04 35, recovery](repo://forms/HO/MS/HO-04-35/2023-02.md#L127-L137)).

Document deductible recovery interest, recovery-related storage and inspection expenses, all demands and correspondence from responsible parties or their insurers, and the final recovery disposition. Use neutral language: a recovery referral is not an admission of liability by the insured or carrier.

## Authority, referral, and closure

### Mandatory referral controls

Refer and document direction before making a material disposition when any of the following applies:

- evaluated exposure exceeds **$25,000**; suspend settlement authority pending direction;
- coverage is disputed or a reservation of rights is involved; issue a reservation within **10 days** when coverage remains unresolved;
- suspected material misrepresentation, fraud, arson, intentional loss, fatality, serious bodily injury, criminal conduct, structural instability, environmental contamination, mold or microbial growth, collapse, flood or uncertain water source, vacancy, business use, code or authority action, attorney or public-adjuster involvement, appraisal or mediation demand, punitive or bad-faith demand, or complaint is present;
- ownership, insured status, mortgagee or lienholder rights, payment direction, condominium responsibility, assessment validity, scheduled-item identity or value, salvage value, or recovery rights are disputed; or
- product failure, defective work, utility involvement, contractor dispute, repeated loss, material scope dispute, or any evidence-preservation conflict could affect coverage, payment, or recovery.

The manual also requires large-loss reporting for condominium exposure at or above **$100,000**. Referral does not automatically stop necessary mitigation or ordinary investigation; it stops the affected unauthorized commitment and preserves the need for direction ([claims manual, authority controls](repo://manuals/claims/manual.md#L141-L151); [claims manual, referral triggers](repo://manuals/claims/manual.md#L6287-L6357); [claims manual, specialized and property triggers](repo://manuals/claims/manual.md#L6389-L6615); [claims manual, condominium large loss](repo://manuals/claims/manual.md#L4751-L4755)).

Do not issue a denial, reservation, settlement, payment, release, or liability admission without the required authority. Record the issue referred, recipient, date, authority status, direction received, and communication issued. Do not split transactions to evade authority limits ([claims manual, Chapter 1](repo://manuals/claims/manual.md#L141-L175); [claims manual, Chapter 2](repo://manuals/claims/manual.md#L657-L663)).

### Closure checklist

Before closing, confirm that the file states: the controlling form and provisions; verified parties and interests; cause and scope findings; separate liability, condominium, scheduled-property, and recovery analyses; mitigation and evidence status; valuation, deductible, payments, and payees; referrals and authority approvals; salvage and recovery disposition; material communications; and unresolved issues. A condominium claim remains open while material property-interest or responsibility questions are unaddressed. A scheduled-property claim remains open until every item has a documented final disposition. A recovery referral remains open until required documentation and disposition direction are complete ([claims manual, Chapter 14](repo://manuals/claims/manual.md#L5033-L5067); [claims manual, Chapter 17](repo://manuals/claims/manual.md#L5971-L5981); [claims manual, Chapter 18](repo://manuals/claims/manual.md#L6273-L6283)).

If credible new information shows additional loss-related damage, a changed cause, an unresolved property interest, or an impaired recovery path, reopen or re-refer the investigation and document what changed. Closure is a controlled lifecycle state, not merely the point at which visible repairs finish.

## Source map

- Internal workflow and authority: [Property Claims Handling Manual](repo://manuals/claims/manual.md#L15-L175), [First Notice and Acknowledgement](repo://manuals/claims/manual.md#L389-L707), [Liability Claims](repo://manuals/claims/manual.md#L2527-L2755), [Condominium and Association Losses](repo://manuals/claims/manual.md#L4721-L5067), [Scheduled and High-Value Property](repo://manuals/claims/manual.md#L5783-L5981), and [Subrogation and Salvage](repo://manuals/claims/manual.md#L5983-L6283).
- Liability interpretation and separation of property concepts: [Liability Claim Handling Guidance](repo://guidelines/claims/liability-claim-handling.md#L13-L41).
- Coverage and assessment conclusions: [HO-3 2024-03](repo://forms/HO/MS/HO-3/2024-03.md#L1023-L1071), [HO-6 2023-02](repo://forms/HO/MS/HO-6/2023-02.md#L1000-L1050), and [HO 04 35 Loss Assessment Coverage](repo://forms/HO/MS/HO-04-35/2023-02.md#L41-L145).
- Interpretive condominium context only: [The Condominium Master Policy Gap](repo://training/condo-master-policy-gap.md#L59-L195).
