# Can the elementary model give useful speed guidance in an independent traffic model?

**Current decision:** C-P coupled point qualification with choke-line
completion is selected, closing the revised S3-M2 choice gate. Exact
terminal-service qualification and full Step 3 freeze remain pending.
The earlier geometry comparison and unselected proposal below are history.

[Accepted coupled point direction and closure scope](vsl_step3_coupled_point_decision.md)

**Latest discussion, 2026-10-14:** the user identified continuing-traffic
slowdown and its upstream/downstream consequences as a causal requirement.
The J-P/J-F geometry framing and its point-boundary recommendation below
are now historical. They do not specify that coupling. S3-M2 is revised
to coupled point service versus a downstream recovery representation, with
the objective domain explicit. Step 3 freeze readiness is withdrawn pending
this qualification; no approved model equation was changed.

[Current philosophy response and revised proposal](vsl_step3_merge_feedback_and_completion_response.md)

The accepted ladder is now the fixed basis of Step 3: verify the elementary
model, test its advice on SUMO's restricted task S-P, then test the same
advice on the more natural lane-ending condition S-L. The resumed review
has assembled the information, gradient, reference and comparison protocol.
It has reached the original **VSL-S3-G1** with one remaining physical
representation choice inside S-P. **Step 3 is at its review gate, not closed.**
No traffic simulation or numerical gradient check was performed.

The central traffic question remains whether a modest slowdown gives drivers
enough additional usable adjacent-lane space to finish more merging upstream,
and whether the saved compulsory-merge waiting outweighs the added travel
time. Our predictor answers this with homogeneous lane densities and a
compact terminal queue. SUMO must answer through its own gaps, braking and
right-of-way. Agreement would support useful guidance; disagreement would
identify the elementary model's limits.

The new positive finding is a physical interpretation of the predictor's
speed-dependent headroom. The new unresolved finding concerns the compulsory
merge itself: SUMO can treat the priority conflict as a point or retain motion
through a finite junction. That choice changes what the measured delay means.

[Accepted ladder and S3-M1 closure](vsl_step3_validation_ladder_decision.md)

[Consolidated evidence protocol](../../synthesis/research_readiness/vsl_step3_first_verification_protocol_draft.md)

## What the resumed review establishes

**The headroom law has a conditional microscopic interpretation.** At a lower
uniform speed, vehicles can maintain their desired following time with less
physical separation. A crowded continuing lane can therefore have more room
per metre for additional vehicles even though its vehicles move more slowly.
SUMO documents a stationary minimum-headway calculation for homogeneous
Krauss vehicles. Our algebra shows that its ideal capacity and density curves
have the same shape as the triangular-diagram expressions used in H1.
This is a source-to-model deduction, not a SUMO experiment. It helps explain
the direction of the preparation mechanism; it does not establish transient
receiving, realised merging, or equality between permitted and actual speed.

