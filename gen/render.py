"""Typed values -> the words a document of that voice uses. Ph. 02 §3.

The validator accepts ANY of a value's renderings, so a fact is found whether
the file says "five thousand dollars" or "$5,000". Renderings are the only
place a number becomes text, which is what makes "no unslotted numerals" a
checkable rule: a numeral in a draft is a model inventing a value.
"""
from __future__ import annotations

import re

import _paths  # noqa: F401
from ledger.schema import Concept, Document, FactValue, Reference

ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


def words(n: int) -> str:
    """Integer -> English words, the way a policy form spells amounts."""
    if n < 0:
        return "minus " + words(-n)
    if n < 20:
        return ONES[n]
    if n < 100:
        return TENS[n // 10] + ("" if n % 10 == 0 else "-" + ONES[n % 10])
    if n < 1000:
        return ONES[n // 100] + " hundred" + ("" if n % 100 == 0 else " " + words(n % 100))
    if n < 1_000_000:
        return words(n // 1000) + " thousand" + ("" if n % 1000 == 0 else " " + words(n % 1000))
    return words(n // 1_000_000) + " million" + ("" if n % 1_000_000 == 0 else " " + words(n % 1_000_000))


def _num(v) -> int:
    return int(v) if float(v) == int(float(v)) else v


def renderings(value: FactValue) -> list[str]:
    """Every acceptable text form of a value, canonical (voice-specific) first."""
    k, v = value.kind, value.value
    if k == "money":
        n = _num(v)
        return [f"{words(n)} dollars", f"${n:,}", f"${n:,} ({words(n)} dollars)", f"${n:,}.00"]
    if k == "percent":
        n = _num(v)
        return [f"{words(n)} percent", f"{n}%", f"{words(n)} ({n}) percent", f"{n} percent"]
    if k in ("days", "years", "hours", "feet", "count"):
        unit = {"days": "days", "years": "years", "hours": "hours", "feet": "feet", "count": ""}[k]
        n = _num(v)
        w = words(n)
        if k == "count":
            return [w, str(n), f"{w} ({n})"]
        singular = unit[:-1] if n == 1 and unit.endswith("s") else unit
        if k == "feet" and n == 1:
            singular = "foot"
        return [f"{w} {singular}", f"{n} {singular}", f"{w} ({n}) {singular}"]
    if k == "horsepower":
        n = _num(v)
        return [f"{words(n)} horsepower", f"{n} horsepower", f"{n} hp"]
    if k == "date":
        y, m = str(v).split("-")[:2]
        return [f"Edition {y}-{m}", f"{MONTHS[int(m) - 1]} {y}", f"{m}/{y}", f"the {y} edition"]
    if k == "boolean":
        return ["is required", "required"] if v else ["is not required", "not required"]
    if k in ("text", "enum"):
        return [str(v)]
    raise ValueError(k)


def render_value(value: FactValue, voice: str) -> str:
    """The rendering a document of this voice uses. Index into renderings()."""
    r = renderings(value)
    if value.kind == "boolean":
        return r[0]
    pick = {"iso-form": 0, "regulator": 2, "carrier-manual": 1, "carrier-guide": 1, "filing-memo": 2, "trainer": 2}[voice]
    return r[min(pick, len(r) - 1)]


def render_reference(ref: Reference, src: Document, dst: Document, dst_title: str | None) -> str:
    """The ledger's wording plus a locator the reader can follow."""
    if ref.dst_definition:
        where = f'as defined in the Definitions of {dst.title}' if dst.id != src.id else "as defined in the Definitions"
        return f"{ref.wording} ({where})"
    if dst.id == src.id:
        return f"{ref.wording} (see {ref.dst_section}, {dst_title})"
    return f"{ref.wording} (see {dst.title}, {ref.dst_section} {dst_title})"


def surface(concept: Concept, voice: str, salt: int = 0) -> str:
    """The form of a concept this voice uses; `salt` rotates for distractor
    mentions so every synonym appears somewhere in the corpus (V2)."""
    forms = [concept.canonical, *concept.synonyms]
    base = {"iso-form": 0, "regulator": 1, "carrier-manual": 2, "carrier-guide": 3, "filing-memo": 1, "trainer": 2}[voice]
    return forms[(base + salt) % len(forms)]


def value_occurrences(text: str, value: FactValue) -> int:
    """How many times a value's rendering occurs in `text` as a value of its
    own — not as the tail of a larger number ("five hundred dollars" inside
    "two thousand five hundred dollars") and not as digits inside an
    identifier ("12" inside "100.12")."""
    low = " ".join(text.split()).lower()
    n = 0
    for r in renderings(value):
        r = r.lower()
        # digit adjacency matters only at a digit edge: "12" must not match inside
        # "100.12" or "$5,000", but "sixty (60) days," is a value followed by a comma
        pre = r"(?<![\w$])" if not r[0].isdigit() else r"(?<![\w$.,\-])"
        post = r"(?![\w\-])" if not r[-1].isdigit() else r"(?!\d|[.,]\d|[\w\-])"
        pat = re.compile(pre + re.escape(r) + post)
        for m in pat.finditer(low):
            before = low[:m.start()].rstrip()
            prev = re.findall(r"[a-z\-]+$", before)
            if prev and (prev[0] in NUMBER_WORDS or all(p in NUMBER_WORDS for p in prev[0].split("-"))):
                continue
            n += 1
        if n:
            break
    return n


# --- the unslotted-numeral sweep ---------------------------------------------------
NUMBER_WORDS = set(ONES[1:] + [t for t in TENS if t] + ["hundred", "thousand", "million"])
_ALLOWED_DIGIT_PATTERNS = [
    re.compile(r"\*\*[A-Z]{1,3}\.\d+(?:\.\d+)?\*\*"),      # **A.1**, **B.2.1**, **210.A** handled below
    re.compile(r"\*\*\d{3}\.[A-Z]\*\*"),                     # **210.A**
    re.compile(r"\*\*\d{1,3}\.\d+(?:\.\d+)?\*\*"),         # **110.1**, **12.3.4** — bold paragraph numbers are structure
    re.compile(r"\*\*\d+\.\*\*"),                            # **1.**
    re.compile(r"\b(?:Rule|Chapter|Part|Table|Section|Paragraph)s? \d{1,3}(?:\.\d+)?\b"),
    re.compile(r"\b[A-Z]{1,3}\.\d+(?:\.\d+)?\b"),           # A.3, I.S.5, T.1
    re.compile(r"\b(?:HO|DP) \d{2} \d{2}\b"),               # HO 04 90
    re.compile(r"\b(?:HO|DP)-\d\b"),                        # HO-3
    re.compile(r"\b[A-Z]{1,5}-\d{4}-\d{2}\b"),              # B-2021-08
    re.compile(r"\bC\d{1,2}\b|\bR\d{3}\b|\bP\d{1,2}\b|\bW\.\d\b|\bM\.\d\b|\bL\.\d\b|\bH\.\d\b"),
]


def unslotted_numerals(text: str, allowed_phrases: tuple[str, ...] | list[str] = ()) -> list[str]:
    """Numbers, amounts and number words in prose that are not inside a slot,
    an allowed identifier, or an allowed phrase (concept names such as "eighty
    percent condition" are the one legitimate place a number word appears).
    Empty means the draft invented nothing."""
    scrub = re.sub(r"\{\{[^}]*\}\}", " ", text)
    for phrase in sorted(allowed_phrases, key=len, reverse=True):
        scrub = re.sub(re.escape(phrase), " ", scrub, flags=re.I)
    for pat in _ALLOWED_DIGIT_PATTERNS:
        scrub = pat.sub(" ", scrub)
    hits = []
    hits += re.findall(r"\$\s?\d[\d,]*(?:\.\d+)?", scrub)
    hits += re.findall(r"\b\d[\d,]*(?:\.\d+)?\s?%", scrub)
    hits += re.findall(r"\b\d[\d,]*(?:\.\d+)?\b", scrub)
    for w in re.findall(r"[A-Za-z\-]+", scrub):
        low = w.lower()
        if low in NUMBER_WORDS or (("-" in low) and all(p in NUMBER_WORDS for p in low.split("-"))):
            hits.append(w)
    return hits
