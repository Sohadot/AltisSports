# Targeted Boundary Deepening — Sprint 6

**Asset:** AltisSports  
**Sprint:** Sprint 6 — Targeted Boundary Deepening and Schema v0.3 Decision  
**Status:** Human-Reviewed Targeted Research — Not a Standard  
**Access date:** 2026-07-24  
**Depends on:** `SECOND_STRATUM_FINDINGS_V0.2.md`, BC-015, BC-017, BC-018, BC-019, BC-020

## 1. Purpose

Sprint 6 does not add a third broad case wave. It deepens the four structural gaps exposed by BC-011–BC-020 and decides whether schema v0.2 can represent them without distortion.

The targeted questions are:

1. Does examined Virtual Taekwondo evidence establish a geographically distributed synchronous contest?
2. Can time-varying human–machine agency be represented without phase-level records?
3. How should intentional biological control be represented without equating visible movement with embodiment or every biosignal with athletic performance?
4. How should spectators or other outsiders who alter resources or constraints be represented?
5. Does the evidence justify schema v0.3?

## 2. BC-015 — Remote Distributed Arena Deepening

### Evidence examined

1. Virtual Taekwondo, **VTKD Rule Book Archive — WT Virtual Taekwondo Rules and Regulations (April 2026)**  
   https://virtualtkd.gg/rulebooks/
2. Virtual Taekwondo, **VTKD User Manual 1.2.34**  
   https://virtualtkd.gg/manuals/vtkd-user-manual-1-2-34/
3. Virtual Taekwondo, **Patch Notes**  
   https://virtualtkd.gg/patch-notes/
4. Existing World Taekwondo and Virtual Taekwondo evidence retained in BC-015.

### Finding

The examined public materials support a co-located, multi-station competition architecture with:

- event mats and start positions;
- shared displays and technical operators;
- Game Master administration;
- players joining a shared match room;
- same-network setup instructions;
- session and player calibration;
- active work on calibration consistency.

They do **not** establish:

- opponents in geographically separate physical sites competing synchronously;
- a public latency budget;
- cross-site calibration equivalence;
- cross-site safety responsibility;
- remote officiation and protest handling;
- network-failure remediation for a distributed match.

### Decision

BC-015 remains a supported **co-located Spatial Athletic Contest**. The remote-distributed hypothesis is closed as **not evidenced in the examined public configuration**, not as impossible.

Global distribution, multiple event hubs, or the technical possibility of networked rooms must not be converted into evidence of remote synchronous contest integrity.

### Schema implication

A `distributed_arena_relation` is required because “remote” is not one property. It must identify topology, shared state, synchronization, latency governance, calibration, officiation, safety, evidence, and uncertainty.

## 3. BC-017 and BC-019 — Phase-Level Agency

### BC-017 evidence pressure

CYBATHLON states that exoskeletons may operate in manual, semi-autonomous, or autonomous modes. The permitted control regime can therefore shift the causal relationship between pilot and device.

Primary source:

- CYBATHLON / ETH Zurich, **Exoskeleton Race**  
  https://cybathlon.com/en/event/disciplines/exo

The public source establishes permitted regimes. It does not establish the exact transition sequence used by every team or task.

### BC-019 evidence pressure

DARPA describes autonomous systems that map, navigate, and search subterranean environments, while teams contribute design, configuration, command-post supervision, and permitted intervention.

Primary sources:

- DARPA, **Subterranean Challenge program**  
  https://www.darpa.mil/research/programs/darpa-subterranean-challenge
- DARPA, **Subterranean Challenge Final Event**  
  https://www.darpa.mil/research/challenges/subterranean

One summary list containing `design_engineering`, `agency_handoff`, and `autonomous_execution` cannot show when each relation applied or what caused the evaluated result.

### Decision

`agency_segments` is required.

Each segment must identify:

- phase or declared control regime;
- whether the segment is observed, rule-declared, inferred, or unknown;
- active agents;
- primary control;
- transition trigger;
- permitted assistance;
- causal attribution;
- evidence;
- uncertainty.

A declared regime must not be presented as an observed transition.

## 4. BC-018 — Intentional Biological Control

### Evidence examined

1. CYBATHLON / ETH Zurich, **Brain-Computer Interface Race**  
   https://cybathlon.com/en/event/disciplines/bci
2. CYBATHLON / ETH Zurich, **Brain-Computer Interface Race Tasks**  
   https://cybathlon.com/en/events/challenges/challenges-2024/bci-tasks
3. Existing team-specific research retained in BC-018.

The pilot intentionally generates brain-activity patterns at task-relevant times. A decoder translates those patterns into commands controlling an animated task environment.

### Decision

Intentional biological control is recognized as a **live bodily-origin performance channel** when:

- signal generation is intentional;
- the signal is task-coupled;
- human skill is causally necessary;
- incidental biosignal measurement is excluded;
- decoder mediation is disclosed.

This supports Performance Agency.

It does **not** automatically establish athletic embodiment or Spatial Athletic System membership. BC-018 remains unresolved on that category relation.

### Schema implication

A dedicated optional profile is justified because existing `physiological_sensing` and `cognitive` labels cannot record intentionality, task coupling, decoder mediation, incidental-signal exclusion, and the unresolved athletic-embodiment relation.

No embodiment score or threshold is introduced.

## 5. BC-020 — Participatory Rule/Resource Actors

### Evidence retained

Formula E’s historical FANBOOST rule allowed public voting to allocate an optional power resource. The driver retained vehicle control and the decision whether and when to deploy the resource.

Existing official Formula E sources remain attached to BC-020.

### Decision

The spectator public is represented as a **Participatory Rule/Resource Actor**:

- it acts through a rule-authorized mechanism;
- it changes an available resource;
- it can indirectly affect the contest;
- it does not execute the driving performance;
- it is not an official by default;
- it does not acquire Performance Agency merely by influencing opportunity.

### Schema implication

`participatory_actor_relations` is required to describe actor type, mechanism, action window, resource or constraint effect, Performance Agency relation, rule-authority relation, evidence, and uncertainty.

## 6. Schema Decision

Schema v0.2 is structurally insufficient for the repeated distinctions above.

Schema v0.3 is authorized as an additive, non-scoring evolution with four fields:

- `agency_segments`
- `distributed_arena_relation`
- `participatory_actor_relations`
- `intentional_biological_control`

The v0.2 schema and native v0.2 dataset remain immutable.

## 7. What Sprint 6 Does Not Establish

Sprint 6 does not establish:

- a remote Virtual Taekwondo competition;
- a normative latency limit;
- a universal agency-attribution formula;
- a minimum embodiment threshold;
- BCI membership in the Spatial Athletic System class;
- spectator Performance Agency;
- ASR conformance;
- certification;
- any total score or maturity level.

## 8. One-Sentence Verdict

Schema v0.3 is justified because v0.2 cannot faithfully represent when agency changes, how arenas are distributed, how intentional biosignals become action, or how outsiders alter contest resources without becoming performers.
