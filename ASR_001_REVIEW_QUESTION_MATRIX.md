# ASR-001 Operator Review Question Matrix

**Version:** 0.1  
**Status:** Prepared; review not activated  
**Question count:** 43

## Core Questions

| ID | Question | Domains | Issue types | Response | Criticality |
| --- | --- | --- | --- | --- | --- |
| `RQ-CORE-01` | Is the bounded profile subject identifiable without silently generalizing from one configuration to a product family, organization, activity, or sport? | D01 | object_lock_failure, scope_violation | `yes_no_with_rationale` | `blocking` |
| `RQ-CORE-02` | Can you distinguish clause applicability from missing, partial, disputed, or unavailable evidence in the reviewed examples? | D02, D13 | applicability_defect, evidence_state_defect | `yes_no_with_example` | `blocking` |
| `RQ-CORE-03` | Does any candidate clause imply certification, endorsement, quality ranking, safety approval, clinical validation, or category membership beyond the evidence profile? | D09, D12, D13, D14 | conformance_boundary_leak, safety_boundary_leak, scope_violation | `clause_list_with_rationale` | `blocking` |
| `RQ-CORE-04` | Is each assigned clause specific enough to verify without requiring undisclosed assumptions or private organizational knowledge? | D01, D02, D03, D04, D05, D06, D07, D08, D09, D10, D11, D12, D13, D14, D15 | unverifiable_requirement, ambiguity | `clause_list_with_proposed_text` | `major` |
| `RQ-CORE-05` | Do the uncertainty states preserve genuine unknowns and disputes without converting them into failure, absence, or a numerical judgment? | D13 | evidence_state_defect, conformance_boundary_leak | `yes_no_with_rationale` | `blocking` |
| `RQ-CORE-06` | Are any two clauses duplicative enough to create inconsistent disclosures or unnecessary review burden? | D01, D02, D03, D04, D05, D06, D07, D08, D09, D10, D11, D12, D13, D14, D15 | duplicate_obligation, implementation_burden | `clause_pairs_with_rationale` | `major` |
| `RQ-CORE-07` | Does the current profile model contain every field needed to satisfy the assigned clauses, without inheriting research-only concepts from the boundary corpus? | D15 | missing_field, implementation_schema_defect | `field_list_with_mapping` | `major` |
| `RQ-CORE-08` | Would the correction and supersession mechanism preserve a trustworthy history in your operational setting? | D14 | lifecycle_gap, implementation_burden | `yes_no_with_operational_scenario` | `major` |

## RC-01 — Sport governance and integrity

| ID | Question | Domains | Clauses | Issue types | Criticality |
| --- | --- | --- | --- | --- | --- |
| `RQ-RC01-01` | Do D01 object-lock clauses prevent federation, event, platform, and activity findings from being conflated? | D01 | ASR001-D01-C01, ASR001-D01-C02 | object_lock_failure, terminology_collision | `blocking` |
| `RQ-RC01-02` | Are rule authority and operative rule execution sufficiently separated for integrity review? | D06 | ASR001-D06-C01, ASR001-D06-C02 | missing_disclosure, verification_gap | `major` |
| `RQ-RC01-03` | Can human, software, operator, and hybrid officiation authority be reconstructed from D09 disclosures? | D09 | ASR001-D09-C01 | missing_disclosure, ambiguity | `major` |
| `RQ-RC01-04` | Does the audience-participation example preserve the distinction between rule influence and Performance Agency? | D11 | ASR001-D11-C02 | agency_boundary_defect, terminology_collision | `blocking` |
| `RQ-RC01-05` | Do governance and claim-classification clauses prevent review participation from being represented as recognition or endorsement? | D13, D14 | ASR001-D13-C01, ASR001-D14-C01 | conformance_boundary_leak, conflict_disclosure_gap | `blocking` |

## RC-02 — Competition operations

