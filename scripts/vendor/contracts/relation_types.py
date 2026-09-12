"""Normalising a document relation to one of six types. Contract C11.

The corpus brief defines six verbs and a direction rule. Measured effect of
adding it, over one clean regeneration:

                                   before    after
    relation candidates              84       123
    stated with a controlled verb     8        43   (9% -> 34%)
    direction correct, verifiable    1/3     23/33
    distinct directed edges          22        25

The other 80 are GENUINE relations expressed in synonyms — "replaces",
"overrides", "changes only", the noun "write-back", "does not restore". The
information is there; the vocabulary constraint held about a third of the time.

That is a tier-4 failure in the enforcement taxonomy, which is why the map
lives here rather than being trusted from the claim text. The brief raises the
signal; this produces the contract.
"""

from __future__ import annotations

import re

#: Ordered most-specific first; first match wins. Order matters: "replaces"
#: appears under both writes-back and supersedes, and an endorsement replacing
#: an exclusion is a write-back while an edition replacing an edition is a
#: supersession, so the exclusion-scoped pattern must be tried first.
PATTERNS: tuple[tuple[str, str], ...] = (
    (
        "writes-back",
        # `(?<!not )` because "does NOT restore" is a preserves, not a
        # write-back, and this pattern is tried first. Without the lookbehind
        # every negated restoration inverts to its opposite.
        r"\bwrit(?:e|es|ing|ten)[ -]back\b|\bwrite-back\b"
        r"|(?<!not )\brestor(?:e|es|ing)\b"
        # `[\s\S]` not `[^.]`: provision references contain dots ("A.3"), so a
        # dot-excluding gap never reaches the word "exclusion".
        r"|\boverrid(?:e|es)\b|\breplaces?\b[\s\S]{0,40}\bexclusion\b"
        r"|\bnotwithstanding\b|\bexcept as provided\b",
    ),
    (
        "preserves",
        r"\bpreserv(?:e|es)\b|\bcontinues? to apply\b|\bremains? in (?:full )?(?:force|effect)\b"
        r"|\bin full\b|\bunchanged\b|\bstill (?:applies|excluded)\b"
        r"|\bdoes not (?:restore|extend|provide)\b",
    ),
    (
        "supersedes",
        r"\bsupersede[sd]?\b|\bremains (?:the governing form|in force) for policies\b"
        r"|\bedition in force\b|\bprior edition\b|\bgoverning (?:form|edition)\b",
    ),
    (
        "implements",
        r"\bimplement(?:s|ed|ing)?\b|\bas required by\b|\bpursuant to\b|\bcarries out\b",
    ),
    (
        "constrains",
        r"\bmay not\b|\bmust not\b|\bprohibit(?:s|ed)?\b|\brequires? referral\b"
        r"|\boutside appetite\b|\brequires? (?:inspection|approval)\b|\bauthority\b",
    ),
    (
        "modifies",
        r"\bmodif(?:y|ies|ied)\b|\bamend(?:s|ed)?\b|\bchanges only\b|\bsubject to\b"
        r"|\bschedule in\b|\bsublimit\b|\bdeductible\b|\bsettle[sd]?\b|\blimits? (?:to|the)\b",
    ),
)

TYPES: tuple[str, ...] = tuple(name for name, _ in PATTERNS)

_COMPILED = tuple((name, re.compile(pattern, re.I)) for name, pattern in PATTERNS)


def normalize(statement: str) -> str | None:
    """Return one of TYPES, or None.

    None rather than a guess, deliberately. `preserves` and `writes-back` are
    opposites — HO 04 90 writes back Section I A.3 and expressly preserves A.1
    and A.2 — so a wrong type inverts a coverage answer. A missing type only
    withholds one.
    """
    text = statement or ""
    for name, pattern in _COMPILED:
        if pattern.search(text):
            return name
    return None
