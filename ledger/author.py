"""Author the fact ledger. Corpus expansion ph. 01 §4.

This file IS the design: which documents exist, which concepts a question can
be about, what every value is in every line, edition and state, where each
fact is planted, which references form chains, which documents misstate what.
Scripts expand the repetitive parts (a concept across eight states, two
editions of a form) so that ~1,000 facts are a few hundred lines of tables.

    uv run python -m ledger.author          # writes ledger/data/*.yaml, then loads and reports

Nothing here is prose. The values are invented and ISO-shaped (ov. X1).
"""
from __future__ import annotations

import pathlib
import sys

from .schema import (Composition, Concept, Contradiction, Definition, Document, EditionDiff, Fact, FactValue,
                     History, HistoryEntry, Ledger, Reference, Section, dump)

OUT = pathlib.Path(__file__).resolve().parent / "data"

# ---------------------------------------------------------------------------
# Concepts. (id, kind, canonical, synonyms, group, ambiguous)
# ---------------------------------------------------------------------------
CONCEPTS = [
    # coverage limits
    ("cov-b-limit-pct", "percent", "Coverage B limit as a percentage of Coverage A", ["other structures limit", "appurtenant structures percentage", "Coverage B percentage"], "limits", True),
    ("cov-c-limit-pct", "percent", "Coverage C limit as a percentage of Coverage A", ["personal property limit percentage", "contents limit percentage", "Coverage C percentage"], "limits", True),
    ("cov-d-limit-pct", "percent", "Coverage D limit as a percentage of Coverage A", ["loss of use limit", "additional living expense limit", "ALE percentage"], "limits", True),
    ("cov-a-unit-owner-default", "money", "default Coverage A limit for a unit owner", ["built-in unit coverage", "condominium dwelling default limit"], "limits", False),
    ("special-limit-money", "money", "special limit on money and precious metals", ["cash sublimit", "currency and bullion limit", "money limit"], "special-limits", False),
    ("special-limit-jewelry", "money", "special limit on theft of jewelry, watches and precious stones", ["jewelry theft sublimit", "jewelry and watches limit", "precious stones theft limit"], "special-limits", True),
    ("special-limit-firearms", "money", "special limit on theft of firearms", ["firearms theft sublimit", "guns limit", "firearm theft cap"], "special-limits", False),
    ("special-limit-watercraft", "money", "special limit on watercraft including trailers", ["boats and trailers limit", "watercraft sublimit", "small craft limit"], "special-limits", False),
    ("special-limit-silverware", "money", "special limit on theft of silverware", ["silverware theft sublimit", "flatware and goldware limit"], "special-limits", False),
    ("special-limit-business-property", "money", "special limit on business property on the residence premises", ["home business contents limit", "business property sublimit", "on-premises business property cap"], "special-limits", True),
    ("special-limit-electronics-vehicle", "money", "special limit on electronic apparatus in a motor vehicle", ["in-vehicle electronics limit", "car electronics sublimit"], "special-limits", False),
    # additional coverages
    ("debris-removal-pct", "percent", "debris removal additional percentage", ["rubble removal percentage", "debris removal additional amount", "clean-up allowance percentage"], "additional", True),
    ("trees-shrubs-limit-pct", "percent", "trees, shrubs and plants limit as a percentage of Coverage A", ["landscaping limit percentage", "plants and shrubs percentage"], "additional", False),
    ("trees-per-item-limit", "money", "limit for any one tree, shrub or plant", ["per-tree limit", "single plant limit", "per-item landscaping limit"], "additional", False),
    ("fire-department-charge", "money", "fire department service charge limit", ["fire service charge coverage", "fire department call fee", "fire response charge"], "additional", True),
    ("credit-card-forgery-limit", "money", "credit card, fund transfer card and forgery limit", ["card and forgery limit", "counterfeit money coverage limit"], "additional", False),
    ("loss-assessment-limit", "money", "loss assessment additional coverage limit", ["association assessment limit", "assessment coverage limit", "special assessment limit"], "additional", True),
    ("ordinance-law-pct", "percent", "ordinance or law coverage as a percentage of Coverage A", ["code upgrade percentage", "building code coverage percentage", "ordinance or law additional amount"], "additional", True),
    ("landlord-furnishings-limit", "money", "landlord's furnishings limit", ["rented unit furnishings limit", "landlord contents sublimit"], "additional", False),
    ("grave-markers-limit", "money", "grave markers limit", ["mausoleum and marker limit", "headstone coverage limit"], "additional", False),
    ("refrigerated-property-limit", "money", "refrigerated property limit", ["food spoilage limit", "frozen food coverage limit"], "additional", False),
    ("insured-to-value-pct", "percent", "insured-to-value threshold for replacement cost settlement", ["eighty percent condition", "coinsurance threshold", "replacement cost threshold percentage"], "settlement", True),
    # deductibles and wind
    ("section-i-deductible-min", "money", "minimum Section I deductible", ["all-other-perils deductible minimum", "AOP deductible floor", "base deductible minimum"], "deductibles", True),
    ("wind-hail-deductible-min-pct", "percent", "minimum windstorm and hail deductible percentage", ["named storm deductible minimum", "hurricane deductible floor", "wind percentage deductible minimum"], "deductibles", True),
    ("wind-hail-deductible-max-pct", "percent", "maximum windstorm and hail deductible percentage", ["hurricane deductible cap", "wind deductible ceiling", "maximum named storm deductible"], "deductibles", True),
    ("wind-seacoast-max-pct", "percent", "maximum windstorm deductible in seacoast territories", ["coastal territory wind maximum", "tier one county wind cap", "seacoast deductible ceiling"], "deductibles", False),
    ("wind-deductible-notice-days", "days", "notice before a windstorm deductible increase takes effect", ["deductible increase notice period", "advance notice of deductible change", "renewal deductible notice"], "deductibles", True),
    ("named-storm-period-hours", "hours", "hours after a named storm designation ends that the named storm period lasts", ["named storm window", "hurricane occurrence tail", "storm period duration"], "deductibles", False),
    # conditions
    ("proof-of-loss-days", "days", "days to submit a signed, sworn proof of loss", ["sworn statement deadline", "proof of loss period", "sworn proof deadline"], "conditions", True),
    ("suit-limitation-years", "years", "years within which an action against the insurer must be brought", ["time to bring action", "suit against us period", "legal action deadline"], "conditions", True),
    ("loss-payment-days", "days", "days after agreement within which loss is payable", ["payment after agreement period", "claim payment deadline", "loss payable period"], "conditions", False),
    ("cancellation-notice-nonpay-days", "days", "notice of cancellation for nonpayment of premium", ["nonpayment cancellation notice", "premium default notice period", "notice for nonpayment"], "conditions", True),
    ("cancellation-notice-other-days", "days", "notice of cancellation for reasons other than nonpayment", ["cancellation notice period", "notice of cancellation for other reasons", "general cancellation notice"], "conditions", True),
    ("nonrenewal-notice-days", "days", "notice of nonrenewal", ["nonrenewal notice period", "notice of intent not to renew", "renewal refusal notice"], "conditions", True),
    ("appraisal-demand-days", "days", "days to select an appraiser after a demand for appraisal", ["appraiser selection period", "appraisal response time"], "conditions", False),
    ("vacancy-days", "days", "consecutive days of vacancy after which vandalism is excluded", ["unoccupancy limit", "vacant dwelling period", "vacancy exclusion trigger"], "conditions", True),
    ("claim-acknowledgement-days", "days", "days to acknowledge receipt of a claim", ["acknowledgment of claim deadline", "receipt acknowledgement period", "claim contact deadline"], "claims-handling", True),
    ("claim-decision-business-days", "business-days", "business days to accept or reject a claim after receiving requested items", ["accept or deny deadline", "coverage decision period", "claim determination window"], "claims-handling", True),
    ("claim-payment-business-days", "business-days", "business days to pay an accepted claim", ["prompt payment period", "payment after acceptance deadline", "claim disbursement window"], "claims-handling", False),
    # liability
    ("medical-payments-years", "years", "years within which medical expenses must be incurred to be payable", ["medical payments time limit", "Coverage F accrual period", "medical expense window"], "liability", False),
    ("damage-to-property-of-others-limit", "money", "damage to property of others limit", ["property of others limit", "good neighbor coverage limit", "borrowed property limit"], "liability", False),
    ("watercraft-hp-threshold", "horsepower", "outboard horsepower above which watercraft liability is excluded", ["outboard horsepower exclusion threshold", "motor size limit for watercraft", "outboard motor threshold"], "liability", True),
    ("watercraft-length-threshold", "feet", "sailing vessel length above which liability is excluded", ["sailboat length threshold", "sailing vessel size limit"], "liability", False),
    ("rental-days-exception", "days", "days of occasional rental permitted without the business exclusion applying", ["short-term rental allowance", "occasional rental exception", "rental day allowance"], "liability", False),
    # endorsements
    ("water-backup-sublimit", "money", "water backup and sump overflow sublimit", ["sewer backup limit", "backup and sump overflow limit", "drain backup sublimit"], "endorsements", True),
    ("water-backup-deductible", "money", "water backup endorsement deductible", ["backup endorsement deductible", "sump overflow deductible", "sewer backup deductible"], "endorsements", False),
    ("backflow-requirement", "boolean", "backwater valve requirement for finished areas below grade", ["backflow preventer condition", "check valve requirement", "backwater device condition"], "endorsements", False),
    ("roof-acv-age-threshold-years", "years", "roof age from which the actual cash value roof schedule applies", ["roof schedule trigger age", "roof surfacing age threshold", "ACV roof age"], "roof", True),
    ("roof-min-payment-pct", "percent", "minimum payable percentage of roof surfacing replacement cost", ["roof settlement floor", "minimum roof payment percentage", "roof payment floor"], "roof", False),
    ("roof-comp-shingle-20yr-pct", "percent", "payable percentage for composition shingle aged twenty years or more", ["asphalt shingle depreciation floor", "twenty-year shingle percentage"], "roof", False),
    ("fungi-limit", "money", "fungi, wet or dry rot, or bacteria aggregate limit", ["mold coverage limit", "fungi and bacteria aggregate", "microbial remediation limit"], "endorsements", True),
    ("earthquake-deductible-pct", "percent", "earthquake deductible percentage", ["seismic deductible", "earth movement deductible percentage", "quake deductible"], "endorsements", False),
    ("identity-fraud-limit", "money", "identity fraud expense limit", ["identity theft expense limit", "identity recovery coverage limit"], "endorsements", False),
    ("scheduled-property-deductible", "money", "deductible applying to scheduled personal property", ["scheduled items deductible", "floater deductible"], "endorsements", False),
    ("extended-replacement-pct", "percent", "specified additional amount of insurance for Coverage A", ["extended replacement cost percentage", "additional amount percentage", "dwelling extension percentage"], "endorsements", False),
    ("loss-assessment-endorsement-limit", "money", "loss assessment endorsement limit", ["increased assessment limit", "assessment endorsement amount"], "endorsements", False),
    ("business-pursuits-limit", "money", "business pursuits liability sublimit", ["incidental business liability limit"], "endorsements", False),
    # underwriting, rating, claims
    ("roof-inspection-age-years", "years", "roof age at or above which an inspection is required before binding", ["inspection trigger roof age", "roof survey age", "roof inspection threshold"], "underwriting", True),
    ("roof-max-age-years", "years", "roof age at or above which the risk is outside appetite", ["maximum insurable roof age", "roof age declination point", "roof age ceiling"], "underwriting", True),
    ("prior-claims-referral-count", "count", "number of paid property claims that triggers referral", ["claims frequency referral trigger", "loss count threshold", "prior loss referral count"], "underwriting", True),
    ("prior-claims-lookback-years", "years", "years of loss history considered", ["loss history window", "claims lookback", "prior loss period"], "underwriting", False),
    ("line-authority-cov-a", "money", "line underwriter Coverage A binding authority", ["binding authority limit", "underwriter authority ceiling", "line authority"], "underwriting", True),
    ("senior-authority-cov-a", "money", "senior underwriter Coverage A binding authority", ["senior binding authority", "senior underwriter ceiling"], "underwriting", False),
    ("water-backup-referral-limit", "money", "water backup limit above which referral is required", ["backup limit needing referral", "backup referral threshold"], "underwriting", False),
    ("protection-class-max", "count", "maximum protection class written", ["maximum protection class", "PPC eligibility limit", "protection class cutoff"], "underwriting", False),
    ("min-cov-a", "money", "minimum Coverage A limit written", ["minimum dwelling limit", "Coverage A floor"], "underwriting", False),
    ("max-cov-a", "money", "maximum Coverage A limit written", ["maximum dwelling limit", "Coverage A ceiling"], "underwriting", False),
    ("referral-loss-threshold", "money", "claim amount above which a loss is referred", ["large loss referral threshold", "adjuster authority limit", "loss referral amount"], "claims-handling", True),
    ("reservation-of-rights-days", "days", "days within which a reservation of rights letter must issue", ["ROR letter deadline", "rights reservation period"], "claims-handling", False),
    ("roof-credit-pct", "percent", "new roof premium credit", ["roof age credit", "new roof discount", "roof replacement credit"], "rating", False),
    ("protective-device-credit-pct", "percent", "protective device premium credit", ["alarm credit", "central station discount", "burglar and fire alarm credit"], "rating", False),
    ("wind-mitigation-credit-pct", "percent", "windstorm mitigation premium credit", ["hurricane mitigation discount", "opening protection credit", "wind loss mitigation credit"], "rating", False),
    ("pool-fence-height-feet", "feet", "minimum swimming pool fence height", ["pool enclosure height", "pool barrier minimum", "swimming pool fence requirement"], "underwriting", False),
    # conditions and handling numbers that give every section a fact (R10)
    ("loss-notice-days", "days", "days within which a loss must be reported", ["notice of loss deadline", "claim reporting period", "prompt notice window"], "conditions", True),
    ("mitigation-duty-days", "days", "days after discovery within which mitigation must begin", ["dry-out deadline", "mitigation start period", "duty to mitigate window"], "claims-handling", False),
    ("contents-inventory-days", "days", "days to submit an inventory of damaged personal property", ["inventory submission deadline", "contents list period"], "claims-handling", False),
    ("ale-max-months", "count", "maximum months of additional living expense payable", ["ALE duration cap", "loss of use time limit", "living expense months"], "claims-handling", False),
    ("emergency-repair-authority", "money", "emergency repair amount an insured may incur without prior approval", ["emergency repair allowance", "pre-approval repair threshold"], "claims-handling", False),
    ("salvage-retention-days", "days", "days salvage must be retained for inspection", ["salvage hold period", "retain damaged property days"], "claims-handling", False),
    ("subrogation-notice-days", "days", "days to notify the subrogation unit of a recoverable loss", ["recovery referral deadline", "subrogation referral window"], "claims-handling", False),
    ("settlement-basis-contents", "enum", "loss settlement basis for personal property under the endorsement", ["contents settlement method", "personal property valuation basis", "contents loss valuation"], "endorsements", True),
    ("flood-excluded", "boolean", "flood and surface water remain excluded under the endorsement", ["flood carve-out", "surface water exclusion preserved", "no flood write-back"], "endorsements", False),
    ("premium-impact-pct", "percent", "overall rate impact of the filing", ["filed rate change", "premium effect of the revision", "rate level change"], "rating", False),
    ("inspection-validity-months", "count", "months an inspection report remains valid", ["inspection age limit", "report validity period", "inspection shelf life"], "underwriting", False),
    ("binding-suspension-hours", "hours", "hours before forecast landfall at which binding is suspended", ["binding moratorium window", "storm binding suspension", "pre-landfall binding cutoff"], "underwriting", True),
    ("wind-mitigation-inspection-cov-a", "money", "Coverage A above which a wind mitigation inspection is required", ["mitigation inspection threshold", "wind survey limit trigger"], "underwriting", False),
    ("large-loss-report-threshold", "money", "loss amount requiring a large loss report", ["large loss notice threshold", "major loss reporting amount", "severity report trigger"], "claims-handling", False),
    ("appraisal-umpire-days", "days", "days for the two appraisers to agree on an umpire", ["umpire selection period", "appraisal umpire deadline"], "conditions", False),
]
CONCEPT_BY_ID = {c[0]: c for c in CONCEPTS}


