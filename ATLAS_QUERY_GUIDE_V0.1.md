# Atlas Query / Reference Surface — Usage Guide v0.1

**Status:** Foundation Draft — Not Ratified
**Applies to:** `ATLAS_DESCRIPTIVE_V0.1.json` via `ATLAS_QUERY_CONTRACT_V0.1.json`

This is a usage document, not a description of results as judgments. The query
surface **retrieves, resolves, and filters what the Atlas already states**. It
does not infer, score, rank, recommend, or add anything the Atlas does not
contain. Results are descriptive records, never verdicts or recommendations.

## What you can query

Two ways to consume the surface:

1. **CLI** — `query_descriptive_atlas.py` (Python standard library only).
2. **Static distribution** — the `atlas/` directory: one JSON file per record
   plus resolver indexes, so a consumer can fetch a single record without the
   whole corpus. Suitable for plain static hosting; no server required.

### Selectors (exact resolve / activity match)

| Selector | Meaning |
| --- | --- |
| `--atlas-id ATL-D-018` | Resolve exactly one record by its Atlas id. |
| `--case-id BC-018` | Resolve exactly one record by its source boundary-case id. |
| `--activity "Chess"` | Exact, case-sensitive activity match. |
| `--activity-contains formula` | Case-insensitive substring match on activity. |

### Filters (descriptive retrieval only)

Filters combine with logical AND. Each retrieves an existing Atlas value; none
computes a score, similarity, or ranking.

| Filter | Meaning |
| --- | --- |
| `--dimension <name> --status <value>` | Records whose dimension has that status. |
| `--dimension <name> --claim-class <Cn>` | Records whose dimension carries that claim class. |
| `--has-dimension <name>` | Records where an optional dimension is present. |
| `--sport-contest-axis <value>` | Records whose **source** provisional finding has that axis. |
| `--category-relation <value>` | Records whose **source** provisional finding has that relation. |
| `--confidence <value>` | Records with that source confidence. |

The exact allowed values for every field are enumerated in
`ATLAS_QUERY_CONTRACT_V0.1.json` (derived from the live Atlas). A value outside
that vocabulary is an invalid query, not an empty result.

## What you cannot query

The surface deliberately does **not** support, and will reject or never
produce:

- similarity, "closest sports", relevance ranking, or any hidden ordering;
- normalized or weighted metrics, scores, grades, maturity or readiness levels;
- derived taxonomies (e.g. inferring `physical` / `virtual` / `hybrid`,
  `human-dominant` / `machine-dominant`, or sport-likeness) — these are not in
  the Atlas and are never synthesized;
- arbitrary JSONPath or code expressions; only the allowlisted selectors and
  filters above are permitted.

## Reading a result

Every result carries provenance — it is never a bare summary:

- `atlas_record_id` and `source_case_id`;
- `activity`, `temporal_status` (`provisional`), `license` (CC BY 4.0);
- the full `record`, with each dimension's `status` and `claim_class` preserved
  exactly as recorded in the source corpus;
- `source_provisional_finding` — the corpus's own attributed reading (with its
  claim class). This is the source's finding, **not** a new Atlas verdict.

### Claim classes (from `SOURCE_AND_CLAIM_POLICY.md`)

`C1` documented fact · `C2` multi-source synthesis · `C3` attributed external /
provider claim · `C4` Altis analytical interpretation · `C5` provisional
category proposition · `C6` commercial/forecast. A dimension keeps the claim
class the corpus assigned it; the surface never upgrades or launders it.

## Atlas record id vs source citation id — citability limits

An Atlas record id such as `ATL-D-018` is a stable handle for retrieval. It is
**not** a registered citation identifier: `ATL-D-*` ids are not in
`CITATION_REGISTRY_V0.1.json`. Every result states this explicitly:

```
"citability": {
  "atlas_record_citability": "not_independently_registered",
  "source_citation_id": "BC-018",
  "source_citation_registered": true,
  "source_citation_externally_citable": true
}
```

To cite, use the **source** citation id (the `BC-*` id) under its registered
terms. Whether Atlas records should themselves become independent citation
objects is a deliberate, separate governance decision, not assumed here — it is
recorded in `ATLAS_CITATION_ARCHITECTURE_DECISION_V0.1.md` (for v0.1: `BC-*` is
the canonical citation identity; `ATL-D-*` is a stable derived reference handle).

## Result and exit semantics

| Situation | Exit code | Shape |
| --- | --- | --- |
| Valid query, one or more matches | 0 | `result_count > 0`, `results[]` |
| Valid query, no matches | 0 | `result_count: 0` — empty is not an error |
| Invalid query (unknown field or value) | 2 | `{"error": "invalid_query", ...}` |
| Broken source/reference | 3 | `{"error": "broken_source", ...}` |

A no-result answer never looks like an integrity failure, and an integrity
failure never looks like a no-result answer.

## Examples

```
python3 query_descriptive_atlas.py --atlas-id ATL-D-018
python3 query_descriptive_atlas.py --case-id BC-018
python3 query_descriptive_atlas.py --activity-contains formula
python3 query_descriptive_atlas.py --dimension measurement --status supported
python3 query_descriptive_atlas.py --sport-contest-axis sport
```

## Static distribution layout

```
atlas/
  manifest.json            distribution manifest, per-file sha256
  by-atlas-id.json         ATL-D-NNN -> records/ATL-D-NNN.json
  by-case.json             BC-NNN    -> records/ATL-D-NNN.json
  records/ATL-D-001.json   one self-contained record (with citability block)
  ...
  records/ATL-D-020.json
```

Every file under `atlas/` and the query contract are generated by
`build_atlas_distribution.py` from the Atlas. Do not hand-edit them; CI proves
they are a byte-for-byte deterministic function of the source.
