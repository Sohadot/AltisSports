# Boundary Cases BC-011 – BC-020

**Asset:** AltisSports  
**Sprint:** Sprint 5 — Second Antagonistic Stratum  
**Schema:** `BOUNDARY_CASE_SCHEMA_V0.2.json`  
**Version:** 0.2  
**Status:** Provisional Native v0.2 Research — Not a Standard  
**Access date:** 2026-07-24

## Sample Design

This stratum tests the v0.2 corrections through low-locomotion embodiment, strong computational arenas, support systems, assisted and alternative agency, human–AI handoff, and spectator intervention. Selection does not imply category membership.

| ID | Case | Provisional relation |
| --- | --- | --- |
| BC-011 | ISSF competitive shooting | `outside_core_spatial_athletic_class` |
| BC-012 | WPA cue sports | `outside_core_spatial_athletic_class` |
| BC-013 | Beat Saber World Cup competition | `spatial_athletic_contest` |
| BC-014 | Zero Latency Sol Raiders free-roam competitive experience | `spatial_athletic_system` |
| BC-015 | World Taekwondo Virtual Taekwondo competition | `spatial_athletic_contest` |
| BC-016 | MindMotion GO rehabilitation exercise system | `spatial_support_system` |
| BC-017 | CYBATHLON Exoskeleton Race | `outside_core_spatial_athletic_class` |
| BC-018 | CYBATHLON Brain-Computer Interface Race | `unresolved` |
| BC-019 | DARPA Subterranean Challenge Systems Competition | `outside_core_spatial_athletic_class` |
| BC-020 | Formula E race with FANBOOST | `outside_core_spatial_athletic_class` |

---

## BC-011 — ISSF competitive shooting

### Classified object

**Primary:** `activity`  
**Secondary:** `athletic_system`, `event`

ISSF-governed rifle, pistol, and shotgun competition is used as a low-locomotion embodied sport reference; no single discipline is generalized beyond common structural features.

### Evidence

1. **ISSF Rules — 2026 Rule Book** — International Shooting Sport Federation. https://www.issf-sports.org/rules — `federation_or_league_rules`, `C1`, temporal status `current`. Limitation: The portal hosts multiple discipline-specific rulebooks; this record does not claim one event format represents every shooting discipline.
2. **ISSF announces changes with 2026 Rulebook** — International Shooting Sport Federation. https://www.issf-sports.org/news/4878 — `official_announcement`, `C1`, temporal status `current`. Limitation: Announcement summarizes changes; the rulebook remains the controlling source.

### Performance window and agency

**Window:** From authorized preparation through shot release and scored series completion.

**Finding:** Athlete precision, timing, posture, and trigger execution materially determine the shot during the firing sequence.

**Agency modes:** `live_performance`

### AS³ reading

| Layer | Observation |
| --- | --- |
| L1 — Performance Agency | Clear live athlete agency during each shot. |
| L2 — Interface / Embodied Demand | Fine-motor and balance demands through regulated equipment. |
| L3 — Arena | Physical range and target geometry. |
| L4 — Rules | Detailed federation rules and equipment controls. |
| L5 — Sensing | Electronic target sensing may be used. |
| L6 — Measurement / Comparability | High precision; comparability is event-class specific. |
| L7 — Officiation / Outcome | Officials plus results systems. |
| L8 — Presence / Participation | Spectators do not determine performance. |
| L9 — Safety / Accessibility | Range safety and equipment governance are central. |
| L10 — Governance / Evidence | ISSF rulebooks are inspectable and versioned. |

### Operational Spatial Integration Profile

**Overall:** `partial` — Computational systems may support measurement and officiation, but the performance arena remains physical and the spatial-athletic core is not established.

| Function | Status | Significance | Mechanism | Failure effect |
| --- | --- | --- | --- | --- |
| `measure` | `supported` | `supportive` | Electronic target and results systems convert physical impacts into scored records. | A sensing or scoring failure can invalidate a shot value or result. |
| `officiate` | `partial` | `supportive` | Electronic scoring assists officials but does not constitute the athletic arena. | Incorrect system interpretation can trigger protest or correction. |

### Candidate invariant reading

| Candidate | Status | Notes |
| --- | --- | --- |
| `performance_agency` | `supported` | Live skill is causally necessary. |
| `constraint_integrity` | `supported` | Rule and equipment precision are high. |
| `comparability` | `supported` | Engineered within event classes. |
| `outcome_openness` | `supported` | Shot outcomes are performance-dependent. |

### Provisional finding

- **Sport/contest axis:** `sport`
- **Category relation:** `outside_core_spatial_athletic_class`
- **Confidence:** `high`

A strong embodied sport with little locomotion; it confirms that Embodied Performance must include fine motor, balance, and sensorimotor control without treating physical spatial skill as computational Spatiality.

### Objections and limitations

- Precision electronics could be over-read as a computational arena.
- Different shooting disciplines impose materially different demands.
- This case does not evaluate every ISSF discipline or adaptive classification.

### What would change the judgment

- A competition in which shared computational geometry directly constrains athlete targeting or movement as a constitutive arena.

---

## BC-012 — WPA cue sports

### Classified object

**Primary:** `activity`  
**Secondary:** `athletic_system`

