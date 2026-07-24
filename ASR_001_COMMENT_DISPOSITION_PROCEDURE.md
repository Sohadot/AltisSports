# ASR-001 Comment Disposition Procedure

**Version:** 1.0  
**Applies to:** Limited written operator-review comments after owner activation

## 1. Intake

Each accepted comment receives:

```text
ORC-YYYY-NNN
```

The intake record includes:

- reviewer identifier and class;
- conflict declaration identifier;
- attribution preference;
- target clause, field, or artifact;
- issue type and severity;
- evidence description;
- requested disposition.

Comments are preserved in their submitted form, subject only to necessary redaction of personal, confidential, or security-sensitive material.

## 2. Completeness Check

A comment is returned for clarification when it lacks:

- a target;
- a specific observation;
- an operational scenario or evidence basis;
- a stated consequence;
- sufficient information to distinguish technical defect from preference.

Incomplete comments remain logged; they are not silently deleted.

## 3. Triage

The maintainer assigns:

- issue type;
- severity;
- affected clauses and fields;
- duplicate relationship;
- scope impact;
- conformance-boundary impact;
- required reviewer class for secondary review.

The maintainer can revise the submitter's proposed classification but records the change and rationale.

## 4. Technical Review

The issue is tested against:

- approved ASR-001 scope;
- Working Draft v0.2 baseline;
- clause traceability;
- internal trial profiles;
- evidence and claim policy;
- exclusions;
- implementation model;
- historical decisions.

A blocking issue receives explicit owner review.

A blocking issue cannot be closed as `no change` without explicit written rationale and owner approval.

## 5. Dispositions

### `accept`

The proposed change is adopted substantially as submitted.

### `accept_with_revision`

The issue is accepted, but the final wording or model change differs.

### `reject_with_rationale`

The issue is understood but not adopted. The response identifies the evidence, boundary, or design reason.

### `defer_pending_evidence`

The issue can be material but lacks sufficient evidence for a current change.

### `out_of_scope`

The concern belongs outside ASR-001 or requires a new scope decision.

### `duplicate`

The issue is linked to an earlier comment and inherits its disposition.

### `no_change`

Testing confirms the current clause or model remains appropriate.

## 6. Change Effect

Every accepted change records:

- affected clause identifiers;
- affected field paths;
- applicability impact;
- verification impact;
- evidence-burden impact;
- compatibility impact;
- scope impact;
- exclusion impact;
- version effect.

## 7. Scope Expansion Hold

A proposed change that expands the approved scope is not applied through comment disposition.

It triggers:

1. `potential_expansion_requires_hold`;
2. owner review;
3. a new governance decision;
4. a new scope gate when necessary.

## 8. Response Record

Each comment receives a written disposition containing:

- comment identifier;
- decision;
- rationale;
- change reference;
- version target;
- attribution treatment;
- unresolved evidence.

## 9. No Voting

Comment counts, reviewer seniority, organizational size, or favorable sentiment do not determine disposition.

The process is evidence- and boundary-driven, not majoritarian.

## 10. Publication Boundary

Disposition records can be prepared internally.

They are not published as a public-review report until a separate authorization exists.
