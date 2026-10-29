# BP-R Stage 3 — joined physical core and reduction audit

Date: 2026-10-06. **Accepted interim snapshot; complete study contract not frozen.**
The 2026-10-07 [interface continuation](interface_continuation_assessment.md)
adds a dynamic compact source law, inactive hand check and conditional tail
results. Current discussion is [S3-G2-Q](../../../reporting/rm12/bp_r_stage3/compact_closure_gate.md);
Stage 3 stays open. The source/status findings below retain their original scope.
All three A selections are approved. This is a static transcription/consistency
assessment, not a simulator or an adopted new closure. The
[mathematical companion](post_priority_static_contract.pdf) retains equations
and their assumptions; its [TeX source](post_priority_static_contract.tex) is beside it.

## What the traffic model is trying to represent

Ramp traffic first waits for permission to enter a finite approach. It then
travels towards the merge. At the merge, ramp and mainline traffic compete for
one finite receiving resource according to the approved priority. A slow
entrant can constrain traffic behind it while accelerating. Traffic can move
between available mainline lanes according to the source's lane-flow rule.
The controller's consequence is measured by when the entire offered population
exits, with waiting charged wherever it happens.

This is a local merge task with a rate actuator and a moving-disturbance
mechanism. It does not presume that every vehicle identity is needed, that
lane contrast is sufficient, or that ramp metering must improve the objective.
BP-R asks which independently evolved state preserves the intervention response.

## Binding and update interfaces

| Link | Qualified binding | Explicit limit |
|---|---|---|
| Offered arrivals → waiting → approach | M.A: actual admission respects available continuous mass, upstream rate permission and approach receiving; debit waiting and credit approach once | No individual stop-line launch model or direct merge cap is inferred |
| Approach and lane traffic → demands | Spatial KW/CTM sending with source local lane-flow demands; outgoing movements share each donor's budget | Exact lengths, mesh/support and public initialization remain declared task settings, not parameters chosen for a favorable result |
| Incoming demands → mandatory receiving | N.A: fixed ramp priority, unused shares reallocated; all compatible non-ramp inflows share their group award in incoming-demand proportions | Priority is fixed physical data, not a control; no 40% calibration or extra physical capacity is imported |
| Flows → conserved state | Each actual transfer has one donor debit and receiver credit; sink exits and outside arrivals are the only net population changes | Source lateral transfer already advances to the downstream target cell; do not add a second longitudinal advance |
| Actual transfers → disturbances | Deterministic cumulative thresholds create descriptors, with donor-speed birth evidence from the 2004 antecedent | Descriptors do not add mass; no Poisson sampling, optimized phase or extra TST merge-work term |
| Disturbances ↔ traffic field | Final-journal constrained motion and cumulative-count moving-boundary coupling | Existing constraints cannot be replaced by a guessed scalar capacity penalty; exact mandatory-boundary/event integration remains unverified |
| Exits → objective | Complete entrance, ramp and road inventory integral; common arrivals/population and the whole clearing tail | Mean flow, an endpoint throughput count or freeway-only waiting is insufficient |

The conceptual sequence is causal but is not a claim that an arbitrary split
solver reproduces the source. Existing constraint paths, receiving and motion
must be coupled consistently. New entries create constraints on their actual
entry time; a sampled next-step convention must not silently change that law.
The current source route does not yet qualify coincident births, a descriptor
at the node, and the selected group-priority boundary as one complete solver.
These are named E2 obligations rather than an invented algorithm.

## Checks possible without running traffic

**Node bounds.** The approved operator serves every demand when it fits. Under
scarcity, its ramp award lies between the residual that mainline cannot use and
the ramp demand, while mainline receives the remainder. Both demands are bounded
and receiving is used once. Proportional subdivision cannot increase a donor's
requested flow. This proves the local allocation bounds, not coupled reference
accuracy or future clearance.

