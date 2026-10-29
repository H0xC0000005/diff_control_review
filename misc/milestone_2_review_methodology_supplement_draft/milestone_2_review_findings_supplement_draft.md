# Downstream-task review findings relevant to Milestone 2 — draft supplement

Status: **Draft supplementary input; non-authoritative until separately approved and migrated**  
Prepared: **2026-09-15**  
Intended audience: the user and the future Milestone 2 planning/development agent

## 1. Role of this supplement

The closed reviews sharpen the scientific task that later milestones should
support. They do not replace the active Milestone 2 Phase B decision process.
This supplement records only the consequences that Milestone 2 interfaces and
evidence should be able to support without importing later behavior.

The active Milestone 2 status remains:

- G1--G6 are closed;
- component-local discussion is active, beginning with Component 2.1;
- no authoritative Phase C plan exists; and
- no implementation phase is open.

The review findings are compatible with the closed global backbone. They do not
justify reopening G1--G6.

## 2. Scientific task that Milestone 2 is preparing for

The accepted first downstream task is fixed-time effective-service allocation
at a regular, rotationally symmetric four-leg intersection. The task allocates
continuous service fractions among four protected movement groups and evaluates
clearance-complete total system time. The experiment suite progresses from a
neutral representation case to shared-lane order, finite storage, combined
ordered accessibility, and held-out cases.

For Milestone 2, this task is an **architectural anchor**, not a behavior claim.
Milestone 2 should construct and conservatively couple the lane-local
interaction-zone state. It should not claim that order, shared-lane blockage, or
turn-bay accessibility already changes service. Those mechanisms remain later
Milestone 3 responsibilities.

The four-leg layout and four service groups are the default experimental
scenario, not restrictions to hard-code into reusable network, lane, movement,
or signal APIs.

## 3. Review findings and methodology-side recommendations

The labels below distinguish accepted review conclusions from recommendations
about how Milestone 2 should remain ready for them.

### RF-M2-01 — keep scenario semantics explicit and reusable

**Accepted review conclusion.** The primary task uses a symmetric four-leg
intersection and four interpretable protected service groups.

**Recommendation for Milestone 2.** Preserve explicit, inspectable lane order,
lane permissions, route-to-movement mapping, refined-link selection, and
scenario metadata. The structural API should express the default scenario and
its rotations without assuming that every network has four legs or four groups.
Permutation/rotation checks should transform every associated structural map,
not merely reorder one tensor.

**Boundary.** This recommendation does not choose the concrete Component 2.1
record type or Component 2.5 scenario class.

### RF-M2-02 — make neutral refinement an identifiable comparison

**Accepted review conclusion.** The first experiment must establish neutrality
before attributing any benefit to order or storage detail.

**Recommendation for Milestone 2.** Retain both comparison meanings already
fixed by G5:

1. a physically matched split-domain aggregate comparator, used to isolate the
   effect of lane/grid representation and coupling; and
2. a separately reported comparison with the original unsplit Milestone 0 link,
   used to expose finite-step subdivision effects.

The first comparison supports a representation-neutrality claim. The second
must not be mislabeled as evidence for or against selective order. Reference-only
logic must remain outside production behavior.

**Boundary.** This adds interpretation and traceability; it does not change the
G1/G2 decomposition or G5 decision.

### RF-M2-03 — reserve single-count traffic accounting for the later objective

**Accepted review conclusion.** The downstream objective is
clearance-complete total system time: all released physical traffic mass is
counted once while waiting at sources or residing in the modeled network until
completion. Moving traffic is included; the objective is not queue-only.

**Recommendation for Milestone 2.** Histories and accounting snapshots should
make the physical ownership partition observable across source queues,
unrefined/upstream aggregate regions, lane-local interaction zones, downstream
links, and completed traffic. The ordered ledger and cached movement grid are
two views of physical mass and must never be added as independent occupancy.
Transitions should be traceable by route and location in reference mode so that
double ownership, omission, or misrouting can be diagnosed.

Milestone 2 need not freeze the final clearance runner or experiment objective.
It should expose enough authoritative state for a later objective to compute the
quantity without reconstructing behavior from diagnostics.

**Boundary.** This is an interface/evidence obligation, not authorization to
replace the accepted Milestone 0 diagnostic objective during Milestone 2.

### RF-M2-04 — preserve the continuous control-to-state path and its signatures

**Accepted review conclusion.** Forward fidelity, derivative correctness, and
downstream gradient usefulness are separate claims. Ordinary differentiation is
valid only within a fixed structural realization and stable active signature.

**Recommendation for Milestone 2.** Keep continuous ledger masses and timing,
route-to-movement projection, ledger-to-bin overlap, storage/eligibility limits,
service replay, and reported continuous outputs connected to the tensor graph.
Keep route IDs, lane/movement labels, topology, order skeletons, and permissions
structural. Every operation that can change the local piecewise formula should
expose sufficient signature evidence for reverse-mode AD, JVP, and central
finite-difference comparison on stable rows.

Do not smooth events, introduce surrogate gradients, or make a differentiable
copy of structural metadata merely to obtain nonzero derivatives.