def V(kind: str, value) -> FactValue:
    return FactValue(kind=kind, value=value)


# ---------------------------------------------------------------------------
# Lines, states, editions
# ---------------------------------------------------------------------------
LINES = {
    "HO-3": ("Homeowners 3 — Special Form", ["2011-05", "2018-09", "2024-03"]),
    "HO-5": ("Homeowners 5 — Comprehensive Form", ["2015-01", "2022-06"]),
    "HO-4": ("Homeowners 4 — Contents Broad Form", ["2013-07", "2021-10"]),
    "HO-6": ("Homeowners 6 — Unit-Owners Form", ["2014-04", "2023-02"]),
    "DP-3": ("Dwelling Property 3 — Special Form", ["2012-11", "2020-08", "2026-01"]),
}
STATES = ["FL", "TX", "CA", "NY", "LA", "NC", "CO", "IL"]
STATE_NAMES = {"FL": "Florida", "TX": "Texas", "CA": "California", "NY": "New York", "LA": "Louisiana", "NC": "North Carolina", "CO": "Colorado", "IL": "Illinois"}

# Base values per line, then per-edition overrides. Each override is a real
# revision: 15-25 changed facts between consecutive editions (R6).
FORM_BASE = {
    "HO-3": dict(**{"cov-b-limit-pct": 10, "cov-c-limit-pct": 50, "cov-d-limit-pct": 20, "special-limit-money": 200, "special-limit-jewelry": 1000,
                    "special-limit-firearms": 2000, "special-limit-watercraft": 1000, "special-limit-silverware": 2500, "special-limit-business-property": 2500,
                    "special-limit-electronics-vehicle": 1000, "debris-removal-pct": 5, "trees-shrubs-limit-pct": 5, "trees-per-item-limit": 500,
                    "fire-department-charge": 500, "credit-card-forgery-limit": 500, "loss-assessment-limit": 1000, "ordinance-law-pct": 10,
                    "landlord-furnishings-limit": 2500, "grave-markers-limit": 5000, "refrigerated-property-limit": 500, "insured-to-value-pct": 80,
                    "section-i-deductible-min": 500, "proof-of-loss-days": 60, "suit-limitation-years": 2, "loss-payment-days": 60,
                    "cancellation-notice-nonpay-days": 10, "cancellation-notice-other-days": 30, "nonrenewal-notice-days": 30, "appraisal-demand-days": 20,
                    "vacancy-days": 60, "medical-payments-years": 3, "damage-to-property-of-others-limit": 1000, "watercraft-hp-threshold": 25,
                    "watercraft-length-threshold": 26, "rental-days-exception": 14}),
}
FORM_BASE["HO-5"] = {**FORM_BASE["HO-3"], "cov-c-limit-pct": 50, "special-limit-jewelry": 2500, "special-limit-firearms": 3000, "special-limit-silverware": 5000, "special-limit-money": 300, "section-i-deductible-min": 1000, "debris-removal-pct": 10}
FORM_BASE["HO-4"] = {k: v for k, v in FORM_BASE["HO-3"].items() if k not in ("cov-b-limit-pct", "cov-c-limit-pct", "insured-to-value-pct", "trees-shrubs-limit-pct", "trees-per-item-limit", "landlord-furnishings-limit", "grave-markers-limit")}
FORM_BASE["HO-4"].update({"cov-d-limit-pct": 30, "special-limit-jewelry": 1500, "loss-assessment-limit": 1000, "ordinance-law-pct": 10, "section-i-deductible-min": 250})
FORM_BASE["HO-6"] = {k: v for k, v in FORM_BASE["HO-3"].items() if k not in ("cov-b-limit-pct", "cov-c-limit-pct", "trees-shrubs-limit-pct", "trees-per-item-limit", "grave-markers-limit")}
FORM_BASE["HO-6"].update({"cov-a-unit-owner-default": 5000, "cov-d-limit-pct": 50, "loss-assessment-limit": 1000, "special-limit-jewelry": 1500, "section-i-deductible-min": 500})
FORM_BASE["DP-3"] = {k: v for k, v in FORM_BASE["HO-3"].items() if k not in ("special-limit-money", "special-limit-jewelry", "special-limit-firearms", "special-limit-watercraft", "special-limit-silverware", "special-limit-business-property", "special-limit-electronics-vehicle", "credit-card-forgery-limit", "loss-assessment-limit", "grave-markers-limit", "refrigerated-property-limit", "medical-payments-years", "damage-to-property-of-others-limit", "watercraft-hp-threshold", "watercraft-length-threshold", "rental-days-exception", "landlord-furnishings-limit")}
FORM_BASE["DP-3"].update({"cov-b-limit-pct": 10, "cov-c-limit-pct": 0, "cov-d-limit-pct": 20, "insured-to-value-pct": 80, "vacancy-days": 60, "section-i-deductible-min": 500})

# Per-edition overrides, applied cumulatively in edition order. Each dict is
# one edition's changes from the previous. Sizes chosen to land in 15-25.
FORM_EDITION_CHANGES = {
    "HO-3": {
        "2011-05": {},
        "2018-09": {"special-limit-jewelry": 1500, "special-limit-firearms": 2500, "special-limit-watercraft": 1500, "special-limit-business-property": 3000,
                    "special-limit-electronics-vehicle": 1500, "trees-per-item-limit": 750, "fire-department-charge": 750, "credit-card-forgery-limit": 1000,
                    "loss-assessment-limit": 1500, "refrigerated-property-limit": 1000, "cancellation-notice-other-days": 45, "nonrenewal-notice-days": 45,
                    "vacancy-days": 30, "rental-days-exception": 15, "watercraft-length-threshold": 30, "landlord-furnishings-limit": 3000, "special-limit-money": 250},
        "2024-03": {"special-limit-jewelry": 2000, "special-limit-firearms": 3000, "special-limit-silverware": 3000, "debris-removal-pct": 10, "trees-shrubs-limit-pct": 10,
                    "trees-per-item-limit": 1000, "fire-department-charge": 1000, "credit-card-forgery-limit": 1500, "loss-assessment-limit": 2000, "ordinance-law-pct": 15,
                    "grave-markers-limit": 7500, "refrigerated-property-limit": 1500, "section-i-deductible-min": 1000, "proof-of-loss-days": 90, "appraisal-demand-days": 30,
                    "damage-to-property-of-others-limit": 2000, "watercraft-hp-threshold": 50, "special-limit-money": 300},
    },
    "HO-5": {
        "2015-01": {},
        "2022-06": {"special-limit-jewelry": 3000, "special-limit-firearms": 3500, "special-limit-watercraft": 2000, "special-limit-business-property": 5000,
                    "special-limit-electronics-vehicle": 2000, "trees-per-item-limit": 1000, "fire-department-charge": 1000, "credit-card-forgery-limit": 2500,
                    "loss-assessment-limit": 2500, "ordinance-law-pct": 15, "refrigerated-property-limit": 1500, "cancellation-notice-other-days": 45,
                    "nonrenewal-notice-days": 60, "vacancy-days": 30, "rental-days-exception": 15, "damage-to-property-of-others-limit": 2500, "grave-markers-limit": 7500},
    },
    "HO-4": {
        "2013-07": {},
        "2021-10": {"cov-d-limit-pct": 40, "special-limit-jewelry": 2000, "special-limit-firearms": 2500, "special-limit-watercraft": 1500, "special-limit-business-property": 3000,
                    "special-limit-electronics-vehicle": 1500, "fire-department-charge": 750, "credit-card-forgery-limit": 1000, "loss-assessment-limit": 1500,
                    "refrigerated-property-limit": 1000, "cancellation-notice-other-days": 45, "nonrenewal-notice-days": 45, "vacancy-days": 30, "rental-days-exception": 15,
                    "damage-to-property-of-others-limit": 1500, "special-limit-money": 250},
    },
    "HO-6": {
        "2014-04": {},
        "2023-02": {"cov-a-unit-owner-default": 10000, "special-limit-jewelry": 2000, "special-limit-firearms": 2500, "special-limit-watercraft": 1500,
                    "special-limit-business-property": 3000, "special-limit-electronics-vehicle": 1500, "fire-department-charge": 750, "credit-card-forgery-limit": 1000,
                    "loss-assessment-limit": 2000, "ordinance-law-pct": 15, "refrigerated-property-limit": 1000, "cancellation-notice-other-days": 45,
                    "nonrenewal-notice-days": 45, "vacancy-days": 30, "rental-days-exception": 15, "landlord-furnishings-limit": 3000, "special-limit-money": 250},
    },
    "DP-3": {
        "2012-11": {},
        "2020-08": {"cov-d-limit-pct": 25, "debris-removal-pct": 10, "trees-shrubs-limit-pct": 10, "trees-per-item-limit": 750, "fire-department-charge": 750,
                    "ordinance-law-pct": 15, "insured-to-value-pct": 90, "section-i-deductible-min": 1000, "proof-of-loss-days": 90, "loss-payment-days": 45,
                    "cancellation-notice-nonpay-days": 15, "cancellation-notice-other-days": 45, "nonrenewal-notice-days": 45, "appraisal-demand-days": 30, "vacancy-days": 30},
        "2026-01": {"cov-b-limit-pct": 15, "cov-d-limit-pct": 30, "debris-removal-pct": 15, "trees-per-item-limit": 1000, "fire-department-charge": 1000,
                    "ordinance-law-pct": 20, "insured-to-value-pct": 80, "section-i-deductible-min": 1500, "proof-of-loss-days": 60, "loss-payment-days": 30,
                    "cancellation-notice-nonpay-days": 10, "cancellation-notice-other-days": 60, "nonrenewal-notice-days": 60, "appraisal-demand-days": 20, "vacancy-days": 45},
    },
}
RENUMBERINGS = {  # (older edition -> newer edition) : [(old section id, new section id)]
    ("HO-3", "2011-05", "2018-09"): [("I.X.D", "I.X.E"), ("I.S.4", "I.S.5")],
    ("HO-3", "2018-09", "2024-03"): [("I.X.E", "I.X.F")],
    ("HO-5", "2015-01", "2022-06"): [("I.X.C", "I.X.D")],
    ("HO-6", "2014-04", "2023-02"): [("I.A.3", "I.A.4")],
    ("DP-3", "2012-11", "2020-08"): [("I.S.3", "I.S.4")],
    ("DP-3", "2020-08", "2026-01"): [("I.X.B", "I.X.C")],
}