**Conservation.** Paired internal transfers cancel in the total inventory
balance. Descriptor creation adds no population. Finite storage still requires
the coupled receiving law to enforce it; conservative bookkeeping alone does
not prove that law's implementation respects storage.

**Inactive equivalence.** Remove nonbinding disturbances and retain the same
geometry, admission, priority and lateral rules: the physical core reduces to
the matched unobstructed KW/node model. Matching this limit is a necessary
comparison check. Passing it says nothing about active-case sufficiency.

**Queue relocation.** Common arrivals and initial population with identical
complete exit histories imply identical TST, even if traffic waits in different
places. All holding decisions must therefore affect exit timing to change this
objective. A higher terminal count alone does not establish that difference.

**Clearance.** Finite arrivals and a positive final permission are insufficient
as a proof. Routes must lead to exits, constraints must release or leave, and
the receiving/kinetic law must permit discharge. A convergent inventory tail
with a certified residual is an alternative to exact emptying. No source theorem
was obtained for clearance of this *joined* adapted reference. This remains a
formulation obligation before a study is declared ready; no arbitrary terminal
penalty or assumption that the road is empty was used.

**Policy limits.** No entrants/no binding disturbances and pure queue relocation
are valid equivalence cases. Active merge evidence supports a possible rate
path through queue/entry speed and disturbances, but does not prove that the
highest rate fails to dominate, that an interior optimum exists, or that a
particular derivative is useful under the complete objective.

## What a fair independent reduction must specify

Every model receives public physical initialization and forcing under an explicit
projection. It evolves its own ramp, lane, speed/mode/moment and event states.
No future reference entry/exit history, hidden-state correction or per-test-rate
fitting is permitted. Common geometry, action timing, physical parameters and
inventory accounting are retained; model-specific closure approximations must
be named and separated from claims about removing state alone.

| Role | Initial retained information | Independent update requirement | Present status |
|---|---|---|---|
| Spatial lane KW | Per-section/per-lane mass, ramp approach and waiting | Same conservative transport and approved node without disturbance constraints | A well-defined limit comparison; insufficient as the sole serious active rival |
| Queue/regime memory | Spatial state plus declared public congestion/entry memory | Own transition and effect on shared receiving, compatible with this actuator/storage | Source family supported; exact matched closure unbound |
| Mean/moment service | Spatial state plus justified speed/age/insertion statistics | Entry-driven transport and aging; a service calculation using its own quantities | Mean-capacity evidence supported; transient closure unbound |
| Lane aggregate | Lane mass and qualified local speed/service state | Own coupled lateral and receiving evolution | Retains lane information; source mean framework not a finished transient law |
| Selective trajectories | Explicit subset/coarsening of public constraint state | Conservative reconstruction and independent constrained evolution | A possible study direction; no new coarsening law approved |

Consider a brief reduction in upstream permission followed by release. A mean
capacity formula may predict a long-run rate for each traffic regime. It does
not by itself say which previously admitted slow entrants still constrain the
road, how quickly that effect changes, or how a compact statistic evolves after
the release. A memory model could answer this; it must supply its own update.
Using reference trajectories to fill that gap would not test independent
representation adequacy. This example explains the missing interface; it is
not a simulated counterexample or proof that an event-free model fails.

## Bounded outcome

E1 qualifies the source ingredients; N closes allocation ownership. E2 has an
explicit candidate core and local proofs, but not a completed boundary/event
and clearance qualification. E3 has strong, fair roles but lacks a fully matched
transient compact law. E4 separates those gaps from genuine negative results.
No complete research-ready task, compact insufficiency, added-state necessity
or useful-gradient chain is certified. The result is **partial/evidence-limited**,
not impossibility and not a positive necessity claim. See
[evidence](../../../extraction/rm12/bp_r_stage3/post_priority_evidence_audit.md)
and [S3-G3 disposition](../../../reporting/rm12/bp_r_stage3/post_priority_findings_and_disposition.md).
