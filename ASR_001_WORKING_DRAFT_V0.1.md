# ASR-001 — Spatial Athletic System Evidence Profile

**Document state:** Non-public Working Draft  
**Version:** 0.1  
**Status:** Candidate Normative Core — unpublished  
**Conformance subject:** Evidence-profile document or machine-readable profile instance only

## 1. Interpretation

The key words **MUST**, **MUST NOT**, **SHOULD**, and **MAY** in this Working Draft express candidate normative intent.

They do not establish a published standard, certification program, industry adoption, or product approval.

A conditional clause applies only when its declared trigger is present. Missing evidence is preserved as unknown, disputed, or not evidenced rather than converted into a score.

## 2. Conformance Boundary

Candidate conformance concerns the evidence profile. It does not certify the underlying sport, product, system quality, safety, clinical efficacy, federation recognition, category membership, or market rank.

## 3. Profile Clauses

### D01 — Subject Identity and Object Lock

#### ASR001-D01-C01 — Canonical profile subject

**Candidate clause:** The profile MUST identify one bounded, versioned configuration as its canonical subject.

**Applicability:** `always`

**Condition:** Every ASR-001 profile.

**Profile field:** `subject.canonical_subject`

**Verification:** Verify `subject.canonical_subject` through document_presence, field_presence, human_review.

**Rationale:** Object lock is the precondition for interpreting every other disclosure.

**Uncertainty:** Ambiguity is recorded as unresolved rather than broadened silently.

**Evidence anchors:** BC-007, BC-009, BC-014, BC-016

**Exclusion guards:** automatic_category_certification, product_ranking

#### ASR001-D01-C02 — Related-object boundary

**Candidate clause:** The profile MUST identify secondary related objects and states which findings do not transfer to them.

**Applicability:** `always`

**Condition:** Whenever secondary objects, organizations, platforms, activities, or events are referenced.

**Profile field:** `subject.related_objects`

**Verification:** Verify `subject.related_objects` through cross_reference_integrity, human_review.

**Rationale:** Explicit boundaries prevent scope inflation.

**Uncertainty:** Unknown relationships remain unknown.

**Evidence anchors:** BC-007, BC-009, BC-014

**Exclusion guards:** universal_sport_definition, automatic_category_certification

### D02 — Operating Context and System Roles

#### ASR001-D02-C01 — Operating context

**Candidate clause:** The profile MUST describe the deployment context, location, participant setting, temporal state, and intended use.

**Applicability:** `always`

**Condition:** Every profile.

**Profile field:** `operating_context`

**Verification:** Verify `operating_context` through document_presence, field_presence, temporal_consistency.

**Rationale:** Context determines applicability and interpretation.

**Uncertainty:** Unpublished configuration details are marked not evidenced.

**Evidence anchors:** BC-009, BC-014, BC-016, BC-019

**Exclusion guards:** clinical_efficacy_requirements, product_ranking

#### ASR001-D02-C02 — System roles and dependencies

**Candidate clause:** The profile MUST list system roles and material technical, institutional, equipment, and organizational dependencies.

**Applicability:** `always`

**Condition:** Every profile; empty roles are not permitted.

**Profile field:** `system_roles_and_dependencies`

**Verification:** Verify `system_roles_and_dependencies` through field_presence, cross_reference_integrity, human_review.

**Rationale:** Profiles remain configuration-specific only when dependencies are visible.

**Uncertainty:** Dependency availability can be unknown or version-limited.

**Evidence anchors:** BC-008, BC-013, BC-015, BC-016

**Exclusion guards:** commercial_endorsement, federation_recognition

### D03 — Performance Window and Performance Agency

#### ASR001-D03-C01 — Performance window

**Candidate clause:** When human Performance Agency or performance-dependent result is claimed, the profile MUST define the interval during which actions can materially affect the evaluated result or support outcome.

**Applicability:** `when_human_performance_claimed`

**Condition:** Human Performance Agency or performance-dependent result is claimed.

**Profile field:** `performance.performance_window`

**Verification:** Verify `performance.performance_window` through field_presence, evidence_traceability, human_review.

**Rationale:** The performance window separates live performance from prior design or later analysis.