# Which section of a form each concept is planted in.
FORM_SECTION_OF = {
    "cov-b-limit-pct": "I.B", "cov-c-limit-pct": "I.C", "cov-d-limit-pct": "I.D", "cov-a-unit-owner-default": "I.A",
    **{k: "I.C" for k in ("special-limit-money", "special-limit-jewelry", "special-limit-firearms", "special-limit-watercraft", "special-limit-silverware", "special-limit-business-property", "special-limit-electronics-vehicle")},
    **{k: "I.E" for k in ("debris-removal-pct", "trees-shrubs-limit-pct", "trees-per-item-limit", "fire-department-charge", "credit-card-forgery-limit", "loss-assessment-limit", "ordinance-law-pct", "landlord-furnishings-limit", "grave-markers-limit", "refrigerated-property-limit")},
    "insured-to-value-pct": "I.A", "section-i-deductible-min": "I.S", "proof-of-loss-days": "I.S", "suit-limitation-years": "I.S", "loss-payment-days": "I.S",
    "appraisal-demand-days": "I.S", "vacancy-days": "I.X", "cancellation-notice-nonpay-days": "G", "cancellation-notice-other-days": "G", "nonrenewal-notice-days": "G",
    "medical-payments-years": "II.F", "damage-to-property-of-others-limit": "II.E2", "watercraft-hp-threshold": "II.X", "watercraft-length-threshold": "II.X", "rental-days-exception": "II.X",
}
FORM_DEFINED_TERMS = ["actual cash value", "replacement cost", "occurrence", "residence premises", "insured", "insured location", "business", "motor vehicle",
                      "residence employee", "bodily injury", "property damage", "sudden and accidental", "vacant", "named storm"]


def form_toc(line: str) -> list[Section]:
    liability = line != "DP-3"
    toc = [
        Section(id="AGR", title="Agreement", target_lines=24, kind="prose"),
        Section(id="DEF", title="Definitions", target_lines=70, kind="definitions"),
        Section(id="I.A", title="Coverage A — Dwelling" if line != "HO-4" else "Coverage A — Not Provided", target_lines=70),
        Section(id="I.B", title="Coverage B — Other Structures", target_lines=60),
        Section(id="I.C", title="Coverage C — Personal Property", target_lines=150),
        Section(id="I.D", title="Coverage D — Loss of Use" if line != "DP-3" else "Coverage D — Fair Rental Value and E — Additional Living Expense", target_lines=60),
        Section(id="I.E", title="Additional Coverages", target_lines=190),
        Section(id="I.P", title="Perils Insured Against", target_lines=130),
        Section(id="I.X", title="Section I — Exclusions", target_lines=170),
        Section(id="I.S", title="Section I — Conditions", target_lines=210),
    ]
    if liability:
        toc += [
            Section(id="II.E", title="Coverage E — Personal Liability", target_lines=60),
            Section(id="II.F", title="Coverage F — Medical Payments to Others", target_lines=50),
            Section(id="II.X", title="Section II — Exclusions", target_lines=130),
            Section(id="II.E2", title="Section II — Additional Coverages", target_lines=70),
            Section(id="II.S", title="Section II — Conditions", target_lines=80),
        ]
    toc += [Section(id="G", title="Sections I and II — Conditions", target_lines=130)]
    return toc


def surface_form(concept_id: str, voice: str) -> str:
    _, _, canonical, syns, _, _ = CONCEPT_BY_ID[concept_id]
    order = {"iso-form": 0, "regulator": 1, "carrier-manual": 2, "carrier-guide": 3, "filing-memo": 1, "trainer": 2}[voice]
    forms = [canonical, *syns]
    return forms[order % len(forms)]


# ---------------------------------------------------------------------------
# Builders
# ---------------------------------------------------------------------------
class Build:
    def __init__(self):
        self.documents: list[Document] = []
        self.facts: list[Fact] = []
        self.definitions: list[Definition] = []
        self.references: list[Reference] = []
        self.editions: list[EditionDiff] = []
        self.contradictions: list[Contradiction] = []
        self.histories: list[History] = []
        self.compositions: list[Composition] = []
        self.fact_by = {}  # (doc, concept) -> fact id

    def add_doc(self, doc: Document) -> Document:
        self.documents.append(doc)
        return doc

    def plant(self, doc: Document, section_id: str, concept: str, value, *, depth: int | None = None, phrasing: str | None = None) -> str:
        kind = CONCEPT_BY_ID[concept][1]
        authority = {"form": "contract", "endorsement": "contract", "amendatory": "contract", "bulletin": "regulation", "manual": "guidance",
                     "guide": "guidance", "memorandum": "interpretation", "training": "interpretation"}[doc.type]
        fid = f"{doc.id}.{section_id}.{concept}"
        self.facts.append(Fact(id=fid, concept=concept, document=doc.id, section=section_id, value=V(kind, value),
                               surface_form=surface_form(concept, doc.voice), phrasing=phrasing, depth_target=depth, authority=authority))
        sec = next(s for s in doc.sections if s.id == section_id)
        sec.facts.append(fid)
        self.fact_by[(doc.id, concept)] = fid
        return fid

    def ref(self, chain: str, src: Document, src_section: str, dst: Document, *, dst_section: str | None = None, dst_definition: str | None = None, wording: str) -> Reference:
        rid = f"{chain}.{len([r for r in self.references if r.chain == chain]) + 1}"
        r = Reference(id=rid, chain=chain, src_document=src.id, src_section=src_section, dst_document=dst.id, dst_section=dst_section, dst_definition=dst_definition, wording=wording)
        self.references.append(r)
        next(s for s in src.sections if s.id == src_section).references_out.append(rid)
        return r

    def distract(self, doc: Document, section_id: str, *concepts: str) -> None:
        sec = next(s for s in doc.sections if s.id == section_id)
        for c in concepts:
            if c not in sec.distractor_concepts and (doc.id, c) not in self.fact_by:
                sec.distractor_concepts.append(c)


def form_id(line: str, edition: str) -> str:
    return f"form.{line.lower().replace('-', '')}.{edition}"


def build_forms(b: Build) -> dict[str, list[Document]]:
    by_line: dict[str, list[Document]] = {}
    for line, (title, editions) in LINES.items():
        values = dict(FORM_BASE[line])
        prev: Document | None = None
        for i, ed in enumerate(editions):
            changes = FORM_EDITION_CHANGES[line][ed]
            values = {**values, **changes}
            code = line.replace("-", "-")
            doc = b.add_doc(Document(
                id=form_id(line, ed), path=f"forms/{line.split('-')[0]}/MS/{line}/{ed}.md", type="form", title=f"{line} {title} (Edition {ed})",
                line=line, edition=ed, effective=f"{ed}-01", voice="iso-form", sections=form_toc(line),
                supersedes=prev.id if prev else None))
            if prev:
                prev.superseded_by = doc.id
            for concept, value in values.items():
                sec = FORM_SECTION_OF[concept]
                if sec.startswith("II") and line == "DP-3":
                    continue
                b.plant(doc, sec, concept, value)
            for term in FORM_DEFINED_TERMS:
                if term == "named storm" and ed < "2018":
                    continue
                b.definitions.append(Definition(id=f"{doc.id}.def.{term.replace(' ', '-')}", term=term, document=doc.id, section="DEF"))
            # ambiguous vocabulary in sections without the fact (R1)
            b.distract(doc, "I.X", "water-backup-sublimit", "fungi-limit", "ordinance-law-pct", "wind-hail-deductible-min-pct")
            b.distract(doc, "I.S", "wind-hail-deductible-max-pct", "wind-deductible-notice-days", "claim-acknowledgement-days", "referral-loss-threshold")
            b.distract(doc, "I.P", "roof-acv-age-threshold-years", "insured-to-value-pct")
            if prev:
                old_vals = {f.concept: f for f in b.facts if f.document == prev.id}
                new_vals = {f.concept: f for f in b.facts if f.document == doc.id}
                changed = [(old_vals[c].id, new_vals[c].id) for c in new_vals if c in old_vals and old_vals[c].value != new_vals[c].value]
                b.editions.append(EditionDiff(form=line, older=prev.id, newer=doc.id, changed=changed,
                                              added=[new_vals[c].id for c in new_vals if c not in old_vals], removed=[old_vals[c].id for c in old_vals if c not in new_vals],
                                              renumbered=RENUMBERINGS.get((line, editions[i - 1], ed), [])))
            prev = doc
            by_line.setdefault(line, []).append(doc)
    return by_line


# Endorsement families: (form number, title, lines it attaches to, editions, facts {concept: value per edition}, distractor?)
ENDORSEMENTS = [
    ("HO 04 90", "Water Backup and Sump Discharge or Overflow", ["HO-3", "HO-5"], ["2010-10", "2027-01"],
     {"2010-10": {"water-backup-sublimit": 5000, "water-backup-deductible": 500, "backflow-requirement": False},
      "2027-01": {"water-backup-sublimit": 10000, "water-backup-deductible": 1000, "backflow-requirement": True}}),
    ("HO 04 91", "Water Backup — Unit-Owners", ["HO-6"], ["2019-03"], {"2019-03": {"water-backup-sublimit": 7500, "water-backup-deductible": 750, "backflow-requirement": False}}),
    ("HO 04 92", "Water Backup — Tenants", ["HO-4"], ["2019-03"], {"2019-03": {"water-backup-sublimit": 2500, "water-backup-deductible": 250, "backflow-requirement": False}}),
    ("DP 04 95", "Water Backup — Dwelling Property", ["DP-3"], ["2021-05"], {"2021-05": {"water-backup-sublimit": 5000, "water-backup-deductible": 1000, "backflow-requirement": True}}),
    ("HO 23 74", "Actual Cash Value Loss Settlement — Roof Surfacing", ["HO-3", "HO-5", "DP-3"], ["2018-09", "2025-05"],
     {"2018-09": {"roof-acv-age-threshold-years": 15, "roof-min-payment-pct": 25, "roof-comp-shingle-20yr-pct": 25},
      "2025-05": {"roof-acv-age-threshold-years": 12, "roof-min-payment-pct": 30, "roof-comp-shingle-20yr-pct": 20}}),
    ("HO 04 16", "Ordinance or Law Coverage", ["HO-3", "HO-5", "HO-6"], ["2018-09", "2023-11"],
     {"2018-09": {"ordinance-law-pct": 10}, "2023-11": {"ordinance-law-pct": 25}}),
    ("HO 04 81", "Limited Fungi, Wet or Dry Rot, or Bacteria Coverage", ["HO-3", "HO-5", "HO-4", "HO-6"], ["2018-09"], {"2018-09": {"fungi-limit": 10000}}),
    ("HO 04 48", "Other Structures — Increased Limits", ["HO-3", "HO-5"], ["2026-06"], {"2026-06": {"cov-b-limit-pct": 20}}),
    ("HO 04 61", "Scheduled Personal Property", ["HO-3", "HO-5", "HO-4", "HO-6"], ["2012-02", "2020-11"],
     {"2012-02": {"scheduled-property-deductible": 0}, "2020-11": {"scheduled-property-deductible": 250}}),
    ("HO 04 65", "Coverage C — Increased Special Limits of Liability", ["HO-3", "HO-4", "HO-6"], ["2018-09"], {"2018-09": {"special-limit-jewelry": 5000, "special-limit-firearms": 6500, "special-limit-silverware": 10000}}),
    ("HO 04 20", "Specified Additional Amount of Insurance for Coverage A", ["HO-3", "HO-5"], ["2016-08"], {"2016-08": {"extended-replacement-pct": 25}}),
    ("HO 04 12", "Increased Limits on Business Property", ["HO-3", "HO-5", "HO-4"], ["2018-09"], {"2018-09": {"special-limit-business-property": 10000}}),
    ("HO 04 42", "Permitted Incidental Occupancies", ["HO-3", "HO-5"], ["2011-05"], None),
    ("HO 04 53", "Credit Card, Fund Transfer Card, Forgery — Increased Limit", ["HO-3", "HO-5", "HO-4", "HO-6"], ["2013-06"], {"2013-06": {"credit-card-forgery-limit": 10000}}),
    ("HO 04 54", "Earthquake", ["HO-3", "HO-5", "HO-6", "DP-3"], ["2009-04", "2021-12"],
     {"2009-04": {"earthquake-deductible-pct": 5}, "2021-12": {"earthquake-deductible-pct": 10}}),
    ("HO 04 55", "Identity Fraud Expense Coverage", ["HO-3", "HO-5", "HO-4", "HO-6"], ["2017-01"], {"2017-01": {"identity-fraud-limit": 15000}}),
    ("HO 04 96", "No Section II — Liability Coverages", ["HO-3", "HO-4", "HO-6"], ["2011-05"], None),
    ("HO 24 82", "Personal Injury Coverage", ["HO-3", "HO-5", "HO-4", "HO-6"], ["2011-05"], None),
    ("HO 24 71", "Business Pursuits", ["HO-3", "HO-5", "HO-4", "HO-6"], ["2011-05"], {"2011-05": {"business-pursuits-limit": 100000}}),
    ("HO 24 73", "Farmers Personal Liability", ["HO-3", "HO-5"], ["2011-05"], None),
    ("HO 05 24", "Special Personal Property Coverage", ["HO-3"], ["2018-09"], {"2018-09": {"special-limit-jewelry": 2500}}),
    ("HO 17 32", "Unit-Owners Rental to Others", ["HO-6"], ["2014-04"], {"2014-04": {"landlord-furnishings-limit": 5000}}),
    ("HO 17 33", "Unit-Owners Coverage A — Special Coverage", ["HO-6"], ["2014-04"], {"2014-04": {"cov-a-unit-owner-default": 25000}}),
    ("HO 04 40", "Structures Rented to Others — Residence Premises", ["HO-3", "HO-5"], ["2011-05"], {"2011-05": {"landlord-furnishings-limit": 5000}}),
    ("HO 04 41", "Additional Insured — Residence Premises", ["HO-3", "HO-5", "HO-6"], ["2011-05"], None),
    ("HO 04 10", "Additional Interests — Residence Premises", ["HO-3", "HO-5", "HO-4", "HO-6", "DP-3"], ["2011-05"], None),
    ("HO 23 77", "Windstorm or Hail Percentage Deductible", ["HO-3", "HO-5", "HO-6", "DP-3"], ["2014-02", "2022-07"],
     {"2014-02": {"wind-hail-deductible-min-pct": 1, "wind-hail-deductible-max-pct": 5, "named-storm-period-hours": 72},
      "2022-07": {"wind-hail-deductible-min-pct": 2, "wind-hail-deductible-max-pct": 10, "named-storm-period-hours": 96}}),
    ("HO 04 27", "Limited Water Damage Coverage", ["HO-4", "HO-6"], ["2016-05"], {"2016-05": {"water-backup-sublimit": 2500, "fungi-limit": 5000}}),
    ("HO 04 35", "Loss Assessment Coverage", ["HO-6", "HO-3"], ["2014-04", "2023-02"],
     {"2014-04": {"loss-assessment-endorsement-limit": 10000}, "2023-02": {"loss-assessment-endorsement-limit": 25000}}),
]
DISTRACTOR_ENDORSEMENTS = {"HO 04 42", "HO 04 96", "HO 24 82", "HO 24 73", "HO 04 41", "HO 04 10"}
ENDORSEMENT_SECTION_OF = {
    "water-backup-sublimit": "W.2", "water-backup-deductible": "W.3", "backflow-requirement": "W.6", "roof-acv-age-threshold-years": "W.1", "roof-min-payment-pct": "W.4",
    "roof-comp-shingle-20yr-pct": "W.3", "ordinance-law-pct": "W.2", "fungi-limit": "W.2", "cov-b-limit-pct": "W.2", "scheduled-property-deductible": "W.3",
    "special-limit-jewelry": "W.2", "special-limit-firearms": "W.2", "special-limit-silverware": "W.2", "extended-replacement-pct": "W.2", "special-limit-business-property": "W.2",
    "credit-card-forgery-limit": "W.2", "earthquake-deductible-pct": "W.3", "identity-fraud-limit": "W.2", "business-pursuits-limit": "W.2", "landlord-furnishings-limit": "W.2",
    "cov-a-unit-owner-default": "W.2", "wind-hail-deductible-min-pct": "W.3", "wind-hail-deductible-max-pct": "W.3", "named-storm-period-hours": "W.6", "loss-assessment-endorsement-limit": "W.2",
}


