# Atlas Citation Architecture Decision v0.1

**Status:** Owner Decision — Ratified for Descriptive Atlas v0.1
**Applies to:** `ATLAS_DESCRIPTIVE_V0.1.json` and its query/reference surface
**Depends on:** `REFERENCE_AUTHORITY_AND_CITABILITY_MODEL.md`, `SOURCE_AND_CLAIM_POLICY.md`, `ATLAS_ID_LOCK_V0.1.json`, `CITATION_REGISTRY_V0.1.json`

## 1. Decision

> ATL-D-* identifiers are stable reference handles and deterministic derived
> views, not independent citation objects. BC-* remains the canonical citation
> identity for the underlying descriptive record.

`ATL-D-*` identifiers are **not** added to `CITATION_REGISTRY_V0.1.json`.

This decision is specific to Descriptive Atlas v0.1. It is not a permanent bar
on reconsideration; the conditions under which it may be reopened are stated in
§7.

## 2. Governing Principle

One epistemic object should have one canonical citation identity, unless an
independently governed derivative becomes a genuinely distinct epistemic
object.

## 3. Four Concepts, Kept Distinct

| # | Concept | Identifier / form | Role |
| --- | --- | --- | --- |
| 1 | Source record | `BC-NNN` | The underlying boundary-case record. |
| 2 | Canonical citation identity | `BC-NNN` (currently the same as the source) | The identifier one cites. |
| 3 | Derived Atlas view | `ATL-D-NNN` | A stable retrieval/reference handle over a deterministic view of the source. |
| 4 | Distribution / resource location | e.g. `atlas/records/ATL-D-018.json` | Where a copy of the view is fetched. |

A path or URL is **not** a citation identity. An Atlas handle is **not**
automatically a citation authority. For every pair, `ATL-D-NNN` resolves to and
is bound to exactly one `BC-NNN` (see `ATLAS_ID_LOCK_V0.1.json`); the citation
provenance of that record is `BC-NNN`.

Example: `ATL-D-018` may be used to access or point at the Atlas record, but the
reference/citation is made through `BC-018`.

## 4. Precise Wording on Referenceability

`ATL-D-*` **is not independently registered as a canonical citation object.**

This is deliberately **not** the same as "ATL-D-* cannot be referenced." A
human or a system may point at `ATL-D-018` as a retrieval/reference handle; the
final citation provenance still resolves to `BC-018`. The query surface already
encodes this: every result and every distribution record carries
`atlas_record_citability = not_independently_registered` together with the
`source_citation_id` (the BC id) and whether that source id is registered and
externally citable.

## 5. Inheritance (the view is never more authoritative than its source)

An Atlas view neither raises nor changes any of the following; it exposes them
as derived from the source:

- claim class;
- license;
- temporal status;
- provider / Altis attribution separation;
- falsifiability reference;
- correction state.

If the source changes through a legitimate, governed correction, the Atlas view
must be regenerated deterministically under the hosted validation gate. A view
must never become more authoritative than the source it is derived from.

## 6. Correction Semantics

Two error classes are kept strictly separate:

1. **Error in the knowledge / claim** (the descriptive content is wrong): correct
   it in the **canonical source `BC-*`** under `SOURCE_AND_CLAIM_POLICY.md` §9,
   then regenerate the Atlas. The Atlas is never a parallel place to correct
   source knowledge.
2. **Error in the derivation / distribution only** (the transform or packaging
   is wrong, the source claim is correct): fix the generator or the Atlas
   derivation and regenerate, **without** changing the source claim.

These two paths must not be conflated. Source knowledge is corrected source-first.

## 7. Conditions to Reopen the Decision

`ATL-D-*` may become an independent citation object in the future **only if** an
Atlas record acquires genuine independent epistemic identity, for example:

- it contains Altis-authored synthesis not present in the BC source;
- it merges more than one source case into a single object;
- it carries an independent lifecycle / version history;
- it carries an independent correction history;
- it carries an independent falsifier;
- an external citation need arises that a BC citation cannot represent precisely;
- the Atlas advances to a new authorized layer that differs substantively from a
  merely derived descriptive view.

The following are explicitly **insufficient** on their own:

- that `ATL-D-*` has a URL;
- that it is used in the CLI;
- that it has a stable id;
- that it becomes widely used.

Popularity alone does not create epistemic independence.

## 8. Machine-Readable Companion

`ATLAS_CITATION_ARCHITECTURE_V0.1.json` states this decision in machine form
(identity model, namespaces, `independent_atlas_citation = false`,
`correction_authority = source-first`, reconsideration triggers). It does not
duplicate the 20 mappings; `ATLAS_ID_LOCK_V0.1.json` remains their governing
source.

## 9. Scope of This Step

This is a clarification of citation architecture only. It does not change
`LICENSE-ASR-001`, `BLOCKER-OPREVIEW-BASELINE-001`, ASR, corpus claims, Atlas
descriptive content, general ratification status, or evaluative permissions.