**Uncertainty:** If the window cannot be bounded, the agency finding remains disputed or unknown.

**Evidence anchors:** BC-010, BC-017, BC-018, BC-019

**Exclusion guards:** causal_attribution_scoring, final_bci_athletic_membership

#### ASR001-D03-C02 — Agency modes and segments

**Candidate clause:** When more than one agency mode exists or control varies by phase or regime, the profile MUST describe active agents, assistance, autonomy, and phase-level handoff when control changes.

**Applicability:** `when_human_performance_claimed`

**Condition:** More than one agency mode exists or control varies by phase or regime.

**Profile field:** `performance.agency_segments`

**Verification:** Verify `performance.agency_segments` through conditional_logic, evidence_traceability, human_review.

**Rationale:** Agency Segments preserve observed control without pretending to solve causal attribution.

**Uncertainty:** Permitted control modes are not presented as observed transitions without evidence.

**Evidence anchors:** BC-010, BC-017, BC-019

**Exclusion guards:** causal_attribution_scoring, automatic_category_certification

### D04 — Performance Interface and Embodied Demand

#### ASR001-D04-C01 — Performance interface channels

**Candidate clause:** When human performance is part of the profiled configuration, the profile MUST describe the channels through which human action or intention enters the system.

**Applicability:** `when_human_performance_claimed`

**Condition:** Human performance is part of the profiled configuration.

**Profile field:** `performance.interface_channels`

**Verification:** Verify `performance.interface_channels` through field_presence, controlled_vocabulary, human_review.

**Rationale:** Interface description prevents remote, assisted, tracked, and biological channels from being collapsed.

**Uncertainty:** Unclear or proprietary interface behavior is marked not evidenced.

**Evidence anchors:** BC-004, BC-005, BC-013, BC-017, BC-018

**Exclusion guards:** minimum_embodiment_threshold, final_bci_athletic_membership

#### ASR001-D04-C02 — Embodied demand and biological control

**Candidate clause:** When the profile makes an embodiment, athletic, physiological, or biological-control claim, the profile MUST describe evidenced bodily, physiological, sensorimotor, cognitive, or adaptive demands without assigning an embodiment score.

**Applicability:** `when_human_performance_claimed`

**Condition:** The profile makes an embodiment, athletic, physiological, or biological-control claim.

**Profile field:** `performance.embodied_demand`

**Verification:** Verify `performance.embodied_demand` through evidence_traceability, human_review.

**Rationale:** Channel-based disclosure preserves diversity without inventing a universal threshold.

**Uncertainty:** BCI and other disputed channels retain unresolved category relation.

**Evidence anchors:** BC-002, BC-011, BC-012, BC-018

**Exclusion guards:** minimum_embodiment_threshold, final_bci_athletic_membership, spatiality_level

### D05 — Arena and Distributed-Arena Relation

#### ASR001-D05-C01 — Arena configuration

**Candidate clause:** The profile MUST describe physical, computational, and unified arenas, rule-bearing zones, and tracking volumes relevant to the configuration.

**Applicability:** `always`

**Condition:** Every profile; non-spatial support contexts can state not applicable for specific arena elements.

**Profile field:** `arena.configuration`

**Verification:** Verify `arena.configuration` through field_presence, evidence_traceability, human_review.

**Rationale:** Arena disclosure anchors Operational Spatial Integration claims.

**Uncertainty:** Absent public technical detail is preserved as not evidenced.

**Evidence anchors:** BC-005, BC-011, BC-012, BC-014

**Exclusion guards:** spatiality_level, automatic_category_certification

#### ASR001-D05-C02 — Distributed-arena relation

**Candidate clause:** When more than one physical site or remote-control relation is material, the profile MUST describe topology, shared state, synchronization, sites, remote operators, calibration relation, officiation, and responsibility when distributed operation is claimed.

**Applicability:** `when_distributed_operation_claimed`

**Condition:** More than one physical site or remote-control relation is material.

**Profile field:** `arena.distributed_relation`

**Verification:** Verify `arena.distributed_relation` through conditional_logic, evidence_traceability, human_review.

**Rationale:** Explicit topology prevents global availability from being mistaken for remote synchronous integrity.

