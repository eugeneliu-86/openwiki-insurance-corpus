"""The drafting call, the slot checks, the cache. Ph. 02 §2.

One model call per section. The model writes prose around slots and never
sees a value. A draft is rejected before it reaches a file if it omits or
duplicates a slot, invents a number, misses its length band, or names a
section id that is not a reference. Drafts are cached by job hash so a
re-build with an unchanged ledger makes no model calls.
"""
from __future__ import annotations

import concurrent.futures as cf
import hashlib
import os
import pathlib
import re
import sys
from collections.abc import Callable

from .plan import SectionJob
from .render import unslotted_numerals
from .voices import CARDS

CACHE_DIR = pathlib.Path(os.environ.get("DRAFT_CACHE_DIR", pathlib.Path(__file__).resolve().parent.parent / ".draft-cache"))
MODEL = "gpt-5.6-terra"
DEFAULT_BASE_URL = "https://gateway.smith.langchain.com/openai/v1"
MAX_ATTEMPTS = 3

KIND_GUIDANCE = {
    "prose": "Write continuous prose paragraphs. No numbered provisions.",
    "provisions": "Write numbered provisions in this voice's numbering style, using the numbering prefix given.",
    "definitions": "Write a numbered list of defined terms. Each entry begins with the bold number and the term in double quotes, where the term is the slot marker, then 'means' and a definition of three to five sentences with an example of what the term does and does not include. Use each term's marker ONLY in its own heading position; when a term is mentioned inside another definition, write the word plainly without any marker. Do not define anything that is not a slot.",
    "faq": "Write the section in the trainer's question-and-answer or worked-example style as the section title suggests.",
    "table": "Do not write a table. Write two or three short paragraphs introducing what the table (which will be generated separately) contains.",
    "schedule": "Write two or three short paragraphs introducing the schedule; the schedule itself is generated separately.",
}


def build_prompt(job: SectionJob) -> str:
    slots = "\n".join(
        f"- {s.marker} — {('the defined term ' if s.kind == 'definition' else 'the ' + s.value_kind + ' value of ')}\"{s.concept_name}\" ({s.concept_desc})"
        + (f". Constraint: {s.phrasing}" if s.phrasing else "")
        for s in job.slots) or "(none)"
    refs = "\n".join(f"- {r.marker} — write the phrase \"{r.wording}\" and put this marker immediately after it; it points to {r.destination}" for r in job.refs) or "(none)"
    distract = ", ".join(f'"{d}"' for d in job.distractors) or "(none)"
    return f"""You are drafting one section of an insurance document. Follow the style card exactly.

STYLE CARD
{CARDS[job.voice]}

DOCUMENT
{job.document_context}

SECTION
Title: {job.title}
Kind: {job.kind}. {KIND_GUIDANCE[job.kind]}
Numbering prefix for paragraphs: {job.numbering_prefix}
Target length: about {job.target_lines} lines of Markdown (a line is a paragraph or a blank line; aim for paragraphs of two to five sentences). Stay within 70% to 140% of the target.
{('Previous section ended with:\n' + job.previous_tail) if job.previous_tail else ''}

SLOTS — use EVERY marker below EXACTLY ONCE, verbatim, where the value belongs in the sentence. The marker will be replaced by the actual value. Write the sentence so the value reads naturally in that position (for a money value: "The most we will pay is {{{{…}}}}."; for a boolean written as "is required"/"is not required": "A backwater valve {{{{…}}}} where …").
{slots}

REFERENCES — write each phrase and place its marker right after the phrase:
{refs}

MENTION WITHOUT NUMBERS — refer to these concepts by these exact names somewhere in the section, saying nothing quantitative about them (no amounts, no periods, no percentages):
{distract}

RULES
1. Every slot marker exactly once. No marker you were not given.
2. Invent no numbers: no digits, dollar amounts, percentages, dates, periods, form numbers, or number words (one, two, ten, twenty, hundred, thousand …) anywhere outside the markers. Paragraph numbering with the given prefix (e.g. **{job.numbering_prefix}.1**) is the only exception.
3. Do not state any slot's fact in other words elsewhere in the section.
4. Do not refer to other sections or documents except through the reference markers given.
5. Output only the section body in Markdown. No section heading, no title, no preamble, no closing remarks.
"""


class DraftRejected(Exception):
    pass


def check_draft(job: SectionJob, text: str) -> list[str]:
    """Why a draft is unusable; empty when it is fine."""
    problems = []
    for s in job.slots:
        n = text.count(s.marker)
        if n != 1:
            problems.append(f"slot {s.marker} appears {n} times")
    for r in job.refs:
        n = text.count(r.marker)
        if n != 1:
            problems.append(f"reference {r.marker} appears {n} times")
    known = {s.marker for s in job.slots} | {r.marker for r in job.refs}
    for m in set(re.findall(r"\{\{[^}]*\}\}", text)):
        if m not in known:
            problems.append(f"unknown marker {m}")
    if job.kind not in ("table", "schedule"):
        nums = unslotted_numerals(text, [s.concept_name for s in job.slots] + job.distractors)
        if nums:
            problems.append(f"unslotted numerals: {sorted(set(nums))[:8]}")
    lines = text.count("\n") + 1
    lo, hi = int(job.target_lines * 0.7), int(job.target_lines * 1.4)
    if job.kind == "definitions":
        # a glossary is two lines per term (entry + blank) however long the target says;
        # the floor is the number of terms, and the model is not asked to pad it
        ndefs = sum(1 for s in job.slots if s.kind == "definition")
        lo = min(int(job.target_lines * 0.4), max(3, 2 * ndefs - 1))
    if job.kind in ("table", "schedule"):
        lo, hi = 3, 40
    if not lo <= lines <= hi:
        problems.append(f"length {lines} lines, wanted {lo}-{hi}")
    if re.search(r"^#{1,6} ", text, re.M):
        problems.append("contains a heading")
    return problems


