---
type: "Reference"
title: "Coverage Wiki Quickstart"
openwiki_generated: true
verified:
  - by: openwiki/0.6.1
    at: 2026-10-02T02:44:58.116Z
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
  - id: openwiki-source-0de2907066d0f023c5c2e68b
    resource: repo://forms/HO/MS/HO-04-81/2018-09.md
  - id: openwiki-source-65c1bab72aeee4cf69ba7892
    resource: repo://forms/HO/MS/HO-04-81/2026-09.md
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
generated: { by: "openwiki/0.6.1", at: "2026-10-02T02:44:58.116Z" }
---


# Coverage Wiki Quickstart

<!-- openwiki: broken internal link [README.md#L15-L27] file "README.md" does not exist. Fix the href or restore the target, then delete this comment. -->
<!-- openwiki: broken internal link [training/guidance-versus-contract.md#L61-L83] file "training/guidance-versus-contract.md" does not exist. Fix the href or restore the target, then delete this comment. -->
This is a compact task-routing map, not a substitute for an issued policy, endorsement, state form, claims procedure, or applicable law. Forms and attached endorsements supply contract wording; claims pages and manuals provide operational guidance. A memorandum or training page can explain a change or review method, but cannot create, expand, restrict, or waive coverage ([document roles](README.md#L15-L27), [guidance boundary](training/guidance-versus-contract.md#L61-L83)).

When documents are combined, name the relationship: an endorsement **modifies** or **writes back** a base provision; a later edition **supersedes** an earlier edition for its stated policies; a state form **implements** a bulletin; and guidance **constrains** internal operations. Do not treat a limit, endorsement title, or claims instruction as a coverage grant.

## Required route

```mermaid
flowchart TD
    q["Loss or coverage question"] --> identify["Identify line, state, and effective date"]
    identify --> record["Check declarations and every attached endorsement"]
    record --> edition["Select the issued base and endorsement editions"]
    edition --> subject["Trace cause, property, and coverage subject"]
    subject --> wording["Read the governing contract wording"]
    wording --> route{"Operational follow-up"}
    route --> coverage["Coverage brief"]
    route --> claims["Claims guidance"]
    coverage --> verify["Recheck exclusions, limits, and evidence"]
    claims --> verify
```

1. Identify the line and state.
2. Confirm the policy-effective or renewal date and retrieve the issued base form.
3. Read declarations, schedules, and the complete attachment package.
4. Select the coverage part and damaged interest; establish the reported cause and sequence.
5. Read the applicable form and endorsement before consulting claims guidance.
6. Keep coverage, causation, scope and valuation, payment authority, and recovery as separate work products.

<!-- openwiki: broken internal link [README.md#L15-L31] file "README.md" does not exist. Fix the href or restore the target, then delete this comment. -->
<!-- openwiki: broken internal link [README.md#L33-L41] file "README.md" does not exist. Fix the href or restore the target, then delete this comment. -->
The repository path is load-bearing: it carries line, state, form, and edition context that a claim record does not carry ([repository layout](README.md#L15-L31)). Frozen forms remain available by edition; an older form continues to govern policies written under it, while guidelines and manuals are living operational material ([source lifecycle](README.md#L33-L41)). Use [Editions, Endorsements, and State Attachments](policy-assembly/editions-and-state-attachments.md) when the policy record is incomplete or documents must be composed.

## Fungi, mold, and water route

For a plumbing, appliance, seepage, flood, roof-entry, or microbial question, start with the two coverage briefs:

- [Water Damage](coverage/perils/water-damage.md) — trace the source and entry path, distinguish sudden discharge from repeated seepage, flood, external water, backup, freezing, and roof entry, then separate the failed source component from resulting damage.
- [Fungi, Wet or Dry Rot, and Bacteria](coverage/perils/fungi-and-bacteria.md) — apply the covered-cause-first prerequisite, preserved exclusions, remediation boundaries, and edition-specific aggregate.

<!-- openwiki: broken internal link [../forms/HO/MS/HO-04-81/2018-09.md#L8-L12] heading anchor "L8-L12" does not exist in "../forms/HO/MS/HO-04-81/2018-09.md". Fix the href or restore the target, then delete this comment. -->
<!-- openwiki: broken internal link [../forms/HO/MS/HO-04-81/2026-09.md#L1-L7] heading anchor "L1-L7" does not exist in "../forms/HO/MS/HO-04-81/2026-09.md". Fix the href or restore the target, then delete this comment. -->
<!-- openwiki: broken internal link [../forms/HO/MS/HO-04-81/2026-09.md#L23-L33] heading anchor "L23-L33" does not exist in "../forms/HO/MS/HO-04-81/2026-09.md". Fix the href or restore the target, then delete this comment. -->
HO 04 81 is an attached multistate endorsement to HO-3, not a stand-alone mold policy. The 2018-09 form remains applicable to policies written under that edition, including later-reported losses; its aggregate is $10,000. The 2026-09 edition applies to policies written or renewed on or after 2026-10-01, replaces 2018-09 for those policies, and raises the aggregate to $25,000. The 2026 edition states that other provisions are unchanged; do not infer a broader coverage result from the changed limit ([2018-09 supersession notice](../forms/HO/MS/HO-04-81/2018-09.md#L8-L12), [2026-09 applicability and change](../forms/HO/MS/HO-04-81/2026-09.md#L1-L7), [2026-09 limit](../forms/HO/MS/HO-04-81/2026-09.md#L23-L33)).

<!-- openwiki: broken internal link [../forms/HO/MS/HO-04-81/2018-09.md#L49-L67] heading anchor "L49-L67" does not exist in "../forms/HO/MS/HO-04-81/2018-09.md". Fix the href or restore the target, then delete this comment. -->
<!-- openwiki: broken internal link [../forms/HO/MS/HO-04-81/2026-09.md#L9-L21] heading anchor "L9-L21" does not exist in "../forms/HO/MS/HO-04-81/2026-09.md". Fix the href or restore the target, then delete this comment. -->
Both editions require fungi-related direct physical loss to covered property to result from a covered cause that occurred first. Both retain limitations for fungi arising from constant or repeated seepage or leakage and from flood. The endorsement does not turn an excluded water event into covered fungi loss; establish the water cause and the base-form grant or exclusion first ([2018 coverage sequence and exclusions](../forms/HO/MS/HO-04-81/2018-09.md#L49-L67), [2026 coverage sequence and exclusions](../forms/HO/MS/HO-04-81/2026-09.md#L9-L21)).

## Claims follow-up

After the contract route, use the operational pages:

- [Water Loss Handling](claims/guidelines/water-loss-handling.md) — source and movement, mitigation, evidence, coverage consultation, limits, escalation, payment, and closure.
- [Mold Claim Handling](claims/guidelines/mold-claim-handling.md) — moisture causation, microbial evidence, mitigation and remediation, coverage consultation, and closure.

<!-- openwiki: broken internal link [manuals/claims/manual.md#L13-L19] file "manuals/claims/manual.md" does not exist. Fix the href or restore the target, then delete this comment. -->
<!-- openwiki: broken internal link [forms/HO/MS/HO-04-81/2018-09.md#L35-L45] file "forms/HO/MS/HO-04-81/2018-09.md" does not exist. Fix the href or restore the target, then delete this comment. -->
Investigation, inspection, testing, mitigation, vendor assignment, or a remediation invoice does not itself establish coverage. Preserve failed parts, photographs, invoices, reports, timing, and repair findings where possible; separate emergency protection from permanent repair. Apply claims guidance only after checking the issued policy, attached endorsement, declarations, and applicable edition. The claims manual controls file handling and delegated authority, not contract interpretation ([claims manual boundary](manuals/claims/manual.md#L13-L19), [HO 04 81 investigation and cooperation](forms/HO/MS/HO-04-81/2018-09.md#L35-L45)).

## Final evidence check

Before publishing a position, confirm:

- line, state, effective date, declarations, and attachment status;
- governing base and endorsement editions, including superseded editions that still govern older policies;
- water source, movement, timing, covered property, and direct versus resulting damage;
- the acting grant, exclusion, write-back, limit, deductible, and settlement terms;
- the contract-versus-guidance boundary; and
- unresolved causation, attachment, valuation, authority, or evidence issues are escalated rather than guessed.

Use narrow canonical evidence citations such as `repo://forms/HO/MS/HO-04-81/2026-09.md#L23-L33` in research and review. The quickstart routes the work; the issued form and complete policy record decide the contract result.