Pocket billiards under WPA rules is used as a fine-motor physical-geometry case; the analysis does not generalize to every cue-sport discipline.

### Evidence

1. **World Pool Rules** — World Pool-Billiard Association. https://wpapool.com/rules/ — `federation_or_league_rules`, `C1`, temporal status `current`. Limitation: Rules cover pool disciplines; other cue-sport federations may use different codes.
2. **About the WPA** — World Pool-Billiard Association. https://wpapool.com/about/ — `official_announcement`, `C1`, temporal status `current`. Limitation: Organization history and self-description do not independently settle every definition of sport.

### Performance window and agency

**Window:** From the start of a turn through completion of the stroke sequence and resulting table state.

**Finding:** Players exercise live aiming, stroke, speed, spin, and positional judgment during each inning.

**Agency modes:** `live_performance`

### AS³ reading

| Layer | Observation |
| --- | --- |
| L1 — Performance Agency | Live player skill controls the table state. |
| L2 — Interface / Embodied Demand | Fine-motor cue delivery and sensorimotor control. |
| L3 — Arena | Physical table geometry is rule-bearing. |
| L4 — Rules | Rules and fouls are explicit. |
| L5 — Sensing | Human observation; no computational tracking required. |
| L6 — Measurement / Comparability | Equipment specifications and match formats. |
| L7 — Officiation / Outcome | Referees and declared winning conditions. |
| L8 — Presence / Participation | Spectators are non-constitutive. |
| L9 — Safety / Accessibility | Low-contact but posture and accessibility still matter. |
| L10 — Governance / Evidence | WPA publishes rules and governance material. |

### Operational Spatial Integration Profile

**Overall:** `absent` — The activity demands sophisticated physical spatial reasoning, but no computationally mediated space is operationally integrated by default.

No computational Spatial Function was evidenced for the classified object.

### Candidate invariant reading

| Candidate | Status | Notes |
| --- | --- | --- |
| `performance_agency` | `supported` | Live stroke execution is decisive. |
| `constraint_integrity` | `supported` | Physical geometry and rules are inspectable. |
| `comparability` | `supported` | Supported within specified equipment and formats. |
| `outcome_openness` | `supported` | Results emerge through play. |

### Provisional finding

- **Sport/contest axis:** `sport`
- **Category relation:** `outside_core_spatial_athletic_class`
- **Confidence:** `high`

Cue sports confirm that spatial skill and rule-bearing physical geometry are not Operational Spatial Integration. “Spatial” in everyday skill language must not be confused with the Altis category term.

### Objections and limitations

- The word spatial naturally describes positional skill, creating semantic confusion.
- Automated table tracking products would need separate product-level analysis.
- This record focuses on WPA pool, not snooker, carom, or every local equipment condition.

### What would change the judgment

- A contest where computational geometry jointly changes legal positions, measurement, or officiation as a constitutive arena.

---

## BC-013 — Beat Saber World Cup competition

### Classified object

**Primary:** `contest`  
**Secondary:** `spatial_athletic_contest`, `computational_contest`, `event`

The classified object is the Cube Community Beat Saber World Cup contest format, not Beat Saber as an entire product category or all rhythm games.

### Evidence

1. **Beat Saber World Cup 2026 Rulebook** — Cube Community. https://bs-announcements.vercel.app/ — `standard_or_sporting_code`, `C1`, temporal status `current`. Limitation: Community tournament rules are not federation recognition or an industry standard.
2. **Beat Saber World Cup 2022 — Rules and Match Flow** — Cube Community. https://old.cube.community/main/tournament/bswc2022/info — `standard_or_sporting_code`, `C1`, temporal status `historical`. Limitation: Historical rule edition; useful for explicit scoring and Tournament Assistant structure, not current details.
3. **Beat Saber — official product site** — Beat Games. https://beatsaber.com/ — `first_party_technical`, `C3`, temporal status `current`. Limitation: Product marketing establishes intended interaction, not competitive integrity.

### Performance window and agency

**Window:** From map start through completion and score submission in the scheduled match.

**Finding:** Players execute tracked hand and upper-body movements live; in-game score depends on timing and motion during each map.

**Agency modes:** `live_performance`

### AS³ reading

| Layer | Observation |
| --- | --- |
| L1 — Performance Agency | Clear live tracked performance. |
| L2 — Interface / Embodied Demand | Tracked controllers and sustained sensorimotor execution. |
| L3 — Arena | Computational rhythm map and obstacles. |
| L4 — Rules | Game code plus tournament rules. |
| L5 — Sensing | Headset/controller tracking is constitutive. |
| L6 — Measurement / Comparability | Score is precise; hardware and patch comparability remain risks. |
| L7 — Officiation / Outcome | Software, plugins, and staff determine valid results. |
| L8 — Presence / Participation | Remote teams and streams support participation. |
| L9 — Safety / Accessibility | Fatigue, room safety, and hardware access matter. |
| L10 — Governance / Evidence | Community rules are inspectable but institutionally limited. |

### Operational Spatial Integration Profile

**Overall:** `supported` — Embodied live performance and a rule-bearing computational arena are jointly constitutive. Contest governance exists, although it is community- rather than federation-based.

