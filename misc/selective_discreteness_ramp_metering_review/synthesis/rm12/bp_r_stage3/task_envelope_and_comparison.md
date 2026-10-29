# BP-R Stage 3 — conditional task envelope and comparison

Date: 2026-10-06. **All three A decisions approved; partial result accepted; continuation at S3-G2-Q.**
Read the [current interface assessment](interface_continuation_assessment.md) and
[compact-closure discussion](../../../reporting/rm12/bp_r_stage3/compact_closure_gate.md).
Read the [latest joined-contract audit](joined_contract_and_reduction_audit.md)
and [current disposition](../../../reporting/rm12/bp_r_stage3/post_priority_findings_and_disposition.md).
Read [source qualification](../../../extraction/rm12/bp_r_stage3/source_to_task_audit.md)
and [S3-G2](../../../reporting/rm12/bp_r_stage3/findings_and_reference_gate.md).
The user selects [S3-G2-M.A upstream admission](../../../reporting/rm12/bp_r_stage3/meter_boundary_gate.md).
The [selected interface](upstream_admission_interface.md) is transcribed;
the [supplied-original audit](../../../extraction/rm12/bp_r_stage3/supplied_originals_audit.md)
qualifies source CM/local IT. The current
[S3-G2-N allocation gate](../../../reporting/rm12/bp_r_stage3/merge_allocation_gate.md)
records approved fixed priority/reallocation N.A. Upstream admission M.A is
adopted; proportional allocation B remains unselected.
The [mathematical companion](accounting_and_reference_contract.pdf) defines the
balances, units and complete system-time derivation. It is analytical bookkeeping,
not a simulator, traffic witness or derivative validation.

## The traffic task in ordinary language

A finite rush of mainline and ramp traffic must pass one local freeway merge.
An open-loop meter can hold ramp traffic and change when it reaches the merge.
In the candidate physical family, a slow entering or changing vehicle can leave
a moving gap while it accelerates; this can affect traffic behind it. Holding
traffic may reduce some disturbances, but also charges waiting time and can
leave queued traffic entering slowly. The question is whether a compact model
can predict the resulting **all-stream travel-time response to the same rate
changes**, or needs additional state describing those disturbances.

This does not assume that metering improves travel time, that identity is needed,
or that the lowest/highest rate is suboptimal. It also does not require two
physically different states to have identical ideal aggregate histories. Those
are precisely the inherited BP-R claim changes.

## Shared conservative envelope

| Item | Conditional binding / status |
|---|---|
| Geometry | One controlled ramp and a bounded mainline approach, local merge and downstream exit. Begin with the source's point-merge topology; no added acceleration lane, extra ramp or extra lanes to force a distinction. Lane count/lengths must be read and declared before a final task is frozen; screenshots were unavailable in this pass. |
| Physical state | Continuous cell/lane mass or density and bounded storage; entrance waiting is separate. Under the hybrid candidate, moving-constraint descriptors contain lane, position, speed and event progress. The source conservation field counts traffic; descriptors add restrictions, not extra TST population. Conservative event insertion still requires transcription. |
| Units | Traffic mass in vehicle equivalents; time in seconds; length in metres; rates in veh/s; density in veh/m; speed in m/s; acceleration in m/s². Convert source km/h values explicitly if later used. |
| Public data | One declared physical initial state, boundary arrival histories, geometry, laws and fixed parameters. If initially active constraints exist, their initial descriptors and event phases are public too. Each reduction receives its stated projection and initial memory; no reference updates after initialization. |
| Population | Finite offered demand over a declared arrival horizon. Road inflow blocked by storage becomes entrance waiting; ramp traffic remains on its approach or upstream of it. No traffic disappears because the physical ramp is full. |
| Control | Common bounded piecewise-constant **rate permissions**, not realized entry. No VSL, lane-changing ban or separately optimized release phase. Control knots are common. After the decision horizon, use the same declared draining policy in every model. |
| Meter transfer | S3-G2-M.A is approved: cap admission to the finite KW ramp approach using available traffic, permission and approach receiving; count held mass upstream. Actual freeway entry follows propagation and source allocation, without a direct contemporaneous merge cap. B remains unselected. Source CM is now read; donor-speed at birth and joined coupling still need transcription. No new launch law, optimized release phase or arbitrary entrant speed is authorized. |
| Receiving | Finite receiving shared by ramp and every compatible non-ramp inflow. S3-G2-N.A fixed priority/reallocation is approved; local bounds are proved in the post-priority PDF. Exact source 40% construction is excluded; it is not a physical capacity gain. |
| Mass update | Compute admissible demands and receiving from the current state; allocate compatible longitudinal/lateral/node transfers under the qualified law; apply each transfer once with paired debits/credits; advance continuous state and constraint trajectories with consistent event timing. Do not reuse RM9's separate-resource rule to negate this family's moving-obstruction physics. |
| Outcome | Integrate every waiting and road inventory from the declared start through clearance. For pre-existing traffic, this is remaining system time; prior elapsed time is a common constant. Divide by the common finite population only if mean time is reported. No extra recovery-cost term is added to TST. |
| Clearance | Exact emptying if the law supports it; otherwise a convergent inventory integral and a certified residual-tail bound. A stopped finite horizon with uncharged remaining traffic is invalid. A draining tail cannot be assumed to clear forever-blocked or infeasible traffic. |