**Uncertainty:** Technical values remain not evidenced when no authoritative source exists.

**Evidence anchors:** BC-005, BC-008, BC-013, BC-015, BC-019

**Exclusion guards:** remote_synchronous_technical_tolerances, automatic_category_certification

### D06 — Constraints and Rule Execution

#### ASR001-D06-C01 — Rule and constraint sources

**Candidate clause:** When rules, eligibility, task constraints, or contest procedures govern the configuration, the profile MUST identify the authoritative rules, constraints, versions, and responsible bodies used by the configuration.

**Applicability:** `when_feature_present`

**Condition:** Rules, eligibility, task constraints, or contest procedures govern the configuration.

**Profile field:** `constraints.authoritative_sources`

**Verification:** Verify `constraints.authoritative_sources` through cross_reference_integrity, temporal_consistency, evidence_traceability.

**Rationale:** Rule provenance supports integrity and correction.

**Uncertainty:** Unavailable operative rules are disclosed rather than inferred from marketing.

**Evidence anchors:** BC-001, BC-003, BC-013, BC-015, BC-017

**Exclusion guards:** federation_recognition, commercial_endorsement

#### ASR001-D06-C02 — Operative rule execution

**Candidate clause:** When a rule-bearing or constraint-bearing mechanism exists, the profile MUST describe whether constraints are applied through people, equipment, sensors, geometry, software, or combinations.

**Applicability:** `when_feature_present`

**Condition:** A rule-bearing or constraint-bearing mechanism exists.

**Profile field:** `constraints.execution`

**Verification:** Verify `constraints.execution` through field_presence, evidence_traceability, human_review.

**Rationale:** Implementation disclosure exposes divergence and failure paths.

**Uncertainty:** Opaque code can be recorded as partially evidenced.

**Evidence anchors:** BC-013, BC-015, BC-017, BC-020

**Exclusion guards:** automatic_category_certification, quality_grade

### D07 — Sensing, Tracking, and State Estimation

#### ASR001-D07-C01 — Observation and estimation boundary

**Candidate clause:** When sensing, tracking, physiological measurement, or state estimation is used, the profile MUST the profile distinguishes directly measured state, inferred state, calculated state, and provider-declared state.

**Applicability:** `when_feature_present`

**Condition:** Sensing, tracking, physiological measurement, or state estimation is used.

**Profile field:** `sensing.observation_estimation_boundary`

**Verification:** Verify `sensing.observation_estimation_boundary` through field_presence, evidence_traceability, human_review.

**Rationale:** The distinction is necessary for interpreting measurement and failure.

**Uncertainty:** Undisclosed algorithms remain not evidenced.

**Evidence anchors:** BC-008, BC-013, BC-015, BC-018, BC-019

**Exclusion guards:** quality_grade, clinical_efficacy_requirements

#### ASR001-D07-C02 — Sensing failure and uncertainty

**Candidate clause:** When sensing, tracking, or state estimation is material, the profile MUST describe known loss, drift, occlusion, latency, decoder, or state-estimation limitations and their effect on the profile subject.

**Applicability:** `when_feature_present`

**Condition:** Sensing, tracking, or state estimation is material.

**Profile field:** `sensing.failure_and_uncertainty`

**Verification:** Verify `sensing.failure_and_uncertainty` through evidence_traceability, human_review.

**Rationale:** Failure disclosure connects technical conditions to integrity without creating a score.

**Uncertainty:** Unknown failure characteristics remain unknown.

**Evidence anchors:** BC-013, BC-014, BC-015, BC-018

**Exclusion guards:** safety_certification, remote_synchronous_technical_tolerances

### D08 — Measurement and Comparability Conditions

#### ASR001-D08-C01 — Metric and calibration disclosure

**Candidate clause:** When a metric, measurement, ranking, assessment, or quantitative claim is presented, the profile MUST identify each material metric, unit, source, calibration basis, uncertainty, and intended use.

**Applicability:** `when_measurement_or_comparison_claimed`

**Condition:** A metric, measurement, ranking, assessment, or quantitative claim is presented.

**Profile field:** `measurement.metrics`

