---
type: coverage
title: Coverage E and F — Liability and Medical Payments
description: Explains HO-3 Section II Coverage E and Coverage F, including the defense and medical-payments grants, edition-specific triggers, and the business-activity and motor-vehicle/watercraft/aircraft exclusions that limit both coverages.
tags: [homeowners, coverage-e, coverage-f, section-ii, liability, medical-payments]
verified:
  - by: openwiki/0.5.0
    at: 2026-09-12T23:52:37.758Z
sources:
  - id: openwiki-source-0de2907066d0f023c5c2e68b
    resource: repo://forms/HO/MS/HO-04-81/2018-09.md
  - id: openwiki-source-e727058d16eee86c951e380a
    resource: repo://forms/HO/MS/HO-3/2011-05.md
  - id: openwiki-source-f4ebd2ece3eaf490178dfc41
    resource: repo://forms/HO/MS/HO-3/2018-09.md
  - id: openwiki-source-da67a262bebb42780999bd2a
    resource: repo://guidelines/appetite/tx-homeowners.md
  - id: openwiki-source-c7690df4255f266075cd43d2
    resource: repo://guidelines/authority/referral-matrix.md
generated: { by: "openwiki/0.5.0", at: "2026-09-12T23:52:37.758Z" }
---

# Coverage E and F — Liability and Medical Payments

Coverage E and Coverage F belong to **Section II**, not Section I. Read them with the issued HO-3 edition, the Declarations, and any attached endorsements, but keep the analysis separate from property coverage rules such as settlement basis, deductibles, or Section I write-backs unless the form expressly says otherwise.

## Coverage E — Personal Liability

Coverage E responds when a claim is made or a suit is brought against an insured for damages because of bodily injury or property damage caused by an occurrence to which the coverage applies. The insurer’s promise is twofold: it pays, up to the applicable limit of liability, the damages for which an insured is legally liable, and it provides a defense at its expense.

That defense duty is part of the Coverage E grant itself. It is not a Section I property benefit and should be analyzed against the claim or suit, the occurrence definition, and the Section II exclusions.

The payment promise is capped by the limit of liability shown for Coverage E in the Declarations.

## Coverage F — Medical Payments to Others

Coverage F is a separate medical-expense promise. It pays the necessary medical expenses incurred or medically ascertained within three years from the date of an accident causing bodily injury to a person other than an insured.

In the 2018-09 form, Coverage F also requires that the bodily injury arise out of a condition on the insured location or be caused by the activities of an insured. That location-or-activity connection is edition-specific and should not be read into the earlier 2011-05 form.

## Section II exclusions that bound both coverages

### Business activities

Both supplied editions exclude Coverage E and Coverage F for bodily injury or property damage arising out of the business activities of an insured. The 2018-09 form adds a narrow exception for the occasional rental of the residence premises for fewer than 15 days in a policy year. That exception belongs to the Section II exclusion text; it is not a general rental coverage grant.

### Motor vehicle, watercraft, and aircraft

Both supplied editions exclude Coverage E and Coverage F for bodily injury or property damage arising out of the ownership, maintenance, or use of a motor vehicle, watercraft over 25 horsepower, or aircraft.

### Coverage E property damage to insured-owned or insured-rented property

The 2018-09 form adds a Coverage E-only exclusion for property damage to property owned by or rented to an insured. The earlier 2011-05 Section II exclusions end at the motor-vehicle/watercraft/aircraft exclusion.

## Reading sequence

A practical Section II review is:

1. Identify the issued HO-3 edition.
2. Decide whether the demand is for Coverage E or Coverage F.
3. Test the grant requirements for that coverage.
4. Apply the Section II exclusions that the issued form actually contains.
5. Use the Declarations for the applicable limit, and do not import Section I settlement or deductible rules into Section II unless the form expressly does so.

```mermaid
flowchart TD
    A["Identify the issued HO-3 edition"] --> B{"Coverage E or Coverage F?"}
    B -- "Coverage E" --> C["Claim or suit seeks damages because of bodily injury or property damage"]
    C --> D{"Occurrence and no Section II exclusion"}
    D -- "Yes" --> E["Pay damages up to the Coverage E limit and defend at insurer expense"]
    D -- "No" --> X["No Coverage E response"]
    B -- "Coverage F" --> F["Medical expenses for a person other than an insured"]
    F --> G{"Incurred or medically ascertained within three years?"}
    G -- "No" --> X
    G -- "Yes" --> H{"2018-09 only: condition on insured location or insured activity?"}
    H -- "No" --> X
    H -- "Yes" --> I{"No Section II exclusion applies"}
    I -- "Yes" --> J["Pay necessary medical expenses under Coverage F"]
    I -- "No" --> X
```

The diagram separates the liability-defense path from the medical-payments path and keeps the edition-specific Coverage F trigger in the right place. Motor-vehicle, watercraft, aircraft, and business-activity exclusions cut off both paths when they apply.
