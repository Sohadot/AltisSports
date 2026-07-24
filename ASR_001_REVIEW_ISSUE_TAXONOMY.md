# ASR-001 Review Issue Taxonomy

**Version:** 1.0  
**Status:** Prepared for limited written operator review

## Severity

- `blocking` — the issue can invalidate scope integrity, evidence interpretation, verification, or the profile-only conformance boundary.
- `major` — the issue materially impairs operational use, consistency, or implementation.
- `minor` — the issue is bounded and does not change the clause's core effect.
- `editorial` — wording, structure, or presentation issue with no technical effect.
- `observation` — useful information that does not yet justify a change.

Severity is not a score, vote, or reviewer rank.

## Issue Types

| Type | Meaning |
| --- | --- |
| `scope_violation` | The clause or artifact exceeds the approved ASR-001 scope |
| `object_lock_failure` | Findings can transfer silently across configurations or object types |
| `ambiguity` | More than one materially different interpretation is plausible |
| `applicability_defect` | A trigger is too broad, too narrow, or not observable |
| `evidence_state_defect` | Applicability, evidence state, absence, or uncertainty are conflated |
| `evidence_burden_defect` | The required evidence is disproportionate, artificial, or insufficient |
| `evidence_classification_gap` | Claim class, provenance, limitation, or temporal status is unclear |
| `verification_gap` | The proposed verification cannot establish the stated disclosure |
| `unverifiable_requirement` | The clause cannot be tested in a reproducible or reviewable way |
| `duplicate_obligation` | Two clauses create overlapping or inconsistent obligations |
| `missing_disclosure` | A material operational disclosure is absent |
| `missing_field` | The implementation model lacks a required field |
| `implementation_schema_defect` | The machine model misrepresents clause semantics or conditionality |
| `implementation_burden` | The operational cost is disproportionate to the evidence purpose |
| `terminology_collision` | Two terms overlap or a term conflicts with established practice |
| `agency_boundary_defect` | Performer, external actor, designer, automation, or official roles are conflated |
| `causal_attribution_leak` | The text implies causal contribution or weighting not supported by evidence |
| `comparability_defect` | Comparison conditions are insufficient or falsely generalized |
| `construct_validity_gap` | A core concept does not discriminate the intended phenomena |
| `hidden_scoring_risk` | Qualitative disclosures can be converted into an implied score or ladder |
| `conformance_boundary_leak` | Profile validation can be mistaken for system, sport, or product certification |
| `safety_boundary_leak` | Disclosure can be mistaken for safety approval or certification |
| `clinical_boundary_leak` | Disclosure can be mistaken for clinical efficacy or medical advice |
| `accessibility_gap` | Adaptive participation, body variation, or access conditions are underrepresented |
| `privacy_security_gap` | Data protection, identity, telemetry, biometric, or security concerns are missing |
| `lifecycle_gap` | Version, correction, supersession, or authority history is incomplete |
| `machine_readability_gap` | Identifiers, serialization, validation, extensions, or distributions are deficient |
| `licensing_gap` | Reuse, attribution, third-party rights, or distribution licensing is unclear |
| `conflict_disclosure_gap` | Reviewer or publisher interests are not sufficiently visible |
| `editorial_clarity` | Meaning is intact but wording or structure can be improved |
| `no_issue` | The reviewer tested the element and found no actionable defect |

## Disposition Compatibility

Each issue is assigned one disposition:

- accept;
- accept with revision;
- reject with rationale;
- defer pending evidence;
- out of scope;
- duplicate;
- no change.

A blocking issue cannot be closed as `no change` without explicit written rationale and owner approval.