[Stationary headway source](https://sumo.dlr.de/docs/Simulation/RoadCapacity.html)

[Derivation and parameter limits](../../synthesis/research_readiness/vsl_step3_stationary_headway_correspondence.pdf)

**Independent merging service is feasible without copying the predictor.**
An external preparation script can express the wish to move from E into A;
it must leave successful merging and resulting delays to native interactions.
In S-P, remaining E traffic then stays in its own terminal lane and yields to
A at the compulsory boundary. In S-L, remaining drivers can also seek gaps
along the terminal approach. Their native incentives differ, so the preparation
request contract must be made explicit rather than assumed identical.
The script is fixed behaviour, not another optimised actuator. H1's
opportunity scale is an effective model parameter, not automatically a request
frequency or a SUMO setting.

The public source inspection supports lane permissions in ordinary active
lane-change decisions, but also exposes separate handling of ongoing changes
and external commands. Consequently, a road prohibition alone is not an
adequate conformance argument for every request path. The later implementation
must expire preparation requests at the handoff, handle changes that straddle
it, and audit completed events. Current source inspection qualifies a route
to implementation; it does not certify an installed release or a runnable road.

[Official interfaces and inspected source paths](../../extraction/research_readiness/vsl_step3_reference_and_evidence_audit.md#resumed-step-3-source-qualification-2026-10-14)

**A native yielding boundary can add delay for reasons other than competing
traffic.** Visibility-based approach braking and connection geometry need to
be distinguished from the waiting caused by a busy adjacent stream. An E-only
development traversal is therefore a necessary diagnostic. Any such delay
still counts in full TST; it cannot be subtracted from the policy objective
merely to make the reference resemble H1. A is allowed to incur native delay
too: continuing priority does not impose the predictor's zero-A-queue theorem.

[Native approach and junction behaviour](https://sumo.dlr.de/docs/Simulation/Intersections.html)

## Direct answers to the four Step 3 questions

| Question | Core finding and conclusion | Evidence boundary |
|---|---|---|
| **S3-Q1: what information is needed?** | In the accepted model, a complete lane-blind history can leave ending mass unidentified. One initial ending scalar repairs that ambiguity and reproduces the explicit lane-state predictor. A+E is the strongest compact matched peer; G has no additional information advantage. | Exact within the disclosed H1 construction. SUMO needs its own observed-history/inference evidence before claiming the same ambiguity. |
| **S3-Q2: does it change the speed decision?** | It can, but only conditionally. The analytical family admits separated preferred actions at sufficiently large late-work factors; its small-work range instead shares the fastest advice. Ending-state ambiguity alone does not establish control-information value. | No independent traffic evidence admits the positive factor range. No interior optimum or positive advantage is required. |
| **S3-Q3: what gradient must be checked?** | The derivative must follow the entire journey: preparation, moving arrival times, compulsory waiting and last-vehicle clearance. A derivative that freezes those times can miss the actual TST effect. Analytical, numerical-difference and AD evidence remain distinct. | Analytical references exist. No AD, finite-difference traffic calculation or numerical convergence check has run. |
| **S3-Q4: what would make the guidance useful?** | Its feasible advice changes must improve independently measured full-cohort time in admitted S-P cases. Frozen-advice S-L success then adds transfer evidence. Strong scalar search and lawful aggregate inference remain real rivals. | The protocol is assembled; S-P's point-versus-finite boundary is still unselected, and neither reference has passed native admission. |

The stationary headway correspondence strengthens parameter interpretation;
it does not resolve the positive-action regime. In particular, the earlier
dimensionless analytical example is not a calibrated freeway configuration.
The preparation factors, compulsory-work factor and boundary receiving
remain effective parameters requiring development evidence or explicit
analytical status. A single mixed discharge trace need not separate receiving
capacity from compulsory work.

## The remaining choice: what does crossing the compulsory boundary mean?

Imagine six drivers left in E after preparation. None may change lanes along
the S-P terminal. At its end they must wait for A and enter the shared outgoing
lane. The question is whether admission across that conflict completes the
task immediately, or whether they then drive through a finite joining
connection whose travel and occupancy are also part of completion.

**Problem statement, S3-M2.** Should the first restricted-task reference
retain a point priority boundary, or resolve a finite native junction?

**Assumed model-chain function.** T1 already provides a finite physical
approach for travel, storage and waiting. Its compulsory server sits at the
downstream point. S-P needs independent native service at that boundary;
component 7 must count all decision-to-completion time under the selected
physical interpretation.

**Core gap.** S3-M1 settled where lateral opportunities are allowed, not
whether the priority node adds a finite traversed region. Source inspection
shows that SUMO supports both representations. This changes storage,
service and the completion clock, so it cannot be inferred through an
undocumented network-conversion option.

### J-P: a native point priority boundary

Keep the finite terminal approach and its microscopic driving and queueing.
Represent the E/A conflict as a point: E must obtain native right-of-way
before joining the outgoing lane, with no separately simulated junction
interior. This is available through network generation without internal
junction links; ordinary right-of-way remains native. It does **not** switch
SUMO to its mesoscopic mode or prescribe H1's fluid service.

In the six-driver example, all travel and waiting up to the boundary counts.
Crossing it completes the interaction; there is no additional connector stock
or connector-driving time. Finite vehicle length and native following still
affect service upstream and downstream.

- **Pros:** preserves the accepted point-service abstraction and finite
  upstream holding with the smallest additional task assumptions. It isolates
  the preparation-versus-boundary-waiting mechanism while retaining independent
  microscopic approach, gap and service behaviour.
- **Cons:** omits finite junction-interior motion and blocking. It is a
  restricted synthetic benchmark, not a resolved physical merge manoeuvre.
  Native approach delays remain, and driving lengths must be audited.
- **Dependency and consequence:** generated driving distances, rather than
  the visual node outline, must match the declared preparation/terminal
  budget. Runtime deletion of links from an already generated finite-junction
  network is not an equivalent shortcut. Failure to obtain the intended
  priority or distances reopens this mapping before any outcome is admitted.

### J-F: a finite native priority junction

Retain a finite joining connection with native motion, safety and possible
blocking inside it. E still yields to A, and ordinary terminal lateral changes
remain prohibited. Give the connector a declared place within the fixed
terminal/road length budget; distinguish its admission location from the
common section where completion is measured.

In the same example, obtaining a gap is only the beginning of completion.
Each E vehicle must also clear the joining connection. Its traversal can
constrain following vehicles and affect A's service. Those effects count
even if they differ from the predictor's point-server approximation.

- **Pros:** keeps SUMO's usual finite-junction representation and can test
  advice against a physically resolved compulsory joining manoeuvre. It
  exposes a class of service/travel coupling absent from the point model.
- **Cons:** introduces connector travel, occupancy and possible geometry
  effects in the first external condition. The result includes approximation
  error from a finite node as well as from H1/T1's service law, making the
  original mechanism harder to isolate. It requires more physical dimensions.
- **Dependency and consequence:** the connector must not silently add road
  length or shift the task's endpoint. If a defensible layout changes the
  service location, cutoff or objective, explicitly amend G3/G4. Preserve
  its strongest viable form by budgeting real connector space rather than
  treating it as a decorative link of arbitrary length.

| Same six residual drivers | J-P | J-F |
|---|---|---|
| Where can E wait before service? | The finite terminal approach. | The approach, with additional connector occupancy governed by native rules. |
| What completes the compulsory interaction? | Crossing the point priority boundary. | Clearing the finite joining connection. |
| What new physical information is required? | Explicit priority and audited driving lengths. | Those plus connector dimensions, native speeds and admission/completion locations. |
| What is the main scientific tradeoff? | Clean correspondence to the elementary point task; finite manoeuvre dynamics omitted. | Richer compulsory interaction; more reference/predictor discrepancy in the first validation. |

**Delivery-time recommendation, superseded by the feedback discussion: J-P for S-P.** It preserves the accepted T1
traffic picture and supplies independent service with the least added
physical structure. S-L already provides the approved subsequent opportunity
to test transfer to natural terminal merging. J-F is a viable richer boundary
test, but its additional physical meaning should be selected explicitly.
Neither candidate has been selected or built.

[Internal-link behaviour and network-generation distinction](https://sumo.dlr.de/docs/Simulation/Intersections.html#internal-links)

[Driving distance versus displayed geometry](https://sumo.dlr.de/docs/Simulation/Distances.html)

## Gate, ownership and remaining work

S3-M2 is **Type 2**, owned by the methodology reviewer for qualification and
the user for the physical-reference choice. It depends on the closed S3-M1
ladder, G3's terminal meaning and G4's full-time evidence. G2's observers and
the H1/T1 equations remain fixed. After selection, source/configuration
transcription is Type 1; a changed endpoint, added lateral opportunity or
prescribed completed-flow server must return to the affected global contract.

The bounded Step 3 source/evidence pass and comparison-protocol assembly are
now delivered at VSL-S3-G1. **They do not close all of Step 3:** the S-P
physical representation remains a decision, followed by a documentary
consistency check and approval of the consolidated protocol. The separate
execution proposal must later supply version-pinned settings, physical
dimensions, development/held-out preparations, numerical tolerances and
forward-admission evidence. Its criteria are already stated in the protocol;
none of those traffic checks was performed here.

Stop here for J-P/J-F and the Step 3 gate. Step 4, simulator construction,
installations and traffic experiments remain unopened. The ramp line remains
closed. The accepted analytical model source and PDF are unchanged.

[Sources and adaptations](../../extraction/research_readiness/vsl_step3_reference_and_evidence_audit.md#resumed-step-3-source-qualification-2026-10-14)

[Work, checks and stage status](vsl_step3_resumed_review_work_report.md)
