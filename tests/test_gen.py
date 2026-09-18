"""The generator: renderer, sweep, slot checks, and a fake-drafted slice that
passes every validator. Corpus expansion ph. 02 §8."""
from __future__ import annotations

import json
import pathlib

import pytest

from gen import assemble, draft, plan, render, validate
from gen.plan import SectionJob, Slot
from ledger import author
from ledger.schema import FactValue

V = FactValue


# --- renderer -----------------------------------------------------------------


@pytest.mark.parametrize("n,w", [(0, "zero"), (5, "five"), (21, "twenty-one"), (100, "one hundred"), (2500, "two thousand five hundred"), (1500000, "one million five hundred thousand")])
def test_words(n, w):
    assert render.words(n) == w


def test_renderings_per_voice():
    assert render.render_value(V(kind="money", value=5000), "iso-form") == "five thousand dollars"
    assert render.render_value(V(kind="money", value=5000), "carrier-manual") == "$5,000"
    assert render.render_value(V(kind="percent", value=2), "regulator") == "two (2) percent"
    assert render.render_value(V(kind="days", value=1), "iso-form") == "one day"
    assert render.render_value(V(kind="business-days", value=15), "regulator") == "fifteen (15) business days"
    assert render.render_value(V(kind="business-days", value=1), "iso-form") == "one business day"
    assert render.render_value(V(kind="boolean", value=False), "trainer") == "is not required"
    assert "September 2018" in render.renderings(V(kind="date", value="2018-09"))


def test_value_occurrences_is_boundary_aware():
    assert render.value_occurrences("The limit is five hundred dollars.", V(kind="money", value=500)) == 1
    assert render.value_occurrences("The limit is two thousand five hundred dollars.", V(kind="money", value=500)) == 0
    assert render.value_occurrences("The limit is $2,500.", V(kind="money", value=500)) == 0
    assert render.value_occurrences("**100.12** Reports are valid for twelve months.", V(kind="count", value=12)) == 1
    assert render.value_occurrences("**100.12** Reports expire.", V(kind="count", value=12)) == 0


def test_unslotted_numerals():
    assert render.unslotted_numerals("We pay {{fact:x}} per loss under **A.3** of HO 04 90.") == []
    assert render.unslotted_numerals("We pay $500 per loss.") == ["$500", "500"]
    assert "twenty" in render.unslotted_numerals("within twenty days")
    assert render.unslotted_numerals("the eighty percent condition applies", ["eighty percent condition"]) == []
    assert render.unslotted_numerals("**110.3** applies; see Rule 210 and Section I.S.5") == []
    assert render.unslotted_numerals("**4.AB** Review the file; see 4.C and 120.AI.") == []
    # a bare small count word is prose; joined to a unit or another number word it is a value
    assert render.unslotted_numerals("if one or more of the following apply to two dwellings") == []
    assert render.unslotted_numerals("within ten days") == ["ten"]
    assert render.unslotted_numerals("twenty one percent") == ["twenty", "one"]
    assert "one" in render.unslotted_numerals("one hundred dollars")


# --- slot checks ----------------------------------------------------------------


def job(**kw) -> SectionJob:
    base = dict(document="d", section="S", title="T", kind="provisions", voice="iso-form", target_lines=12, numbering_prefix="S",
                slots=[Slot(marker="{{fact:a}}", kind="fact", concept_name="limit", concept_desc="the limit", value_kind="money")])
    base.update(kw)
    return SectionJob(**base)


def test_check_draft_rejects_missing_duplicate_unknown_numbers_and_length():
    j = job()
    good = "\n".join(["**S.1** The limit is {{fact:a}}."] + ["**S.%d** A further provision applies in the ordinary case." % i for i in range(2, 12)])
    assert draft.check_draft(j, good) == []
    assert any("appears 0" in p for p in draft.check_draft(j, good.replace("{{fact:a}}", "the limit")))
    assert any("appears 2" in p for p in draft.check_draft(j, good + "\nAgain {{fact:a}}."))
    assert any("unknown marker" in p for p in draft.check_draft(j, good + "\n{{fact:zzz}}"))
    assert any("unslotted" in p for p in draft.check_draft(j, good.replace("ordinary", "$500")))
    assert any("length" in p for p in draft.check_draft(j, "**S.1** {{fact:a}}."))
    assert any("heading" in p for p in draft.check_draft(j, good + "\n## Extra"))


def test_fake_drafter_satisfies_its_own_checks():
    j = job(refs=[plan.RefSlot(marker="{{ref:r}}", wording="as provided elsewhere", destination="X")], distractors=["eighty percent condition"])
    text = draft.fake_drafter(draft.build_prompt(j))
    assert draft.check_draft(j, text) == []
    assert "eighty percent condition" in text


