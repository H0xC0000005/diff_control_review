# Step 3: source access, independent reference and evidence limits

**Current source work, 2026-10-15:** P-H is selected and CP-D1 is closed.
The resumed point-case recheck supports an isolated recovery profile;
continuous mass weighting/additive overlap is explicitly a proposed
adaptation. The exact conditional node and its analytical checks await
CP-D2 confirmation. S3-M1/S3-M2 remain closed; Step 3 remains open.

[References actually rechecked and adaptation boundaries](vsl_ph_source_and_adaptation_audit.md)

[Current formed model and law-confirmation gate](../../reporting/research_readiness/vsl_ph_recovery_work_findings_and_gate.md)

[Viewed references and first C-P interface/source findings](vsl_cp_source_and_interface_audit.md)

**Latest reading:** the through-traffic philosophy response rechecks the
mechanism evidence and separates point geometry, continuing-service coupling
and the completion domain. The user subsequently selected C-P with choke-line
completion, closing S3-M2's representation/objective choice. S3-M1 stays
closed. G3's nominal terminal restriction is narrowly reopened; exact
replacement equations and the full Step 3 freeze remain pending. No new
source was read for this decision closure.

[Accepted direction and closure scope](../../reporting/research_readiness/vsl_step3_coupled_point_decision.md)