| ID | Question | Domains | Clauses | Issue types | Criticality |
| --- | --- | --- | --- | --- | --- |
| `RQ-RC02-01` | Are operating context, site roles, dependencies, and responsibility assignments sufficient to run an event review? | D02, D12 | ASR001-D02-C01, ASR001-D02-C02, ASR001-D12-C02 | missing_disclosure, implementation_burden | `major` |
| `RQ-RC02-02` | Does D05 distinguish co-location, remote control, remote supervision, and remote synchronous competition in operationally useful terms? | D05 | ASR001-D05-C01, ASR001-D05-C02 | terminology_collision, applicability_defect | `blocking` |
| `RQ-RC02-03` | Can failure paths across sensing, network, equipment, and officiation be recorded without inventing technical tolerances? | D07, D09 | ASR001-D07-C02, ASR001-D09-C01 | missing_disclosure, scope_violation | `major` |
| `RQ-RC02-04` | Are appeal, correction, and emergency-responsibility disclosures separated clearly enough for event operations? | D09, D12, D14 | ASR001-D09-C01, ASR001-D12-C02, ASR001-D14-C02 | lifecycle_gap, missing_disclosure | `major` |
| `RQ-RC02-05` | Would applying all relevant clauses create operational burden disproportionate to the profile's evidence purpose? | D02, D05, D06, D07, D09, D12, D14 | cross-domain | implementation_burden, duplicate_obligation | `major` |

## RC-03 — XR and spatial-system engineering

| ID | Question | Domains | Clauses | Issue types | Criticality |
| --- | --- | --- | --- | --- | --- |
| `RQ-RC03-01` | Are performance-interface channels and embodied-demand disclosures technically distinguishable in real XR or spatial systems? | D04 | ASR001-D04-C01, ASR001-D04-C02 | terminology_collision, missing_field | `major` |
| `RQ-RC03-02` | Does the arena model capture physical, computational, unified, and distributed topology without forcing one architecture? | D05 | ASR001-D05-C01, ASR001-D05-C02 | implementation_schema_defect, scope_violation | `major` |
| `RQ-RC03-03` | Is the distinction between direct observation, inferred state, and provider-declared state implementable? | D07 | ASR001-D07-C01 | verification_gap, missing_field | `major` |
| `RQ-RC03-04` | Can every claimed spatial-integration function be linked to a mechanism and failure effect without creating a hidden spatiality score? | D10 | ASR001-D10-C01, ASR001-D10-C02 | conformance_boundary_leak, unverifiable_requirement | `blocking` |
| `RQ-RC03-05` | Is the v0.2 JSON model extensible without allowing extensions to redefine core semantics? | D15 | ASR001-D15-C02 | machine_readability_gap, implementation_schema_defect | `major` |

## RC-04 — Performance measurement

| ID | Question | Domains | Clauses | Issue types | Criticality |
| --- | --- | --- | --- | --- | --- |
| `RQ-RC04-01` | Does the performance-window clause support valid attribution without claiming a causal score? | D03 | ASR001-D03-C01 | causal_attribution_leak, ambiguity | `blocking` |
| `RQ-RC04-02` | Are Agency Segments sufficient to describe changing control while preserving uncertainty about contribution? | D03 | ASR001-D03-C02 | missing_field, causal_attribution_leak | `major` |
| `RQ-RC04-03` | Do metric records require enough information about units, calibration, uncertainty, and intended use? | D08 | ASR001-D08-C01 | missing_disclosure, verification_gap | `blocking` |
| `RQ-RC04-04` | Are comparability conditions specific enough to prevent unsupported equivalence across versions, equipment, sites, or participant classes? | D08 | ASR001-D08-C02 | comparability_defect, scope_violation | `blocking` |
| `RQ-RC04-05` | Can outcome and consequence disclosures distinguish contest results from training, assessment, or rehabilitation outcomes? | D09 | ASR001-D09-C02 | terminology_collision, clinical_boundary_leak | `major` |

## RC-05 — Accessibility and adaptive sport

