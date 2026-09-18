"""The edge layer — graph-expansion phase 02.

The corpus already states how its parts connect; this module derives those
statements into one artifact so the agent can follow them instead of searching
for them. No model is involved anywhere here.

    refers_to    provision -> section        from the text: "(see <Title>, <section> …)" and
                                             "(see <section>, <title>)" for a same-document reference
    cites        claim -> provision          a claim's evidence pointer intersected with the provisions index
    supersedes   document -> document        newer edition of the same form family
    amends       amendatory -> base form     the state amendatory endorsement and the line it amends
    attaches_to  endorsement -> base form    the endorsement and the line it is written for
    lists        index page -> page          the wiki's navigation layer, from its markdown links

Structure edges (section -> provisions, provision <-> neighbours) are not stored:
they are the provisions index's order and the graph module derives them on read.
The claims index's typed document relations (`relates`) are already committed and
are read from there.

Two callers share the builder, as with the provisions index: the refresh
workflow commits `.graph-edges.json` per commit from the vendored copy; the agent
reads it when it matches the tree and otherwise builds the same artifact in
memory. Acceptance is by content — the artifact carries a fingerprint of the
provisions index it was built over — never by SHA, because the workflow commits
one commit behind the SHA the agent pins.

Vendored copy: this file runs on stdlib Python in the corpus workflow; it
imports nothing from langchain.
"""

from __future__ import annotations

import hashlib
import json
import re
from typing import Any

from tools.provisions import FRONT_MATTER_LINES, _match_section, is_source

SCHEMA_VERSION = 1

#: "(see Personal Lines Underwriting Manual, R510 Rule 510 — Texas State Exceptions)"
#: "(see HO 01 09 Florida Amendatory Endorsement (Edition 2021-03), T.1 Windstorm and Hail Deductible)"
#: "(see W.2, Limit of Liability)"  — same document
#: one level of nested parentheses allowed for the form title's "(Edition …)"
SEE = re.compile(r"\(see ((?:[^()]|\([^()]*\))+)\)")
DEFINED = re.compile(r"\(as defined in the Definitions\)")
#: a section id as the corpus writes one: W.2, I.S, B.2, T.1, DEF, R510, P12, C3, Rule 510, Part 12, Chapter 3, Table 2
SECTION_ID = re.compile(r"^((?:Rule|Part|Chapter|Table) \d{1,3}|[A-Z]\d{1,3}|[A-Z]{1,4}(?:\.[A-Z0-9]{1,3})*)$")
LINK = re.compile(r"^\s*- \[([^\]]+)\]\(([^)]+)\)")
TITLE = re.compile(r'^title:\s*"?(.+?)"?\s*$')
KEY = re.compile(r"^(type|line|state|edition|effective):\s*(.+?)\s*$")


# --- front matter -----------------------------------------------------------------
def front_matter(lines: list[str]) -> dict[str, str]:
    out: dict[str, str] = {}
    for l in lines[:FRONT_MATTER_LINES]:
        m = TITLE.match(l)
        if m:
            out["title"] = m.group(1)
            continue
        k = KEY.match(l)
        if k:
            out[k.group(1)] = k.group(2)
    return out


def family(path: str) -> str | None:
    """forms/HO/MS/HO-3/2018-09.md -> forms/HO/MS/HO-3 : the editions of one form."""
    parts = path.split("/")
    return "/".join(parts[:4]) if path.startswith("forms/") and len(parts) == 5 else None


# --- the reference extractor -------------------------------------------------------
def split_reference(body: str, titles: dict[str, str] | None = None) -> tuple[str | None, str | None, str]:
    """"<Title>, <section …>" -> (title, section token, remainder). A body that starts
    with a section id is a same-document reference: (None, section, remainder).

    Titles can carry commas ("HO 04 81 Limited Fungi, Wet or Dry Rot, or Bacteria
    Coverage (Edition 2018-09)"), so a known title is matched as a prefix first and
    the comma split is the fallback."""
    body = " ".join(body.split())
    head = tail = None
    for t in sorted(titles or {}, key=len, reverse=True):
        if body == t or body.startswith(t + ", "):
            head, tail = t, body[len(t) + 2:]
            break
    if head is None:
        # split at the first ", " that is outside parentheses
        depth, cut = 0, -1
        for i, ch in enumerate(body):
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
            elif body.startswith(", ", i) and depth == 0:
                cut = i
                break
        head, tail = (body[:cut], body[cut + 2:]) if cut >= 0 else (body, "")
    if SECTION_ID.match(head.strip()):
        return None, head.strip(), tail
    sec = tail.split(" — ")[0].strip()
    # "R510 Rule 510" -> "Rule 510"; "T.1 Windstorm and Hail Deductible" -> "T.1"
    m = re.match(r"^([A-Z]\d{1,3}) ((?:Rule|Part|Chapter|Table) \d{1,3})\b", sec)
    if m:
        sec = m.group(2)
    else:
        first = sec.split(" ")[0]
        sec = first if SECTION_ID.match(first) else sec
    return head.strip(), (sec or None), tail