| Function | Status | Significance | Mechanism | Failure effect |
| --- | --- | --- | --- | --- |
| `represent` | `supported` | `constitutive` | The computational arena represents notes, obstacles, timing, and player action. | Loss of representation makes the task unintelligible. |
| `enable` | `supported` | `constitutive` | Tracked XR input enables the performance channel. | Tracking loss prevents valid performance. |
| `constrain` | `supported` | `constitutive` | Map timing, note direction, and obstacle geometry constrain legal action. | Patch or map inconsistency changes the task. |
| `measure` | `supported` | `constitutive` | The game converts tracked actions into score. | Tracking or scoring defects alter results. |
| `compare` | `partial` | `supportive` | Tournament controls versions, maps, and aggregation but cannot eliminate all hardware variance. | Uncontrolled hardware or software differences weaken comparison. |
| `officiate` | `partial` | `supportive` | Software and tournament staff jointly resolve match state and rule violations. | Plugin or stream evidence failure can make disputes difficult to resolve. |

### Candidate invariant reading

| Candidate | Status | Notes |
| --- | --- | --- |
| `performance_agency` | `supported` | Live tracked skill is necessary. |
| `constraint_integrity` | `supported` | Game and tournament rules are identifiable. |
| `comparability` | `partial` | Controls exist but hardware and version conditions remain imperfect. |
| `outcome_openness` | `supported` | Scores are performance-dependent. |

### Provisional finding

- **Sport/contest axis:** `digital_competition_not_settled_as_sport`
- **Category relation:** `spatial_athletic_contest`
- **Confidence:** `medium`

The contest provisionally satisfies the Spatial Athletic Contest structure even though broader sport recognition remains unsettled. System membership and institutional sport status are separate questions.

### Objections and limitations

- Community governance may not support federation-grade appeals or equipment control.
- One tournament does not establish all VR rhythm competitions.
- Current 2026 announcement is concise; some explicit mechanics rely on historical rules and first-party product material.

### What would change the judgment

- Evidence that tracked bodily input is incidental rather than causally necessary.
- Rules showing uncontrolled or non-comparable scoring across participants.

---

## BC-014 — Zero Latency Sol Raiders free-roam competitive experience

### Classified object

**Primary:** `product`  
**Secondary:** `spatial_athletic_system`, `experience`

The classified object is the Sol Raiders-enabled free-roam product/experience configuration, not a formal league or all location-based VR.

### Evidence

1. **Zero Latency launches the first truly wireless free-roam VR system** — Zero Latency VR. https://invest.zerolatencyvr.com/news-and-events/next-gen-launch-announcement — `official_announcement`, `C3`, temporal status `current`. Limitation: First-party claims establish intended system capabilities, not independent performance validation.
2. **Zero Latency VR FAQ** — Zero Latency VR. https://invest.zerolatencyvr.com/zero-latency-vr-faq — `first_party_technical`, `C3`, temporal status `current`. Limitation: Operational and safety claims are provider statements; venue implementations may differ.

### Performance window and agency

**Window:** From session start through the scored competitive experience.

**Finding:** Players move, aim, coordinate, and make tactical decisions live inside the shared session.

**Agency modes:** `live_performance`

### AS³ reading

| Layer | Observation |
| --- | --- |
| L1 — Performance Agency | Live player movement and tactics. |
| L2 — Interface / Embodied Demand | Free-roam tracked XR and controllers. |
| L3 — Arena | Aligned physical and virtual arena. |
| L4 — Rules | Primarily code-enforced; public rules thin. |
| L5 — Sensing | Constitutive tracking and proximity alerts. |
| L6 — Measurement / Comparability | Public metric and cross-venue controls are insufficient. |
| L7 — Officiation / Outcome | Automated events plus venue monitoring. |
| L8 — Presence / Participation | Up to multiple co-located players share space. |
| L9 — Safety / Accessibility | Boundary alignment and collision systems are central. |
| L10 — Governance / Evidence | Provider documentation dominates; independent governance is limited. |

### Operational Spatial Integration Profile

**Overall:** `supported` — Physical and computational arenas are jointly operational and safety-coupled. Evidence supports a Spatial Athletic System more strongly than a mature Spatial Athletic Contest.

| Function | Status | Significance | Mechanism | Failure effect |
| --- | --- | --- | --- | --- |
| `represent` | `supported` | `constitutive` | The virtual environment represents the shared arena and opponents. | Representation failure destroys shared situational awareness. |
| `enable` | `supported` | `constitutive` | Wireless tracking enables bodily movement as input. | Tracking loss breaks valid participation. |
| `constrain` | `supported` | `constitutive` | Virtual geometry and physical arena boundaries jointly constrain movement. | Boundary divergence creates unfairness or collision risk. |
| `measure` | `partial` | `supportive` | The game records hits and outcomes, but metric transparency is limited. | Opaque scoring defects cannot be independently audited. |
| `officiate` | `partial` | `supportive` | Code resolves game events and proximity systems support safety. | Software or monitoring failure can alter outcome or safety. |

### Candidate invariant reading

| Candidate | Status | Notes |
| --- | --- | --- |
| `performance_agency` | `supported` | Live movement and tactics are necessary. |
| `constraint_integrity` | `partial` | Code constraints exist but public inspection is limited. |
| `comparability` | `unknown` | Cross-venue controls are not sufficiently evidenced. |
| `outcome_openness` | `supported` | The competitive result depends on player performance. |

