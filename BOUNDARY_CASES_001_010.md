# Boundary Cases BC-001 – BC-010

**Asset:** AltisSports  
**Sprint:** Sprint 2 — Boundary Case Validation  
**Version:** 0.1  
**Status:** Provisional Stratified Sample — Open to Correction  
**Method:** `BOUNDARY_CASE_METHOD.md`  
**Machine export:** `boundary-cases-001-010.json`  
**Access date for cited sources:** 2026-07-24

## Sample Design

This is not a popularity sample of “the top ten sports.” It is an antagonistic stratum designed to stress Human Agency, embodiment, mediation, adaptation, remote control, digital competition, hybrid physical–computational systems, simulation, and automation.

| ID | Activity | Primary stress test |
| --- | --- | --- |
| BC-001 | Association Football | Conventional sport reference |
| BC-002 | Chess | Mind sport / embodiment threshold |
| BC-003 | Formula One | Vehicle-mediated human performance |
| BC-004 | Para Athletics | Agency and adaptation without one normative body |
| BC-005 | Drone Racing | Remote skill and intermediate operational space |
| BC-006 | Tactical Shooter Esport | Digital skill contest with limited embodiment |
| BC-007 | VR Boxing | Embodied motion inside a virtual arena |
| BC-008 | Virtual Cycling with Physical Resistance | Body–machine–platform–space entanglement |
| BC-009 | Flight Simulation Competition | Skillful simulation near the sport boundary |
| BC-010 | Autonomous Robot Competition | Competitive outcome without live human performance |

---

## BC-001 — Association Football

### Classified object

**Primary:** activity (association football as governed athletic contest)  
**Secondary:** athletic system (match under IFAB Laws); optional officiating layer (VAR / technology) as system adjunct

### Sources