| ID | Question | Domains | Clauses | Issue types | Criticality |
| --- | --- | --- | --- | --- | --- |
| `RQ-RC05-01` | Do the clauses treat adaptive equipment and classification context as first-class conditions rather than exceptions? | D02, D08, D12 | ASR001-D02-C01, ASR001-D08-C02, ASR001-D12-C01 | accessibility_gap, missing_disclosure | `blocking` |
| `RQ-RC05-02` | Can a rehabilitation support configuration be profiled without implying sport status or clinical efficacy? | D02, D09, D12 | ASR001-D02-C01, ASR001-D09-C02, ASR001-D12-C01 | clinical_boundary_leak, scope_violation | `blocking` |
| `RQ-RC05-03` | Does D04 support diverse bodily and biological-control channels without imposing a universal embodiment threshold? | D04 | ASR001-D04-C02 | accessibility_gap, conformance_boundary_leak | `blocking` |
| `RQ-RC05-04` | Are responsibility and limitation disclosures sufficient for supervised, assisted, and adaptive participation? | D11, D12 | ASR001-D11-C01, ASR001-D12-C02 | missing_disclosure, safety_boundary_leak | `major` |
| `RQ-RC05-05` | Could any wording be interpreted as universal usability, accessibility certification, or medical advice? | D12, D13 | ASR001-D12-C01, ASR001-D13-C01 | accessibility_gap, safety_boundary_leak, clinical_boundary_leak | `blocking` |

## RC-06 — Research methodology

| ID | Question | Domains | Clauses | Issue types | Criticality |
| --- | --- | --- | --- | --- | --- |
| `RQ-RC06-01` | Are the constructs Performance Agency, Embodied Demand, Operational Spatial Integration, and Consequence sufficiently discriminant? | D03, D04, D09, D10 | cross-domain | construct_validity_gap, terminology_collision | `blocking` |
| `RQ-RC06-02` | Does the evidence model distinguish direct fact, attributed claim, synthesis, interpretation, proposition, and forecast clearly enough? | D13 | ASR001-D13-C01 | evidence_classification_gap, ambiguity | `major` |
| `RQ-RC06-03` | Do internal trial examples risk becoming hidden precedents or weights for category membership? | D10, D13 | ASR001-D10-C01, ASR001-D13-C02 | hidden_scoring_risk, conformance_boundary_leak | `blocking` |
| `RQ-RC06-04` | Are unknown, disputed, partial, absent, and not-evidenced states epistemically distinct in the current model? | D13 | ASR001-D13-C02 | evidence_state_defect, terminology_collision | `blocking` |
| `RQ-RC06-05` | Is any clause broader than the evidence base represented by BC-001–BC-020 and the internal trials? | D01, D02, D03, D04, D05, D06, D07, D08, D09, D10, D11, D12, D13, D14, D15 | cross-domain | scope_violation, evidence_burden_defect | `blocking` |

## RC-07 — Evidence and data governance

| ID | Question | Domains | Clauses | Issue types | Criticality |
| --- | --- | --- | --- | --- | --- |
| `RQ-RC07-01` | Are source provenance, temporal status, access date, limitation, and claim class sufficient for audit and reuse? | D13, D15 | ASR001-D13-C01, ASR001-D15-C01 | evidence_classification_gap, machine_readability_gap | `blocking` |
| `RQ-RC07-02` | Does correction and supersession preserve a complete audit trail without silently overwriting material changes? | D14 | ASR001-D14-C02 | lifecycle_gap, verification_gap | `blocking` |
| `RQ-RC07-03` | Are biometric, physiological, identity, telemetry, and reviewer data governance concerns visible without pretending ASR-001 is a privacy standard? | D07, D12, D14 | ASR001-D07-C01, ASR001-D12-C01, ASR001-D14-C01 | privacy_security_gap, scope_violation | `blocking` |
| `RQ-RC07-04` | Can machine validation distinguish structural validity from evidence truth, reviewer judgment, and underlying-system quality? | D13, D15 | ASR001-D13-C01, ASR001-D15-C02 | conformance_boundary_leak, verification_gap | `blocking` |
| `RQ-RC07-05` | Are extension namespaces, licensing notices, and reuse boundaries sufficient for machine-readable distributions? | D15 | ASR001-D15-C02 | machine_readability_gap, licensing_gap | `major` |

## Interpretation

Criticality organizes review attention. It is not a numerical score, vote, reviewer rank, or adoption threshold.