### Provisional finding

- **Sport/contest axis:** `digital_competition_not_settled_as_sport`
- **Category relation:** `spatial_athletic_system`
- **Confidence:** `medium`

The product is a strong Spatial Athletic System candidate because physical and virtual arenas are constitutively coupled, but published evidence is insufficient to establish a mature governed contest class.

### Objections and limitations

- Provider marketing uses “esports” without federation-grade public rules.
- Venue configuration may alter safety and comparability.
- Evidence is primarily first-party; no independent technical audit is attached.

### What would change the judgment

- Public competition rules, metric definitions, cross-venue calibration controls, and appeals procedures.

---

## BC-015 — World Taekwondo Virtual Taekwondo competition

### Classified object

**Primary:** `contest`  
**Secondary:** `spatial_athletic_contest`, `event`, `organization`

The object is the World Taekwondo-governed Virtual Taekwondo contest configuration. The preselected remote-distributed hypothesis is retained but marked unresolved because the cited championships were co-located.

### Evidence

1. **VTKD Competitive League and Rule Book** — Virtual Taekwondo / Refract Technologies. https://virtualtkd.gg/compete/ — `standard_or_sporting_code`, `C3`, temporal status `current`. Limitation: The rulebook is hosted by the product operator and endorsed by World Taekwondo; remote distributed deployment is not established by this page.
2. **Virtual Taekwondo at the Olympic Esports Series finals** — World Taekwondo. https://www.worldtaekwondo.org/competition/view.html?mcd=W02&nid=140192 — `official_announcement`, `C1`, temporal status `historical`. Limitation: Describes a co-located event and does not validate remote latency or distributed arena equivalence.
3. **First World Taekwondo Virtual Championships** — World Taekwondo. https://m.worldtaekwondo.org/competition/view.html?mcd=N03%2F1000&nid=141655&sc=ne — `official_announcement`, `C1`, temporal status `historical`. Limitation: Championship announcement establishes federation operation; technical comparability details remain limited.

### Performance window and agency

**Window:** From round start until knockout or time expiry.

**Finding:** Competitors execute kicks and body movement live; tracked speed, timing, and tactical choice affect the virtual opponent state.

**Agency modes:** `live_performance`

### AS³ reading

| Layer | Observation |
| --- | --- |
| L1 — Performance Agency | Live tracked kicking performance. |
| L2 — Interface / Embodied Demand | Full-body motion tracking and headset. |
| L3 — Arena | Local physical stations linked to one computational arena; remote relation unresolved. |
| L4 — Rules | Federation-approved rules plus code. |
| L5 — Sensing | Constitutive full-body tracking. |
| L6 — Measurement / Comparability | Common system supports comparison; remote latency and calibration not demonstrated. |
| L7 — Officiation / Outcome | Software, referees, and match operators. |
| L8 — Presence / Participation | Competitors and audience share an event environment; remote competition not evidenced. |
| L9 — Safety / Accessibility | Non-contact format reduces contact risk but introduces headset and motion risks. |
| L10 — Governance / Evidence | Federation governance is stronger than in community VR contests. |

### Operational Spatial Integration Profile

**Overall:** `supported` — The co-located contest is strongly spatial-athletic. The planned test of geographically distributed performance remains unresolved rather than inferred from global availability.

| Function | Status | Significance | Mechanism | Failure effect |
| --- | --- | --- | --- | --- |
| `represent` | `supported` | `constitutive` | Avatars and health state represent opponents and contest state. | Representation or state desynchronization makes the contest invalid. |
| `enable` | `supported` | `constitutive` | Motion tracking enables bodily performance as game input. | Tracking loss prevents valid action. |
| `constrain` | `supported` | `constitutive` | Virtual range, legal attacks, damage logic, and round state constrain performance. | Patch or rule-code divergence changes the contest. |
| `measure` | `supported` | `constitutive` | Tracked movement is converted into damage and health state. | Calibration or sensing error changes outcome. |
| `compare` | `partial` | `supportive` | Common system and rules support comparison; distributed latency equivalence is not demonstrated. | Uncontrolled calibration or network conditions weaken fairness. |
| `officiate` | `supported` | `supportive` | Software, referees, and match operators administer results. | Operator or system failure can require correction or replay. |

### Candidate invariant reading

| Candidate | Status | Notes |
| --- | --- | --- |
| `performance_agency` | `supported` | Live bodily skill is necessary. |
| `constraint_integrity` | `supported` | Rules and system logic are declared. |
| `comparability` | `partial` | Co-located comparison is supported; remote distributed equivalence is unresolved. |
| `outcome_openness` | `supported` | Round results are performance-dependent. |

### Provisional finding

- **Sport/contest axis:** `sport_like_contest`
- **Category relation:** `spatial_athletic_contest`
- **Confidence:** `medium`

Virtual Taekwondo supports the Spatial Athletic Contest class for co-located competition. Sprint 5 does not establish a remote distributed arena because current primary evidence does not demonstrate that configuration.

### Objections and limitations

- Federation endorsement does not prove every technical integrity condition.
- Global participation is not the same as simultaneous remote competition.
- The fixed BC-015 remote hypothesis remains only partially tested; a targeted remote case is required.