[Viewed-paper list and limits for the latest response](#through-traffic-feedback-and-completion-recheck-2026-10-14)

Date: 2026-10-14. This audit distinguishes reviewed documentation from paper
evidence. The user selected SUMO for reference qualification. A runnable
evaluator is not admitted and no traffic run is reported. H1/T1 is the closed
predictor. The user accepted S-P first and S-L transfer second; S3-M1 is
closed, while detailed reference correspondence still needs qualification.

## Papers actually viewed in this continuation

| Reference | Material inspected | What is supported and what remains absent |
|---|---|---|
| Nagalur Subraveti, Knoop and van Arem, *First order multi-lane traffic flow model: an incentive based macroscopic model to represent lane change dynamics*, DOI 10.1080/21680566.2019.1700846 | Existing primary final PDF, pages 3–5 and 21–23 of the 24-page archive: printed 1758–1760 and 1776–1778. Reused the accepted methods/budget audit. | Continuous lane densities, longitudinal/lateral transfers and data-based lane-density tests make it a serious reference candidate. The inspected paper does not establish the present common-advice response or an information/gradient-usefulness certificate. Calibration of its diagrams does not calibrate H1's opportunity scale or terminal work factors. |

The publisher/article year discrepancy remains explicit: the article header
says 2020 while the copyright/DOI and repository record use 2019. No year was
invented to resolve it.

[Primary archived paper](../../archive/full_text/FB0030.pdf)

[Publisher DOI](https://doi.org/10.1080/21680566.2019.1700846)

[Accepted equation and limitation audit](../n2_source_studies/FB0030.md)

The approved H1/T1 mathematical source, S13 closure/sufficiency study and
existing baseline screen were also read as project records, not newly viewed
published papers. Earlier Carey/Jin/Yperman source reading remains in the
linked list; no broad new literature search was opened.

[Earlier viewed-paper list and T1 source limits](vsl_k2_terminal_source_and_interface_audit.md)

[Strong aggregate/history/capacity-drop and optimizer rivals](vsl_successor_baselines_and_evidence_gaps.md)

## Official SUMO documentation actually inspected

| Primary documentation | Inspected subject | Direct support and review consequence |
|---|---|---|
| [Variable Speed Signs](https://sumo.dlr.de/docs/Simulation/Variable_Speed_Signs.html) | Lane selection and time/speed sign definition. | Common lane speed advice has a documented intervention. This does not establish its equality to H1's realized preparation speed. |
| [Change Vehicle State](https://sumo.dlr.de/docs/TraCI/Change_Vehicle_State.html) | Speed, maximum speed, acceleration and speed-mode descriptions. | Actual motion remains constrained by native safety/acceleration behavior. Forcing trajectories would require a different intervention and cannot be used to manufacture predictor agreement. |
| [Vehicle/Type/Route definitions](https://sumo.dlr.de/docs/Definition_of_Vehicles,_Vehicle_Types,_and_Routes.html) | Individual vehicles, speed factors and lane-change models/parameters. | Native lane interactions can provide distinct behavioral physics. Their parameters are not H1's fixed opportunity/work factors, and physical initialization needs its own mapping. |
| [VehicleInsertion](https://sumo.dlr.de/docs/Simulation/VehicleInsertion.html) | Feasible insertion, delayed insertion and intended versus actual departure. | A requested initial cohort is not automatically already on the road. Insertion changes must not hide source waiting or replace the approved decision-time preparation. |
| [SaveAndLoad](https://sumo.dlr.de/docs/Simulation/SaveAndLoad.html) | State/RNG handling and known issues. | The page lists internal lane-change/car-follow state limitations. A saved state is not, by itself, proof of equivalent causal history; a later deterministic replay or state qualification is needed. |
| [TripInfo](https://sumo.dlr.de/docs/Simulation/Output/TripInfo.html) | Departure, delay, arrival, duration, waiting and unfinished output. | Complete decision-time cohort time must be reconstructed for all traffic. Completed-trip duration or low-speed waiting alone does not equal the required complete TST. |

An attempted Simulation/Lane-Change_Models page was inaccessible. The primary
vehicle/type/route definition page supplied the lane-change-model material.
Other returned source-code/paper search leads were not substantively inspected
and are not added to the viewed-paper list.

## Follow-up capability check: early merging and prescribed intention

The user expressed a preference for SUMO and asked whether early merging and
a prescribed intention, such as a constant proportion attempting to merge,
can be represented natively or through an external Python script. This is
a documentary capability check; no request policy or evaluator was admitted.

**Direct answer.** Both routes are available. SUMO's normal lane-drop geometry
can make the ending lane have no outgoing connection. Drivers then need to
change lanes to continue their route. Strategic lane-changing parameters
control how early they anticipate that need. In particular, `lcStrategic`
controls eagerness; zero permits changing at the lane end, while minus one
disables strategic changing. Eagerness is not a literal constant merge
probability or a guaranteed completed fraction.

Python/TraCI can instead specify which vehicles receive an early adjacent-lane
request and when. The documented `changeLane` duration is an attempt window,
and `setLaneChangeMode` controls the relationship between external requests,
native motivations and safety. Mode 512 is documented as disabling autonomous
changes while retaining collision avoidance and safety-gap enforcement. It
demonstrates the separation's feasibility; it is not selected here, since
the treatment of remaining mandatory requests and cooperation needs review.
Default TraCI requests are urgent and may induce cooperative speed changes,
so issuing a request is itself part of the disclosed behavioral specification.

A fixed selected share of drivers asking to merge is therefore technically
feasible. Their completed share can still depend on actual gaps, braking and
motion. The definition of a share of drivers versus a request frequency per
metre or per second must be explicit. H1's opportunity scale is tied to
physical progress, so a per-timestep sampling rule is not automatically an
equivalent mapping. No stochastic rule, seed or fraction was selected.

The useful reference boundary is that a script may generate requests while
SUMO's own traffic interactions determine success and delay. Computing
completed transfers with H1's receiving law and imposing those outcomes would
reproduce the predictor's disputed mechanism rather than independently check
it. A prescribed request does not guarantee eventual clearance.

| Additional or re-inspected official source | Capability inspected | Evidence limit |
|---|---|---|
| [Motorways](https://sumo.dlr.de/docs/Simulation/Motorways.html) | Ending-lane connectivity, native lane-number reduction and lane-change permissions. | Establishes a lane-drop modeling route, not equality to T1's point priority or blocked-lateral terminal reach. |
| [Vehicle/type/route definitions: lane-changing models](https://sumo.dlr.de/docs/Definition_of_Vehicles,_Vehicle_Types,_and_Routes.html#lane-changing-models) | `lcStrategic`, lookahead, cooperation and gap-acceptance parameters. | Parameters affect native behavior; they do not implement a constant completed proportion or calibrate H1's work factors. |
| [Change Vehicle State: change lane and lane-change mode](https://sumo.dlr.de/docs/TraCI/Change_Vehicle_State.html) | Request duration, competing motivations, safety modes and urgent cooperative adaptation. | Supports an external request generator with native safety; exact persistence, terminal handoff and behavioral mapping remain unchosen. |
| [Lanechange output](https://sumo.dlr.de/docs/Simulation/Output/Lanechange.html) | Completed-change time, position, reason and target-lane actual/required gaps. | A completed-event log does not by itself record every failed or pending request; a later protocol must record prescribed requests separately. |

Access to the Python vehicle API page failed in this follow-up. No unverified
retrieval helper is proposed. Search results for developer instructions and
the lane-change-model paper were not substantively read as papers; the
viewed-paper list is unchanged. No installation or local SUMO probe was made.

This check strengthens R-M's capability case. Exact region, speed-response,
terminal service, population, history and complete-time mappings remain open.
It neither changes H1/T1 nor establishes a beneficial slowdown in SUMO.

## What is a capability, and what would be an admitted reference

The documentation supports a possible microscopic speed-advice reference,
with native vehicle interaction and outcome/state records. It does not
qualify the present three-to-two preparation, blocked-lateral terminal
section, strict priority, continuous initial population or complete
observation mapping. No SUMO binary or local installation was probed.

A native continuous spatial lane-aware model avoids the initial
continuous-to-vehicle realization issue and gives inspectable lane-density
physics. It still needs a supported common-advice intervention and its own
terminal/handoff mapping. The selected source's lane-density calibration
does not supply those qualifications, and its native budgets/branches
cannot be repaired silently.

For example, both reference candidates could receive the same total initial
traffic with different ending-lane occupancy. A microscopic reference asks
how actual gaps, acceleration and mandatory maneuvering turn common advice
into departures. A continuous spatial reference asks how local lane
density, propagation and lateral service do so. Those are different
independent behavioral meanings. Neither can be treated as the approved
H1 law simply evaluated by another engine.

## The three evidence boundaries

**History.** The new exact collision is proved in the H1 loading construction,
including all declared lane-blind pre-decision fields. It is not observed in
either candidate reference. A field or reference observer with additional
lane/lateral channels may recover ending mass; that inference belongs to A.

**Parameters.** The new conditional action split exists for sufficiently
large late-work factors. No source here independently admits that range.
For factors one through two, the history-matched reference subfamily has a
common fastest action; the wider Step 2 parameter family is not classified.
Parameter provenance must be settled without using held-out optimum
or sensitivity signs as calibration targets.

**Usefulness.** Full-objective analytical sensitivity is defined internally,
with reference branches and event obligations. No AD implementation or
independent perturbation was checked. A faithfully reimplemented H1 server
would be an internal correctness reference.

## SUMO selected: bridge qualification and terminal evidence

The user approved R-M/SUMO after the capability check and directed completing
the chain. The review now specifies how physical preparations and observation
records produce H1 predictions, advice, independent SUMO interactions and
complete-time outcomes. It reached a genuinely new terminal interpretation
after the settled evaluator selection. The user subsequently accepted the
staged ladder to close that strategy choice; mappings remain to be qualified.

| Official source inspected or re-inspected in this pass | Direct source support | Adaptation or unresolved fitness |
|---|---|---|
| [PlainXML: connections and right-of-way](https://sumo.dlr.de/docs/Networks/PlainXML.html) | Explicit incoming/outgoing lane connections; two incoming lanes may join one target; priority and zipper rules; connection geometry/speed controls. The page cautions against some ordinary motorway double connections. | A yielding boundary can represent the restricted terminal, but it is a junction model. The same page describes the default priority as left-lane priority in Special Cases and right-most-lane priority in Multiple Connections. Therefore inspect/configure explicit priority in the later approved build rather than infer a default. |
| [Intersections](https://sumo.dlr.de/docs/Simulation/Intersections.html) | Native approach braking, right-of-way, internal links, connection turning limits and blocking. Disabling internal links changes modeled motion; runtime suppression can also give wrong route lengths. | These are scientifically consequential aspects of a boundary reference, not invisible implementation conveniences. Include native connection travel in time accounting; internal-link/geometry choices remain dependent on the terminal decision. |
| [Motorways](https://sumo.dlr.de/docs/Simulation/Motorways.html) | A usual lane reduction makes the ending lane have no onward connection, requiring lane changes; zipper is an alternative. | Native gap-seeking before the lane end does not enforce T1's exact cutoff. A natural lane-ending reference needs a declared predictor/reference correspondence. |
| [VehicleSpeed](https://sumo.dlr.de/docs/Simulation/VehicleSpeed.html) | Lane-changing and cooperative speed adaptation; missing onward connection causes deceleration/stopping; zipper ordering differs from priority. | Native service is independent of H1's work factor. A normal lane end and a yielding connection are different compulsory interactions. |
| [Variable Speed Signs](https://sumo.dlr.de/docs/Simulation/Variable_Speed_Signs.html) | Common permitted speed on a declared lane list from the decision time. | Ideal preparation speed remains a predictor approximation. Do not force realized trajectories to equal it. |
| [VehicleInsertion](https://sumo.dlr.de/docs/Simulation/VehicleInsertion.html) | Safe insertion may be delayed or discarded under configured limits; forced insertion changes the procedure. | Require the full evaluated cohort already present at the decision, no backlog/later arrival, and record failures. A reference-first exact count projection does not prove feasible native preparation. |
| [SaveAndLoad](https://sumo.dlr.de/docs/Simulation/SaveAndLoad.html) | RNG is not saved by default; known issues include unsaved lane-change and some car-following internal state. | Causal prefix replay is the first comparison rule. Snapshot acceleration requires a later equivalence check, not an assumed exact state transfer. |
| [FCDOutput](https://sumo.dlr.de/docs/Simulation/Output/FCDOutput.html) | Per-step position/speed; front-bumper coordinate convention; native lane identity when enabled. | Provides evaluator state/accounting. A's lane-blind observer is a predeclared projection, not access to all raw coordinates or lane labels. Crossing-time resolution needs a later error budget. |
| [TripInfo](https://sumo.dlr.de/docs/Simulation/Output/TripInfo.html) | Actual insertion/arrival times; trip duration; unfinished trips omitted by default. | Complete decision-to-completion time must include the entire fixed cohort; trip duration and low-speed waiting are cross-checks, not the objective. |
| [Why Vehicles Are Teleporting](https://sumo.dlr.de/docs/Simulation/Why_Vehicles_are_teleporting.html) | Teleporting can remove vehicles stuck on a wrong lane, yielding, or jammed; a negative time-to-teleport disables gridlock teleportation. | Disable task-removing behavior and audit all removals/collisions. A nonclearing case is an admission failure, not an optimistically truncated complete-time result. |

VehicleSpeed and teleportation material was substantively inspected through
official search results; the other pages were also opened or searched within.
The additional sources are documentation, not papers. No new published paper
was substantively viewed in this pass. Existing S13/H1/T1 and baseline studies
were read as accepted project records. No software was installed or probed.

## Present scientific disposition

**R-M/SUMO is selected; R-C is unselected and deferred as the first reference.**
S3-M1 is closed by user acceptance of the staged ladder. S-P is the selected
first external condition, preserving the restricted terminal and native
yielding boundary. S-L is the accepted subsequent transfer condition, with
additional native terminal opportunities explicitly declared under G3/G4.
Native S-P connection physics/geometry and S-L correspondence still need
qualification; neither runnable reference is admitted.

[Accepted ladder and decision closure](../../reporting/research_readiness/vsl_step3_validation_ladder_decision.md)

This belongs to S3-Q4/VQ4/G3, with G4 evidence and G2 initial/observation
dependencies. It does not reopen H1's equations, select a spatial primary
model, or authorize construction. Continuous mass remains continuous in H1;
integer reference counts are exact supplied inputs, not rounded outputs.

[Executed SUMO bridge and terminal meaning gate](../../reporting/research_readiness/vsl_step3_sumo_bridge_and_terminal_gate.md)

[Plain findings, comparison and expanded reference gate](../../reporting/research_readiness/vsl_step3_findings_and_gate.md)

[Draft protocol and outcome interpretation](../../synthesis/research_readiness/vsl_step3_first_verification_protocol_draft.md)

## Resumed Step 3 source qualification, 2026-10-14

The user explicitly directed closing S3-M1 with the accepted model → S-P →
S-L ladder and resuming Step 3. Reused the accepted H1/T1 and S13 findings,
their paper references and the existing strongest-rival screen. **No new
published paper was substantively viewed in this resumed pass.** The following
is the reference list of documentation/source actually inspected, not an
archive of downloaded papers. Search-result leads not substantively read
remain excluded from the viewed-paper inventory.

| Viewed primary reference | Direct support inspected | Review deduction or limit |
|---|---|---|
| [Road Capacity](https://sumo.dlr.de/docs/Simulation/RoadCapacity.html), Computing Headways and Further headway effects | Ideal stationary Krauss spacing and headways; realised traffic need not achieve minimum equal-speed spacing. | Original substitution relates this ideal curve to H1's triangular critical density/capacity. It does not identify native transient wave speed, realised advice or merging work. |
| [Intersections](https://sumo.dlr.de/docs/Simulation/Intersections.html), Internal links and approach/turning/blocking sections | Right-of-way is retained without junction-interior motion. Network generation and runtime removal have different length consequences. Native minor approach braking and finite connection motion matter. | Point-versus-finite S-P representation is Type 2 S3-M2; native priority does not enforce T1's zero continuing queue. E-only approach diagnostics must distinguish nonconflict delay. |
| [Distances](https://sumo.dlr.de/docs/Simulation/Distances.html), Length-Geometry-mismatch | Native behaviour uses lane driving distance; displayed geometry can differ, including after internal-link omission. | Record effective preparation/terminal lengths and completion sections from generated lanes. A drawing alone cannot verify the fixed time/space budget. |
| [Change Vehicle State](https://sumo.dlr.de/docs/TraCI/Change_Vehicle_State.html), lane-change requests/mode and vehicle speed | External requests, their durations and native safety/competing behaviours; common permitted speed must remain distinct from forced actual speed. | Scripted intention can remain independent of completed service; request urgency/cooperation must be declared, not fitted through a fixed successful proportion. |
| [PlainXML](https://sumo.dlr.de/docs/Networks/PlainXML.html), lane permissions and converging connections | Source/target lateral permissions, permitted vehicle classes and explicit connection/priority configuration. | Ordinary passenger cohort is the relevant permission case; bypass classes cannot serve as a shortcut. Conflicting descriptions of default same-edge priority remain unresolved by documentation alone. |
| [Vehicle/type/route definitions](https://sumo.dlr.de/docs/Definition_of_Vehicles,_Vehicle_Types,_and_Routes.html), car-following and lane-changing models | Driver-model/parameter provenance, anticipation and cooperation. | Parameters describe behaviour, not a direct literal mapping to H1's opportunity or forced-work constants. No numerical settings are adopted here. |
| [MSLaneChanger.cpp, public main branch](https://raw.githubusercontent.com/eclipse-sumo/sumo/main/src/microsim/MSLaneChanger.cpp) | `mayChange`, active `change`, `continueChange`, `applyTraCICommands` and the external-influence path. Permissions precede normal new active changes; continued maneuvers and some external-command paths have distinct control flow. | Do not extrapolate the ordinary permission check to every command/lifecycle path. Expire requests and audit completed events at handoff in a later pinned-release conformance test. This inspection is not a bug claim or installed-version verification. |
| [MSAbstractLaneChangeModel.cpp, public main branch](https://raw.githubusercontent.com/eclipse-sumo/sumo/main/src/microsim/lcmodels/MSAbstractLaneChangeModel.cpp) | `checkTraCICommands` feeds external influence into own-state handling. | Reinforces the request-lifecycle obligation; source branch is moving and must be pinned/rechecked for execution. |
| [VehicleSpeed](https://sumo.dlr.de/docs/Simulation/VehicleSpeed.html) | Native lane/junction limitations and cooperative motion. | Actual speed can differ from advice; do not force trajectories to manufacture the predictor's response. |
| [SaveAndLoad](https://sumo.dlr.de/docs/Simulation/SaveAndLoad.html), Known Issues | Previously inspected unsaved lane-change/car-following state limitations were rechecked. | Causal prefix replay remains the admitted comparison approach; snapshot equivalence is not assumed. |

The headway correspondence is a conditional positive interpretation. It
does not provide the missing traffic qualification of the large-work action
split. The accepted small-work/common-fastest result, initial-history limits,
one-scalar sufficiency and direct-search rivalry remain in the protocol.

[Stationary correspondence and work/receiving identifiability mathematics](../../synthesis/research_readiness/vsl_step3_stationary_headway_correspondence.pdf)

**Current disposition:** source/evidence review and protocol assembly are
delivered at VSL-S3-G1. S3-M1 remains closed; S3-M2 is open, with J-P point
boundary provisionally recommended and J-F finite native junction viable.
Neither representation or runnable evaluator is admitted. The full Step 3
freeze remains pending. No source was edited, no dependency was installed,
and no local SUMO binary, network or traffic case was executed.

[Main traffic findings and expanded physical-reference choice](../../reporting/research_readiness/vsl_step3_reference_qualification_and_final_gate.md)

## Through-traffic feedback and completion recheck, 2026-10-14

The user asked whether slow compulsory insertion must affect continuing
traffic, and proposed coupled point service or a downstream interaction
reach. This is a bounded philosophy/evidence response, not a newly opened
model-construction sprint. Reused the accepted S12/H1/T1 audits; the paper
references actually viewed in this response are listed below. Accessed
abstracts or selected sections only as stated; no full-paper qualification
or numerical traffic evidence is inferred.

| Viewed paper reference | Material inspected | Direct support and limit |
|---|---|---|
| [Laval and Daganzo (2006), *Lane-Changing in Traffic Streams*, DOI 10.1016/j.trb.2005.04.003](https://its.berkeley.edu/publications/lane-changing-traffic-streams) | Institutional author/publication abstract rechecked, previously S12-S1. | Particle/void mechanism links lane changes with reduced discharge and moving-bottleneck capacity. No full equations or common-VSL closure newly inspected/adopted. |
| [Leclercq, Knoop, Marczak and Hoogendoorn (2016), *Capacity drops at merges: New analytical investigations*, DOI 10.1016/j.trc.2015.06.025](https://repository.tudelft.nl/record/uuid%3Aeb7471c0-8b30-4ee4-a7ce-d748bf2f7c1e) | Repository manuscript printed pp2–4: abstract, introduction and start of assumptions, reached through its full-text link. S12-S5 previously used the institutional record. | Slow insertion/bounded acceleration and wave/void interactions support the mechanism family. Native domain is a one-lane freeway/on-ramp merge with particular congestion assumptions; no direct permanent-lane-drop mapping, numerical parameter or gradient is adopted. |
| [Jin, Gan and Lebacque (2013 preprint), *A kinematic wave theory of capacity drop*, arXiv:1310.2660](https://arxiv.org/pdf/1310.2660) | Abstract and selected §2, especially boundary-flux formulation and the explicit phenomenological limitation, printed pp4–7. | A point boundary coupled to first-order propagation can produce capacity-drop waves. Its magnitude is exogenous and flux discontinuous; it does not explain slow insertion or supply a gradient-ready component. Kept as a serious aggregate/point precedent, not the chosen law. |
| [Bertini and Leal (2005), *Empirical Study of Traffic Features at a Freeway Lane Drop*, DOI 10.1061/(ASCE)0733-947X(2005)131:6(397)](https://www.researchgate.net/publication/228650849_Empirical_Study_of_Traffic_Features_at_a_Freeway_Lane_Drop) | Publisher search abstract/metadata; direct publisher open failed. Author-uploaded manuscript abstract/introduction text inspected; no figure extraction or field-data reanalysis. | Observed reduced discharge and upstream congestion at lane drops establish relevance. They do not isolate slow entry as the unique cause or calibrate the current finite cohort. The author-uploaded article is primary paper content, not a secondary summary. |

[Inspected Leclercq manuscript link](https://repository.tudelft.nl/file/File_c424c1b3-7374-436b-a6a7-abdf69063aa6)

Official [VehicleSpeed](https://sumo.dlr.de/docs/Simulation/VehicleSpeed.html)
following/acceleration/intersection sections and
[Intersections](https://sumo.dlr.de/docs/Simulation/Intersections.html#internal-links)
were rechecked. Native following and right-of-way are distinct from junction-
interior representation. Their documented capability does not pass a
particular network's receiving/clearance or impulse response. No local
binary, network build or traffic probe was executed.

The response's completion counterexample is original causal reasoning:
a follower may cross the line before catching a slow entering vehicle and
brake later. Hence detector completion and physical removal are different,
and point-completion time need not equal recovery-inclusive time. No sampled
trajectory, fitted closure or numerical size of omitted delay is claimed.

The frozen H1/T1 source explicitly gives A immediate departure while only
E has an eligible queue. Its work factor cannot create A delay under the
accepted domain. A narrow G3 terminal-service reassessment is proposed;
G4 is implicated if the measurement extends downstream. Old certificates
remain restricted to their unchanged member. Through-traffic impact alone
does not establish richer-information necessity or an interior optimum.

[Current plain response, shared example and revised proposals](../../reporting/research_readiness/vsl_step3_merge_feedback_and_completion_response.md)

[Reused S12 mechanism evidence and aggregate rivals](../s12_advice_merge_service_source_audit.md)