def _provision_at(provisions: list[dict], line: int) -> dict | None:
    return next((p for p in provisions if p["start"] <= line <= p["end"]), None)


def extract_references(corpus, pindex: dict, titles: dict[str, str]) -> tuple[list[dict], list[dict]]:
    """(edges, unresolved). One `refers_to` edge per rendered reference, from the
    provision that carries it to the section it names."""
    edges: list[dict] = []
    unresolved: list[dict] = []
    from tools.provisions import text_of

    # over each provision's rejoined text, not line by line: on pdf-text documents a
    # reference wraps across lines and a page header can cut through it
    for p in pindex["provisions"]:
        doc = p["document"]
        body = " ".join(text_of(corpus, p).split())
        for m in list(SEE.finditer(body)) + list(DEFINED.finditer(body)):
            src_id = p["id"]
            text = m.group(0)
            if m.re is DEFINED:
                sec = next((s for s in pindex["sections"].get(doc, []) if "definition" in (s["title"] or s["id"]).lower()), None)
                if sec:
                    edges.append({"from": src_id, "to": f"{doc}#{sec['id']}", "type": "refers_to", "via": "text", "label": text})
                else:
                    unresolved.append({"from": src_id, "text": text, "why": "no definitions section"})
                continue
            title, section, _ = split_reference(m.group(1), titles)
            dst_doc = doc if title is None else titles.get(title)
            if dst_doc is None:
                unresolved.append({"from": src_id, "text": text, "why": f"no document titled {title!r}"})
                continue
            if section is None:
                edges.append({"from": src_id, "to": dst_doc, "type": "refers_to", "via": "text", "label": text})
                continue
            sec = _match_section(pindex, dst_doc, section, None)
            if sec is None:
                unresolved.append({"from": src_id, "text": text, "why": f"{dst_doc} has no section {section!r}"})
                continue
            edges.append({"from": src_id, "to": f"{dst_doc}#{sec['id']}", "type": "refers_to", "via": "text", "label": text})
    return edges, unresolved


# --- claims -> provisions ------------------------------------------------------------
def claim_edges(claims: list[dict], pindex: dict) -> list[dict]:
    """`cites` edges from each claim to every provision its pointers overlap, in
    pointer order then document order. A pointer inside the front matter cites the
    document, not a provision, and yields a `cites` edge to the document instead."""
    by_doc: dict[str, list[dict]] = {}
    for p in pindex["provisions"]:
        by_doc.setdefault(p["document"], []).append(p)
    out: list[dict] = []
    for c in claims:
        seen: set[str] = set()
        for item in c.get("evidence", []):
            doc, start, end = item.get("document"), item.get("start"), item.get("end")
            if not doc or start is None or end is None or doc not in pindex["sections"]:
                continue
            hits = [p for p in by_doc.get(doc, []) if p["start"] <= end and p["end"] >= start]
            targets = [p["id"] for p in hits] if hits and end > FRONT_MATTER_LINES else [doc]
            for t in targets:
                if t not in seen:
                    seen.add(t)
                    out.append({"from": c["id"], "to": t, "type": "cites", "via": "claims", "label": item.get("resource", "")})
    return out


# --- documents -----------------------------------------------------------------------
def document_edges(meta: dict[str, dict[str, str]]) -> list[dict]:
    """supersedes (within a form family, by edition), amends (state amendatory -> the
    base forms of its line), attaches_to (endorsement -> the base forms of its line)."""
    out: list[dict] = []
    fams: dict[str, list[str]] = {}
    for path in meta:
        f = family(path)
        if f:
            fams.setdefault(f, []).append(path)
    for f, paths in sorted(fams.items()):
        ordered = sorted(paths, key=lambda p: meta[p].get("edition", ""))
        for older, newer in zip(ordered, ordered[1:]):
            out.append({"from": newer, "to": older, "type": "supersedes", "via": "structure",
                        "label": f"Edition {meta[newer].get('edition', '?')} supersedes {meta[older].get('edition', '?')}"})
    base_by_line: dict[str, list[str]] = {}
    for path, m in meta.items():
        if m.get("type") == "form" and m.get("line"):
            base_by_line.setdefault(m["line"], []).append(path)
    for path, m in sorted(meta.items()):
        line = m.get("line")
        if not line or m.get("type") not in ("amendatory", "endorsement"):
            continue
        kind = "amends" if m["type"] == "amendatory" else "attaches_to"
        for base in sorted(base_by_line.get(line, [])):
            out.append({"from": path, "to": base, "type": kind, "via": "structure",
                        "label": f"{m.get('state') + ' ' if m.get('state') else ''}{m['type']} for {line}"})
    return out