### What would change the judgment

- Published remote match rules, latency budgets, calibration procedures, and evidence of competitors in different physical sites sharing one match.

---

## BC-016 — MindMotion GO rehabilitation exercise system

### Classified object

**Primary:** `spatial_support_system`  
**Secondary:** `product`, `experience`

The object is the regulated rehabilitation product and supervised exercise configuration, not stroke rehabilitation as a whole and not a competitive sport.

### Evidence

1. **510(k) K173931 — MindMotion GO** — U.S. Food and Drug Administration. https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm?ID=K173931 — `law_or_regulation`, `C1`, temporal status `current`. Limitation: FDA clearance concerns device equivalence and intended use; it is not proof of superior clinical effectiveness.
2. **NCT07534124 — Virtual Reality-Based Upper Limb Rehabilitation in Chronic Stroke** — ClinicalTrials.gov / U.S. National Library of Medicine. https://clinicaltrials.gov/study/NCT07534124 — `reputable_research`, `C1`, temporal status `current`. Limitation: Registry information includes retrospectively registered completed study details and should be read with the study limitations.
3. **Clinically Meaningful Upper Limb Motor Recovery with MindMotion GO — randomized trial preprint** — medRxiv. https://www.medrxiv.org/content/10.64898/2026.04.27.26351882v1 — `reputable_research`, `C3`, temporal status `current`. Limitation: Preprint; small sample; between-group differences were not statistically significant; not peer reviewed.

### Performance window and agency

**Window:** During each supervised therapeutic exercise and feedback cycle.

**Finding:** The patient must generate goal-directed movement during each exercise; performance agency exists without a competitive opponent.

**Agency modes:** `live_performance`, `assisted_performance`

### AS³ reading

| Layer | Observation |
| --- | --- |
| L1 — Performance Agency | Patient movement is live and causally necessary. |
| L2 — Interface / Embodied Demand | Motion-captured adaptive upper-limb exercise. |
| L3 — Arena | Computer-mediated therapeutic task space. |
| L4 — Rules | Therapeutic protocol, not sport rules. |
| L5 — Sensing | Motion capture is constitutive. |
| L6 — Measurement / Comparability | Requires clinical protocol and validated outcomes. |
| L7 — Officiation / Outcome | No sport officiation; therapist oversight. |
| L8 — Presence / Participation | Patient–therapist relationship is central. |
| L9 — Safety / Accessibility | Clinical suitability, fatigue, and impairment variation govern use. |
| L10 — Governance / Evidence | FDA status and research limitations must remain visible. |

### Operational Spatial Integration Profile

**Overall:** `supported` — The system is strongly embodied and computationally mediated, but its correct class is Spatial Support System because therapeutic purpose and protocol replace contest structure.

| Function | Status | Significance | Mechanism | Failure effect |
| --- | --- | --- | --- | --- |
| `represent` | `supported` | `supportive` | Interactive tasks represent goals and movement feedback. | Misleading representation may impair instruction or motivation. |
| `enable` | `supported` | `constitutive` | Motion capture enables bodily exercise to control the therapeutic environment. | Tracking failure interrupts or misrepresents therapy. |
| `mediate` | `supported` | `constitutive` | The system mediates therapist-designed exercises and patient feedback. | Poor mapping can change the intended therapeutic task. |
| `measure` | `supported` | `supportive` | Movement and standardized clinical outcomes provide evidence of performance and progress. | Invalid measurement can produce unsafe or unsupported conclusions. |

### Candidate invariant reading

| Candidate | Status | Notes |
| --- | --- | --- |
| `performance_agency` | `supported` | Patient action is necessary for exercises. |
| `constraint_integrity` | `partial` | Therapeutic protocol is identifiable but not a contest structure. |
| `comparability` | `partial` | Only under matched clinical design and outcomes. |
| `outcome_openness` | `not_applicable` | No open contest result is claimed. |

### Provisional finding

- **Sport/contest axis:** `training_or_simulation`
- **Category relation:** `spatial_support_system`
- **Confidence:** `high`

This case strongly validates the Spatial Support System sibling class: embodied spatial interaction can be clinically meaningful without being sport or contest.

### Objections and limitations

- Gamification and scores may tempt sport-like labeling.
- FDA clearance must not be converted into an efficacy ranking.
- The 2026 effectiveness report is a non-peer-reviewed preprint with a small sample and non-significant between-group differences.

### What would change the judgment

- A separately governed competitive event using the same technical platform with open outcomes and contest rules.

---

## BC-017 — CYBATHLON Exoskeleton Race

### Classified object

**Primary:** `contest`  
**Secondary:** `athletic_system`, `event`

The object is the CYBATHLON EXO contest, where a pilot and exoskeleton complete physical tasks; individual devices may use different control modes.

### Evidence

1. **Exoskeleton Race** — CYBATHLON / ETH Zurich. https://cybathlon.com/en/event/disciplines/exo — `first_party_technical`, `C1`, temporal status `current`. Limitation: Discipline page summarizes permitted modes; detailed event rules remain controlling.
2. **CYBATHLON 2024** — CYBATHLON / ETH Zurich. https://cybathlon.com/en/events/edition/cybathlon-2024 — `official_announcement`, `C1`, temporal status `historical`. Limitation: Event page establishes competition scope and results, not every device’s internal assistance logic.

