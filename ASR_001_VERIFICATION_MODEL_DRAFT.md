# ASR-001 Verification Model Draft

**Version:** 0.1  
**Status:** Candidate verification architecture — not a conformance program

## 1. Purpose

Verification checks the structure and traceability of an ASR-001 profile.

It does not independently prove the safety, effectiveness, quality, category membership, or superiority of the underlying system.

## 2. Verification Modes

### Document Presence

Checks that a required profile section or disclosure exists.

### Field Presence

Checks that an expected field exists in a machine-readable profile when applicable.

### Cross-Reference Integrity

Checks that identifiers, sources, dependencies, corrections, and linked records resolve consistently.

### Evidence Traceability

Checks that a claim or field points to an evidence record with source, date, class, status, and limitations.

### Controlled Vocabulary

Checks that declared states and relation types use the applicable vocabulary or an explicitly namespaced extension.

### Conditional Logic

Checks that triggered disclosures are present and non-triggered clauses are not falsely marked failed.

### Temporal Consistency

Checks agreement among profile date, system version, ruleset, source date, access date, and supersession status.

### Human Review

Checks object lock, analytical interpretation, ambiguity, and cases that cannot be validated from syntax alone.

### Machine Validation

Checks syntax, identifiers, data types, required structures, and deterministic constraints in a future implementation model.

## 3. Verification Result

Candidate verification outcomes:

- `verified`;
- `partially_verified`;
- `not_verified`;
- `not_applicable`;
- `requires_human_review`;
- `blocked_by_missing_evidence`.

These describe profile verification, not product status.

## 4. Evidence Strength Boundary

Verification can establish that:

- a claim is attributed;
- a source is attached;
- a limitation is disclosed;
- a profile state is represented;
- a version is declared.

Verification does not automatically establish that the source is true, complete, current, or independent. Source-quality review remains distinct.

## 5. Correction

A later profile-validation design retains:

- prior profile identifier;
- affected clauses;
- corrected fields;
- reason;
- evidence;
- revision date;
- supersession relation.

Substantive corrections remain visible.
