# ASR-001 Licensing and Citability Decision v0.1

**Decision ID:** ASR-001-LICENSING-DECISION-V0.1
**Status:** Owner Decision — Ratified (owner-delegated)
**Date:** 2026-08-14
**Resolves:** `LICENSE-ASR-001`
**Introduces:** `CITE-HOLD-ASR-001`
**Depends on:** `DATASET_LICENSE.md`, `REFERENCE_AUTHORITY_AND_CITABILITY_MODEL.md`, `SOURCE_AND_CLAIM_POLICY.md`, `CITATION_REGISTRY_V0.1.json`

## 1. Decision

Two separate gates are decided distinctly:

1. **Licensing.** The Altis-authored ASR normative clause text (the candidate
   normative clause catalogs and clause-to-field maps of the ASR family) is made
   available under **CC BY 4.0**, by explicit extension of `DATASET_LICENSE.md`
   §1. This **resolves `LICENSE-ASR-001`**.

2. **Citability.** ASR clause identifiers remain **not externally citable** as
   canonical objects, held by the new, explicit **`CITE-HOLD-ASR-001`**, because
   ASR is still an unpublished Working Draft (claim class C5, provisional). The
   hold lifts only on a later ASR publication / public-review decision.

## 2. Why the Two Gates Are Separated

Licensing grants a legal reuse right. Canonical citability asserts that an
identifier names a stable, registered reference object. These are different
questions. Extending the license serves researchers, engineers, journalists,
RAG systems, and AI agents who need to quote, adapt, or ingest the material —
without asserting that ASR is a published or adopted standard. Keeping
citability tied to publication preserves the published/unpublished distinction
this project has guarded throughout, and mirrors the Atlas citation
architecture (`ATLAS_CITATION_ARCHITECTURE_DECISION_V0.1.md`): being
referenceable is not the same as being a registered canonical citation object.

## 3. Effect on the Citation Registry

For the 30 ASR clause identifiers:

| Field | Before | After |
| --- | --- | --- |
| `license` | `null` | `CC-BY-4.0` |
| `license_blocker` | `LICENSE-ASR-001` (open) | `CITE-HOLD-ASR-001` (open) |
| `non_citable_reason` | — | `licensed_but_unpublished_working_draft` |
| `externally_citable` | `false` | `false` (unchanged) |
| `claim_class` | `C5` | `C5` (unchanged) |
| `temporal_status` | `provisional` | `provisional` (unchanged) |

The externally-citable set is unchanged (39 = 20 boundary cases + 19 AS³
elements). No identifier, source binding, kind, or claim class changed. The
registry validator continues to enforce that any identifier under an open hold
is not externally citable, so ASR cannot be marked citable while
`CITE-HOLD-ASR-001` is open.

## 4. Referenceability, Precisely

Consistent with `REFERENCE_AUTHORITY_AND_CITABILITY_MODEL.md` §5 and the Atlas
citation architecture: ASR clauses **may be reused and referenced** under CC BY
4.0 with their provisional/unpublished status attached. They are **not**
registered externally-citable canonical objects. Reuse must not represent ASR
as an adopted, recognized, or published standard.

## 5. What This Decision Does Not Do

It does not publish ASR, ratify it, make it a Public Review Draft, activate
operator review, establish conformance or certification, or change adoption or
recognition status. It changes no normative clause, scope, profile semantics,
review question, or evidentiary meaning. `BLOCKER-OPREVIEW-BASELINE-001` remains
resolved (DEC-018); no other blocker is affected.

## 6. Reopening / Lifting the Hold

`CITE-HOLD-ASR-001` lifts when ASR reaches a governed publication or
public-review state that makes its clause identifiers appropriate as canonical
citation objects. That is a separate owner decision, recorded when taken.