### Performance window and agency

**Window:** From task start through completion, including mode changes and device responses.

**Finding:** Pilot skill and decisions matter, but permitted manual, semi-autonomous, and autonomous modes can shift causal control during tasks.

**Agency modes:** `live_performance`, `assisted_performance`, `autonomous_execution`, `agency_handoff`

### AS³ reading

| Layer | Observation |
| --- | --- |
| L1 — Performance Agency | Pilot and device may share control across modes. |
| L2 — Interface / Embodied Demand | Robotic assistive exoskeleton and adaptive bodily performance. |
| L3 — Arena | Physical variable task course. |
| L4 — Rules | Published eligibility and technology rules. |
| L5 — Sensing | Device sensing varies by team. |
| L6 — Measurement / Comparability | Common tasks; heterogeneous assistance complicates attribution. |
| L7 — Officiation / Outcome | Officials record task success and time. |
| L8 — Presence / Participation | Team engineers support preparation; pilot performs during run. |
| L9 — Safety / Accessibility | Safety and disability-specific access are constitutive. |
| L10 — Governance / Evidence | Competition openly permits multiple autonomy modes. |

### Operational Spatial Integration Profile

**Overall:** `partial` — The contest is deeply human–machine mediated, but the arena remains physical. Assistance and agency handoff—not computational Spatiality—are the primary analytical pressures.

| Function | Status | Significance | Mechanism | Failure effect |
| --- | --- | --- | --- | --- |
| `mediate` | `partial` | `supportive` | On-device sensing and control mediate pilot intent and physical movement. | Undeclared or poorly attributed control can obscure who performed the task. |
| `measure` | `supported` | `supportive` | Competition records task completion and time. | Timing or task-state errors affect ranking. |

### Candidate invariant reading

| Candidate | Status | Notes |
| --- | --- | --- |
| `performance_agency` | `partial` | Live pilot agency exists, but causal contribution may shift to automation. |
| `constraint_integrity` | `supported` | Technology permissions and tasks are declared. |
| `comparability` | `partial` | Common tasks coexist with heterogeneous assistance regimes. |
| `outcome_openness` | `supported` | Run outcomes depend on pilot-device execution. |

### Provisional finding

- **Sport/contest axis:** `research_or_engineering_contest`
- **Category relation:** `outside_core_spatial_athletic_class`
- **Confidence:** `high`

The case confirms Assisted Performance Agency but shows that the schema’s summary-level agency modes cannot fully represent when control shifts during a run. Phase-level agency segments are needed before normative attribution.

### Objections and limitations

- Calling assistance either irrelevant or disqualifying would erase the actual pilot–device relation.
- Different teams may implement “autonomous” functions with very different scope.
- Public discipline material does not expose every team’s control architecture or time-varying handoff.

### What would change the judgment

- Task-level logs identifying control mode, pilot input, autonomous action, and failure at each phase.

---

## BC-018 — CYBATHLON Brain-Computer Interface Race

### Classified object

**Primary:** `contest`  
**Secondary:** `computational_contest`, `event`

The object is the BCI Race contest in which a pilot uses measured brain activity to control a computer-based vehicle or game process.

### Evidence

1. **Brain-Computer Interface Race** — CYBATHLON / ETH Zurich. https://cybathlon.com/en/event/disciplines/bci — `first_party_technical`, `C1`, temporal status `current`. Limitation: Discipline page describes permitted brain-signal technologies and tasks; team implementations vary.
2. **CYBATHLON 2024** — CYBATHLON / ETH Zurich. https://cybathlon.com/en/events/edition/cybathlon-2024 — `official_announcement`, `C1`, temporal status `historical`. Limitation: Event page does not resolve philosophical or category questions about embodiment.
3. **Improving motor imagery decoding methods for an EEG-based mobile BCI in CYBATHLON 2024** — neuroTUM research team / arXiv. https://arxiv.org/abs/2511.23384 — `reputable_research`, `C2`, temporal status `current`. Limitation: Preprint; one team implementation; reported competition performance was lower than offline performance.

### Performance window and agency

**Window:** During each command opportunity and continuous-control phase of the race.

**Finding:** The pilot intentionally generates brain-activity patterns during the race; decoded commands materially influence the vehicle.

**Agency modes:** `live_performance`, `assisted_performance`

### AS³ reading

| Layer | Observation |
| --- | --- |
| L1 — Performance Agency | Live intentional brain-signal generation. |
| L2 — Interface / Embodied Demand | Physiological sensing and cognitive demand. |
| L3 — Arena | Animated computational race environment. |
| L4 — Rules | Competition rules plus software tasks. |
| L5 — Sensing | Real-time brain activity measurement and classification. |
| L6 — Measurement / Comparability | Participant-specific calibration and stress complicate comparison. |
| L7 — Officiation / Outcome | Software and officials record task success and time. |
| L8 — Presence / Participation | Pilot interacts through neural signals; spectators are non-constitutive. |
| L9 — Safety / Accessibility | Designed for severe motor impairment; fatigue and signal burden matter. |
| L10 — Governance / Evidence | Open discipline rules; team algorithms vary. |