def endorsement_toc(long: bool) -> list[Section]:
    m = 1.6 if long else 1.0
    return [
        Section(id="W.0", title="Preamble and Attachment", target_lines=int(24 * m), kind="prose"),
        Section(id="W.1", title="Coverage Provided", target_lines=int(90 * m)),
        Section(id="W.2", title="Limit of Liability", target_lines=int(60 * m)),
        Section(id="W.3", title="Deductible", target_lines=int(50 * m)),
        Section(id="W.4", title="What Remains Excluded", target_lines=int(110 * m)),
        Section(id="W.5", title="Conditions", target_lines=int(120 * m)),
        Section(id="W.6", title="Special Requirements", target_lines=int(70 * m)),
        Section(id="W.7", title="Loss Settlement", target_lines=int(70 * m)),
        Section(id="W.8", title="Definitions", target_lines=int(60 * m), kind="definitions"),
    ]


def build_endorsements(b: Build, forms: dict[str, list[Document]]) -> dict[str, list[Document]]:
    by_number: dict[str, list[Document]] = {}
    for number, title, lines, editions, values, in ENDORSEMENTS:
        prev = None
        for i, ed in enumerate(editions):
            slug = number.replace(" ", "-")
            line_dir = "DP" if number.startswith("DP") else "HO"
            distractor = number in DISTRACTOR_ENDORSEMENTS
            doc = b.add_doc(Document(id=f"end.{slug.lower()}.{ed}", path=f"forms/{line_dir}/MS/{slug}/{ed}.md", type="endorsement",
                                     title=f"{number} {title} (Edition {ed})", line=lines[0], edition=ed, effective=f"{ed}-01", voice="iso-form",
                                     distractor=distractor, sections=endorsement_toc(long=len(lines) >= 3), supersedes=prev.id if prev else None))
            if prev:
                prev.superseded_by = doc.id
            if values:
                for concept, value in values[ed].items():
                    b.plant(doc, ENDORSEMENT_SECTION_OF[concept], concept, value)
                fam = [e[0] for e in ENDORSEMENTS].index(number)
                b.plant(doc, "W.5", "loss-notice-days", (30, 60, 90)[fam % 3])
                b.plant(doc, "W.7", "settlement-basis-contents", "actual cash value" if "Water" in title or "Roof" in title else "replacement cost")
                b.plant(doc, "W.4", "flood-excluded", True)
            # every endorsement talks about the base deductible and the insured-to-value condition without stating them (R1)
            b.distract(doc, "W.5", "section-i-deductible-min", "insured-to-value-pct", "proof-of-loss-days", "suit-limitation-years")
            b.distract(doc, "W.4", "wind-hail-deductible-min-pct", "cov-b-limit-pct", "cov-c-limit-pct", "cov-d-limit-pct", "debris-removal-pct")
            b.distract(doc, "W.7", "loss-assessment-limit", "fire-department-charge", "special-limit-jewelry", "special-limit-business-property")
            if prev and values:
                old = {f.concept: f for f in b.facts if f.document == prev.id}
                new = {f.concept: f for f in b.facts if f.document == doc.id}
                # endorsement pairs are small revisions; they are not R6 pairs, but the diff is recorded for questions
                b.editions.append(EditionDiff(form=number, older=prev.id, newer=doc.id,
                                              changed=[(old[c].id, new[c].id) for c in new if c in old and old[c].value != new[c].value],
                                              added=[new[c].id for c in new if c not in old], removed=[old[c].id for c in old if c not in new]))
            prev = doc
            by_number.setdefault(number, []).append(doc)
    return by_number


# State overlays: per-state numbers for the same concepts (R2: shared vocabulary, different values).
STATE_VALUES = {
    "FL": {"wind-hail-deductible-min-pct": 2, "wind-hail-deductible-max-pct": 10, "wind-deductible-notice-days": 45, "named-storm-period-hours": 72, "cancellation-notice-nonpay-days": 10, "cancellation-notice-other-days": 45, "nonrenewal-notice-days": 120, "claim-acknowledgement-days": 14, "claim-decision-business-days": 90, "claim-payment-business-days": 20, "suit-limitation-years": 5, "roof-acv-age-threshold-years": 10},
    "TX": {"wind-hail-deductible-min-pct": 1, "wind-hail-deductible-max-pct": 5, "wind-seacoast-max-pct": 10, "wind-deductible-notice-days": 30, "named-storm-period-hours": 72, "cancellation-notice-nonpay-days": 10, "cancellation-notice-other-days": 30, "nonrenewal-notice-days": 30, "claim-acknowledgement-days": 15, "claim-decision-business-days": 15, "claim-payment-business-days": 5, "suit-limitation-years": 2},
    "CA": {"earthquake-deductible-pct": 15, "cancellation-notice-nonpay-days": 10, "cancellation-notice-other-days": 20, "nonrenewal-notice-days": 75, "claim-acknowledgement-days": 15, "claim-decision-business-days": 40, "claim-payment-business-days": 30, "suit-limitation-years": 1, "insured-to-value-pct": 100},
    "NY": {"cancellation-notice-nonpay-days": 15, "cancellation-notice-other-days": 20, "nonrenewal-notice-days": 60, "claim-acknowledgement-days": 15, "claim-decision-business-days": 15, "claim-payment-business-days": 5, "suit-limitation-years": 2, "wind-hail-deductible-min-pct": 1, "wind-hail-deductible-max-pct": 5},
    "LA": {"wind-hail-deductible-min-pct": 2, "wind-hail-deductible-max-pct": 5, "wind-deductible-notice-days": 30, "named-storm-period-hours": 72, "cancellation-notice-nonpay-days": 10, "cancellation-notice-other-days": 30, "nonrenewal-notice-days": 30, "claim-acknowledgement-days": 14, "claim-decision-business-days": 30, "claim-payment-business-days": 30, "suit-limitation-years": 2},
    "NC": {"wind-hail-deductible-min-pct": 1, "wind-hail-deductible-max-pct": 5, "wind-seacoast-max-pct": 10, "wind-deductible-notice-days": 30, "cancellation-notice-nonpay-days": 15, "cancellation-notice-other-days": 30, "nonrenewal-notice-days": 45, "claim-acknowledgement-days": 30, "claim-decision-business-days": 30, "claim-payment-business-days": 30, "suit-limitation-years": 3, "fungi-limit": 5000},
    "CO": {"wind-hail-deductible-min-pct": 1, "wind-hail-deductible-max-pct": 5, "wind-deductible-notice-days": 30, "cancellation-notice-nonpay-days": 10, "cancellation-notice-other-days": 30, "nonrenewal-notice-days": 30, "claim-acknowledgement-days": 15, "claim-decision-business-days": 60, "claim-payment-business-days": 30, "suit-limitation-years": 2, "roof-acv-age-threshold-years": 15},
    "IL": {"cancellation-notice-nonpay-days": 10, "cancellation-notice-other-days": 30, "nonrenewal-notice-days": 60, "claim-acknowledgement-days": 15, "claim-decision-business-days": 30, "claim-payment-business-days": 30, "suit-limitation-years": 2, "water-backup-sublimit": 5000},
}
AMENDATORY = [  # (state, form number, line, editions)
    ("FL", "HO 01 09", "HO-3", ["2019-01", "2023-07"]), ("TX", "HO 01 45", "HO-3", ["2019-01", "2022-01"]), ("CA", "HO 01 04", "HO-3", ["2021-06"]),
    ("NY", "HO 01 31", "HO-3", ["2016-04"]), ("LA", "HO 01 17", "HO-3", ["2020-09"]), ("NC", "HO 01 32", "HO-3", ["2018-05"]), ("CO", "HO 01 05", "HO-3", ["2022-10"]),
    ("IL", "HO 01 12", "HO-3", ["2015-02"]), ("FL", "DP 01 09", "DP-3", ["2021-03"]), ("TX", "DP 01 45", "DP-3", ["2022-01"]),
]
AMEND_SECTION_OF = {"wind-hail-deductible-min-pct": "T.1", "wind-hail-deductible-max-pct": "T.1", "wind-seacoast-max-pct": "T.6", "wind-deductible-notice-days": "T.2", "named-storm-period-hours": "T.3",
                    "cancellation-notice-nonpay-days": "T.4", "cancellation-notice-other-days": "T.4", "nonrenewal-notice-days": "T.4", "claim-acknowledgement-days": "T.5",
                    "claim-decision-business-days": "T.5", "claim-payment-business-days": "T.5", "suit-limitation-years": "T.7", "roof-acv-age-threshold-years": "T.8",
                    "earthquake-deductible-pct": "T.8", "insured-to-value-pct": "T.8", "fungi-limit": "T.8", "water-backup-sublimit": "T.8"}


def amendatory_toc() -> list[Section]:
    return [
        Section(id="T.0", title="Scope and Precedence", target_lines=40, kind="prose"),
        Section(id="T.1", title="Windstorm and Hail Deductible", target_lines=140),
        Section(id="T.2", title="Notice of Deductible Change", target_lines=60),
        Section(id="T.3", title="Named Storm Period", target_lines=60),
        Section(id="T.4", title="Cancellation and Nonrenewal", target_lines=150),
        Section(id="T.5", title="Claims Handling", target_lines=130),
        Section(id="T.6", title="Seacoast Territories", target_lines=60),
        Section(id="T.7", title="Suit Against Us", target_lines=50),
        Section(id="T.8", title="Other Amendments", target_lines=120),
        Section(id="T.9", title="Definitions Amended", target_lines=70, kind="definitions"),
    ]


def build_amendatory(b: Build) -> dict[str, list[Document]]:
    by_state: dict[str, list[Document]] = {}
    for state, number, line, editions in AMENDATORY:
        prev = None
        for i, ed in enumerate(editions):
            slug = number.replace(" ", "-")
            doc = b.add_doc(Document(id=f"amend.{state.lower()}.{slug.lower()}.{ed}", path=f"forms/{line.split('-')[0]}/{state}/{slug}/{ed}.md", type="amendatory",
                                     title=f"{number} {STATE_NAMES[state]} Amendatory Endorsement (Edition {ed})", line=line, state=state, edition=ed, effective=f"{ed}-01",
                                     voice="iso-form", sections=amendatory_toc(), supersedes=prev.id if prev else None))
            if prev:
                prev.superseded_by = doc.id
            vals = dict(STATE_VALUES[state])
            if i > 0:  # the newer edition revises a handful of numbers
                for k, delta in (("nonrenewal-notice-days", 15), ("claim-decision-business-days", -5), ("wind-deductible-notice-days", 15)):
                    if k in vals:
                        vals[k] = vals[k] + delta
                if "wind-hail-deductible-max-pct" in vals:
                    vals["wind-hail-deductible-max-pct"] = vals["wind-hail-deductible-max-pct"] + 5
            for concept, value in vals.items():
                b.plant(doc, AMEND_SECTION_OF[concept], concept, value)
            b.distract(doc, "T.0", "section-i-deductible-min", "proof-of-loss-days", "insured-to-value-pct")
            b.distract(doc, "T.8", "loss-assessment-limit", "ordinance-law-pct", "debris-removal-pct", "fire-department-charge")
            if prev:
                old = {f.concept: f for f in b.facts if f.document == prev.id}
                new = {f.concept: f for f in b.facts if f.document == doc.id}
                b.editions.append(EditionDiff(form=number, older=prev.id, newer=doc.id,
                                              changed=[(old[c].id, new[c].id) for c in new if c in old and old[c].value != new[c].value]))
            prev = doc
            by_state.setdefault(state, []).append(doc)
    return by_state