def test_prompt_never_carries_a_value():
    j = job()
    p = draft.build_prompt(j)
    assert "{{fact:a}}" in p and "5,000" not in p and "five thousand" not in p


def test_job_hash_ignores_continuity_context():
    a, b = job(), job(previous_tail="something")
    assert a.hash() == b.hash()
    assert job(title="Other").hash() != a.hash()


# --- a fake-drafted slice passes every validator ------------------------------------

SLICE = ["form.ho3.2024-03", "form.ho3.2018-09", "end.ho-04-90.2027-01", "end.ho-04-90.2010-10", "amend.tx.ho-01-45.2022-01",
         "bulletin.tx.b-2021-08-windstorm-deductibles", "manual.underwriting", "guide.appetite.tx-homeowners", "memo.ho-3.2024-03",
         "training.water-losses-101", "training.customer-faq-homeowners", "end.ho-04-41.2011-05"]


@pytest.fixture(scope="module")
def built(tmp_path_factory):
    ledger = author.author()
    docs = [ledger.doc(d) for d in SLICE]
    out = tmp_path_factory.mktemp("corpus")
    jobs = [j for d in docs for j in plan.jobs_for(ledger, d)]
    drafts = draft.draft_all(jobs, drafter=draft.fake_drafter, concurrency=4, cache=False)
    placements = assemble.build_documents(ledger, docs, drafts, out)
    return ledger, docs, out, placements


def test_slice_passes_validators(built):
    ledger, docs, out, placements = built
    results = validate.run_all(ledger, out, placements, only_documents={d.id for d in docs})
    assert {k: v for k, v in results.items() if v} == {}


def test_no_marker_survives_and_every_fact_is_placed(built):
    ledger, docs, out, placements = built
    for d in docs:
        assert "{{" not in (out / d.path).read_text()
    for f in ledger.facts:
        if f.document in SLICE:
            assert f.id in placements and placements[f.id]["path"] == ledger.doc(f.document).path


def test_front_matter_is_exactly_twelve_lines_and_marks_supersession(built):
    ledger, docs, out, _ = built
    lines = (out / ledger.doc("form.ho3.2018-09").path).read_text().split("\n")
    assert lines[0] == "---" and lines[12].startswith("## ")
    assert any(l.startswith("> SUPERSEDED by") for l in lines[:12])
    newest = (out / ledger.doc("form.ho3.2024-03").path).read_text().split("\n")
    assert not any(l.startswith("> SUPERSEDED") for l in newest[:12])


def test_same_ledger_builds_identical_bytes(built, tmp_path):
    ledger, docs, out, _ = built
    jobs = [j for d in docs for j in plan.jobs_for(ledger, d)]
    drafts = draft.draft_all(jobs, drafter=draft.fake_drafter, concurrency=4, cache=False)
    assemble.build_documents(ledger, docs, drafts, tmp_path)
    for d in docs:
        assert (tmp_path / d.path).read_text() == (out / d.path).read_text(), d.id


def test_placements_serialise(built, tmp_path):
    _, _, _, placements = built
    assemble.write_placements(placements, tmp_path / "p.json")
    back = json.loads((tmp_path / "p.json").read_text())
    assert set(back) == set(placements)


def test_pdf_text_wrap_keeps_a_rendered_value_on_one_line():
    from gen.assemble import WRAP, wrap_paragraph
    para = ("**W.2** " + "word " * 14 + "is ten thousand dollars, including any covered expenses, " + "word " * 20
            + "The following are not covered: a. loss caused by flood; b. loss to property of others; (1) unless in custody.")
    lines = wrap_paragraph(para, ("ten thousand dollars",))
    assert all(len(l) <= WRAP for l in lines)
    assert sum("ten thousand dollars" in l for l in lines) == 1
    assert any(l.startswith("  a. ") for l in lines) and any(l.startswith("  (1) ") for l in lines)


def test_mangled_marker_is_repaired_when_unambiguous():
    from gen.draft import repair_markers
    from gen.plan import SectionJob, Slot
    j = SectionJob(document="d", section="S", title="T", kind="provisions", voice="iso-form", target_lines=12, numbering_prefix="S",
                   slots=[Slot(marker="{{fact:bulletin.tx.b-2021-08.B.3.named-storm-period-hours}}", kind="fact", concept_name="x", concept_desc="x", value_kind="hours")])
    fixed = repair_markers(j, "The period is {{fact:bulletin.tx-b-2021-08.B.3.named-storm-period-hours}} after landfall.")
    assert "{{fact:bulletin.tx.b-2021-08.B.3.named-storm-period-hours}}" in fixed
    assert repair_markers(j, "{{fact:something.else}}") == "{{fact:something.else}}"  # no unique match: left for the check