### Operational Spatial Integration Profile

**Overall:** `supported` — Operational spatial integration is constitutive, but embodiment is category-disputed because performance is physiological and cognitive rather than conventionally motor.

| Function | Status | Significance | Mechanism | Failure effect |
| --- | --- | --- | --- | --- |
| `represent` | `supported` | `constitutive` | The animated scenario represents the race vehicle and task state. | Representation failure prevents meaningful control. |
| `enable` | `supported` | `constitutive` | Brain-signal decoding enables the pilot to act in the computational environment. | Signal or classifier failure removes the performance channel. |
| `mediate` | `supported` | `constitutive` | The BCI pipeline mediates intention into control commands. | Decoder bias or lag changes agency attribution and performance. |
| `constrain` | `supported` | `constitutive` | The animated scenario and task prompts constrain permissible commands and timing. | Software divergence changes the task. |
| `measure` | `supported` | `constitutive` | The system measures signals, command success, progress, and time. | Measurement error can invalidate results. |
| `compare` | `partial` | `supportive` | Common tasks support comparison, but participant-specific calibration and signal variability remain substantial. | Uncontrolled calibration reduces fairness. |
| `officiate` | `supported` | `supportive` | Software and officials determine completion and ranking. | State or timing errors alter results. |

### Candidate invariant reading

| Candidate | Status | Notes |
| --- | --- | --- |
| `performance_agency` | `supported` | Intentional live neural activity is causally necessary. |
| `constraint_integrity` | `supported` | Tasks and technology permissions are declared. |
| `comparability` | `partial` | Calibration and signal variability remain material. |
| `outcome_openness` | `supported` | Results depend on pilot and decoder performance. |

### Provisional finding

- **Sport/contest axis:** `research_or_engineering_contest`
- **Category relation:** `unresolved`
- **Confidence:** `medium`

The case cannot be reduced to an ordinary computational contest because the human biological signal is the live performance channel; nor can v0.2 yet assert that this is sufficient Embodied Performance for Spatial Athletic System membership.

### Objections and limitations

- Visible movement is not the only possible bodily channel.
- Treating any biological signal as sufficient embodiment would make the class too broad.
- Embodiment remains a conceptual boundary; team-specific decoding performance varies.

### What would change the judgment

- A defensible category rule distinguishing intentional physiological performance from incidental biosignal measurement.

---

## BC-019 — DARPA Subterranean Challenge Systems Competition

### Classified object

**Primary:** `contest`  
**Secondary:** `event`, `organization`

The object is the physical Systems Competition in which human teams design and supervise autonomous robot teams searching a physical course.

### Evidence

1. **DARPA Subterranean Challenge program** — Defense Advanced Research Projects Agency. https://www.darpa.mil/research/programs/darpa-subterranean-challenge — `official_announcement`, `C1`, temporal status `historical`. Limitation: Program page is archival because the challenge is complete.
2. **Subterranean Challenge Final Event** — Defense Advanced Research Projects Agency. https://www.darpa.mil/research/challenges/subterranean — `official_announcement`, `C1`, temporal status `historical`. Limitation: Final event overview summarizes systems and scoring; full rules contain greater detail.
3. **Teams CoSTAR and BARCS Take Top Spots in DARPA SubT Urban Circuit** — Defense Advanced Research Projects Agency. https://www.darpa.mil/news/2020/costar-barcs-subterranean-challenge — `official_announcement`, `C1`, temporal status `historical`. Limitation: One circuit report; control arrangements may differ across Systems and Virtual tracks.

### Performance window and agency

**Window:** Across pre-run system design and configuration, command-post supervision, and autonomous course execution.

**Finding:** Human design and supervisory decisions matter, but robots perform substantial autonomous navigation and search during the timed run.

**Agency modes:** `design_engineering`, `autonomous_execution`, `agency_handoff`

### AS³ reading

| Layer | Observation |
| --- | --- |
| L1 — Performance Agency | Design, supervision, autonomous execution, and handoff coexist. |
| L2 — Interface / Embodied Demand | Remote command and autonomous robots; no live human bodily performance in the course. |
| L3 — Arena | Physical subterranean course plus computational maps. |
| L4 — Rules | Challenge rules and hidden course conditions. |
| L5 — Sensing | Robot perception, localization, and networking are constitutive. |
| L6 — Measurement / Comparability | Artifact accuracy, report limits, and time. |
| L7 — Officiation / Outcome | Automated and official report validation. |
| L8 — Presence / Participation | Human supervisors act from command posts. |
| L9 — Safety / Accessibility | Robots enter hazardous spaces to reduce human risk. |
| L10 — Governance / Evidence | DARPA rules and archival results are inspectable. |

### Operational Spatial Integration Profile

**Overall:** `supported` — The competition has rich operational spatial integration, but not human athletic embodiment. It is an engineering contest outside the Spatial Athletic core.