# Bulletins: (state, id slug, issued, title, facts, superseded_by slug or None, distractor)
BULLETINS = [
    ("TX", "b-2016-04-windstorm-deductibles", "2016-08-19", "Separate Windstorm and Hail Deductibles", {"wind-hail-deductible-min-pct": 1, "wind-hail-deductible-max-pct": 3, "wind-deductible-notice-days": 30}, "b-2021-08-windstorm-deductibles", False),
    ("TX", "b-2021-08-windstorm-deductibles", "2021-08-19", "Separate Windstorm and Hail Deductibles", {"wind-hail-deductible-min-pct": 1, "wind-hail-deductible-max-pct": 5, "wind-seacoast-max-pct": 10, "wind-deductible-notice-days": 30, "named-storm-period-hours": 72}, None, False),
    ("TX", "b-2019-02-prompt-payment", "2019-02-11", "Prompt Payment of Claims", {"claim-acknowledgement-days": 15, "claim-decision-business-days": 15, "claim-payment-business-days": 5}, None, False),
    ("FL", "oir-2019-11-roof-age", "2019-11-05", "Roof Age Underwriting Restrictions", {"roof-acv-age-threshold-years": 15, "roof-inspection-age-years": 20, "nonrenewal-notice-days": 90}, "oir-2023-04-roof-age-nonrenewal", False),
    ("FL", "oir-2023-04-roof-age-nonrenewal", "2023-04-11", "Roof Age and Nonrenewal", {"roof-acv-age-threshold-years": 10, "roof-inspection-age-years": 15, "nonrenewal-notice-days": 120}, None, False),
    ("FL", "oir-2022-01-hurricane-deductible", "2022-01-20", "Hurricane Deductible Disclosure", {"wind-hail-deductible-min-pct": 2, "wind-hail-deductible-max-pct": 10, "wind-deductible-notice-days": 45}, None, False),
    ("CA", "cdi-2014-06-earthquake-offer", "2014-06-30", "Mandatory Earthquake Coverage Offer", {"earthquake-deductible-pct": 10}, "cdi-2022-03-earthquake-offer", False),
    ("CA", "cdi-2022-03-earthquake-offer", "2022-03-14", "Mandatory Earthquake Coverage Offer", {"earthquake-deductible-pct": 15, "nonrenewal-notice-days": 75}, None, False),
    ("LA", "ldi-2012-05-hurricane-deductible", "2012-05-01", "Hurricane Deductible Notice", {"wind-deductible-notice-days": 30, "wind-hail-deductible-max-pct": 5}, "ldi-2020-07-hurricane-deductible", False),
    ("LA", "ldi-2020-07-hurricane-deductible", "2020-07-15", "Hurricane Deductible Notice and Named Storm Periods", {"wind-deductible-notice-days": 30, "wind-hail-deductible-max-pct": 5, "named-storm-period-hours": 72}, None, False),
    ("NY", "dfs-2010-09-nonrenewal", "2010-09-01", "Nonrenewal Notice Requirements", {"nonrenewal-notice-days": 45, "cancellation-notice-other-days": 20}, "dfs-2016-02-nonrenewal", False),
    ("NY", "dfs-2016-02-nonrenewal", "2016-02-22", "Nonrenewal and Cancellation Notice Requirements", {"nonrenewal-notice-days": 60, "cancellation-notice-other-days": 20, "cancellation-notice-nonpay-days": 15}, None, False),
    ("NC", "ncdoi-2018-03-fungi-disclosure", "2018-03-12", "Fungi Coverage Limit Disclosure", {"fungi-limit": 5000}, None, False),
    ("NC", "ncdoi-2021-06-claims-handling", "2021-06-01", "Claims Handling Standards", {"claim-acknowledgement-days": 30, "claim-decision-business-days": 30}, None, False),
    ("CO", "doi-2022-08-roof-settlement", "2022-08-09", "Roof Settlement Disclosures", {"roof-acv-age-threshold-years": 15, "roof-min-payment-pct": 25}, None, False),
    ("CO", "doi-2013-01-hail-deductibles", "2013-01-15", "Hail Deductibles", {"wind-hail-deductible-max-pct": 3}, "doi-2019-05-hail-deductibles", False),
    ("CO", "doi-2019-05-hail-deductibles", "2019-05-20", "Hail Deductibles", {"wind-hail-deductible-max-pct": 5, "wind-deductible-notice-days": 30}, None, False),
    ("IL", "idoi-2017-10-water-backup-disclosure", "2017-10-02", "Water Backup Coverage Disclosure", {"water-backup-sublimit": 5000}, None, False),
    ("IL", "idoi-2015-04-producer-licensing", "2015-04-06", "Producer Licensing Renewals", {}, None, True),
    ("NY", "dfs-2018-11-data-call", "2018-11-19", "Annual Homeowners Data Call", {}, None, True),
]
BULLETIN_SECTION_OF = {c: "B.2" for c in ("wind-hail-deductible-min-pct", "wind-hail-deductible-max-pct", "wind-seacoast-max-pct", "earthquake-deductible-pct", "roof-acv-age-threshold-years", "roof-min-payment-pct", "fungi-limit", "water-backup-sublimit")}
BULLETIN_SECTION_OF.update({c: "B.3" for c in ("wind-deductible-notice-days", "named-storm-period-hours", "nonrenewal-notice-days", "cancellation-notice-other-days", "cancellation-notice-nonpay-days", "roof-inspection-age-years")})
BULLETIN_SECTION_OF.update({c: "B.4" for c in ("claim-acknowledgement-days", "claim-decision-business-days", "claim-payment-business-days")})


def bulletin_toc() -> list[Section]:
    return [
        Section(id="B.1", title="Purpose and Applicability", target_lines=40, kind="prose"),
        Section(id="B.2", title="Requirements", target_lines=110),
        Section(id="B.3", title="Notice and Disclosure", target_lines=70),
        Section(id="B.4", title="Claims Standards", target_lines=50),
        Section(id="B.5", title="Filing and Effective Date", target_lines=30, kind="prose"),
    ]


def build_bulletins(b: Build) -> dict[str, Document]:
    docs: dict[str, Document] = {}
    for state, slug, issued, title, facts, superseded_by, distractor in BULLETINS:
        doc = b.add_doc(Document(id=f"bulletin.{state.lower()}.{slug}", path=f"bulletins/{state}/{slug}.md", type="bulletin",
                                 title=f"{STATE_NAMES[state]} Bulletin {slug.split('-', 1)[0].upper()}-{'-'.join(slug.split('-')[1:3])} — {title}", state=state,
                                 edition=issued, effective=issued, voice="regulator", distractor=distractor, sections=bulletin_toc()))
        docs[slug] = doc
        for concept, value in facts.items():
            b.plant(doc, BULLETIN_SECTION_OF[concept], concept, value)
        b.distract(doc, "B.1", "section-i-deductible-min", "insured-to-value-pct", "cov-d-limit-pct")
        if distractor:
            b.distract(doc, "B.2", "nonrenewal-notice-days", "cancellation-notice-other-days", "proof-of-loss-days", "loss-assessment-limit")
    for state, slug, *_rest in BULLETINS:
        sup = _rest[3]
        if sup:
            docs[slug].superseded_by = docs[sup].id
            docs[sup].supersedes = docs[slug].id
    return docs


# Manuals. Chapters × ~300 lines; facts planted deep (R4).
def manual(b: Build, doc_id: str, path: str, title: str, chapters: list[tuple[str, str, int, dict, list[str]]], kind_default: str = "provisions") -> Document:
    sections = [Section(id=cid, title=ctitle, target_lines=lines, kind=("table" if ctitle.lower().startswith("table") else kind_default), distractor_concepts=[]) for cid, ctitle, lines, _, _ in chapters]
    doc = b.add_doc(Document(id=doc_id, path=path, type="manual", title=title, voice="carrier-manual", sections=sections))
    starts = doc.section_starts()
    for cid, _, _, facts, distractors in chapters:
        for concept, value in facts.items():
            b.plant(doc, cid, concept, value, depth=(starts[cid] if starts[cid] > 2000 else None))
        b.distract(doc, cid, *distractors)
    return doc