**Verification:** Verify `measurement.metrics` through field_presence, evidence_traceability, temporal_consistency.

**Rationale:** Metric provenance is necessary before comparison.

**Uncertainty:** Unavailable calibration information is not converted into zero quality.

**Evidence anchors:** BC-008, BC-011, BC-013, BC-015, BC-018

**Exclusion guards:** total_score, quality_grade, clinical_efficacy_requirements

#### ASR001-D08-C02 — Comparability conditions

**Candidate clause:** When two or more performances, systems, sessions, or results are compared, the profile MUST state the equipment, version, environment, classification, adaptation, network, and procedural conditions under which a comparison is intended.

**Applicability:** `when_measurement_or_comparison_claimed`

**Condition:** Two or more performances, systems, sessions, or results are compared.

**Profile field:** `measurement.comparability_conditions`

**Verification:** Verify `measurement.comparability_conditions` through conditional_logic, evidence_traceability, human_review.

**Rationale:** Explicit conditions prevent unqualified equivalence claims.

**Uncertainty:** Partial comparability remains a valid state.

**Evidence anchors:** BC-003, BC-004, BC-008, BC-013, BC-015, BC-017

**Exclusion guards:** vendor_ranking, product_ranking, remote_synchronous_technical_tolerances

### D09 — Officiation, Outcome, and Consequence Structure

#### ASR001-D09-C01 — Officiation and decision authority

**Candidate clause:** When a contest, result, penalty, therapeutic decision, or formal outcome is present, the profile MUST identify human, automated, operator, and hybrid decision authorities, including correction or appeal paths where they exist.

**Applicability:** `when_contest_or_outcome_present`

**Condition:** A contest, result, penalty, therapeutic decision, or formal outcome is present.

**Profile field:** `outcome.officiation_and_authority`

**Verification:** Verify `outcome.officiation_and_authority` through field_presence, cross_reference_integrity, human_review.

**Rationale:** Authority disclosure supports accountability.

**Uncertainty:** No appeal process is recorded as absent or not evidenced, not invented.

**Evidence anchors:** BC-001, BC-013, BC-015, BC-016, BC-019

**Exclusion guards:** federation_recognition, safety_certification

#### ASR001-D09-C02 — Outcome and consequence structure

**Candidate clause:** When a result or consequential support process exists, the profile MUST describe the evaluated outcome, openness, ranking or support result, and derived consequence structure.

**Applicability:** `when_contest_or_outcome_present`

**Condition:** A result or consequential support process exists.

**Profile field:** `outcome.outcome_and_consequence`

**Verification:** Verify `outcome.outcome_and_consequence` through field_presence, human_review.

**Rationale:** Consequence remains descriptive and derived rather than a score.

**Uncertainty:** Non-contest systems can mark outcome openness not applicable.

**Evidence anchors:** BC-010, BC-016, BC-017, BC-020

**Exclusion guards:** total_score, clinical_efficacy_requirements

### D10 — Operational Spatial Integration Functions

#### ASR001-D10-C01 — Spatial function claims

**Candidate clause:** When the profile claims computationally mediated space represents, enables, mediates, constrains, measures, compares, or officiates, the profile MUST identify each claimed Operational Spatial Integration function and links it to a mechanism, affected object, evidence, and significance.

**Applicability:** `when_claim_made`

**Condition:** The profile claims computationally mediated space represents, enables, mediates, constrains, measures, compares, or officiates.

**Profile field:** `spatial_integration.functions`

**Verification:** Verify `spatial_integration.functions` through controlled_vocabulary, evidence_traceability, human_review.

**Rationale:** Function-level claims preserve discrimination without a spatiality score.

**Uncertainty:** Disputed or partial functions remain explicit.

**Evidence anchors:** BC-005, BC-006, BC-008, BC-013, BC-014, BC-019

**Exclusion guards:** spatiality_level, automatic_category_certification

#### ASR001-D10-C02 — Spatial function failure effects

**Candidate clause:** When an Operational Spatial Integration function is claimed, the profile MUST describe how failure or removal of each constitutive or supportive spatial function changes the configured activity or result.

**Applicability:** `when_claim_made`

**Condition:** An Operational Spatial Integration function is claimed.