The conservative/accounting envelope follows the approved boundaries. The source
route A and upstream admission are approved; exact constraint/merge coupling
remains to qualify. This separation
allows useful preparatory work without pretending that the joined task exists.

## Strong independent reductions — conditional roles

These are candidate **roles**, not selected software or a final baseline roster.
All may use the same public physics and fixed calibration evidence. No model is
denied public initialization to manufacture an advantage. A different calibration
under each test rate, replay of future reference states, or reference exit-flow
oracle is inadmissible. Capacity/state closures must be named before assessing
their adequacy; weak arbitrary penalties are not substitutes for strong rivals.

| Role | Retained state / initial projection | Independent evolution and adequacy obligation |
|---|---|---|
| Spatial first-order aggregate | Road section density/mass, ramp approach and waiting inventories; public per-section mass projection | Conservative sending/receiving and node allocation. Preserve spatial queues rather than only total mass. A constant capacity law is a limit comparator, not the sole macro competitor. |
| Congestion/entry memory | Spatial state plus declared queue/regime variables and entry-speed/recovery memory derived from the initial physical state | Update that memory from its own state, controls and public forcing. A hysteretic mode may encode a real capacity drop. It cannot obtain tomorrow's mode or speed from the reference. Source hysteresis models require receiving/storage qualification. |
| Endogenous service / moments | Spatial inventories plus relevant initial mean speed, disturbance-age/speed moments or insertion statistics, with explicit projection | Own dynamic closure driven by actual entries and traffic state; reproduce stationary capacity where its source assumptions apply. Mean-capacity evidence alone does not prove transient adequacy. If these few statistics suffice, that is a valid result. |
| Lane aggregate | Per-lane spatial mass and qualified speed/memory, without individual disturbance ordering | Same lanes and permissions. Tests need for additional disturbance state **beyond lanes**; cannot be called lane blind. Source multilane mean closures are relevant but need dynamic qualification. |
| Selective disturbance state | Continuous background mass plus a declared subset of constraint positions/speeds/ages/order or coarsened descriptors | A proposed intermediate reduction, only after its law/projection is bound. Compare removal of one feature at a time; do not assume full vehicle identity or microscopic car following is necessary. |

No proof of exact hidden-information irreducibility is demanded. There is also no
restriction that compact models must use the elementary RM9 law. Shared physical
parameters and conserved inventory accounting are required; model-specific
closure parameters may be fit under a declared common training/held-out protocol.
Once rate candidates are compared against the same physical reference, feasibility
uses the same physical definition. A model's own feasibility prediction must also
be reported; it cannot silently define an easier feasible set for itself.

## Static limit and study audit

1. **No disruptive entry / acceleration-inactive limit.** Matched reductions
   should recover the underlying conservative KW/node behavior when constraints
   are absent or no longer bind. Artificially retained disruption is a model defect.
2. **Pure queue relocation.** If common arrivals give the same cumulative exits
   for all rate choices, complete TST is identical regardless of where queues
   sit. A prettier freeway queue or higher endpoint exit count is insufficient.
3. **Relevant transient response.** Disturbances can change exit timing in this
   family, but actual common-rate/full-TST leverage is not yet demonstrated.
   Queued-ramp state may explain much of it compactly. The critical test is
   independent prediction under interventions, not mean-flow fitting.
4. **Policy dominance.** Once the actuator law is bound, examine whether an
   extreme rate dominates through the complete objective or all rates only
   relocate waiting. Tradeoffs are plausible; they are not evidence of a
   nontrivial optimum. A simple optimum alone does not settle local response
   fidelity or gradient usefulness.
5. **Sensitivity structure.** Cumulative thresholds change event count/topology;
   within a fixed event pattern, perturbations can change event times and speeds.
   Ordinary differentiation through sampled floor values can miss that path.
   No smooth surrogate, straight-through estimator or gradient theorem is
   adopted. This is a later Stage 4 obligation, not a numerical test here.
6. **Meaningful ablations.** Conditional candidates include spatial resolution,
   ramp queue/entry-speed memory, disturbance-age/speed moments, lane resolution
   and detailed constraint timing/order. Retain shared actuator/accounting. More
   lanes, extra ramps, geometric opportunity control or micro release timing are
   deferred changes, not automatic ablations needed for a positive result.

## What this pass binds and what remains

The bounded pass binds accounting, selected allocation and source motion/local
allocation ingredients. The [post-priority audit](joined_contract_and_reduction_audit.md)
adds birth-speed transcription and static bounds. Complete joined reference/
clearance and strong compact transient laws remain partial; it does not reject
compact models or establish useful gradients. All three A decisions are closed.
The interim partial result is accepted; the continuation stays in Stage 3 and
now reaches S3-G2-Q. No completed task is declared by source-route selection
or conditional comparison roles alone. Final S3-G3 closure is pending.