**Boundary.** Passing Milestone 2 derivative checks establishes local numerical
correctness only. It does not establish that a gradient improves the later
traffic-control task or transfers to a richer evaluator.

### RF-M2-05 — keep the Milestone 2 to Milestone 3 seam policy-neutral

**Accepted review conclusion.** Milestone 3 owns the choice among exact FIFO and
an explicitly bounded bin-scale partial-FIFO/intra-bin-homogeneity policy,
including any permitted defragmentation and its error evidence. Exact FIFO is
not preselected as the eventual production policy.

**Recommendation for Milestone 2.** Retain the exact ordered route-mass ledger
as semantic authority, allow only lossless adjacent merging already permitted by
the project, and expose a policy-neutral resolved-removal-plan/application seam.
The Milestone 2 neutral service domain may generate only its approved exact
bookkeeping plans. Its data structures should not assume that the later policy
can be represented only by a scalar lane prefix, because a future approved
bin-scale policy may resolve movement-specific removal within a bin.

Fragmentation telemetry may be measured. Lossy within-bin canonicalization,
behavioral lane reassignment, shared-lane head blocking, and turn-pocket
accessibility must not be activated in Milestone 2.

**Boundary.** The future Milestone 3 plan must define preserved versus relaxed
information, discharge-time semantics, conservation, resolution sensitivity,
and forward/gradient bias checks before any lossy policy is implemented.

### RF-M2-06 — expose comparison seams without implementing later baselines

**Accepted review conclusion.** The later representation ladder distinguishes a
homogeneous macro model, a structured movement-queue model, a lane/storage-aware
aggregate model, the selective-order model, and richer forward references. A
representation comparison is distinct from an optimizer comparison.

**Recommendation for Milestone 2.** Preserve explicit dispatch between refined
and unrefined links, stable scenario IDs, common physical inputs, and result
fields that can be compared under the same objective. Do not bake a later
baseline's state or correction factor into the Milestone 2 implementation. A
missing mechanism should remain a visible capability boundary rather than being
hidden by scenario-specific tuning.

**Boundary.** Selecting and faithfully transcribing the structured-queue and
lane/storage baseline equations belongs to later approved plans. SUMO or another
richer evaluator is not a Milestone 2 dependency.

### RF-M2-07 — keep ramp metering outside the Milestone 2 scientific task

**Accepted review conclusion.** Ramp metering is not adopted as a parallel
scientific task. Aggregate-compatible formulations add little distinct evidence
for the current selective-discreteness hypothesis, while stronger freeway-side
mesoscopic formulations require substantial behavior outside the project.

**Recommendation for Milestone 2.** Do not generalize the interaction-zone API,
validation suite, or acceptance contract specifically for freeway weaving,
lane-changing, capacity-drop hysteresis, speed control, or ramp-control
optimization. A simple merge/ramp layout may be used later only if independently
approved as a low-cost correctness or macro-limit fixture; it is not a project
task or implementation obligation.

**Boundary.** This is a scope guard. It does not claim that ramp metering is
generally unimportant or that macroscopic models are universally sufficient.

## 4. What Milestone 2 should and should not establish

Milestone 2 should be able to establish:

- a conservative physical partition between upstream aggregate propagation and
  the lane-local interaction zone;
- a per-lane equal-mass-rank representation synchronized with exact route/order
  metadata;
- storage-limited admission and causal feedback without silent mass loss;
- representation-neutral service fixtures that do not import Milestone 3
  blockage behavior;
- matched split-domain reference evidence and separately reported unsplit-link
  subdivision effects; and
- local derivative correctness on stable structural signatures.

Milestone 2 should not claim or establish:

- useful signal-control gradients;
- superiority over macro, structured-queue, lane/storage, or microscopic
  alternatives;
- shared-lane FIFO blockage, finite turn-pocket accessibility, or behavioral
  lane allocation;
- an approved exact- versus partial-FIFO production policy;
- a calibrated four-leg experiment bank or final clearance protocol;
- cross-fidelity transfer to SUMO; or
- a second freeway/ramp-metering task.

## 5. Evidence provenance

This supplement is a synthesis of already closed local review artifacts; it did
not perform a new literature search. Its principal inputs are:

- `misc/selective_discreteness_downstream_task_review/synthesis/experiment_formulation.md`;
- `misc/selective_discreteness_downstream_task_review/synthesis/baseline_realization_matrix.md`;
- `misc/selective_discreteness_downstream_task_review/synthesis/project_impact_matrix.md`;
- `misc/selective_discreteness_downstream_task_review/synthesis/milestone_impact_summary.md`;
- `misc/selective_discreteness_downstream_task_review/reporting/closure_record.md`;
- `misc/selective_discreteness_ramp_metering_review/reporting/closure_record.md`; and
- the accepted Milestone 2 modeling/global-decision records already present in
  the repository.

The literature review was targeted rather than universally exhaustive. Detailed
adoption claims and source-level limitations remain in the review packages. This
supplement transfers their accepted project consequences, not their entire
screening archive.