UW = [  # (chapter id, title, lines, facts, distractor concepts)
    ("R100", "Rule 100 — Purpose, Authority and Use of This Manual", 260, {"inspection-validity-months": 12}, ["line-authority-cov-a", "section-i-deductible-min"]),
    ("R110", "Rule 110 — Eligibility: HO-3 Special Form", 320, {"min-cov-a": 150000, "max-cov-a": 1500000, "protection-class-max": 8}, ["insured-to-value-pct", "cov-b-limit-pct"]),
    ("R120", "Rule 120 — Eligibility: HO-5 Comprehensive Form", 300, {"min-cov-a": 300000, "max-cov-a": 2500000, "protection-class-max": 6}, ["special-limit-jewelry", "cov-c-limit-pct"]),
    ("R130", "Rule 130 — Eligibility: HO-4 Contents Broad Form", 280, {"protection-class-max": 9}, ["cov-d-limit-pct", "loss-assessment-limit"]),
    ("R140", "Rule 140 — Eligibility: HO-6 Unit-Owners Form", 300, {"min-cov-a": 5000, "max-cov-a": 250000}, ["cov-a-unit-owner-default", "loss-assessment-limit"]),
    ("R150", "Rule 150 — Eligibility: DP-3 Dwelling Property", 300, {"min-cov-a": 75000, "max-cov-a": 750000, "vacancy-days": 30}, ["insured-to-value-pct", "cov-d-limit-pct"]),
    ("R200", "Rule 200 — Construction and Protection Class", 320, {"wind-mitigation-inspection-cov-a": 750000}, ["protection-class-max", "wind-mitigation-credit-pct", "fire-department-charge"]),
    ("R210", "Rule 210 — Roof Condition, Age and Material", 340, {"roof-inspection-age-years": 15, "roof-max-age-years": 25}, ["roof-acv-age-threshold-years", "roof-min-payment-pct"]),
    ("R220", "Rule 220 — Water Exposure and Plumbing", 320, {"water-backup-referral-limit": 25000}, ["water-backup-sublimit", "water-backup-deductible", "backflow-requirement"]),
    ("R230", "Rule 230 — Liability Hazards", 320, {"pool-fence-height-feet": 4}, ["watercraft-hp-threshold", "damage-to-property-of-others-limit", "rental-days-exception"]),
    ("R240", "Rule 240 — Prior Loss History", 300, {"prior-claims-referral-count": 2, "prior-claims-lookback-years": 3}, ["referral-loss-threshold", "fungi-limit"]),
    ("R250", "Rule 250 — Occupancy, Vacancy and Rental", 300, {"vacancy-days": 60}, ["vacancy-days", "rental-days-exception", "landlord-furnishings-limit"]),
    ("R300", "Rule 300 — Binding Authority", 320, {"line-authority-cov-a": 800000, "senior-authority-cov-a": 1500000}, ["min-cov-a", "max-cov-a"]),
    ("R310", "Rule 310 — Mandatory Referral Conditions", 320, {"large-loss-report-threshold": 100000}, ["prior-claims-referral-count", "water-backup-referral-limit", "roof-max-age-years"]),
    ("R320", "Rule 320 — Conditions That Cannot Be Cleared", 280, {"binding-suspension-hours": 48}, ["insured-to-value-pct", "roof-inspection-age-years"]),
    ("R400", "Rule 400 — Endorsement Attachment Rules", 340, {"inspection-validity-months": 6}, ["water-backup-sublimit", "fungi-limit", "ordinance-law-pct", "extended-replacement-pct", "earthquake-deductible-pct"]),
    ("R410", "Rule 410 — Deductible Options", 320, {"section-i-deductible-min": 500}, ["wind-hail-deductible-min-pct", "wind-hail-deductible-max-pct"]),
    ("R500", "Rule 500 — Florida State Exceptions", 320, {"roof-inspection-age-years": 15, "roof-max-age-years": 20, "line-authority-cov-a": 600000, "senior-authority-cov-a": 900000, "max-cov-a": 900000, "min-cov-a": 200000}, ["wind-hail-deductible-max-pct", "nonrenewal-notice-days"]),
    ("R510", "Rule 510 — Texas State Exceptions", 320, {"line-authority-cov-a": 800000, "senior-authority-cov-a": 1200000, "max-cov-a": 1200000, "water-backup-referral-limit": 25000, "roof-inspection-age-years": 15}, ["wind-seacoast-max-pct", "claim-decision-business-days"]),
    ("R520", "Rule 520 — California State Exceptions", 300, {"line-authority-cov-a": 1000000, "max-cov-a": 2000000, "insured-to-value-pct": 100}, ["earthquake-deductible-pct", "nonrenewal-notice-days"]),
    ("R530", "Rule 530 — New York State Exceptions", 300, {"line-authority-cov-a": 750000, "prior-claims-referral-count": 3}, ["nonrenewal-notice-days", "cancellation-notice-nonpay-days"]),
    ("R540", "Rule 540 — Louisiana State Exceptions", 300, {"roof-max-age-years": 20, "line-authority-cov-a": 500000, "max-cov-a": 750000}, ["wind-hail-deductible-max-pct", "named-storm-period-hours"]),
    ("R550", "Rule 550 — North Carolina State Exceptions", 300, {"line-authority-cov-a": 700000, "roof-inspection-age-years": 18}, ["fungi-limit", "wind-seacoast-max-pct"]),
    ("R560", "Rule 560 — Colorado State Exceptions", 300, {"roof-inspection-age-years": 12, "roof-max-age-years": 22, "line-authority-cov-a": 850000}, ["roof-acv-age-threshold-years", "wind-hail-deductible-max-pct"]),
    ("R570", "Rule 570 — Illinois State Exceptions", 300, {"line-authority-cov-a": 700000, "water-backup-referral-limit": 15000}, ["water-backup-sublimit", "nonrenewal-notice-days"]),
    ("R600", "Rule 600 — Inspections", 320, {"roof-inspection-age-years": 15}, ["roof-max-age-years", "protection-class-max"]),
    ("R610", "Rule 610 — Documentation Standards", 300, {"inspection-validity-months": 18}, ["prior-claims-lookback-years", "line-authority-cov-a"]),
    ("R700", "Rule 700 — Renewal Underwriting", 320, {"prior-claims-referral-count": 2, "inspection-validity-months": 12}, ["nonrenewal-notice-days", "roof-max-age-years", "cancellation-notice-other-days"]),
    ("R800", "Rule 800 — Cancellation and Nonrenewal Procedures", 320, {"binding-suspension-hours": 72, "nonrenewal-notice-days": 45, "cancellation-notice-nonpay-days": 10}, ["cancellation-notice-nonpay-days", "cancellation-notice-other-days", "nonrenewal-notice-days", "wind-deductible-notice-days"]),
    ("R900", "Rule 900 — Appendix: Referral Matrix", 300, {"referral-loss-threshold": 25000, "senior-authority-cov-a": 1500000, "prior-claims-lookback-years": 3, "roof-max-age-years": 25, "water-backup-referral-limit": 25000}, ["water-backup-referral-limit", "prior-claims-referral-count"]),
]
CLAIMS = [
    ("C1", "Chapter 1 — Purpose and Adjuster Authority", 280, {"referral-loss-threshold": 25000}, ["claim-acknowledgement-days", "section-i-deductible-min"]),
    ("C2", "Chapter 2 — First Notice, Acknowledgement and Reservation of Rights", 320, {"reservation-of-rights-days": 10}, ["claim-acknowledgement-days", "claim-decision-business-days", "proof-of-loss-days"]),
    ("C3", "Chapter 3 — Water Losses", 340, {"mitigation-duty-days": 3}, ["water-backup-sublimit", "water-backup-deductible", "fungi-limit", "backflow-requirement"]),
    ("C4", "Chapter 4 — Roof Losses", 340, {"emergency-repair-authority": 5000}, ["roof-acv-age-threshold-years", "roof-min-payment-pct", "roof-comp-shingle-20yr-pct", "ordinance-law-pct"]),
    ("C5", "Chapter 5 — Fire and Smoke", 300, {"salvage-retention-days": 30}, ["debris-removal-pct", "fire-department-charge", "insured-to-value-pct"]),
    ("C6", "Chapter 6 — Theft and Mysterious Disappearance", 300, {"contents-inventory-days": 30}, ["special-limit-jewelry", "special-limit-firearms", "special-limit-silverware", "special-limit-money"]),
    ("C7", "Chapter 7 — Weather: Wind, Hail and Named Storms", 320, {"binding-suspension-hours": 48}, ["wind-hail-deductible-min-pct", "wind-hail-deductible-max-pct", "named-storm-period-hours", "wind-seacoast-max-pct"]),
    ("C8", "Chapter 8 — Liability Claims", 320, {"loss-notice-days": 30}, ["damage-to-property-of-others-limit", "medical-payments-years", "watercraft-hp-threshold"]),
    ("C9", "Chapter 9 — Mold, Fungi and Bacteria", 300, {"mitigation-duty-days": 5}, ["fungi-limit"]),
    ("C10", "Chapter 10 — Loss of Use and Additional Living Expense", 280, {"ale-max-months": 24}, ["cov-d-limit-pct"]),
    ("C11", "Chapter 11 — Proof of Loss, Appraisal and Suit", 320, {"appraisal-umpire-days": 15}, ["proof-of-loss-days", "appraisal-demand-days", "suit-limitation-years", "loss-payment-days"]),
    ("C12", "Chapter 12 — State Prompt Payment Standards", 340, {"claim-acknowledgement-days": 15}, ["claim-acknowledgement-days", "claim-decision-business-days", "claim-payment-business-days"]),
    ("C13", "Chapter 13 — Catastrophe Operations", 300, {"referral-loss-threshold": 50000}, ["named-storm-period-hours", "wind-deductible-notice-days"]),
    ("C14", "Chapter 14 — Condominium and Association Losses", 300, {"large-loss-report-threshold": 100000}, ["loss-assessment-limit", "loss-assessment-endorsement-limit", "cov-a-unit-owner-default"]),
    ("C15", "Chapter 15 — Dwelling Property Losses", 280, {"vacancy-days": 60}, ["vacancy-days", "cov-d-limit-pct"]),
    ("C16", "Chapter 16 — Ordinance or Law", 280, {"emergency-repair-authority": 2500}, ["ordinance-law-pct"]),
    ("C17", "Chapter 17 — Scheduled and High-Value Property", 280, {"contents-inventory-days": 60}, ["scheduled-property-deductible", "special-limit-jewelry"]),
    ("C18", "Chapter 18 — Subrogation and Salvage", 280, {"subrogation-notice-days": 10, "salvage-retention-days": 60}, ["referral-loss-threshold"]),
    ("C19", "Chapter 19 — Referral Triggers", 300, {"referral-loss-threshold": 25000, "reservation-of-rights-days": 10}, ["prior-claims-referral-count"]),
    ("C20", "Chapter 20 — Appendix: Form Provision Cross-Reference", 320, {"loss-notice-days": 60}, ["proof-of-loss-days", "suit-limitation-years", "vacancy-days"]),
]
RATING = [
    ("P1", "Part 1 — Rating Procedure", 240, {}, ["section-i-deductible-min", "insured-to-value-pct"]),
    ("P2", "Table 2 — Base Rates by Territory: HO-3", 900, {}, ["cov-b-limit-pct"]),
    ("P3", "Table 3 — Base Rates by Territory: HO-5", 900, {}, ["cov-c-limit-pct"]),
    ("P4", "Table 4 — Base Rates by Territory: HO-4 and HO-6", 900, {}, ["cov-d-limit-pct"]),
    ("P5", "Table 5 — Base Rates by Territory: DP-3", 900, {}, ["vacancy-days"]),
    ("P6", "Part 6 — Deductible Factors", 400, {"section-i-deductible-min": 500}, ["wind-hail-deductible-min-pct", "wind-hail-deductible-max-pct"]),
    ("P7", "Part 7 — Protective Device Credits", 320, {"protective-device-credit-pct": 15}, []),
    ("P8", "Part 8 — Roof Credits and Surcharges", 360, {"roof-credit-pct": 20}, ["roof-acv-age-threshold-years", "roof-max-age-years"]),
    ("P9", "Part 9 — Windstorm Mitigation Credits", 420, {"wind-mitigation-credit-pct": 35}, ["wind-hail-deductible-min-pct", "named-storm-period-hours"]),
    ("P10", "Table 10 — Endorsement Premiums", 1200, {}, ["water-backup-sublimit", "fungi-limit", "ordinance-law-pct", "extended-replacement-pct", "earthquake-deductible-pct", "identity-fraud-limit"]),
    ("P11", "Table 11 — Increased Limits Factors", 900, {}, ["special-limit-jewelry", "loss-assessment-limit", "credit-card-forgery-limit"]),
    ("P12", "Part 12 — State Exception Pages", 1400, {"wind-mitigation-credit-pct": 45, "roof-credit-pct": 10, "protective-device-credit-pct": 10, "earthquake-deductible-pct": 15}, ["wind-seacoast-max-pct", "earthquake-deductible-pct", "roof-acv-age-threshold-years"]),
]


def build_manuals(b: Build) -> dict[str, Document]:
    uw = manual(b, "manual.underwriting", "manuals/underwriting/manual.md", "Personal Lines Underwriting Manual", UW)
    cl = manual(b, "manual.claims", "manuals/claims/manual.md", "Property Claims Handling Manual", CLAIMS)
    rt = manual(b, "manual.rating", "manuals/rating/manual.md", "Homeowners and Dwelling Rating Manual", RATING)
    return {"underwriting": uw, "claims": cl, "rating": rt}


GUIDES = [  # (area, slug, title, state, facts)
    ("appetite", "fl-homeowners", "Florida Homeowners Appetite Guide", "FL", {"min-cov-a": 200000, "max-cov-a": 900000, "roof-inspection-age-years": 15, "roof-max-age-years": 20, "line-authority-cov-a": 600000, "senior-authority-cov-a": 900000, "prior-claims-referral-count": 2, "prior-claims-lookback-years": 5, "water-backup-referral-limit": 10000}),
    ("appetite", "tx-homeowners", "Texas Homeowners Appetite Guide", "TX", {"min-cov-a": 150000, "max-cov-a": 1200000, "roof-inspection-age-years": 15, "roof-max-age-years": 25, "line-authority-cov-a": 800000, "senior-authority-cov-a": 1200000, "prior-claims-referral-count": 2, "prior-claims-lookback-years": 3, "water-backup-referral-limit": 25000, "protection-class-max": 8}),
    ("appetite", "ca-homeowners", "California Homeowners Appetite Guide", "CA", {"min-cov-a": 300000, "max-cov-a": 2000000, "roof-inspection-age-years": 20, "line-authority-cov-a": 1000000, "prior-claims-referral-count": 2, "prior-claims-lookback-years": 5, "protection-class-max": 7}),
    ("appetite", "ny-homeowners", "New York Homeowners Appetite Guide", "NY", {"min-cov-a": 200000, "max-cov-a": 1500000, "line-authority-cov-a": 750000, "prior-claims-referral-count": 3, "prior-claims-lookback-years": 3, "protection-class-max": 8}),
    ("appetite", "la-homeowners", "Louisiana Homeowners Appetite Guide", "LA", {"min-cov-a": 125000, "max-cov-a": 750000, "roof-max-age-years": 20, "line-authority-cov-a": 500000, "prior-claims-referral-count": 2, "prior-claims-lookback-years": 5}),
    ("appetite", "nc-homeowners", "North Carolina Homeowners Appetite Guide", "NC", {"min-cov-a": 150000, "max-cov-a": 1000000, "roof-inspection-age-years": 18, "line-authority-cov-a": 700000, "prior-claims-referral-count": 2, "prior-claims-lookback-years": 3}),
    ("claims", "water-loss-handling", "Water Loss Claim Handling Guidance", None, {"referral-loss-threshold": 25000, "reservation-of-rights-days": 10}),
    ("claims", "roof-claim-handling", "Roof Claim Handling Guidance", None, {"referral-loss-threshold": 10000}),
    ("claims", "liability-claim-handling", "Liability Claim Handling Guidance", None, {"referral-loss-threshold": 50000, "reservation-of-rights-days": 15}),
    ("claims", "mold-claim-handling", "Fungi and Mold Claim Handling Guidance", None, {"referral-loss-threshold": 10000}),
    ("authority", "referral-matrix", "Underwriting Referral and Authority Matrix", None, {"line-authority-cov-a": 800000, "senior-authority-cov-a": 1500000, "water-backup-referral-limit": 25000, "prior-claims-referral-count": 2, "prior-claims-lookback-years": 3, "roof-max-age-years": 25}),
    ("authority", "binding-authority", "Binding Authority and Exceptions", None, {"line-authority-cov-a": 800000, "senior-authority-cov-a": 1500000}),
]
GUIDE_SECTION_OF = {"min-cov-a": "H.1", "max-cov-a": "H.1", "protection-class-max": "H.1", "roof-inspection-age-years": "H.2", "roof-max-age-years": "H.2", "water-backup-referral-limit": "H.4",
                    "prior-claims-referral-count": "H.5", "prior-claims-lookback-years": "H.5", "line-authority-cov-a": "H.7", "senior-authority-cov-a": "H.7", "referral-loss-threshold": "H.5", "reservation-of-rights-days": "H.6"}


def guide_toc() -> list[Section]:
    return [
        Section(id="H.0", title="Purpose and Status", target_lines=40, kind="prose"),
        Section(id="H.1", title="In Appetite", target_lines=120),
        Section(id="H.2", title="Roof Age and Condition", target_lines=110),
        Section(id="H.3", title="Wind and Hail", target_lines=90),
        Section(id="H.4", title="Water Backup", target_lines=100),
        Section(id="H.5", title="Prior Losses and Referral", target_lines=110),
        Section(id="H.6", title="Handling Procedures", target_lines=100),
        Section(id="H.7", title="Authority Limits", target_lines=90),
    ]


