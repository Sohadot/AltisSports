# ASR-001 Profile Model Refinement v0.1 to v0.2

**Status:** Controlled implementation-model revision  
**Research schema impact:** None

## 1. Applicability and Evidence Are Separated

v0.1 allowed `not_evidenced` as an applicability or feature state.

Internal trial analysis found that this conflates two different questions:

1. Does the clause apply?
2. What evidence supports the disclosure?

v0.2 therefore uses:

- feature states: `present`, `absent`, `unknown`, `disputed`;
- applicability states: `applicable`, `not_applicable`, `unknown`, `disputed`;
- evidence states: `supported`, `partial`, `absent`, `unknown`, `not_evidenced`, `not_applicable`.

## 2. Explicit Evidence Requirement

Each clause record includes:

- `evidence_requirement`;
- `evidence_state`;
- `evidence_refs`.

An applicable clause can remain validly disclosed as `not_evidenced`, provided the absence is explicit and the verification result does not claim full support.

## 3. Correction and Supersession

v0.2 adds:

- `supersedes_profile_id`;
- `superseded_by_profile_id`;
- structured correction records.

This supports append-only lifecycle integrity.

## 4. JSON Distribution Trigger

A JSON profile instance fixes `machine_readable_distribution_provided` to `present`.

This is an implementation constraint, not a universal requirement for every human-readable ASR-001 document.

## 5. Model Independence

The model remains clause-derived and separate from `BOUNDARY_CASE_SCHEMA_V0.3.json`.

No historical schema or dataset is modified.
