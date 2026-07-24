# ASR-001 Applicability Model

**Version:** 0.1  
**Status:** Working Draft support model — not conformance rules

## 1. Purpose

Applicability determines whether a candidate disclosure obligation is relevant to the bounded profile subject.

It prevents two errors:

1. forcing irrelevant fields into every profile;
2. hiding relevant evidence by treating all clauses as optional.

## 2. Applicability Classes

### `always`

The profile needs the information for basic identity, interpretation, provenance, governance, or lifecycle control.

### `when_feature_present`

The obligation applies when the profiled configuration contains the feature or relation named by the clause.

### `when_claim_made`

The obligation applies when the profile or provider makes the relevant factual, analytical, category, safety, performance, or commercial claim.

### `when_measurement_or_comparison_claimed`

The obligation applies when metrics, rankings, comparison, calibration, equivalence, or performance interpretation are presented.

### `when_contest_or_outcome_present`

The obligation applies when the profile contains a contest, result, officiation process, ranking, penalty, or consequence structure.

### `when_distributed_operation_claimed`

The obligation applies when more than one physical site, remote performer, remote operator, shared computational state, or cross-site integrity relation is claimed.

### `when_human_performance_claimed`

The obligation applies when live, remote, assisted, physiological, or other human Performance Agency is claimed.

### `when_machine_readable_distribution_provided`

The obligation applies when JSON, CSV, RDF, an API, or another structured profile distribution is supplied.

## 3. Applicability Result

A future profile records one of:

- `applicable`;
- `not_applicable`;
- `unknown`;
- `not_evidenced`;
- `disputed`.

A result includes a short basis.

`not_applicable` describes the clause trigger, not product quality.

## 4. Conditional Integrity

A conditional clause can depend on another clause.

Examples:

- distributed-arena details depend on a distributed-operation claim;
- calibration disclosure depends on measurement or comparison;
- Agency Segments depend on time-varying or regime-varying control;
- intentional biological control details depend on that performance channel;
- participatory actor details depend on material external influence.

Dependencies are explicit rather than inferred from empty fields.

## 5. Missing Information

When a clause is applicable but evidence is unavailable, the profile preserves `unknown` or `not_evidenced`.

Missing evidence does not become:

- absence;
- failure of the underlying system;
- a zero score;
- a negative vendor ranking.

## 6. Applicability Review

Applicability can be checked through:

- configuration documentation;
- rulebooks;
- technical specifications;
- event procedures;
- provider declarations;
- evidence records;
- human review.

The reviewer records ambiguity rather than silently selecting the most favorable interpretation.