def build_guides(b: Build) -> dict[str, Document]:
    out = {}
    for area, slug, title, state, facts in GUIDES:
        doc = b.add_doc(Document(id=f"guide.{area}.{slug}", path=f"guidelines/{area}/{slug}.md", type="guide", title=title, state=state, voice="carrier-guide", sections=guide_toc()))
        for concept, value in facts.items():
            b.plant(doc, GUIDE_SECTION_OF[concept], concept, value)
        b.plant(doc, "H.3", "wind-mitigation-inspection-cov-a", 500000 if state in ("FL", "TX", "LA", "NC") else 1000000)
        b.plant(doc, "H.4", "loss-notice-days", 30 if area == "claims" else 60)
        b.plant(doc, "H.6", "mitigation-duty-days", 3 if area == "claims" else 7)
        b.distract(doc, "H.3", "wind-hail-deductible-min-pct", "wind-hail-deductible-max-pct", "wind-deductible-notice-days", "named-storm-period-hours")
        b.distract(doc, "H.4", "water-backup-sublimit", "water-backup-deductible", "backflow-requirement", "fungi-limit")
        b.distract(doc, "H.6", "claim-acknowledgement-days", "proof-of-loss-days", "suit-limitation-years", "section-i-deductible-min")
        b.distract(doc, "H.2", "roof-acv-age-threshold-years", "roof-min-payment-pct", "insured-to-value-pct")
        out[slug] = doc
    return out


def memo_toc() -> list[Section]:
    return [
        Section(id="M.1", title="Summary of Filing", target_lines=80, kind="prose"),
        Section(id="M.2", title="Changes to Definitions", target_lines=60),
        Section(id="M.3", title="Changes to Section I Coverages and Limits", target_lines=300),
        Section(id="M.4", title="Changes to Exclusions and Conditions", target_lines=260),
        Section(id="M.5", title="Changes to Section II", target_lines=90),
        Section(id="M.6", title="Renumbering and Editorial Changes", target_lines=70),
        Section(id="M.7", title="Rate and Premium Impact", target_lines=80),
    ]


def build_memoranda(b: Build, forms: dict[str, list[Document]], ends: dict[str, list[Document]]) -> list[Document]:
    memos = []
    targets = [(form_id("HO-3", "2018-09"), "HO-3", "2018-09"), (form_id("HO-3", "2024-03"), "HO-3", "2024-03"), (form_id("HO-5", "2022-06"), "HO-5", "2022-06"),
               (form_id("HO-4", "2021-10"), "HO-4", "2021-10"), (form_id("HO-6", "2023-02"), "HO-6", "2023-02"), (form_id("DP-3", "2020-08"), "DP-3", "2020-08"),
               (form_id("DP-3", "2026-01"), "DP-3", "2026-01"), ("end.ho-04-90.2027-01", "HO 04 90", "2027-01")]
    for doc_id, form, ed in targets:
        slug = form.replace(" ", "-")
        memo = b.add_doc(Document(id=f"memo.{slug.lower()}.{ed}", path=f"memoranda/{slug}-{ed}.md", type="memorandum", title=f"Filing Memorandum — {form} Edition {ed}", edition=ed, voice="filing-memo", sections=memo_toc()))
        # a memo restates the NEW values (interpretation authority) for the edition's changed facts
        diff = next((e for e in b.editions if e.newer == doc_id), None)
        if diff:
            for k, (_, new_fid) in enumerate(diff.changed[:12]):
                f = b.fact(new_fid) if hasattr(b, "fact") else next(x for x in b.facts if x.id == new_fid)
                sec = "M.5" if f.section.startswith("II") else "M.4" if f.section in ("I.X", "I.S", "G") else "M.3"
                b.plant(memo, sec, f.concept, f.value.value)
        b.plant(memo, "M.7", "premium-impact-pct", [3, 5, 2, 4, 6, 3, 7, 1][len(memos) % 8])
        if not any(f.document == memo.id and f.section == "M.5" for f in b.facts):
            b.plant(memo, "M.5", "loss-notice-days", 60)
        if not any(f.document == memo.id and f.section == "M.4" for f in b.facts):
            # the memo restates an unchanged condition from the new edition when nothing in M.4 changed
            base = next((f for f in b.facts if f.document == doc_id and f.concept == "proof-of-loss-days"), None)
            b.plant(memo, "M.4", "proof-of-loss-days", base.value.value if base else 60)
        b.distract(memo, "M.2", "insured-to-value-pct", "vacancy-days", "named-storm-period-hours")
        b.distract(memo, "M.6", "section-i-deductible-min", "cov-b-limit-pct", "cov-c-limit-pct")
        memos.append(memo)
    return memos


TRAINING = [  # (slug, title, restated facts {concept: (value, source doc id)}, distractor?)
    ("water-losses-101", "Water Losses 101", {"water-backup-sublimit": (10000, "end.ho-04-90.2027-01"), "water-backup-deductible": (1000, "end.ho-04-90.2027-01"), "fungi-limit": (10000, "end.ho-04-81.2018-09")}, False),
    ("roof-claims-and-the-schedule", "Roof Claims and the ACV Schedule", {"roof-min-payment-pct": (30, "end.ho-23-74.2025-05"), "roof-acv-age-threshold-years": (12, "end.ho-23-74.2025-05")}, False),
    ("choosing-the-governing-edition", "Choosing the Governing Edition", {"special-limit-jewelry": (2000, form_id("HO-3", "2024-03")), "proof-of-loss-days": (90, form_id("HO-3", "2024-03"))}, False),
    ("attaching-endorsements", "Attaching Endorsements Correctly", {"ordinance-law-pct": (25, "end.ho-04-16.2023-11"), "extended-replacement-pct": (25, "end.ho-04-20.2016-08")}, False),
    ("state-deductibles-explained", "State Wind and Hail Deductibles Explained", {"wind-hail-deductible-max-pct": (10, "amend.fl.ho-01-09.2023-07"), "named-storm-period-hours": (72, "amend.tx.ho-01-45.2022-01")}, False),
    ("guidance-versus-contract", "Guidance Versus Contract Language", {}, True),
    ("condo-master-policy-gap", "The Condominium Master Policy Gap", {"loss-assessment-endorsement-limit": (25000, "end.ho-04-35.2023-02"), "cov-a-unit-owner-default": (10000, form_id("HO-6", "2023-02"))}, False),
    ("customer-faq-homeowners", "Customer FAQ — Homeowners", {}, True),
]


def training_toc() -> list[Section]:
    return [
        Section(id="L.1", title="Learning Objectives", target_lines=40, kind="prose"),
        Section(id="L.2", title="Key Concepts", target_lines=220, kind="faq"),
        Section(id="L.3", title="Worked Examples", target_lines=260, kind="faq"),
        Section(id="L.4", title="Common Mistakes", target_lines=160, kind="faq"),
        Section(id="L.5", title="Quick Reference", target_lines=120, kind="table"),
        Section(id="L.6", title="Knowledge Check", target_lines=100, kind="faq"),
    ]


def build_training(b: Build) -> list[Document]:
    out = []
    for slug, title, facts, distractor in TRAINING:
        doc = b.add_doc(Document(id=f"training.{slug}", path=f"training/{slug}.md", type="training", title=title, voice="trainer", distractor=distractor, sections=training_toc()))
        for i, (concept, (value, _src)) in enumerate(facts.items()):
            b.plant(doc, ("L.2", "L.3", "L.5")[i % 3], concept, value)
        b.distract(doc, "L.3", "section-i-deductible-min", "insured-to-value-pct", "special-limit-jewelry", "water-backup-sublimit", "wind-hail-deductible-min-pct")
        b.distract(doc, "L.4", "proof-of-loss-days", "suit-limitation-years", "nonrenewal-notice-days", "loss-assessment-limit", "fungi-limit", "ordinance-law-pct")
        b.distract(doc, "L.5", "cov-b-limit-pct", "cov-c-limit-pct", "cov-d-limit-pct", "debris-removal-pct", "fire-department-charge", "roof-acv-age-threshold-years")
        out.append(doc)
    return out


# ---------------------------------------------------------------------------
# Derived: chains, contradictions, histories, compositions
# ---------------------------------------------------------------------------
def build_references(b: Build, forms, ends, amends, bulletins, manuals, guides, memos):
    D = {d.id: d for d in b.documents}
    ho3 = forms["HO-3"][-1]  # 2024-03
    # depth-3, cross-document: form S.5 -> state amendatory T.1 -> state bulletin (8 states where a wind/notice bulletin exists)
    wind_bulletin = {"TX": "bulletin.tx.b-2021-08-windstorm-deductibles", "FL": "bulletin.fl.oir-2022-01-hurricane-deductible", "LA": "bulletin.la.ldi-2020-07-hurricane-deductible",
                     "CO": "bulletin.co.doi-2019-05-hail-deductibles", "NC": "bulletin.nc.ncdoi-2021-06-claims-handling", "NY": "bulletin.ny.dfs-2016-02-nonrenewal",
                     "CA": "bulletin.ca.cdi-2022-03-earthquake-offer", "IL": "bulletin.il.idoi-2017-10-water-backup-disclosure"}
    for state in STATES:
        am = amends[state][-1]
        chain = f"chain.state-overlay.{state.lower()}"
        b.ref(chain, ho3, "I.S", am, dst_section="T.1", wording="where required by a state amendatory endorsement")
        b.ref(chain, am, "T.1", D[wind_bulletin[state]], dst_section="B.2", wording=f"as required by {STATE_NAMES[state]} bulletin")
        b.ref(chain, D[wind_bulletin[state]], "B.2", manuals["underwriting"], dst_section={"FL": "R500", "TX": "R510", "CA": "R520", "NY": "R530", "LA": "R540", "NC": "R550", "CO": "R560", "IL": "R570"}[state], wording="carrier implementation in the underwriting manual state exception")
    # depth-2: base-form exclusion -> endorsement write-back, per line
    for line, end_id, sec in (("HO-3", "end.ho-04-90.2027-01", "W.2"), ("HO-5", "end.ho-04-90.2027-01", "W.2"), ("HO-6", "end.ho-04-91.2019-03", "W.2"), ("HO-4", "end.ho-04-92.2019-03", "W.2"), ("DP-3", "end.dp-04-95.2021-05", "W.2")):
        f = forms[line][-1]
        b.ref(f"chain.water-backup.{line.lower()}", f, "I.X", D[end_id], dst_section="W.1", wording="unless a water backup endorsement is attached")
        b.ref(f"chain.water-backup.{line.lower()}", D[end_id], "W.1", D[end_id], dst_section=sec, wording="subject to the limit in")
    for line in ("HO-3", "HO-5", "DP-3"):
        f = forms[line][-1]
        b.ref(f"chain.roof.{line.lower()}", f, "I.A", D["end.ho-23-74.2025-05"], dst_section="W.1", wording="unless an actual cash value roof schedule endorsement is attached")
        b.ref(f"chain.roof.{line.lower()}", D["end.ho-23-74.2025-05"], "W.1", D["end.ho-23-74.2025-05"], dst_section="W.4", wording="never less than the floor in")
    for line in ("HO-3", "HO-5", "HO-6"):
        f = forms[line][-1]
        b.ref(f"chain.ordinance.{line.lower()}", f, "I.X", D["end.ho-04-16.2023-11"], dst_section="W.1", wording="unless an ordinance or law endorsement is attached")
        b.ref(f"chain.ordinance.{line.lower()}", D["end.ho-04-16.2023-11"], "W.1", D["end.ho-04-16.2023-11"], dst_section="W.2", wording="the most we will pay is stated in")
    for line in ("HO-3", "HO-5", "HO-4", "HO-6"):
        f = forms[line][-1]
        b.ref(f"chain.fungi.{line.lower()}", f, "I.X", D["end.ho-04-81.2018-09"], dst_section="W.1", wording="except as provided by a limited fungi endorsement")
        b.ref(f"chain.fungi.{line.lower()}", D["end.ho-04-81.2018-09"], "W.1", D["end.ho-04-81.2018-09"], dst_section="W.2", wording="up to the aggregate in")
    # depth-2 with a manual hop beyond line 3000: state appetite guide -> underwriting manual state exception -> rating manual state pages
    for state, guide_slug, rule in (("FL", "fl-homeowners", "R500"), ("TX", "tx-homeowners", "R510"), ("CA", "ca-homeowners", "R520"), ("NY", "ny-homeowners", "R530"), ("LA", "la-homeowners", "R540"), ("NC", "nc-homeowners", "R550")):
        g = guides[guide_slug]
        chain = f"chain.appetite.{state.lower()}"
        b.ref(chain, g, "H.7", manuals["underwriting"], dst_section=rule, wording="ceilings are set by the state exception rule")
        b.ref(chain, manuals["underwriting"], rule, manuals["rating"], dst_section="P12", wording="credits on the state exception pages of the rating manual")
    # definitions: endorsements use base-form defined terms
    for line, docs in forms.items():
        f = docs[-1]
        for e_docs in ends.values():
            for e in e_docs:
                if e.line == line:
                    for term in ("residence premises", "actual cash value", "sudden and accidental"):
                        dfn = f"{f.id}.def.{term.replace(' ', '-')}"
                        if any(d.id == dfn for d in b.definitions):
                            next(d for d in b.definitions if d.id == dfn).used_by.append(e.id)
        b.ref(f"chain.definition.{line.lower()}", f, "I.X", f, dst_definition=f"{f.id}.def.sudden-and-accidental", wording="as defined in Definitions")
        b.ref(f"chain.definition.{line.lower()}", f, "DEF", manuals["claims"], dst_section="C3", wording="the claims manual's duration test applies the definition")


