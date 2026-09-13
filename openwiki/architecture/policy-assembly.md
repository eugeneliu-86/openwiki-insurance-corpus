---
type: policy assembly concept
title: Policy Assembly and Governing Form Editions
description: Explain how an issued homeowners policy is assembled from the selected HO-3 edition, verified attachments, and state amendatory forms, and how edition supersession controls the governing contract terms.
tags: [homeowners, policy-assembly, endorsements, editions, attachment, supersession, state-amendatory]
verified:
  - by: openwiki/0.5.0
    at: 2026-09-12T23:52:37.758Z
sources:
  - id: openwiki-source-cd26c30cc942869b52618f95
    resource: repo://forms/HO/MS/HO-04-90/2010-10.md
  - id: openwiki-source-36bcf8e9754ce8cd9b63db52
    resource: repo://forms/HO/MS/HO-04-90/2026-01.md
  - id: openwiki-source-e727058d16eee86c951e380a
    resource: repo://forms/HO/MS/HO-3/2011-05.md
  - id: openwiki-source-f4ebd2ece3eaf490178dfc41
    resource: repo://forms/HO/MS/HO-3/2018-09.md
  - id: openwiki-source-ff7de1315ac46ce4dd65d251
    resource: repo://forms/HO/TX/HO-01-45/2022-01.md
  - id: openwiki-source-23775c3de52f3ab95a13cb8b
    resource: repo://README.md
generated: { by: "openwiki/0.5.0", at: "2026-09-12T23:52:37.758Z" }
---

# Policy Assembly and Governing Form Editions

A homeowners policy is assembled in a fixed order: first select the HO-3 base edition from the policy-written date, then verify which endorsements are actually attached, then apply any state amendatory form that is attached and in scope, and only after that analyze the resulting grant, exclusion, deductible, settlement, or condition terms. A repository copy of a form is not evidence that the form is issued or attached.

## Assembly sequence

<!-- openwiki: mermaid parse failed and this diagram was converted to a text fence so it does not break rendering. Fix the diagram source and restore the mermaid fence. Parser error: Parse error on line 9: ...n date Policy->>End: Verify attachme Expecting '+', '-', '()', 'ACTOR', got 'end' -->
```text
sequenceDiagram
    participant Policy as Issued policy record
    participant Base as HO-3 base edition
    participant End as Attached endorsement
    participant State as Attached state amendatory form
    participant Analysis as Coverage analysis

    Policy->>Base: Select edition by written date
    Policy->>End: Verify attachment and exact edition
    Policy->>State: Verify attachment and conflict scope
    Base->>Analysis: Supply base exclusions and duties
    End->>Analysis: Write back or modify named section only
    State->>Analysis: Govern only its stated conflict scope
```

The diagram shows the governing order only. It does not imply that an endorsement or state form exists just because the repository contains a current file for it.

## HO-3 edition governs first

The supplied HO-3 editions are versioned contract authorities. HO-3 2011-05 remains the governing base form for policies written under it, while HO-3 2018-09 is the later base form issued for policies written on or after its own effective date and supersedes the earlier edition for later-written policies. The HO-3 selection is therefore a separate written-date decision that must be made before any endorsement analysis.

## Attachment is a separate factual gate

After the base form is selected, verify the issued policy record for the endorsement or amendatory form itself. Do not infer attachment from the existence of a form in the repository, a bulletin, an underwriting appetite page, or a claim note. For HO 04 90, attachment must be verified independently before its terms are applied, and the attached edition must be identified as either 2010-10 or 2026-01 from the policy-written date. For HO 01 45, the Texas amendatory endorsement attaches to HO-3 and governs only when its own scope and conflict rule are triggered on an issued Texas policy.

## HO 04 90 edition supersession

HO 04 90 is an attachment-dependent write-back to HO-3 Section I Exclusion A.3. The endorsement has its own edition rule: HO 04 90 2010-10 remains in force for policies written under it, even if loss is reported later, and HO 04 90 2026-01 replaces 2010-10 for policies written on or after 2026-01-01. The later edition is not a retroactive patch for the earlier one, and the earlier edition is not automatically displaced for a policy written before the replacement date.

## Scope of the attached terms

Once a specific HO 04 90 edition is verified attached, its W.1 route writes back A.3 for sewer or drain backup and sump-related overflow or discharge, including mechanical breakdown, while W.4 leaves A.1 flood and surface-water exclusions and A.2 subsurface-water exclusions in force. W.5 in both editions independently tests the insured's known, unremedied maintenance failure. The edition then adds its own payment and settlement rules: 2010-10 uses the legacy policy-period sublimit, separate deductible, and Coverage C actual-cash-value settlement rule; 2026-01 uses the later sublimit, separate deductible, the new below-grade backflow-prevention gate, and the later settlement numbering. These are contract terms, not underwriting thresholds.

## State amendatory scope

Texas HO 01 45 is a state amendatory endorsement with its own effective-date and conflict rule. It applies to HO-3 policies with an effective date on or after 2022-01-01 and governs where it conflicts with the form to which it attaches. Its windstorm-and-hail deductible provisions are regulatory contract changes for Texas policies, not HO 04 90 sublimits or attachment evidence.

## Governing terms and failure modes

The governing contract terms come from the combination of the selected HO-3 edition, the actually attached endorsement edition, and any attached state amendatory form within its stated scope. If the attachment record is missing, the edition cannot be dated, or an amendatory form's conflict scope is not established, coverage analysis must stop at the unresolved factual issue rather than assuming the current repository form controls.

## Practical checklist

1. Identify the policy-written date.
2. Select the correct HO-3 edition.
3. Verify which endorsements are actually attached.
4. Select the attached HO 04 90 edition separately from the HO-3 edition.
5. Apply any attached state amendatory form only within its stated scope and conflict rule.
6. Analyze coverage, exclusions, limits, deductibles, and settlement only after those governing forms are fixed.

## Focused validation points

- A later form file in the repository does not by itself govern an earlier policy.
- HO 04 90 attachment must be verified before using its A.3 write-back, W.4 retained exclusions, W.5 maintenance condition, or edition-specific payment terms.
- HO 04 90 2010-10 and 2026-01 are separate governing editions, selected by policy-written date after attachment is proved.
- A Texas amendatory form can change HO-3 terms only within its own conflict scope; it does not establish coverage by itself.
- Coverage analysis for water backup, settlement, and deductible issues must use the issued base form and the verified attached endorsement edition, not the existence of a current source file.
