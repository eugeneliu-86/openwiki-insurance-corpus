---
type: policy-assembly
title: Editions, Endorsements, and State Attachments
description: A policy-assembly workflow for routing by line, state, effective date, Declarations, and the complete issued package before interpreting coverage. It separates contract forms, regulatory bulletins, and internal guidance while resolving endorsement and state-form conflicts.
tags: [policy assembly, insurance forms, endorsements, state attachments]
verified:
  - by: openwiki/0.5.2
    at: 2026-09-19T07:29:25.602Z
sources:
  - id: openwiki-source-38049e374f54d1eb9a15f4ef
    resource: repo://bulletins/TX/b-2021-08-windstorm-deductibles.md
  - id: openwiki-source-cd26c30cc942869b52618f95
    resource: repo://forms/HO/MS/HO-04-90/2010-10.md
  - id: openwiki-source-6a71dbfe57881e21b8a0e5ea
    resource: repo://forms/HO/MS/HO-04-90/2027-01.md
  - id: openwiki-source-f4ebd2ece3eaf490178dfc41
    resource: repo://forms/HO/MS/HO-3/2018-09.md
  - id: openwiki-source-7176aead92778c93cb0441d2
    resource: repo://forms/HO/MS/HO-3/2024-03.md
  - id: openwiki-source-ff7de1315ac46ce4dd65d251
    resource: repo://forms/HO/TX/HO-01-45/2022-01.md
  - id: openwiki-source-da67a262bebb42780999bd2a
    resource: repo://guidelines/appetite/tx-homeowners.md
  - id: openwiki-source-2b86de67275893a8b33d953b
    resource: repo://manuals/underwriting/manual.md
  - id: openwiki-source-d3cc221b966da1c2185d5b2f
    resource: repo://memoranda/HO-04-90-2027-01.md
  - id: openwiki-source-7433017bf6321ec1bc9e4bb0
    resource: repo://memoranda/HO-3-2018-09.md
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
generated: { by: "openwiki/0.5.2", at: "2026-09-19T07:29:25.602Z" }
---


# Editions, Endorsements, and State Attachments