def build_contradictions(b: Build):
    F = {f.id: f for f in b.facts}
    def fid(doc, sec, concept): return f"{doc}.{sec}.{concept}"
    items = [
        ("training.water-losses-101", "L.4", fid("end.ho-04-90.2027-01", "W.2", "water-backup-sublimit"), V("money", 5000), "stale"),
        ("training.roof-claims-and-the-schedule", "L.4", fid("end.ho-23-74.2025-05", "W.4", "roof-min-payment-pct"), V("percent", 25), "stale"),
        ("training.choosing-the-governing-edition", "L.4", fid(form_id("HO-3", "2018-09"), "I.C", "special-limit-jewelry"), V("money", 2000), "wrong-edition"),
        ("training.customer-faq-homeowners", "L.2", fid(form_id("HO-3", "2024-03"), "I.E", "fire-department-charge"), V("money", 500), "stale"),
        ("training.customer-faq-homeowners", "L.3", fid("end.ho-04-90.2027-01", "W.3", "water-backup-deductible"), V("money", 500), "stale"),
        ("training.guidance-versus-contract", "L.3", fid(form_id("HO-3", "2024-03"), "I.S", "proof-of-loss-days"), V("days", 60), "stale"),
        ("training.guidance-versus-contract", "L.4", fid("guide.appetite.fl-homeowners", "H.2", "roof-max-age-years"), V("years", 25), "misattributed"),
        ("manual.claims", "C12", fid("amend.tx.ho-01-45.2022-01", "T.5", "claim-decision-business-days"), V("days", 30), "stale"),
        ("manual.claims", "C4", fid("end.ho-23-74.2025-05", "W.1", "roof-acv-age-threshold-years"), V("years", 15), "stale"),
        ("guide.appetite.fl-homeowners", "H.2", fid("bulletin.fl.oir-2023-04-roof-age-nonrenewal", "B.2", "roof-acv-age-threshold-years"), V("years", 15), "stale"),
        ("memo.ho-3.2024-03", "M.3", fid(form_id("HO-3", "2024-03"), "I.C", "special-limit-firearms"), V("money", 2500), "overstated"),
        ("guide.claims.water-loss-handling", "H.6", fid("end.ho-04-90.2027-01", "W.6", "backflow-requirement"), V("boolean", False), "stale"),
        ("training.attaching-endorsements", "L.4", fid("end.ho-04-54.2021-12", "W.3", "earthquake-deductible-pct"), V("percent", 5), "wrong-edition"),
        ("training.state-deductibles-explained", "L.4", fid("amend.tx.ho-01-45.2022-01", "T.6", "wind-seacoast-max-pct"), V("percent", 5), "misattributed"),
    ]
    for i, (doc, sec, fact, wrong, kind) in enumerate(items, 1):
        if fact not in F:
            raise SystemExit(f"contradiction references unknown fact {fact}")
        b.contradictions.append(Contradiction(id=f"contra.{i:02d}", fact=fact, document=doc, section=sec, wrong_value=wrong, kind=kind))


def build_histories(b: Build, forms, bulletins):
    def series(hid, concept, entries, current=-1):
        es = [HistoryEntry(date=d, value=V(CONCEPT_BY_ID[concept][1], v), document=doc) for d, v, doc in entries]
        b.histories.append(History(id=hid, concept=concept, entries=es, current=(len(es) - 1 if current == -1 else current)))
    for line, docs in forms.items():
        for concept in ("special-limit-jewelry", "fire-department-charge", "nonrenewal-notice-days"):
            vals = [(d.effective, next((f.value.value for f in b.facts if f.document == d.id and f.concept == concept), None), d.id) for d in docs]
            vals = [v for v in vals if v[1] is not None]
            if len(vals) >= 2:
                series(f"hist.{line.lower()}.{concept}", concept, vals)
    series("hist.tx.wind-max", "wind-hail-deductible-max-pct", [("2016-08-19", 3, "bulletin.tx.b-2016-04-windstorm-deductibles"), ("2021-08-19", 5, "bulletin.tx.b-2021-08-windstorm-deductibles")])
    series("hist.fl.roof-threshold", "roof-acv-age-threshold-years", [("2019-11-05", 15, "bulletin.fl.oir-2019-11-roof-age"), ("2023-04-11", 10, "bulletin.fl.oir-2023-04-roof-age-nonrenewal")])
    series("hist.ca.eq-ded", "earthquake-deductible-pct", [("2014-06-30", 10, "bulletin.ca.cdi-2014-06-earthquake-offer"), ("2022-03-14", 15, "bulletin.ca.cdi-2022-03-earthquake-offer")])
    series("hist.ny.nonrenewal", "nonrenewal-notice-days", [("2010-09-01", 45, "bulletin.ny.dfs-2010-09-nonrenewal"), ("2016-02-22", 60, "bulletin.ny.dfs-2016-02-nonrenewal")])
    series("hist.co.hail-max", "wind-hail-deductible-max-pct", [("2013-01-15", 3, "bulletin.co.doi-2013-01-hail-deductibles"), ("2019-05-20", 5, "bulletin.co.doi-2019-05-hail-deductibles")])
    series("hist.ho0490.sublimit", "water-backup-sublimit", [("2010-10-01", 5000, "end.ho-04-90.2010-10"), ("2027-01-01", 10000, "end.ho-04-90.2027-01")])


def build_compositions(b: Build, forms, amends, guides, manuals):
    fb = b.fact_by
    def add(cid, scenario, *keys):
        facts = [fb[k] for k in keys if k in fb]
        if len({f.split(".")[0] + "." + f.split(".")[1] for f in facts}) < 4 and len({b.fact(f).document if hasattr(b, "fact") else next(x for x in b.facts if x.id == f).document for f in facts}) < 4:
            raise SystemExit(f"composition {cid} spans fewer than 4 documents: {facts}")
        b.compositions.append(Composition(id=cid, facts=facts, scenario=scenario))
    wb = {"HO-3": "end.ho-04-90.2027-01", "HO-5": "end.ho-04-90.2027-01", "HO-6": "end.ho-04-91.2019-03", "HO-4": "end.ho-04-92.2019-03", "DP-3": "end.dp-04-95.2021-05"}
    guide_of = {"FL": "guide.appetite.fl-homeowners", "TX": "guide.appetite.tx-homeowners", "CA": "guide.appetite.ca-homeowners", "NY": "guide.appetite.ny-homeowners", "LA": "guide.appetite.la-homeowners", "NC": "guide.appetite.nc-homeowners"}
    for state in STATES:
        f = forms["HO-3"][-1]; am = amends[state][-1]
        keys = [(f.id, "section-i-deductible-min"), (wb["HO-3"], "water-backup-sublimit"), (wb["HO-3"], "water-backup-deductible"), (am.id, "cancellation-notice-other-days"), ("manual.underwriting", "water-backup-referral-limit")]
        if state in guide_of:
            keys.append((guide_of[state], "water-backup-referral-limit"))
        add(f"comp.water.{state.lower()}", f"{STATE_NAMES[state]} HO-3 policy with water backup: sewer backup in a finished basement; what is payable, which deductible, who must approve the limit", *keys)
    for state in ("FL", "TX", "LA", "NC", "CO"):
        f = forms["HO-3"][-1]; am = amends[state][-1]
        add(f"comp.roof-wind.{state.lower()}", f"{STATE_NAMES[state]} hail loss to an aged roof: schedule, floor, and which deductible", (f.id, "insured-to-value-pct"), ("end.ho-23-74.2025-05", "roof-acv-age-threshold-years"), ("end.ho-23-74.2025-05", "roof-min-payment-pct"), (am.id, "wind-hail-deductible-min-pct"), ("manual.underwriting", "roof-inspection-age-years"))
    for ed in ("2014-04", "2023-02"):
        f = form_id("HO-6", ed)
        add(f"comp.condo.{ed}", "HO-6 unit owner assessed by the association after a hurricane", (f, "loss-assessment-limit"), (f, "cov-a-unit-owner-default"), ("end.ho-04-35.2023-02", "loss-assessment-endorsement-limit"), ("end.ho-04-91.2019-03", "water-backup-sublimit"), ("manual.claims", "referral-loss-threshold"))
    for ed in ("2020-08", "2026-01"):
        f = form_id("DP-3", ed)
        add(f"comp.dwelling.{ed}", "DP-3 vacant rental dwelling, vandalism after a tenant leaves, then a code upgrade", (f, "vacancy-days"), (f, "ordinance-law-pct"), ("end.dp-04-95.2021-05", "water-backup-sublimit"), ("amend.fl.dp-01-09.2021-03", "wind-hail-deductible-max-pct"), ("manual.underwriting", "vacancy-days"))
    add("comp.mold.ho3", "burst pipe then mold under HO-3 with HO 04 81", (form_id("HO-3", "2024-03"), "proof-of-loss-days"), ("end.ho-04-81.2018-09", "fungi-limit"), ("amend.nc.ho-01-32.2018-05", "fungi-limit"), ("guide.claims.mold-claim-handling", "referral-loss-threshold"), ("bulletin.nc.ncdoi-2018-03-fungi-disclosure", "fungi-limit"))
    add("comp.mold.ho4", "tenant's mold claim under HO-4 with HO 04 27", (form_id("HO-4", "2021-10"), "cov-d-limit-pct"), ("end.ho-04-27.2016-05", "fungi-limit"), ("end.ho-04-27.2016-05", "water-backup-sublimit"), ("manual.claims", "reservation-of-rights-days"), ("guide.claims.water-loss-handling", "referral-loss-threshold"))
    add("comp.authority.tx", "Texas $950k dwelling with two prior claims requesting a $30k backup limit", ("guide.appetite.tx-homeowners", "line-authority-cov-a"), ("guide.appetite.tx-homeowners", "prior-claims-referral-count"), ("guide.authority.referral-matrix", "water-backup-referral-limit"), ("manual.underwriting", "senior-authority-cov-a"), ("end.ho-04-90.2027-01", "water-backup-sublimit"))
    add("comp.authority.fl", "Florida new business, eight-year roof, HO 23 74 requested", ("bulletin.fl.oir-2023-04-roof-age-nonrenewal", "roof-acv-age-threshold-years"), ("guide.appetite.fl-homeowners", "roof-inspection-age-years"), ("end.ho-23-74.2025-05", "roof-acv-age-threshold-years"), ("manual.underwriting", "roof-max-age-years"), ("guide.authority.referral-matrix", "roof-max-age-years"))
    add("comp.edition.ho3", "which HO-3 edition governs a 2016 policy's jewelry theft and its proof-of-loss deadline, and what the memo says", (form_id("HO-3", "2011-05"), "special-limit-jewelry"), (form_id("HO-3", "2018-09"), "special-limit-jewelry"), (form_id("HO-3", "2024-03"), "special-limit-jewelry"), ("memo.ho-3.2024-03", "special-limit-jewelry"), ("training.choosing-the-governing-edition", "special-limit-jewelry"))
    add("comp.edition.dp3", "DP-3 insured-to-value threshold across three editions and the manual's eligibility rule", (form_id("DP-3", "2012-11"), "insured-to-value-pct"), (form_id("DP-3", "2020-08"), "insured-to-value-pct"), (form_id("DP-3", "2026-01"), "insured-to-value-pct"), ("manual.underwriting", "min-cov-a"), ("guide.authority.binding-authority", "line-authority-cov-a"))


# ---------------------------------------------------------------------------
def author() -> Ledger:
    b = Build()
    forms = build_forms(b)
    ends = build_endorsements(b, forms)
    amends = build_amendatory(b)
    bulletins = build_bulletins(b)
    manuals = build_manuals(b)
    guides = build_guides(b)
    # a fact lookup for the builders that need it
    b.fact = lambda fid: next(f for f in b.facts if f.id == fid)  # type: ignore[attr-defined]
    memos = build_memoranda(b, forms, ends)
    build_training(b)
    build_references(b, forms, ends, amends, bulletins, manuals, guides, memos)
    build_contradictions(b)
    build_histories(b, forms, bulletins)
    build_compositions(b, forms, amends, guides, manuals)
    # R2 targets: three or more synonyms AND facts in at least two voices, so
    # some answer-bearing document necessarily uses a non-canonical form.
    voices_by_concept: dict[str, set[str]] = {}
    docs_by_id = {d.id: d for d in b.documents}
    for f in b.facts:
        voices_by_concept.setdefault(f.concept, set()).add(docs_by_id[f.document].voice)
    concepts = [Concept(id=i, kind=k, canonical=c, synonyms=s, group=g, ambiguous=a,
                        synonym_target=(len(s) >= 3 and len(voices_by_concept.get(i, ())) >= 2)) for i, k, c, s, g, a in CONCEPTS]
    # every R2 concept is mentioned in several trainer and guide sections so at
    # least three of its forms occur somewhere in the corpus (V2)
    targets = [c.id for c in concepts if c.synonym_target]
    mention_docs = [d for d in b.documents if d.type in ("training", "guide", "memorandum")]
    for k, cid in enumerate(targets):
        for j in range(3):
            d = mention_docs[(k * 3 + j) % len(mention_docs)]
            sec = {"training": "L.6", "guide": "H.0", "memorandum": "M.1"}[d.type]
            b.distract(d, sec, cid)
    # the model lands near its target on average but drafts can run short;
    # eight percent of headroom keeps the corpus average above 1,000 lines
    for d in b.documents:
        for sec in d.sections:
            sec.target_lines = round(sec.target_lines * 1.08)
    return Ledger(documents=b.documents, concepts=concepts, facts=b.facts, definitions=b.definitions, references=b.references,
                  editions=b.editions, contradictions=b.contradictions, histories=b.histories, compositions=b.compositions)


def main() -> int:
    ledger = author()
    dump(ledger, OUT)
    from .report import main as report_main
    return report_main(["report", str(OUT)])


if __name__ == "__main__":
    raise SystemExit(main())