**Profile field:** `spatial_integration.failure_effects`

**Verification:** Verify `spatial_integration.failure_effects` through evidence_traceability, human_review.

**Rationale:** Failure effects test the operational nature of the claim.

**Uncertainty:** When failure effects are unknown, the claim remains limited.

**Evidence anchors:** BC-008, BC-013, BC-014, BC-015, BC-018

**Exclusion guards:** quality_grade, automatic_category_certification

### D11 — Presence, Participation, and External Actors

#### ASR001-D11-C01 — Actor-role disclosure

**Candidate clause:** The profile MUST identify performers, coaches, officials, operators, supervisors, spectators, developers, and other material actors.

**Applicability:** `always`

**Condition:** Every profile.

**Profile field:** `actors.roles`

**Verification:** Verify `actors.roles` through field_presence, controlled_vocabulary, human_review.

**Rationale:** Role separation prevents attribution errors.

**Uncertainty:** Unclear roles remain unresolved.

**Evidence anchors:** BC-003, BC-016, BC-019, BC-020

**Exclusion guards:** federation_recognition, automatic_category_certification

#### ASR001-D11-C02 — Participatory actor relation

**Candidate clause:** When a non-performing actor materially affects the configured process, the profile MUST describe external actors who materially alter resources, constraints, information, triggers, or supervision without performing.

**Applicability:** `when_feature_present`

**Condition:** A non-performing actor materially affects the configured process.

**Profile field:** `actors.participatory_relations`

**Verification:** Verify `actors.participatory_relations` through conditional_logic, evidence_traceability, human_review.

**Rationale:** The relation preserves agency and governance boundaries.

**Uncertainty:** Materiality can remain disputed.

**Evidence anchors:** BC-003, BC-016, BC-020

**Exclusion guards:** causal_attribution_scoring, automatic_category_certification

### D12 — Safety, Accessibility, and Human-Limit Disclosures

#### ASR001-D12-C01 — Safety, accessibility, and human-limit disclosure

**Candidate clause:** The profile MUST record known hazards, accessibility conditions, body variation, adaptive equipment, fatigue, collision, cybersickness, cognitive demand, and relevant limitations.

**Applicability:** `always`

**Condition:** Every profile records applicable disclosures or a justified not-applicable state.

**Profile field:** `human_factors.disclosures`

**Verification:** Verify `human_factors.disclosures` through document_presence, evidence_traceability, human_review.

**Rationale:** Disclosure supports responsible interpretation without certifying safety.

**Uncertainty:** Unknown hazards remain unknown and clinical claims retain their evidence class.

**Evidence anchors:** BC-004, BC-014, BC-015, BC-016, BC-017, BC-018

**Exclusion guards:** safety_certification, clinical_efficacy_requirements, quality_grade

#### ASR001-D12-C02 — Operational responsibility and limitations

**Candidate clause:** When operational responsibility is material to participation or support use, the profile MUST identify responsible parties for deployment, safety controls, access decisions, supervision, and known limitation management.

**Applicability:** `when_feature_present`

**Condition:** Operational responsibility is material to participation or support use.

**Profile field:** `human_factors.operational_responsibility`

**Verification:** Verify `human_factors.operational_responsibility` through cross_reference_integrity, evidence_traceability, human_review.

**Rationale:** Responsibility disclosure separates documentation from approval.

**Uncertainty:** Unassigned responsibility is recorded explicitly.

**Evidence anchors:** BC-014, BC-015, BC-016, BC-017

**Exclusion guards:** safety_certification, clinical_efficacy_requirements

### D13 — Evidence, Claims, and Uncertainty

#### ASR001-D13-C01 — Claim classification and source linkage

**Candidate clause:** The profile MUST assign a claim class and traceable evidence record to each material factual or analytical claim.

**Applicability:** `always`

**Condition:** Every material claim in the profile.

**Profile field:** `evidence.claims`

**Verification:** Verify `evidence.claims` through evidence_traceability, cross_reference_integrity, human_review.

**Rationale:** Claim separation is the core trust function of the profile.

**Uncertainty:** Unsupported claims remain attributed or not evidenced.

**Evidence anchors:** BC-014, BC-015, BC-016, BC-018