1. International Football Association Board (IFAB), *Laws of the Game* — canonical rules authority. [https://theifab.com/](https://theifab.com/) — C1, federation/sporting code.
2. FIFA / IFAB Laws publications confirming universal application of the Laws across levels, with limited organizational modifications. — C1/C2.

### AS³ reading

| Layer | Observation |
| --- | --- |
| L1 | Human players materially determine outcomes through skill, tactics, and physical performance. |
| L2 | Embodied interface is the body; equipment mediation (boots, ball) is conventional, not computational. |
| L3 | Arena is primarily physical: pitch dimensions, lines, and goal geometry constrain play. |
| L4 | Rules reside in IFAB Laws; enforcement is primarily human refereeing. |
| L5 | Sensing is mostly human perception; optional video systems support review. |
| L6 | Goals, time, and disciplinary metrics are standardized; pitch variation is bounded by Laws. |
| L7 | Officiation is human-centered; technology may assist but does not replace the contest structure. |
| L8 | Spectatorship is integral culturally, not constitutive of the athletic result. |
| L9 | Contact, fatigue, collision, and medical protocols are central. |
| L10 | IFAB/FIFA governance and Laws versioning are mature and inspectable. |

### Invariants

- **Human Agency:** supported.
- **Constraint Integrity:** supported.
- **Comparability:** supported within competition classes; not absolute across all pitches and conditions.
- **Outcome Openness:** supported.
- **Consequence:** supported (result, ranking, elimination, physical cost).

### Spatial integration

**Absent to partial.** Computational systems (for example VAR) may assist officiation in some competitions, but the category thesis does not treat optional video review as making association football a Spatial Athletic System by default. Space is operationally physical.

### Objections

- Some elite setups use extensive tracking and data systems; critics may call these “spatial.” Under Altis method, representational or advisory analytics without rule-bearing operational space do not suffice.
- Institutional sport recognition is overwhelming; that does not settle the spatial axis.

### Provisional finding

- **Sport axis:** sport.
- **Spatial Sport axis:** not_spatial_sport (baseline reference).
- **Claim class:** C4 for spatial axis; C1/C2 for sport recognition structure.

### What would change the judgment

Documented competitions in which computationally mediated geometry or shared computational state jointly constrains or officiates performance as part of the unified contest—not merely overlays graphics or post-hoc analytics.

**Confidence:** high.

---

## BC-002 — Chess

### Classified object

**Primary:** activity (competitive chess)  
**Secondary:** organization (FIDE governance); product variants (online platforms) must not collapse into the activity

### Sources

1. FIDE, About FIDE — states recognition by the IOC as a Global Sporting Organization (1999) and describes FIDE as governing body of the sport of chess. [https://www.fide.com/about-fide/](https://www.fide.com/about-fide/) — C1/C3.
2. FIDE Museum / recognition materials describing IOC recognition of FIDE. — C1/C3.

### AS³ reading

| Layer | Observation |
| --- | --- |
| L1 | Outcome depends on human cognitive performance (and, at elite level, preparation, endurance, time management). |
| L2 | Embodied motor expression is minimal relative to football; pieces are moved by hand or digitally. Embodiment is not the performance channel. |
| L3 | Arena is a discrete board state (physical or digital). Geometry is rule-bearing but not athletic locomotion space. |
| L4 | Rules are highly formalized (FIDE Laws of Chess). |
| L5 | State is fully observable in standard play; digital platforms add logging and anti-cheat sensing. |
| L6 | Ratings and pairing systems enable strong comparability. |
| L7 | Arbiter / platform enforcement; digital adjudication common online. |
| L8 | Presence can be over-the-board or remote. |
| L9 | Accessibility differs sharply from locomotion sports; fatigue is largely cognitive/time-pressure. |
| L10 | FIDE governance is mature; IOC recognition is institutional fact about federation status, not an Altis definition of sport. |

### Invariants

- **Human Agency:** supported (cognitive / decision agency).
- **Constraint Integrity:** supported.
- **Comparability:** supported.
- **Outcome Openness:** supported (except engineered cheating cases).
- **Consequence:** supported competitively; bodily exertion is not required for consequence.

### Spatial integration

**Absent** for classical chess as athletic Spatial Sport. Digital boards are computational representations of a discrete state machine. That is not the operational integration of human athletic performance with computationally mediated space targeted by the category thesis.

### Objections

- “Chess is a sport because the IOC recognizes FIDE.” Institutional recognition ≠ Altis invariant satisfaction for Spatial Sport; it does pressure any definition that requires gross motor embodiment as necessary for *sport as such*.
- Online chess with anti-cheat computer vision might look “spatial”; that remains integrity sensing of a non-locomotor contest.

### Provisional finding

- **Sport axis:** sport (institutionally) / sport_like_contest under agency-without-gross-embodiment reading — **disputed only if sport is defined as necessarily bodily**. Under First Principles candidates as written, chess supports agency, constraints, comparability, openness, and consequence without locomotion.
- **Spatial Sport axis:** not_spatial_sport.
- **Claim class:** C4/C5.

### What would change the judgment

A revised Altis definition that makes gross motor embodiment necessary for *all* sport (which would then conflict with IOC/FIDE recognition facts and require explicit scope: “sport” vs “athletic sport”). Or a chess variant where continuous tracked bodily movement in computational space constitutes the performance channel.

**Confidence:** high on spatial axis; medium-high on sport-axis wording because “sport” language is institutionally loaded.

---

## BC-003 — Formula One

### Classified object

**Primary:** athletic system / activity (FIA Formula One Championship competition)  
**Secondary:** product (car as engineered interface); organization (FIA)

### Sources

1. FIA Formula One Sporting Regulations — driver must drive alone and unaided (e.g. B1.8.1 / equivalent article wording in current issues). [https://www.fia.com/](https://www.fia.com/) — C1.
2. Formula 1 / FIA technical and sporting materials describing regulated car, circuit, and energy systems. — C1/C3.

### AS³ reading

| Layer | Observation |
| --- | --- |
| L1 | Driver skill materially affects outcome; team and car performance also matter. Agency is shared across human–machine–organization. |
| L2 | Interface is heavily mediated: cockpit, controls, safety systems, energy deployment modes. |
| L3 | Arena is physical circuit with rule-bearing zones (track limits, sectors, marshal signals). Telemetry is extensive but the contest space remains physical. |
| L4 | Sporting and technical regulations are dense and code/sensor-assisted in enforcement. |
| L5 | High sensing density (timing, ECU, marshalling lights). |
| L6 | Comparability depends on regulated equipment classes and session conditions. |
| L7 | Stewards, Race Director, and technical checks officiate. |
| L8 | Global spectatorship and team radio participation structures. |
| L9 | Extreme safety governance; G-forces, fire, impact protocols. |
| L10 | FIA governance is explicit and versioned. |

### Invariants

- **Human Agency:** supported, but not exclusive; engineering and strategy co-determine results.
- **Constraint Integrity:** supported.
- **Comparability:** partial across seasons/regulations; supported within a regulated championship framework.
- **Outcome Openness:** supported.
- **Consequence:** supported (ranking, risk, physical load).

### Spatial integration

**Absent to partial** as Spatial Sport. Computation is deep inside the car and timing systems, yet the athletic arena is not principally a computationally constituted performance space. F1 stresses **mediated embodiment**, not VR/MR unification.

### Objections

- If “computational mediation” is read too broadly, every ECU-equipped sport becomes Spatial Sport — collapsing the category.
- Conversely, denying F1 as sport because of machine mediation would be historically and institutionally absurd.

### Provisional finding

- **Sport axis:** sport.
- **Spatial Sport axis:** not_spatial_sport under current thesis; **important mediation boundary case**.
- **Claim class:** C4.

### What would change the judgment

A championship format in which a shared computational arena (not merely telemetry) jointly constrains wheel-to-wheel performance as a unified physical–computational contest.

**Confidence:** high.

---

## BC-004 — Para Athletics

### Classified object

**Primary:** activity / athletic system (World Para Athletics competition)  
**Secondary:** governance (classification system)

### Sources

1. World Para Athletics / Paralympic classification overview — eligibility and sport classes minimize impairment impact on outcomes so skill/fitness decide results. [https://www.paralympic.org/athletics/classification](https://www.paralympic.org/athletics/classification) — C1.
2. IPC Athlete Classification Code / International Standard for Athlete Evaluation framework. — C1.

### AS³ reading

| Layer | Observation |
| --- | --- |
| L1 | Human athletic performance remains decisive within class. |
| L2 | Interfaces include prostheses, racing chairs, throwing frames, guide systems — assistive and adaptive, not “less athletic.” |
| L3 | Physical arena (track/field) with class-specific equipment constraints. |
| L4 | Rules + classification rules jointly constitute fair contest structure. |
| L5 | Classification evaluation and competition measurement. |
| L6 | Comparability is explicitly class-relative; this is a feature, not a failure. |
| L7 | Standard athletics officiation plus classification governance. |
| L8 | Parallel to Olympic athletics spectatorship structures. |
| L9 | Accessibility and body variation are constitutive governance concerns. |
| L10 | IPC / World Para Athletics governance is formal. |

### Invariants

- All five candidates are supported **within classification**.
- The case falsifies any unspoken assumption that sport requires one normative body plan.

### Spatial integration

**Absent** by default (physical sport). Classification is an integrity/comparability technology, not computational arena unification.

### Objections

- Some may treat prostheses as “technology mediation” equivalent to esports peripherals. Altis reading: adaptive equipment preserves embodied athletic agency; it does not relocate the contest into computational space.

### Provisional finding

- **Sport axis:** sport.
- **Spatial Sport axis:** not_spatial_sport.
- **Theoretical importance:** forces L2/L9 to treat body variation as first-class, not edge-case.
- **Claim class:** C4.

### What would change the judgment

Para events whose decisive constraints are computationally constituted shared arenas (possible future hybrids), evaluated separately from classification itself.

**Confidence:** high.

---

## BC-005 — Drone Racing

### Classified object

**Primary:** activity / athletic system (FAI F9U drone racing)  
**Secondary:** product (aircraft + FPV system)

### Sources

1. FAI Drone Racing World Cup documents and rules page. [https://www.fai.org/droneracingworldcup-documents-rules](https://www.fai.org/droneracingworldcup-documents-rules) — C1.
2. FAI Sporting Code Volume F9 Drone Sports (F9U class rules). — C1.

### AS³ reading

| Layer | Observation |
| --- | --- |
| L1 | Pilot skill (control, line choice, risk management) is decisive during the race. |
| L2 | Interface is remote: radio control + first-person video. Human body is not co-located with the racing craft. |
| L3 | Physical course gates/obstacles form the arena; FPV video is a sensing/display channel into that arena. |
| L4 | FAI class rules and event procedures. |
| L5 | Onboard video, timing systems, fail-safes. |
| L6 | Comparability depends on class equipment limits and course setup. |
| L7 | Event officiation under FAI sporting structures. |
| L8 | Spectator views often mediated by pilot video feeds. |
| L9 | Safety zones, flyaway risk, frequency management. |
| L10 | FAI / CIAM governance. |

### Invariants

- **Human Agency:** supported (live remote performance agency).
- **Constraint Integrity:** supported in sanctioned events.
- **Comparability:** partial across events/courses.
- **Outcome Openness:** supported.
- **Consequence:** supported.

### Spatial integration

**Partial / disputed.** There is an operational coupling between human control and a physical course mediated by computational sensing/display (FPV). This is closer to Spatial Sport than chess or desktop shooters, yet the decisive arena remains physical gates in airspace rather than a computationally constituted rule-bearing volume. It is a **remote embodied control** case, not automatic Spatial Sport membership.

### Objections

- “FPV is virtual, therefore Spatial Sport.” Display mediation ≠ computational arena as rule-bearing space.
- “Remote control is not sport.” Conflicts with FAI sporting-code treatment of the class.

### Provisional finding

- **Sport axis:** sport / sport_like_contest under air-sports federation governance.
- **Spatial Sport axis:** partial_spatial_integration — unresolved for full Spatial Athletic System membership pending sharper operational-space criteria.
- **Claim class:** C4/C5.

### What would change the judgment

Clear criteria distinguishing (a) remote control of physical craft through video links from (b) contests whose primary constraints are computational geometry. Or events where digital overlays become rule-bearing in the same contest state.

**Confidence:** medium.

---

## BC-006 — Tactical Shooter Esport

### Classified object

**Primary:** event/activity cluster (competitive tactical shooters such as Counter-Strike Majors / ESL Pro Tour)  
**Secondary:** product (game title); organization (publisher + tournament operators)

### Sources

1. Valve Counter-Strike Major Supplemental Rulebook (format, seeding, structure). [https://github.com/ValveSoftware/counter-strike_rules_and_regs](https://github.com/ValveSoftware/counter-strike_rules_and_regs) — C1.
2. ESL Pro Tour Counter-Strike rulebook updates (competition governance). — C1.
3. IOC public positioning historically treating some esports as sporting activity while excluding FPS content from Olympic esports contexts on values grounds — institutional policy, not Altis invariant test. — C3.

### AS³ reading

| Layer | Observation |
| --- | --- |
| L1 | High human skill agency (aim, utility usage, team tactics, economy). |
| L2 | Interface is primarily hands/eyes via mouse-keyboard or controller; gross athletic locomotion is not the performance channel. |
| L3 | Arena is computational map space with rule-bearing zones, vision blockers, bombsites. |
| L4 | Game code + tournament rulebooks. |
| L5 | Engine state is authoritative; anti-cheat sensing is critical integrity layer. |
| L6 | Comparability requires patch version, settings, hardware constraints, latency controls. |
| L7 | In-engine rules plus admin/referee structures. |
| L8 | Strong spectator systems. |
| L9 | Ergonomics, addiction/health, eligibility; not collision sport safety. |
| L10 | Publisher + organizer governance; fragmented global authority vs traditional IFs. |

### Invariants

- Contest invariants are largely supported for elite competition.
- Embodiment invariant—if required for sport—*fails* or is minimal.
- Spatial integration of a kind is present (computational arena is the contest), but **athletic embodiment** claimed by Spatial *Athletic* Sport is weak.

### Spatial integration

**Computational arena: supported.**  
**Spatial Athletic Sport: not automatic.** The thesis centers operational integration of *human performance* with computationally mediated space. Here space is computational and decisive, but the performance channel is not athletic embodiment in the AS³ L2 sense used for Spatial Athletic systems. This case forces a split between:

1. computational contest space, and  
2. spatial athletic integration.

### Objections

- Esports federations and markets call it sport.
- Olympic movement has been selectively receptive and selectively exclusionary.
- If Altis requires embodiment for Spatial Sport, shooters may be “computational contests” without being Spatial Athletic Sport.

### Provisional finding

- **Sport axis:** digital_competition_not_settled_as_sport (institutionally contested) / sport_like_contest under skill-contest reading.
- **Spatial Sport axis:** computational_arena_without_athletic_embodiment_claim.
- **Claim class:** C4/C5.

### What would change the judgment

Ratified Altis definitions that either (a) accept non-embodied computational contests as Spatial Sport, or (b) explicitly reserve Spatial Sport for embodied/performance-interface cases and place tactical shooters in a sibling class.

**Confidence:** medium.

---

## BC-007 — VR Boxing

### Classified object

**Primary:** product-centered hybrid (example family: VR boxing titles such as *Creed: Rise to Glory*)  
**Must not** silently classify “boxing” the sport.

### Sources

1. Survios / Creed product materials describing motion-controller boxing, Phantom Melee Technology, stamina/fatigue simulation, PvP. [https://survios.com/studio/game/creed-rise-to-glory/](https://survios.com/studio/game/creed-rise-to-glory/) and [https://creedrisetoglory.com/](https://creedrisetoglory.com/) — C3 (provider claims).
2. Steam store product description for tracking and PvP features. — C3.

### AS³ reading

| Layer | Observation |
| --- | --- |
| L1 | Player motor skill and timing affect in-game outcomes. |
| L2 | Embodied upper-body interface via headset + controllers; legs often weakly represented. |
| L3 | Virtual ring/arena constrains interaction; physical play space must exist for safe movement. |
| L4 | Rules largely in game code; not boxing’s unified sporting code. |
| L5 | Tracking accuracy/latency critical; vendor claims exceed independent verification here. |
| L6 | Cross-device comparability typically weak or unspecified. |
| L7 | Software determines hits/knockdowns; limited formal athletic officiation. |
| L8 | Immersion is central to the product value proposition. |
| L9 | Cybersickness, collision with real furniture, exertion without full contact risk. |
| L10 | Publisher-controlled; weak public evidence governance for athletic claims. |

### Invariants

- Outcome openness: supported in PvP modes.
- Constraint integrity: supported as game rules; not as boxing sport governance.
- Comparability: weak across hardware.
- Consequence: variable (fitness, ranking, entertainment).
- Human agency: supported.

### Spatial integration

**Partial to supported** at product level: computational arena + embodied tracking jointly affect performance. Immersion is present but is not the decisive criterion. Whether this is Spatial *Sport* depends on contest governance, comparability, and whether the classified object is sport, training, or game.

### Objections

- Marketing as sport/fitness does not create sport.
- Physical boxing federations would reject equivalence.
- Conversely, dismissing all VR combat as “not spatial” ignores operational tracking–arena coupling.

### Provisional finding

- **Sport axis:** hybrid — often game / fitness / training; sport only if a governed contest layer is evidenced.
- **Spatial Sport axis:** partial_spatial_integration as spatial athletic *system candidate*; not automatically Spatial Sport.
- **Claim class:** C4 (analysis), C3 (capabilities).

### What would change the judgment

Independent measurement of tracking fidelity; published comparability protocol across headsets; federation- or league-governed VR boxing rules with inspectable officiation and anti-cheat/integrity model.

**Confidence:** medium (object entanglement is the main uncertainty).

---

## BC-008 — Virtual Cycling with Physical Resistance

### Classified object

**Primary:** athletic system (UCI Cycling Esports World Championships-type events on platforms such as Zwift historically)  
**Secondary:** product/platform (game world + smart trainer)

### Sources

1. Zwift / UCI partnership materials for inaugural 2020 UCI Cycling Esports World Championships; standardized Tacx NEO 2T trainers for fairness. [https://news.zwift.com/](https://news.zwift.com/) — C1/C3.
2. UCI announcement of Wahoo as official smart trainer partner for 2023 UCI Cycling Esports World Championships. [https://www.uci.org/](https://www.uci.org/) — C1.
3. Event technical guides requiring trainer as power source, HR monitoring, equipment neutralization. — C1.

### AS³ reading

| Layer | Observation |
| --- | --- |
| L1 | Human physiological and tactical performance (power, pacing) decisive. |
| L2 | Bike + smart trainer resistance is an embodied machine interface. |
| L3 | Computational course geometry (gradients, drafting rules, arcs) constrains performance jointly with physical power output. |
| L4 | UCI/event rules + platform physics/code. |
| L5 | Power, cadence, HR sensing; anti-cheat and data integrity are central. |
| L6 | Hardware standardization is used precisely because comparability is fragile. |
| L7 | Platform + event officials. |
| L8 | Remote distributed participation with broadcast spectatorship. |
| L9 | Physiological load is real; crash risk differs from road cycling. |
| L10 | UCI involvement provides sporting governance signal uncommon in pure games. |

### Invariants

All five candidates are supported in championship configurations with standardized trainers.

### Spatial integration

**Supported** as a leading Spatial Athletic System candidate: physical performance and computationally mediated course state are structurally interdependent. This is not “3D scenery on a trainer.” Grade, drafting, and virtual position change the mechanical demand and race outcome.

### Objections

- Platform physics opacity and historical cheating controversies challenge integrity.
- Not identical to road cycling; transfer claims need evidence.
- Trainer standardization shows comparability is engineered, not automatic.

### Provisional finding

- **Sport axis:** sport_like_contest with international federation championship recognition (UCI esports worlds) — strong sport-axis support relative to BC-007/BC-009.
- **Spatial Sport axis:** spatial_athletic_system (provisional).
- **Claim class:** C4/C5.

### What would change the judgment

Evidence that virtual gradients/drafting are cosmetic only (would weaken spatial claim), or unresolved systemic incomparability despite hardware controls (would weaken sport integrity claim).

**Confidence:** medium-high.

---

## BC-009 — Flight Simulation Competition

### Classified object

**Primary:** hybrid unresolved — skill competition inside flight-sim products/networks (e.g. Microsoft Flight Simulator racing contests; IVAO/VATSIM community operations are often non-race simulation)  
**Must separate** training simulation, online network flying, and skill contests.

### Sources

1. Microsoft Flight Simulator Reno Air Racing contest official rules — skill-based contest within MSFS racing content. [https://www.flightsimulator.com/reno-air-racing-series/](https://www.flightsimulator.com/reno-air-racing-series/) — C1.
2. IVAO / VATSIM network descriptions — online simulated aviation environments oriented to realistic operations and ATC, not primarily athletic championship definition. — C1/C3.

### AS³ reading

| Layer | Observation |
| --- | --- |
| L1 | Human piloting skill can determine race/contest outcomes. |
| L2 | Interface is typically HOTAS/controller/keyboard — low athletic embodiment; some setups add motion rigs. |
| L3 | Computational airspace/course is the arena. |
| L4 | Product rules + contest rules; aviation networks emphasize procedural realism. |
| L5 | Simulator state authoritative. |
| L6 | Hardware/software variance can be large. |
| L7 | Contest admins or automatic scoring. |
| L8 | Strong community participation. |
| L9 | Low physical risk; high cognitive load. |
| L10 | Publisher or community governance; rarely classical IF sport governance for “flight sim as sport.” |

### Invariants

- Skill contest configurations can satisfy agency, constraints, openness, consequence.
- Embodiment is thin.
- Comparability often weak.

### Spatial integration

Computational arena is real and operational for the contest. Athletic embodiment is typically weak. Closest to BC-006 structurally, with stronger simulation semantics and weaker global championship sport framing than UCI cycling esports.

### Objections

- Professional pilot training use cases are not sport.
- Air-racing sims look like motorsport esports; classification should follow contest structure, not aircraft imagery.

### Provisional finding

- **Sport axis:** training_or_simulation by default; sport_like_contest only for evidenced skill competitions.
- **Spatial Sport axis:** computational_arena_without_athletic_embodiment_claim in typical desktop contests; unresolved if motion-rig embodied variants are specified.
- **Claim class:** C4.

### What would change the judgment

A federation-governed championship with explicit athletic-performance claims, published comparability protocol, and embodied interface requirements.

**Confidence:** medium (object heterogeneity).

---

## BC-010 — Autonomous Robot Competition

### Classified object

**Primary:** research_or_engineering_contest (e.g. RoboCup Humanoid League match play)  
**Secondary:** organization (RoboCup); robots as performing agents during play

### Sources

1. RoboCup Humanoid League rules — robots must act autonomously during competition; no teleoperation / remote brain; human handlers restricted. [https://humanoid.robocup.org/](https://humanoid.robocup.org/) rules PDFs — C1.

### AS³ reading

| Layer | Observation |
| --- | --- |
| L1 | During the match, performing agents are robots. Human contribution is primarily prior design, training data, and engineering—not live performance agency. |
| L2 | No human embodied interface in play (handlers are service exceptions). |
| L3 | Physical field is the arena; perception stacks are computational. |
| L4 | Laws of the game adapted for robots + technical constraints. |
| L5 | Onboard sensing is the contest’s perception channel. |
| L6 | Comparability across teams is research-heterogeneous (except standard platform leagues). |
| L7 | Human referees + game controller systems. |
| L8 | Research community spectatorship. |
| L9 | Robot and human safety procedures. |
| L10 | RoboCup technical committees. |

### Invariants

- **Human Agency (live performance):** absent / fails as athletic contest invariant.
- **Outcome Openness:** supported among robot policies/hardware.
- **Constraint Integrity:** supported.
- **Consequence:** supported within research competition.
- Pre-contest human engineering agency is real but is **not** the same property as in-match athletic performance agency.

### Spatial integration

Operational space exists (field + onboard computation), but without live human athletic performance the Spatial *Sport* thesis does not attach. This is a decisive negative control for Human Agency.

### Objections

- “Humans built the robots, so humans compete.” That collapses design competitions into athletic contests.
- Teleoperated robot sports would be a different case (closer to BC-005).

### Provisional finding

- **Sport axis:** research_or_engineering_contest / not_sport as athletic contest.
- **Spatial Sport axis:** not_spatial_sport.
- **Claim class:** C4/C5.

### What would change the judgment

Rule sets restoring live human teleoperation as the decisive in-match skill channel (reclassify under remote-agency cases), or an explicit Altis subclass for autonomous athletic spectacles that does not claim sport invariants.

**Confidence:** high.

---

## Cross-Case Snapshot

| Case | Sport axis (provisional) | Spatial axis (provisional) | Main lesson |
| --- | --- | --- | --- |
| BC-001 Football | sport | not spatial | Reference physical athletic system |
| BC-002 Chess | sport / mind sport | not spatial | Embodiment not required for all sport |
| BC-003 F1 | sport | not spatial (mediation ≠ spatial category) | Vehicle mediation preserved agency |
| BC-004 Para Athletics | sport | not spatial | No single normative body |
| BC-005 Drone Racing | sport-like / air sport | partial | Remote agency + physical course |
| BC-006 Tactical Shooter | contested / sport-like | computational ≠ athletic spatial | Split classes needed |
| BC-007 VR Boxing | hybrid product | partial spatial athletic candidate | Object lock mandatory |
| BC-008 Virtual Cycling | strong sport-like | spatial athletic system candidate | Best positive spatial case in sample |
| BC-009 Flight Sim Contest | simulation / conditional contest | computational, weak embodiment | Function before imagery |
| BC-010 Autonomous Robots | engineering contest | not spatial sport | Live human performance agency required |

Detailed invariant extraction continues in `INVARIANCE_FINDINGS_V0.1.md`.
