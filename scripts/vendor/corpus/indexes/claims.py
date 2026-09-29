"""The claims index: every grounded claim OpenWiki compiled, with its evidence pointers.

Read from the committed `.claims-index.json` when it matches the sidecars in the
tree, otherwise scanned from `openwiki/.claims/`. Both give the same index.
Cached per commit. Vendored into the corpus repo, which builds the committed copy.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field

from contracts.evidence_anchor import parse_resource

SIDECAR_PREFIX = "openwiki/.claims/"

#: Bumped only for an incompatible shape; a reader seeing another value scans instead.
INDEX_SCHEMA_VERSION = 1

#: Relation direction: the acting document's role comes first.
PRECEDENCE = (
    "training", "memorandum", "guideline", "manual",
    "bulletin", "state-amendatory", "endorsement", "base-form",
)
BASE_FORMS = frozenset({"HO-3", "HO-4", "HO-5", "HO-6", "DP-3"})


def document_role(path: str) -> str | None:
    """The role of a source document, or None for scaffolding such as README.md."""
    if path.startswith("bulletins/"):
        return "bulletin"
    if path.startswith("guidelines/"):
        return "guideline"
    if path.startswith("manuals/"):
        return "manual"
    if path.startswith("memoranda/"):
        return "memorandum"
    if path.startswith("training/"):
        return "training"
    if path.startswith("forms/"):
        parts = path.split("/")
        if len(parts) < 5:
            return None
        _, _line, state, form, _edition = parts
        if form in BASE_FORMS:
            return "base-form"
        return "endorsement" if state == "MS" else "state-amendatory"
    return None


@dataclass
class ClaimsIndex:
    corpus_sha: str
    claims: list[dict] = field(default_factory=list)

    @property
    def evidence_count(self) -> int:
        return sum(len(c["evidence"]) for c in self.claims)

    def by_id(self, claim_id: str) -> dict | None:
        return next((c for c in self.claims if c["id"] == claim_id), None)

    def citing(
        self, document: str, start: int | None = None, end: int | None = None
    ) -> list[dict]:
        """Claims whose evidence touches `document`, or OVERLAPS the range when one is given."""
        hits: list[dict] = []
        for claim in self.claims:
            for item in claim["evidence"]:
                if item["document"] != document:
                    continue
                if start is None or end is None:
                    hits.append(claim)
                    break
                if item["start"] is None:
                    continue
                if start <= item["end"] and end >= item["start"]:
                    hits.append(claim)
                    break
        return hits

    def documents(self) -> dict[str, int]:
        """Cited document -> evidence pointer count."""
        counts: dict[str, int] = {}
        for claim in self.claims:
            for item in claim["evidence"]:
                if item["document"]:
                    counts[item["document"]] = counts.get(item["document"], 0) + 1
        return counts


def scan_sidecars(corpus) -> list[dict]:
    """Every claim in the sidecars of an in-memory corpus. No filesystem access."""
    out: list[dict] = []
    for rel in corpus.paths(prefix=SIDECAR_PREFIX, suffix=".json"):
        page = rel[len(SIDECAR_PREFIX) : -len(".json")]
        data = json.loads("\n".join(corpus.lines(rel)))
        for claim in data.get("claims", []):
            evidence = []
            for item in claim.get("evidence", []):
                resource = item.get("resource", "")
                parsed = parse_resource(resource)
                evidence.append(
                    {
                        "resource": resource,
                        "version": item.get("version", ""),
                        "document": parsed[0] if parsed else None,
                        "start": parsed[1] if parsed else None,
                        "end": parsed[2] if parsed else None,
                    }
                )
            out.append(
                {
                    "id": claim.get("id"),
                    "page": page,
                    "statement": claim.get("statement", ""),
                    "evidence": evidence,
                }
            )
    return out


def relation_edges(index: ClaimsIndex) -> list[dict]:
    """Typed, directed document relations, one per pair of roles a claim's evidence spans.

    Shared by find_relations and the workflow's index builder.
    """
    from contracts.relation_types import normalize

    edges: dict[tuple[str, str], dict] = {}
    for claim in index.claims:
        roles = {
            e["document"]: document_role(e["document"])
            for e in claim["evidence"]
            if e["document"] and document_role(e["document"])
        }
        if len(set(roles.values())) < 2:
            continue   # two editions of one form are not a relationship
        # every distinct-role pair: guideline -> endorsement and endorsement -> base form are both real
        kind = normalize(claim["statement"])
        ordered = sorted(roles.items(), key=lambda kv: PRECEDENCE.index(kv[1]))
        for i, (acting, acting_role) in enumerate(ordered):
            for target, target_role in ordered[i + 1 :]:
                if acting_role == target_role:
                    continue
                edge = edges.setdefault(
                    (acting, target),
                    {"from": acting, "to": target, "types": {}, "claim_ids": []},
                )
                edge["claim_ids"].append(claim["id"])
                if kind:
                    edge["types"][kind] = edge["types"].get(kind, 0) + 1

    out = []
    for edge in edges.values():
        out.append(
            {
                "from": edge["from"],
                "to": edge["to"],
                "type": max(edge["types"], key=edge["types"].get) if edge["types"] else None,
                "types": edge["types"],
                "claim_count": len(edge["claim_ids"]),
                "claim_ids": edge["claim_ids"],
            }
        )
    out.sort(key=lambda e: (-e["claim_count"], e["from"], e["to"]))
    return out


# --- the committed .claims-index.json ------------------------------------------

def sidecar_fingerprint(corpus) -> str:
    """sha256 over every sidecar's path and content.

    This, not the commit, decides whether a committed index fits a tree: later
    commits that only touch source documents carry the same sidecars.
    """
    h = hashlib.sha256()
    for rel in corpus.paths(prefix=SIDECAR_PREFIX, suffix=".json"):
        content = "\n".join(corpus.lines(rel)).encode("utf-8")
        h.update(rel.encode("utf-8"))
        h.update(b"\0")
        h.update(hashlib.sha256(content).hexdigest().encode("ascii"))
        h.update(b"\n")
    return h.hexdigest()


def to_committed(index: ClaimsIndex, corpus) -> dict:
    """The `.claims-index.json` the refresh workflow commits: per-document summaries and
    relations for people, plus the full claims array so readers never need to scan."""
    resources: dict[str, dict] = {}
    for claim in index.claims:
        for item in claim["evidence"]:
            doc = item["document"]
            if not doc:
                continue
            entry = resources.setdefault(doc, {"claim_count": 0, "pages": {}, "claims": []})
            entry["claims"].append(
                {
                    "id": claim["id"],
                    "page": claim["page"],
                    "lines": f"L{item['start']}-L{item['end']}",
                }
            )
    for entry in resources.values():
        ids = {c["id"] for c in entry["claims"]}
        entry["claim_count"] = len(ids)
        pages: dict[str, int] = {}
        seen: set[tuple[str, str]] = set()
        for c in entry["claims"]:
            key = (c["id"], c["page"])
            if key in seen:
                continue
            seen.add(key)
            pages[c["page"]] = pages.get(c["page"], 0) + 1
        entry["pages"] = dict(sorted(pages.items(), key=lambda kv: (-kv[1], kv[0])))

    return {
        "schema_version": INDEX_SCHEMA_VERSION,
        "compiled_from": index.corpus_sha,   # informational; validity is the fingerprint
        "sidecar_fingerprint": sidecar_fingerprint(corpus),
        "claim_count": len(index.claims),
        "evidence_count": index.evidence_count,
        "resources": dict(sorted(resources.items())),
        "relations": relation_edges(index),
        "claims": index.claims,
    }


def from_committed(text: str, sha: str, corpus) -> ClaimsIndex:
    """A ClaimsIndex from `.claims-index.json`, or ValueError if it does not fit this tree."""
    data = json.loads(text)
    if data.get("schema_version") != INDEX_SCHEMA_VERSION:
        raise ValueError(f"unsupported .claims-index.json schema_version {data.get('schema_version')!r}")
    expected = sidecar_fingerprint(corpus)
    if data.get("sidecar_fingerprint") != expected:
        raise ValueError(".claims-index.json does not match the sidecars in this tree")
    claims = data.get("claims")
    if not isinstance(claims, list) or not claims:
        raise ValueError(".claims-index.json carries no claims array")
    for claim in claims:
        for item in claim.get("evidence", []):
            if "version" not in item or "document" not in item:
                raise ValueError("an evidence pointer in .claims-index.json lacks version or document")
    return ClaimsIndex(corpus_sha=sha, claims=claims)


# --- the agent's cached copy ---------------------------------------------------

_INDEXES: dict[str, ClaimsIndex] = {}

#: Per commit, "committed" or "scan": where the index came from. Reported by repo_status.
INDEX_SOURCE: dict[str, str] = {}


async def ensure_index(sha: str, blobs: dict[str, str] | None = None) -> ClaimsIndex:
    """The claims index at `sha`: the committed one when it fits, else a scan."""
    index = _INDEXES.get(sha)
    if index is None:
        from corpus.snapshot.loader import ensure_local_corpus

        corpus = await ensure_local_corpus(sha, blobs)
        try:
            index = from_committed("\n".join(corpus.lines(".claims-index.json")), sha, corpus)
            INDEX_SOURCE[sha] = "committed"
        except (FileNotFoundError, ValueError, json.JSONDecodeError):
            index = ClaimsIndex(corpus_sha=sha, claims=scan_sidecars(corpus))
            INDEX_SOURCE[sha] = "scan"
        _INDEXES[sha] = index
    return index