**Exclusion guards:** commercial_endorsement, paid_favorable_classification

#### ASR001-D13-C02 — Uncertainty and limitation states

**Candidate clause:** The profile MUST the profile preserves supported, partial, absent, disputed, unknown, not applicable, and not evidenced states with a stated basis.

**Applicability:** `always`

**Condition:** Every profile.

**Profile field:** `evidence.uncertainty_states`

**Verification:** Verify `evidence.uncertainty_states` through controlled_vocabulary, conditional_logic, human_review.

**Rationale:** Uncertainty is a valid output rather than a failed score.

**Uncertainty:** Unknown is never inferred as absence.

**Evidence anchors:** BC-005, BC-007, BC-009, BC-015, BC-018

**Exclusion guards:** total_score, maturity_level, quality_grade

### D14 — Governance, Change, and Correction

#### ASR001-D14-C01 — Governance, version, and responsible authority

**Candidate clause:** The profile MUST identify the responsible profile publisher, system authority, rule or software versions, review date, and material commercial relationships.

**Applicability:** `always`

**Condition:** Every profile.

**Profile field:** `governance.authority_and_versions`

**Verification:** Verify `governance.authority_and_versions` through field_presence, temporal_consistency, cross_reference_integrity.

**Rationale:** Governance metadata supports accountability and independence.

**Uncertainty:** Unknown authority is disclosed.

**Evidence anchors:** BC-001, BC-013, BC-015, BC-016, BC-020

**Exclusion guards:** paid_favorable_classification, commercial_endorsement, federation_recognition

#### ASR001-D14-C02 — Correction and supersession

**Candidate clause:** The profile MUST record substantive corrections, affected fields or clauses, reason, evidence, date, and supersession relation.

**Applicability:** `always`

**Condition:** Every profile supports lifecycle correction, even when no correction has occurred.

**Profile field:** `governance.corrections_and_supersession`

**Verification:** Verify `governance.corrections_and_supersession` through document_presence, cross_reference_integrity, temporal_consistency.

**Rationale:** Append-only correction strengthens reference trust.

**Uncertainty:** No-correction history is distinguishable from unavailable history.

**Evidence anchors:** BC-020

**Exclusion guards:** commercial_endorsement, quality_grade

### D15 — Profile Metadata and Machine Readability

#### ASR001-D15-C01 — Profile identity and metadata

**Candidate clause:** The profile MUST have a stable identifier, profile version, creation and revision dates, language, status, subject identifier, and applicable ASR Working Draft version.

**Applicability:** `always`

**Condition:** Every profile.

**Profile field:** `profile_metadata`

**Verification:** Verify `profile_metadata` through field_presence, controlled_vocabulary, temporal_consistency.

**Rationale:** Stable metadata enables citation, correction, and exchange.

**Uncertainty:** Draft status remains visible.

**Evidence anchors:** BC-001, BC-020

**Exclusion guards:** industry_adoption_claim, automatic_category_certification

#### ASR001-D15-C02 — Machine-readable distribution and licensing

**Candidate clause:** When a structured distribution, API, JSON, RDF, CSV, or equivalent is supplied, the profile MUST identify machine-readable distributions, serialization version, validation status, license or reuse notice, and extension namespaces when provided.

**Applicability:** `when_machine_readable_distribution_provided`

**Condition:** A structured distribution, API, JSON, RDF, CSV, or equivalent is supplied.

**Profile field:** `distributions`

**Verification:** Verify `distributions` through machine_validation, cross_reference_integrity, field_presence.

**Rationale:** Distribution metadata supports reliable reuse without converting research licensing into third-party relicensing.

**Uncertainty:** Absent structured distribution is not a profile-quality score.

**Evidence anchors:** BC-001, BC-020

**Exclusion guards:** commercial_endorsement, automatic_category_certification

## 4. Implementation Status

The profile model and schema accompanying this Working Draft are candidate implementation artifacts for internal trial.

They are not the historical Boundary Case Schema and do not alter any corpus record.

## 5. Publication Status

ASR-001 remains unpublished. Public Review, certification, external conformance claims, and industry-adoption claims remain unauthorized.