# --- the navigation layer ----------------------------------------------------------
def index_edges(corpus) -> tuple[list[dict], dict[str, str]]:
    """`lists` edges from every wiki index page to the pages and directories it links,
    and labels for the pages (their link text)."""
    out: list[dict] = []
    labels: dict[str, str] = {}
    for path in corpus.paths(prefix="openwiki/", suffix=".md"):
        if not (path == "openwiki/index.md" or path.endswith("/index.md")):
            continue
        base = path.rsplit("/", 1)[0]
        for l in corpus.lines(path):
            m = LINK.match(l)
            if not m:
                continue
            text, href = m.group(1), m.group(2)
            target = f"{base}/{href}".replace("/./", "/")
            if target.endswith("/"):
                target = target + "index.md"
            out.append({"from": path, "to": target, "type": "lists", "via": "structure", "label": text})
            labels.setdefault(target, text)
    return out, labels


# --- the artifact --------------------------------------------------------------------
def provisions_fingerprint(pindex: dict) -> str:
    h = hashlib.sha256()
    for p in pindex["provisions"]:
        h.update(p["id"].encode()); h.update(b"\0"); h.update(p["content_hash"].encode()); h.update(b"\n")
    return h.hexdigest()


def build_edges(corpus, sha: str, pindex: dict, claims: list[dict]) -> dict[str, Any]:
    """The whole artifact for a corpus at `sha`. Pure over the corpus reader, the
    provisions index and the claims (ClaimsIndex.claims or the committed index's list)."""
    meta: dict[str, dict[str, str]] = {}
    titles: dict[str, str] = {}
    labels: dict[str, str] = {}
    for path in sorted(corpus.paths(suffix=".md")):
        if not is_source(path):
            continue
        fm = front_matter(corpus.lines(path))
        meta[path] = fm
        if fm.get("title"):
            titles[fm["title"]] = path
            labels[path] = fm["title"]
    for doc, secs in pindex["sections"].items():
        for s in secs:
            labels[f"{doc}#{s['id']}"] = f"{s['id']} — {s['title']}" if s.get("title") else s["id"]
    refs, unresolved = extract_references(corpus, pindex, titles)
    lists, page_labels = index_edges(corpus)
    for k, v in page_labels.items():
        labels.setdefault(k, v)
    for path in corpus.paths(prefix="openwiki/", suffix=".md"):
        if path not in labels:
            h1 = next((l[2:].strip() for l in corpus.lines(path) if l.startswith("# ")), None)
            if h1:
                labels[path] = h1
    edges = refs + claim_edges(claims, pindex) + document_edges(meta) + lists
    return {"schema_version": SCHEMA_VERSION, "corpus_sha": sha, "provisions_fingerprint": provisions_fingerprint(pindex),
            "counts": _counts(edges), "edges": edges, "unresolved": unresolved,
            "documents": {p: {k: v for k, v in m.items() if k != "title"} for p, m in meta.items()}, "labels": labels}


def _counts(edges: list[dict]) -> dict[str, int]:
    out: dict[str, int] = {}
    for e in edges:
        out[e["type"]] = out.get(e["type"], 0) + 1
    return dict(sorted(out.items()))


def dumps(artifact: dict[str, Any]) -> str:
    return json.dumps(artifact, indent=1, sort_keys=False, ensure_ascii=False) + "\n"


def matches_provisions(artifact: dict, pindex: dict) -> bool:
    """Does the committed artifact describe this provisions index (which was itself
    accepted by content against the tree)?"""
    return artifact.get("schema_version") == SCHEMA_VERSION and artifact.get("provisions_fingerprint") == provisions_fingerprint(pindex)


# --- the agent's copy -------------------------------------------------------------
_EDGES: dict[str, dict] = {}
EDGES_SOURCE: dict[str, str] = {}


async def ensure_edges(sha: str, blobs: dict[str, str] | None = None) -> dict[str, Any]:
    """The committed `.graph-edges.json` at `sha` when it matches the provisions
    index; otherwise the same artifact built here."""
    art = _EDGES.get(sha)
    if art is None:
        from tools.claims_index import ensure_index
        from tools.corpus_local import ensure_local_corpus
        from tools.provisions import ensure_provisions

        corpus = await ensure_local_corpus(sha, blobs)
        pindex = await ensure_provisions(sha, blobs)
        try:
            art = json.loads("\n".join(corpus.lines(".graph-edges.json")))
            if not matches_provisions(art, pindex):
                raise ValueError("edge artifact does not describe this provisions index")
            EDGES_SOURCE[sha] = "committed"
        except (FileNotFoundError, ValueError, json.JSONDecodeError):
            cindex = await ensure_index(sha, blobs)
            art = build_edges(corpus, sha, pindex, cindex.claims)
            EDGES_SOURCE[sha] = "built"
        _EDGES[sha] = art
    return art