A policy position is assembled from documents with different jobs. Start with the issued policy package: the base form edition, Declarations, attached endorsements, and any applicable state amendatory form are contract authority. Bulletins are regulatory authority that constrains how the carrier files, issues, discloses, and administers the contract. Filing memoranda and training explain or teach; the underwriting manual and appetite guide constrain carrier action. None of those interpretive or internal documents changes the contract conclusion ([README, document families](repo://README.md#L15-L21), [README, authority model](repo://README.md#L35-L41), [Guidance Versus Contract Language](repo://training/guidance-versus-contract.md#L15-L23)).

## Authority layers and relationship vocabulary

| Document | Responsibility | Safe relationship to state |
| --- | --- | --- |
| Base form | Supplies the coverage grants, definitions, limits, exclusions, conditions, and settlement rules for its line and edition. | Read the edition that applies to the issued policy. |
| Attached endorsement | Changes the base policy only within its stated terms and only when attached. | The endorsement modifies the base form; unchanged terms remain applicable. ([HO 04 90 2027-01](repo://forms/HO/MS/HO-04-90/2027-01.md#L16-L36), [HO-3 2024-03](repo://forms/HO/MS/HO-3/2024-03.md#L593-L597)) |
| State amendatory form | Adds state-specific contract wording and a precedence rule for matters it addresses. | The state form implements the relevant bulletin; it is not the bulletin. ([HO 01 45 2022-01](repo://forms/HO/TX/HO-01-45/2022-01.md#L13-L23), [B-2021-08](repo://bulletins/TX/b-2021-08-windstorm-deductibles.md#L13-L27)) |
| Regulator bulletin | Constrains issuance, disclosure, filing, underwriting, rating, or claim administration. | It constrains the carrier, but does not create a deductible or coverage term absent from the policy ([B-2021-08](repo://bulletins/TX/b-2021-08-windstorm-deductibles.md#L19-L27), [B-2021-08](repo://bulletins/TX/b-2021-08-windstorm-deductibles.md#L63-L69)). |
| Filing memorandum and training | Explain an edition or teach a review method. | Interpretation only; they do not replace the filed form ([README](repo://README.md#L20-L21), [Choosing the Governing Edition](repo://training/choosing-the-governing-edition.md#L101-L107)). |
| Appetite guide and underwriting manual | Set eligibility, authority, referral, documentation, and attachment controls. | Internal guidance constrains binding or attachment; it does not alter coverage ([manual Rules 100.B-100.E](repo://manuals/underwriting/manual.md#L21-L43), [Texas appetite guide](repo://guidelines/appetite/tx-homeowners.md#L13-L35)). |

For a composed proposition, name the acting document first and use one of the repository’s directional verbs: `supersedes`, `writes back`, `preserves`, `modifies`, `implements`, or `constrains`. For example, **HO 04 90 2027-01 writes back HO-3 2024-03 X.8-X.9** only within its stated water-backup coverage, while **HO 04 90 2027-01 preserves HO-3 2024-03 terms** that it does not modify. Cite both documents whenever the proposition connects them ([HO 04 90 2027-01](repo://forms/HO/MS/HO-04-90/2027-01.md#L16-L36), [HO 04 90 2027-01 coverage](repo://forms/HO/MS/HO-04-90/2027-01.md#L256-L282), [HO-3 2024-03](repo://forms/HO/MS/HO-3/2024-03.md#L593-L597)).

### Entry gate: route before interpreting coverage

Before interpreting coverage, route the matter by **line, state, policy-effective date, Declarations, complete issued attachment package, and applicable state form**. The repository path carries line, state, form, and edition; the Declarations identify the insurance and applicable limits; and the issued package supplies the wording actually made part of the policy ([README, layout and load-bearing path](repo://README.md#L13-L31), [HO-3 2018-09 agreement](repo://forms/HO/MS/HO-3/2018-09.md#L13-L21)). Treat a schedule or system label as an index, not as the operative endorsement language: a listed-but-missing form needs the complete package or a reliable issued copy, while an attached-but-unlisted form must be reconciled to the policy record ([Attaching Endorsements Correctly](repo://training/attaching-endorsements.md#L65-L87), [Attaching Endorsements Correctly](repo://training/attaching-endorsements.md#L221-L227)).

Do not begin a detailed coverage interpretation until the candidate base form, Declarations, all referenced pages and schedules, attached endorsements, and state amendatory form are identified. If the package is incomplete, labels conflict, or the relevant attachment cannot be tied to the insured, term, location, and property, record the uncertainty and obtain or escalate the missing evidence rather than choosing the wording that produces the preferred result ([Choosing the Governing Edition](repo://training/choosing-the-governing-edition.md#L109-L119), [Attaching Endorsements Correctly](repo://training/attaching-endorsements.md#L193-L215)).

## Date-sensitive edition selection

Use the policy-effective date to select the candidate base and endorsement editions, then verify that the selected wording and endorsements were actually issued and attached. A later frozen authority does not rewrite an older policy: prior editions remain in force for policies written under them ([README, frozen authority](repo://README.md#L35-L37), [Choosing the Governing Edition](repo://training/choosing-the-governing-edition.md#L69-L79)).

For the representative HO-3 package:

- **HO-3 2018-09** is effective 2018-09-01 and is marked superseded by **HO-3 2024-03** for policies effective on or after 2024-03-01. **HO-3 2024-03 supersedes HO-3 2018-09** only at that boundary; the 2018-09 form remains live for policies written under it ([HO-3 2018-09](repo://forms/HO/MS/HO-3/2018-09.md#L1-L9), [HO-3 2024-03](repo://forms/HO/MS/HO-3/2024-03.md#L1-L7)).
- **HO 04 90 2010-10** is marked superseded by **HO 04 90 2027-01** for policies effective on or after 2027-01-01. **HO 04 90 2027-01 supersedes HO 04 90 2010-10** for that later interval; the 2010-10 wording remains the applicable edition for an earlier policy ([HO 04 90 2010-10](repo://forms/HO/MS/HO-04-90/2010-10.md#L1-L9), [HO 04 90 2027-01](repo://forms/HO/MS/HO-04-90/2027-01.md#L1-L7)).

The effective date is a selection rule, not permission to assume attachment. The endorsement training requires review of the request, insured, location, policy term, schedules, and complete package; a listed-but-missing endorsement needs correction or a reliable issued copy ([Attaching Endorsements Correctly](repo://training/attaching-endorsements.md#L65-L87), [Attaching Endorsements Correctly](repo://training/attaching-endorsements.md#L201-L215)). The 2027 endorsement itself says it is effective only when attached and forms part of the policy, and separately says that attachment does not create a separate contract ([HO 04 90 2027-01 attachment](repo://forms/HO/MS/HO-04-90/2027-01.md#L16-L36), [HO 04 90 2027-01 contract relationship](repo://forms/HO/MS/HO-04-90/2027-01.md#L55-L60)).

```mermaid
flowchart TD
    A["Line state effective date Declarations and issued package"] --> B["Route to candidate base and state form"]
    B --> C{"Does the edition match the policy date"}
    C -->|"no"| D["Preserve the applicable older frozen edition"]
    C -->|"yes"| E["Verify the candidate edition"]
    D --> E
    E --> F{"Are attachments schedules and referenced pages complete"}
    F -->|"no"| G["Hold interpretation obtain package or escalate"]
    F -->|"yes"| H["Read base form with attached endorsements"]
    H --> I["Apply the applicable state amendatory form"]
    I --> J["Apply bulletin constraints to operations"]
    J --> K["Run manual and appetite controls separately"]
    K --> L["Interpret the assembled contract"]
```

*This flow shows routing, date selection, package completeness, contract composition, state implementation, regulatory administration, and separate internal controls before coverage interpretation.*

### Selection procedure

1. **Identify the transaction.** Record the line, state, policy-effective date, Declarations, issued form labels, complete attachment package, schedules, and referenced pages. Match each endorsement to the named insured, policy term, location, and insured property. If labels conflict, a schedule is blank, or an attachment is missing, preserve the uncertainty and obtain the issued package rather than choosing the wording that produces the preferred result ([Choosing the Governing Edition](repo://training/choosing-the-governing-edition.md#L109-L119), [Attaching Endorsements Correctly](repo://training/attaching-endorsements.md#L65-L107), [Attaching Endorsements Correctly](repo://training/attaching-endorsements.md#L193-L227)).
2. **Select the base edition.** Choose the edition whose effective interval contains the policy-effective date. Do not substitute the current repository file for a superseded edition that governed the policy when written ([HO-3 2018-09](repo://forms/HO/MS/HO-3/2018-09.md#L1-L9), [HO-3 2024-03](repo://forms/HO/MS/HO-3/2024-03.md#L1-L7)).
3. **Select and verify each endorsement.** Match its edition and effective application to the transaction, confirm it is actually attached to the complete issued package, verify any completed schedule, and read the endorsement with the base form and other attachments. Attachment is required before the endorsement’s contract language can be used ([HO 04 90 2010-10](repo://forms/HO/MS/HO-04-90/2010-10.md#L13-L33), [HO 04 90 2027-01](repo://forms/HO/MS/HO-04-90/2027-01.md#L15-L39), [Attaching Endorsements Correctly](repo://training/attaching-endorsements.md#L173-L207)).
4. **Add the state contract overlay.** Read the state form’s scope and precedence terms with the base form and endorsements. Texas HO 01 45 says a conflicting term in its section governs, a nonconflicting term remains applicable, and the amendatory terms do not provide coverage unless expressly provided ([HO 01 45 2022-01](repo://forms/HO/TX/HO-01-45/2022-01.md#L13-L23)).
5. **Apply the regulatory overlay to operations.** For Texas separate windstorm and hail deductibles, B-2021-08 requires clear identification, a stated trigger and calculation basis, policy-consistent application, supporting records, and at least 30 days’ written notice before a windstorm-deductible increase ([B-2021-08](repo://bulletins/TX/b-2021-08-windstorm-deductibles.md#L19-L27), [B-2021-08](repo://bulletins/TX/b-2021-08-windstorm-deductibles.md#L47-L71), [B-2021-08](repo://bulletins/TX/b-2021-08-windstorm-deductibles.md#L153-L171)).
6. **Run internal controls separately.** Before binding or renewing, apply delegated authority and referral rules, document the decision, and review every requested endorsement. Rule 400 requires supported, eligible, correctly matched attachments and referral for incomplete or conflicting information; it does not change the selected form’s coverage ([manual Rules 100.C-100.E](repo://manuals/underwriting/manual.md#L27-L43), [manual Rule 400](repo://manuals/underwriting/manual.md#L5089-L5129)).

## Conflict resolution and document precedence

When documents overlap, resolve the relationship from the acting document’s operative language, not from a title, memorandum, or preferred outcome. **HO 04 90 2027-01 modifies HO-3 2024-03** within its attached scope: W.4 makes the endorsement control a conflict, W.5 applies the policy terms that it does not change, and W.6 confirms that it supplies no coverage beyond the endorsement and policy. Read the endorsement and base provision together, then give effect only to the stated write-back ([HO 04 90 2027-01](repo://forms/HO/MS/HO-04-90/2027-01.md#L16-L36), [HO-3 2024-03 water exclusions](repo://forms/HO/MS/HO-3/2024-03.md#L591-L601)).

For Texas, **HO 01 45 2022-01 modifies the applicable HO-3 contract** only within the matters it addresses: T.2 gives its conflicting term precedence, T.3 reads compatible provisions together, and T.4 does not provide coverage unless expressly stated. It therefore preserves nonconflicting HO-3 and attached-endorsement terms rather than replacing the entire policy ([HO 01 45 2022-01](repo://forms/HO/TX/HO-01-45/2022-01.md#L13-L23), [HO-3 2024-03 agreement](repo://forms/HO/MS/HO-3/2024-03.md#L15-L39)). **HO 01 45 2022-01 implements Texas Bulletin B-2021-08** through its contractual windstorm-and-hail deductible, while the bulletin constrains disclosure and administration; neither document silently supplies a term missing from the other ([HO 01 45 deductible](repo://forms/HO/TX/HO-01-45/2022-01.md#L59-L91), [B-2021-08 requirements](repo://bulletins/TX/b-2021-08-windstorm-deductibles.md#L47-L73)).

For multiple endorsements, compare the complete package’s operative grants, exclusions, definitions, conditions, limits, deductibles, schedules, and effective dates. Do not stack or choose the broader wording merely because several forms address the same subject. Resolve duplicate or unsupported attachments through the approved correction process; if the operative language cannot be reasonably reconciled, escalate before making a final coverage conclusion ([Attaching Endorsements Correctly](repo://training/attaching-endorsements.md#L173-L215), [Attaching Endorsements Correctly](repo://training/attaching-endorsements.md#L501-L517), [Manual Rule 400.Z-400.AB](repo://manuals/underwriting/manual.md#L5241-L5257)). **Manual Rule 400 constrains** whether an endorsement may attach, but it does not resolve a contract conflict or alter the issued form ([Manual Rule 100.B-100.D](repo://manuals/underwriting/manual.md#L21-L37), [Manual Rule 400.A-400.G](repo://manuals/underwriting/manual.md#L5091-L5131)).

## How contract documents compose

### Base form and water-backup endorsement

The base form’s exclusion is the starting point. HO-3 2018-09 excludes water or waterborne material backing up through sewers, drains, or sumps and sump discharge or overflow in A.12 ([HO-3 2018-09 I.A A.12](repo://forms/HO/MS/HO-3/2018-09.md#L109-L111)). HO-3 2024-03 excludes flood and surface water and separately excludes sewer, drain, and sump water in X.7-X.9, while X.8 identifies an attached water-backup endorsement as the exception ([HO-3 2024-03 X.7-X.9](repo://forms/HO/MS/HO-3/2024-03.md#L593-L597)). **HO 04 90 2027-01 writes back HO-3 2024-03 X.8-X.9** for direct physical loss caused by Water Backup or Sump Discharge or Overflow, subject to its terms and $10,000 limit; it **preserves HO-3 2024-03 exclusions** outside that stated scope. The endorsement itself excludes flood and surface water and does not establish a separate contract ([HO 04 90 2027-01 W.0-W.5](repo://forms/HO/MS/HO-04-90/2027-01.md#L16-L36), [HO 04 90 2027-01 W.12-W.13](repo://forms/HO/MS/HO-04-90/2027-01.md#L55-L60), [HO 04 90 2027-01 coverage and exclusions](repo://forms/HO/MS/HO-04-90/2027-01.md#L256-L282), [HO-3 2024-03 X.7-X.9](repo://forms/HO/MS/HO-3/2024-03.md#L593-L597)).

The 2010-10 endorsement has the same assembly boundary: it is attached to and forms part of the policy, changes policy provisions only as expressly stated, and preserves other exclusions. Its water-backup limit is $5,000 and its endorsement deductible is $500 ([HO 04 90 2010-10 W.0-W.1](repo://forms/HO/MS/HO-04-90/2010-10.md#L15-L33), [HO 04 90 2010-10 limit](repo://forms/HO/MS/HO-04-90/2010-10.md#L107-L113), [HO 04 90 2010-10 deductible](repo://forms/HO/MS/HO-04-90/2010-10.md#L157-L167)). **HO 04 90 2027-01 modifies the endorsement’s limit and deductible relative to HO 04 90 2010-10** to $10,000 and $1,000, but that comparison does not backdate the 2027 amounts to a policy carrying 2010-10 ([HO 04 90 2027-01 metadata](repo://forms/HO/MS/HO-04-90/2027-01.md#L1-L7), [HO 04 90 2027-01 limit](repo://forms/HO/MS/HO-04-90/2027-01.md#L256-L265), [HO 04 90 2027-01 deductible](repo://forms/HO/MS/HO-04-90/2027-01.md#L391-L407), [HO 04 90 2010-10 metadata](repo://forms/HO/MS/HO-04-90/2010-10.md#L1-L9)).

### Texas amendatory form and bulletin

A state form and a regulator bulletin are complementary but different. **HO 01 45 Texas 2022-01 implements Texas Bulletin B-2021-08** through a separate Windstorm and Hail Deductible shown in the Declarations, a 1%–10% contractual range, an applicable-limit calculation, and mixed-cause provisions ([HO 01 45 T.1-T.16](repo://forms/HO/TX/HO-01-45/2022-01.md#L59-L91), [B-2021-08 B.2.1-B.2.10](repo://bulletins/TX/b-2021-08-windstorm-deductibles.md#L47-L71)). **B-2021-08 constrains HO 01 45 and related policy communications** by requiring clear disclosure at application, issuance, and renewal, consistent records, policy-based claim application, and at least 30 days’ notice before a windstorm-deductible increase ([B-2021-08 B.1.3-B.1.6](repo://bulletins/TX/b-2021-08-windstorm-deductibles.md#L19-L27), [B-2021-08 B.3.9-B.3.18](repo://bulletins/TX/b-2021-08-windstorm-deductibles.md#L153-L171), [HO 01 45 T.1-T.5](repo://forms/HO/TX/HO-01-45/2022-01.md#L59-L71)). The bulletin’s regulatory thresholds must not be silently substituted for the contractual terms in the attached form.

### Memoranda, training, and internal guidance

The filing memorandum for HO-3 2018-09 describes revision reasons such as clarifying coverage conditions, exclusions, exceptions, valuation, deductibles, and insured responsibilities. It is interpretation, not a second policy form; the 2018 filed wording supplies the operative result ([HO-3 2018-09 memorandum](repo://memoranda/HO-3-2018-09.md#L13-L99), [HO-3 2018-09 form](repo://forms/HO/MS/HO-3/2018-09.md#L13-L39)). The HO-3 2024-03 memorandum likewise explains deductible wording and multi-cause handling, but the filed 2024-03 form remains the authority ([HO-3 2024-03 memorandum](repo://memoranda/HO-3-2024-03.md#L23-L31), [HO-3 2024-03 form](repo://forms/HO/MS/HO-3/2024-03.md#L15-L39)). The HO 04 90 2027-01 memorandum similarly explains changes made for clarity, organization, terminology, and deductible wording; it does not replace the 2027 endorsement’s coverage, limit, deductible, or exclusions ([HO 04 90 memorandum](repo://memoranda/HO-04-90-2027-01.md#L13-L31), [HO 04 90 2027-01](repo://forms/HO/MS/HO-04-90/2027-01.md#L41-L81)).

Training supports the review method: read the complete endorsement, compare it with the request and policy package, and escalate missing or conflicting material. It does not establish a live policy’s coverage ([Attaching Endorsements Correctly](repo://training/attaching-endorsements.md#L15-L23), [Choosing the Governing Edition](repo://training/choosing-the-governing-edition.md#L35-L49)). The appetite guide and manual operate before binding. **Manual Rule 400 constrains endorsement attachment** by requiring supported, eligible, correctly matched, complete, and intent-consistent requests; **the manual preserves the boundary that carrier-issued terms determine coverage** ([manual Rules 100.B-100.E](repo://manuals/underwriting/manual.md#L21-L43), [manual Rule 400.A-400.G](repo://manuals/underwriting/manual.md#L5091-L5129), [HO 04 90 2027-01](repo://forms/HO/MS/HO-04-90/2027-01.md#L15-L39)). For Texas, Rule 510 adds internal authority and risk controls: Coverage A up to $800,000 may be within line-underwriter authority, amounts through $1,200,000 require senior referral, water-backup limits over $25,000 require referral, a 15-year roof inspection is required, and the Texas address must be verified. These are not hidden policy limits ([manual Rule 510](repo://manuals/underwriting/manual.md#L6227-L6263)).

## Worked assemblies

These examples assume the listed forms are actually issued and attached. They demonstrate the selection method, not a substitute for the policy record.

### Texas HO-3 policy effective 2023-06-01

- **Base:** HO-3 2018-09, because the policy date precedes the 2024-03 boundary. **HO-3 2024-03 supersedes HO-3 2018-09** only for its later interval ([HO-3 2018-09](repo://forms/HO/MS/HO-3/2018-09.md#L1-L9), [HO-3 2024-03](repo://forms/HO/MS/HO-3/2024-03.md#L1-L7)).
- **Water backup:** HO 04 90 2010-10, because 2027-01 is not the applicable endorsement interval. **HO 04 90 2010-10 modifies the HO-3 2018-09 water exclusions** for its stated coverage and preserves policy exclusions not changed by the endorsement; use its $5,000 limit and $500 deductible ([HO-3 2018-09 A.12](repo://forms/HO/MS/HO-3/2018-09.md#L109-L111), [HO 04 90 2010-10](repo://forms/HO/MS/HO-04-90/2010-10.md#L15-L33), [HO 04 90 2010-10 limit](repo://forms/HO/MS/HO-04-90/2010-10.md#L107-L113), [HO 04 90 2010-10 deductible](repo://forms/HO/MS/HO-04-90/2010-10.md#L157-L167)).
- **Texas overlay:** HO 01 45 2022-01, if attached, implements the Texas bulletin’s separate-deductible requirements. The bulletin constrains disclosure and administration but does not replace the form’s contractual wording ([HO 01 45](repo://forms/HO/TX/HO-01-45/2022-01.md#L59-L91), [B-2021-08](repo://bulletins/TX/b-2021-08-windstorm-deductibles.md#L19-L27)).
- **Pre-bind boundary:** the appetite guide and Rules 400 and 510 constrain eligibility, authority, referral, and attachment; they do not modify the HO-3 or HO 04 90 coverage terms ([Texas appetite guide](repo://guidelines/appetite/tx-homeowners.md#L13-L35), [manual Rule 400](repo://manuals/underwriting/manual.md#L5089-L5129), [manual Rule 510](repo://manuals/underwriting/manual.md#L6227-L6263)).

### Texas HO-3 policy effective 2027-02-01

- **Base:** HO-3 2024-03. **HO-3 2024-03 supersedes HO-3 2018-09** for this effective period; do not carry forward the older base wording ([HO-3 2024-03](repo://forms/HO/MS/HO-3/2024-03.md#L1-L7), [HO-3 2018-09 supersession](repo://forms/HO/MS/HO-3/2018-09.md#L8-L9)).
- **Water backup:** HO 04 90 2027-01, if attached. **HO 04 90 2027-01 writes back HO-3 2024-03 X.8-X.9** for the stated water-backup and sump events, preserves unmodified policy terms, and supplies the $10,000 limit and $1,000 deductible ([HO-3 2024-03 X.7-X.9](repo://forms/HO/MS/HO-3/2024-03.md#L593-L597), [HO 04 90 2027-01 attachment and scope](repo://forms/HO/MS/HO-04-90/2027-01.md#L16-L36), [HO 04 90 2027-01 limit](repo://forms/HO/MS/HO-04-90/2027-01.md#L256-L265), [HO 04 90 2027-01 deductible](repo://forms/HO/MS/HO-04-90/2027-01.md#L391-L407)).
- **Texas overlay and operations:** HO 01 45 2022-01 implements the state contract mechanism, B-2021-08 constrains disclosure and administration, and current internal guidance constrains binding and attachment. These layers remain distinct ([HO 01 45](repo://forms/HO/TX/HO-01-45/2022-01.md#L13-L23), [B-2021-08](repo://bulletins/TX/b-2021-08-windstorm-deductibles.md#L153-L171), [manual Rule 400](repo://manuals/underwriting/manual.md#L5091-L5129)).

## Failure checks

- **Wrong edition:** a quote, renewal, or claim file uses HO-3 2024-03 for a policy effective before 2024-03-01, or HO 04 90 2027-01 before 2027-01-01. Re-select by the transaction and preserve the older frozen edition ([README](repo://README.md#L35-L37), [Choosing the Governing Edition](repo://training/choosing-the-governing-edition.md#L251-L265)).
- **Unattached write-back:** someone applies HO 04 90 coverage because the title or schedule appears in a system, without confirming the endorsement is attached. Obtain the complete issued package; the endorsement’s attachment is part of its contract boundary ([Attaching Endorsements Correctly](repo://training/attaching-endorsements.md#L81-L87), [HO 04 90 2027-01](repo://forms/HO/MS/HO-04-90/2027-01.md#L15-L39)).
- **Authority inversion:** an adjuster or underwriter uses a bulletin, memorandum, training page, appetite guide, or manual as though it changes the contract. Return to the applicable issued form and endorsement; use the other document for its regulatory, interpretive, or internal function ([Guidance Versus Contract Language](repo://training/guidance-versus-contract.md#L73-L83), [manual Rule 100.D](repo://manuals/underwriting/manual.md#L33-L37)).
- **Regulatory-contract mismatch:** a Texas separate deductible appears in declarations or communications without a supporting policy provision, trigger, calculation basis, and record. B-2021-08 requires consistency and prohibits applying a deductible not permitted by the policy ([B-2021-08](repo://bulletins/TX/b-2021-08-windstorm-deductibles.md#L19-L27), [B-2021-08](repo://bulletins/TX/b-2021-08-windstorm-deductibles.md#L63-L89)).

For line-specific editions, continue to [HO-3 forms](/openwiki/coverage/forms/ho-3.md). For state requirements, see [Texas state overlays](/openwiki/state-overlays/texas.md). For internal attachment and referral decisions, see [endorsements and deductibles](/openwiki/underwriting/manual/endorsements-and-deductibles.md) and keep those decisions separate from the contract analysis.
