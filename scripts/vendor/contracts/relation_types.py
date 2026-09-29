"""Maps a claim's wording to one of six document-relation types.

The compile brief asks for six controlled verbs, but claims use them only about
a third of the time; the rest say "replaces", "overrides", "does not restore".
So the type is read from the wording here rather than trusted from the claim.
"""

from __future__ import annotations

import re

#: Most specific first; the first match wins. writes-back is tried before supersedes because
#: an endorsement replacing an exclusion is a write-back, not a supersession.
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
    """One of TYPES, or None rather than a guess: preserves and writes-back are opposites."""
    text = statement or ""
    for name, pattern in _COMPILED:
        if pattern.search(text):
            return name
    return None
