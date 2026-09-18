"""The ledger loader and the authored ledger. Corpus expansion ph. 01 §5."""
from __future__ import annotations

import copy
import pathlib

import pytest
import yaml

from ledger import author, report
from ledger.schema import Ledger, dump, load

DATA = pathlib.Path(__file__).resolve().parents[1] / "ledger" / "data"


@pytest.fixture(scope="module")
def ledger() -> Ledger:
    return author.author()


@pytest.fixture(scope="module")
def raw(ledger, tmp_path_factory) -> dict:
    d = tmp_path_factory.mktemp("ledger")
    dump(ledger, d)
    return {f.stem: yaml.safe_load(f.read_text()) for f in d.glob("*.yaml")}


def reject(raw: dict, mutate, match: str):
    data = copy.deepcopy(raw)
    mutate(data)
    with pytest.raises(ValueError, match=match):
        Ledger.model_validate(data)


# --- loader rejections (ph. 01 §5) --------------------------------------------


def test_unknown_key_is_rejected(raw):
    reject(raw, lambda d: d["facts"][0].__setitem__("bogus", 1), "bogus")


def test_fact_planted_twice(raw):
    def mutate(d):
        fid = d["facts"][0]["id"]
        doc = next(x for x in d["documents"] if x["id"] == d["facts"][0]["document"])
        other = next(s for s in doc["sections"] if s["id"] != d["facts"][0]["section"])
        other.setdefault("facts", []).append(fid)
    reject(raw, mutate, "planted twice")


def test_fact_planted_nowhere(raw):
    def mutate(d):
        f = d["facts"][0]
        doc = next(x for x in d["documents"] if x["id"] == f["document"])
        sec = next(s for s in doc["sections"] if s["id"] == f["section"])
        sec["facts"].remove(f["id"])
    reject(raw, mutate, "planted nowhere")


def test_dangling_reference(raw):
    reject(raw, lambda d: d["references"][0].__setitem__("dst_document", "form.nope"), "unknown destination document")


def test_edition_diff_fact_from_wrong_edition(raw):
    def mutate(d):
        e = next(x for x in d["editions"] if x["changed"])
        other = next(f["id"] for f in d["facts"] if f["document"] not in (e["older"], e["newer"]))
        e["changed"][0] = [other, e["changed"][0][1]]
    reject(raw, mutate, "is not in")


def test_depth_target_the_toc_cannot_meet(raw):
    def mutate(d):
        f = next(x for x in d["facts"] if x["document"] == "manual.underwriting" and x["section"] == "R110")
        f["depth_target"] = 9000
    reject(raw, mutate, "cannot meet")


def test_density_violation(raw):
    def mutate(d):
        doc = next(x for x in d["documents"] if x["id"] == "manual.claims")
        for s in doc["sections"]:
            if s["id"] in ("C3", "C4", "C5"):
                for fid in list(s.get("facts", [])):
                    d["facts"] = [f for f in d["facts"] if f["id"] != fid]
                s["facts"] = []
    reject(raw, mutate, "R10")


def test_path_outside_the_contract(raw):
    reject(raw, lambda d: d["documents"][0].__setitem__("path", "notes/HO-3.md"), "CORPUS_PATH_RE")


def test_contradiction_equal_to_the_truth(raw):
    def mutate(d):
        c = d["contradictions"][0]
        f = next(x for x in d["facts"] if x["id"] == c["fact"])
        c["wrong_value"] = f["value"]
    reject(raw, mutate, "equals the fact's value")


# --- the authored ledger ------------------------------------------------------


def test_requirements_all_pass(ledger):
    failing = [k for k, (n, ok, note) in report.counts(ledger).items() if not ok]
    assert failing == [], failing


def test_every_fact_has_a_surface_form_of_its_concept(ledger):
    for f in ledger.facts:
        c = ledger.concept(f.concept)
        assert f.surface_form in [c.canonical, *c.synonyms]


def test_authoring_is_deterministic(tmp_path):
    a, b = tmp_path / "a", tmp_path / "b"
    dump(author.author(), a)
    dump(author.author(), b)
    for f in sorted(a.glob("*.yaml")):
        assert f.read_text() == (b / f.name).read_text(), f.name


def test_dump_load_round_trip(ledger, tmp_path):
    dump(ledger, tmp_path)
    again = load(tmp_path)
    assert again.model_dump() == ledger.model_dump()


def test_checked_in_data_matches_the_author_script(ledger):
    """ledger/data is generated; a hand edit there would be lost on the next
    author run, so it must equal what author.py produces."""
    assert DATA.exists(), "run `uv run python -m ledger.author` to write ledger/data"
    assert load(DATA).model_dump() == ledger.model_dump()


def test_no_contradiction_is_planted_as_a_fact(ledger):
    """A misstatement is planted text with the wrong value; it must not also be
    a fact, or gold would cite the wrong document."""
    fact_docs = {(f.document, f.concept) for f in ledger.facts}
    for c in ledger.contradictions:
        concept = ledger.fact(c.fact).concept
        assert (c.document, concept) not in fact_docs or ledger.fact(c.fact).document != c.document