# --- drafters ------------------------------------------------------------------------
Drafter = Callable[[str], str]


def _model():
    from langchain.chat_models import init_chat_model

    key = os.environ.get("LANGSMITH_API_KEY_GATEWAY") or os.environ.get("ANTHROPIC_API_KEY")
    if not key or key.startswith("lsv2_pt_"):
        raise RuntimeError("drafting needs the gateway key in LANGSMITH_API_KEY_GATEWAY (lsv2_sk_…)")
    return init_chat_model(MODEL, model_provider="openai", base_url=(os.environ.get("MODEL_BASE_URL") or DEFAULT_BASE_URL).rstrip("/"),
                           api_key=key, use_responses_api=True, reasoning={"effort": "medium"}, verbosity="medium", max_tokens=16000)


_MODEL = None


def real_drafter(prompt: str) -> str:
    global _MODEL
    if _MODEL is None:
        _MODEL = _model()
    out = _MODEL.invoke(prompt)
    content = out.content if isinstance(out.content, str) else "".join(b.get("text", "") for b in out.content if isinstance(b, dict))
    return content.strip()


def fake_drafter(prompt: str) -> str:
    """Deterministic filler that satisfies every check: used by tests and by
    dry builds. Reads the slots and refs back out of the prompt."""
    slots = re.findall(r"^- (\{\{(?:fact|def|contra):[^}]+\}\}) — (?:the defined term |the [\w-]+ value of )\"([^\"]+)\"", prompt, re.M)
    refs = re.findall(r"^- (\{\{ref:[^}]+\}\}) — write the phrase \"([^\"]+)\"", prompt, re.M)
    mentions = re.findall(r"MENTION WITHOUT NUMBERS[^\n]*\n(.*)\n", prompt)
    names = re.findall(r'"([^"]+)"', mentions[0]) if mentions and mentions[0] != "(none)" else []
    target = int(re.search(r"about (\d+) lines", prompt).group(1))
    kind = re.search(r"Kind: (\w+)", prompt).group(1)
    prefix = re.search(r"Numbering prefix for paragraphs: (\S+)", prompt).group(1)
    if kind in ("table", "schedule"):
        return "This part sets out the schedule that follows.\n\nThe entries below are applied in the order shown.\n\nRefer to the introductory rule for how factors combine."
    paras = []
    i = 1
    for s, name in slots:
        if s.startswith("{{def:"):
            paras.append(f"**{i}.** \"{s}\" means the thing this document uses that term for, as applied throughout this section and read together with the other defined terms.")
        else:
            paras.append(f"**{prefix}.{i}** Under this provision the {name} is {s}, and it applies as stated here regardless of any other provision of this section.")
        i += 1
    for r, wording in refs:
        paras.append(f"**{prefix}.{i}** This provision applies {wording} {r}, and nothing here enlarges what is provided there.")
        i += 1
    for n in names:
        paras.append(f"**{prefix}.{i}** The {n} is addressed elsewhere in this policy and is not changed by this provision.")
        i += 1
    filler = "**{p}.{i}** This paragraph restates the general rule of this section in the ordinary case and confirms that the conditions stated above continue to apply."
    while (len(paras) * 2 - 1) < int(target * 0.98):
        paras.append(filler.format(p=prefix, i=i)); i += 1
    return "\n\n".join(paras)


def draft(job: SectionJob, drafter: Drafter = real_drafter, cache: bool = True) -> str:
    """A checked draft for the job, from cache when available."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    key = job.hash() + ("" if drafter is real_drafter else "-fake")
    path = CACHE_DIR / f"{key}.md"
    if cache and path.exists():
        return path.read_text()
    prompt = build_prompt(job)
    problems: list[str] = []
    for attempt in range(MAX_ATTEMPTS):
        if problems:
            print(f"[retry {attempt}] {job.document}/{job.section}: {'; '.join(problems)[:200]}", file=sys.stderr, flush=True)
        text = drafter(prompt if not problems else prompt + "\n\nYOUR PREVIOUS ATTEMPT WAS REJECTED FOR:\n- " + "\n- ".join(problems) + "\nFix every item and output the whole section again.")
        problems = check_draft(job, text)
        if not problems:
            if cache:
                path.write_text(text)
            return text
    raise DraftRejected(f"{job.document}/{job.section}: " + "; ".join(problems))


def draft_all(jobs: list[SectionJob], drafter: Drafter = real_drafter, concurrency: int = 8, cache: bool = True) -> dict[tuple[str, str], str]:
    out: dict[tuple[str, str], str] = {}
    with cf.ThreadPoolExecutor(max_workers=concurrency) as pool:
        futs = {pool.submit(draft, j, drafter, cache): j for j in jobs}
        for fut in cf.as_completed(futs):
            j = futs[fut]
            out[(j.document, j.section)] = fut.result()
    return out