| Function | Status | Significance | Mechanism | Failure effect |
| --- | --- | --- | --- | --- |
| `represent` | `supported` | `constitutive` | Robot-generated maps and spatially referenced artifact locations represent the course. | Mapping failure prevents navigation and valid reports. |
| `enable` | `supported` | `constitutive` | Autonomy, networking, and perception enable robot operation in hazardous space. | Loss of autonomy or communications reduces task completion. |
| `mediate` | `supported` | `constitutive` | Command systems mediate human supervision and robot action. | Unclear control handoff obscures attribution and can immobilize the team. |
| `constrain` | `supported` | `constitutive` | Physical terrain, course rules, report limits, and hidden artifacts constrain performance. | Course or rule inconsistency affects fairness. |
| `measure` | `supported` | `constitutive` | Spatial reports are evaluated for type, location tolerance, and time. | Localization or scoring error changes points. |
| `compare` | `supported` | `supportive` | Shared scoring and course conditions compare heterogeneous systems. | Unequal course conditions or report validation would compromise results. |
| `officiate` | `supported` | `supportive` | DARPA validates reports and rankings. | Validation errors alter standings. |

### Candidate invariant reading

| Candidate | Status | Notes |
| --- | --- | --- |
| `performance_agency` | `partial` | Human contribution and live supervision exist, but autonomous execution is decisive. |
| `constraint_integrity` | `supported` | Challenge rules and scoring are explicit. |
| `comparability` | `supported` | Common metrics compare heterogeneous systems. |
| `outcome_openness` | `supported` | Results emerge through system performance. |

### Provisional finding

- **Sport/contest axis:** `research_or_engineering_contest`
- **Category relation:** `outside_core_spatial_athletic_class`
- **Confidence:** `high`

Operational spatial integration can be very strong without Spatial Athletic System membership. The case also confirms that agency handoff requires phase-level representation rather than one summary list.

### Objections and limitations

- Calling the whole team “the performer” can conceal autonomous execution.
- The Systems and Virtual tracks have different control conditions.
- This record focuses on the Systems Competition and does not generalize every SubT track.

### What would change the judgment

- Phase logs showing human commands, autonomous decisions, and causal contribution throughout each run.

---

## BC-020 — Formula E race with FANBOOST

### Classified object

**Primary:** `contest`  
**Secondary:** `event`, `athletic_system`

The object is a historical Formula E race under the FANBOOST rule, not current Formula E and not fan voting in sport generally.

### Evidence

1. **FANBOOST is open — vote to influence Formula E** — FIA Formula E. https://www.fiaformulae.com/en/news/2022 — `official_announcement`, `C1`, temporal status `historical`. Limitation: The mechanism was active in the Gen2 era and is now historical.
2. **Farewell FANBOOST** — FIA Formula E. https://www.fiaformulae.com/en/news/11558 — `official_announcement`, `C1`, temporal status `discontinued`. Limitation: Confirms FANBOOST ended from Season 9; it does not quantify competitive effect.

### Performance window and agency

**Window:** During the race, including the driver’s decision whether and when to deploy the awarded boost.

**Finding:** Drivers retain live vehicle-control agency; fan votes allocate an optional power resource but do not execute the driving action.

**Agency modes:** `live_performance`, `assisted_performance`

### AS³ reading

| Layer | Observation |
| --- | --- |
| L1 — Performance Agency | Driver remains the live performer; spectators influence resources. |
| L2 — Interface / Embodied Demand | Vehicle control and racing load. |
| L3 — Arena | Physical circuit; voting is external to arena space. |
| L4 — Rules | League rule allocates boost to selected drivers. |
| L5 — Sensing | Votes and vehicle systems track eligibility and deployment. |
| L6 — Measurement / Comparability | Declared unequal assistance is part of the rule, not ambient equality. |
| L7 — Officiation / Outcome | Officials and car systems administer deployment. |
| L8 — Presence / Participation | Spectators become participatory rule/resource actors. |
| L9 — Safety / Accessibility | Motorsport safety remains separate from fan voting. |
| L10 — Governance / Evidence | Mechanism and discontinuation are officially documented. |

### Operational Spatial Integration Profile

**Overall:** `absent` — FANBOOST is a digital spectator intervention into resource allocation, not Operational Spatial Integration. L8 participation becomes constitutive without turning spectators into performance agents.

No computational Spatial Function was evidenced for the classified object.

### Candidate invariant reading

| Candidate | Status | Notes |
| --- | --- | --- |
| `performance_agency` | `supported` | Driver skill remains causally necessary; spectators do not drive. |
| `constraint_integrity` | `supported` | The intervention was an explicit championship rule. |
| `comparability` | `partial` | The rule intentionally creates unequal assistance based on votes. |
| `outcome_openness` | `supported` | Drivers still determine deployment and race execution. |

### Provisional finding

- **Sport/contest axis:** `sport`
- **Category relation:** `outside_core_spatial_athletic_class`
- **Confidence:** `high`

Spectator influence can become constitutive to resource allocation without becoming Performance Agency, officiation, or Spatiality. The ontology needs a participatory rule/resource actor relation.

### Objections and limitations

- Popularity-based assistance raises fairness questions even when rules are transparent.
- Spectator influence is not equivalent to spectator performance.
- FANBOOST is discontinued and analyzed as a historical rule mechanism.

### What would change the judgment

- A format in which spectators continuously execute skill-dependent actions that directly control the competitive object.

---

## Stratum Rule

A case that destabilizes v0.2 remains in the record. Unknown is not absence. No AS³ layer is averaged, and no record authorizes a score, certification, or ASR conformance claim.
