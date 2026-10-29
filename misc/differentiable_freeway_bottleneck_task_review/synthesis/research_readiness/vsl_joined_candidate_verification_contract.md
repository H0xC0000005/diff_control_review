# Joined VSL candidate: comparison and sensitivity evidence contract

**Later analytical result, 2026-10-21.** The approved methodology-only
review is complete at JM1. Its new analytical regularity/free-flow results
do not execute or change the prospective numerical requirements below.

[Current findings and JM1 checkpoint](../../reporting/research_readiness/vsl_methodology_review_findings_and_gate.md)

**Scope clarification, 2026-10-21.** This is a prospective evidence contract
for future numerical research. Its tests are not current review work or
conditions for methodological closure. The user rejects the executable
continuation; its unapproved plan and gates are withdrawn. The requirements
below remain available without being executed, frozen as a run configuration
or weakened to make the analytical review pass.

[Active analytical and methodological review plan](vsl_joined_candidate_methodology_review_plan.md)

[Corrected analytical review handoff](../../reporting/research_readiness/vsl_joined_candidate_validation_handoff.md)

2026-10-21. **Prospective contract delivered at JQ1. Nothing below is a
reported numerical result or authorization to run experiments.** LF1/LF2
are selected; the concrete member and mathematical qualifications are in
the linked specification.

[Task, complete equations and analytical evidence](vsl_joined_candidate_contract_and_qualification.pdf)

## The three questions

1. **Information:** does omitting the A/B division change attainable
   full-cohort performance under the same physical model and action?
2. **Representation:** can one small, physically meaningful statistic recover
   the decision benefit, or are richer lane/spatial details useful?
3. **Gradients:** under equal information, do the defined sensitivities support
   useful advice changes compared with simpler action search?

The review proves different service and next-state evolution for a matched
pair. It does not prove a positive optimal-action gap. These questions can
yield zero effects without invalidating a comparison.

## Match the physical decision problem

Use the same declared lane geometry, initial-state pairs, one constant speed
advice, action bounds, source incentives, H budgets, allocation, time/space
grid, exit boundary and full remaining-population objective. Initialization
does not depend on the action being differentiated. No simulator is replaced
inside an observation comparison.

The reset episode starts with the prescribed cohort already inside the road.
Controllers choose advice once at that point. Future aggregate flow can
reveal the mode, but it cannot retroactively change that committed action.
If adding pre-decision histories or repeated feedback actions, provide the
same eligible histories/timing to the comparisons and requalify concealment.
The review does not assert that its two initializations share a hidden
prehistory, or that aggregate information can never identify the mode.

Use matched spatial sampling:

| Observer | Admitted traffic information |
|---|---|
| Aggregate | Total traffic per road cell/row. |
| E plus aggregate mainline | E per row and A+B per row. This is the central reduced observer. |
| One-statistic augmentation | The central reduced observation plus the last A-cell density. It completely identifies the two diagnostic initial modes; sufficiency for larger families is unproved. |
| Lane-resolved | Separate E, A and B densities per physical cell. |

These rowwise aggregate observations give more spatial information than
literal whole-link totals. Link-total versions follow by summing rows and
can be included as coarser rivals. The central comparison removes the lane
split while matching the spatial information; it does not give the full
observer extra road locations.

All observers know the common model, geometry and declared initial-state
distribution. Scenario labels, hidden lane arrays or sampling identifiers
must not become undeclared inputs. A reduced controller may use conditional
model-based reasoning over hidden states; it is not required to guess an
arbitrary equal lane split.

## Separate information value from optimizer quality

For the diagnostic equal-probability pair, compare the best shared action
available from its identical reduced observation with independently chosen
full-information actions. Define ideal values by infima; no blanket global
minimum-attainment claim is made for a model with native switching rules.
The augmented observer and full observer are information-equivalent on
that pair. A positive need for the entire lane vector cannot be claimed
from this diagnostic alone.

Under each eligible observation, include maximum advice/no-control and
bounded scalar action search. Compare gradient use under equal information,
initialization, forward-objective definition and declared computational
budget. A finite grid/refinement search is a reference approximation, not
an automatically certified global optimizer. Report that numerical gap
rather than calling a failed local gradient run an information effect.

An aggregate simulator with different evolution equations would be a separate
model/gradient-fidelity comparison. Source feedback controls requiring
different action timing need a matched variant; they are not silently
instantiated as the same once-chosen scalar task. SUMO remains an optional
later variation, not a review closure requirement.

## Derivative evidence

The analytical derivative includes the finite trajectory and the exact
remaining-time value. The latter has both a state-sensitivity term and a
direct speed term. Stopping differentiation at a residual-mass threshold
would omit real travel time and is not this contract.

Before claiming gradient correctness, implementation must compare the
analytical/AD directional derivative against independently evaluated
complete-objective differences on regular fixed scenarios. Use double
precision, decreasing perturbations and a stable interval of agreement;
declare numerical tolerances and branch-margin diagnostics before those
checks are accepted. This document does not substitute an unrun test or
arbitrary retrospective tolerance for evidence.

At switching surfaces, distinguish one-sided derivatives, finite action
differences and possible jumps. Do not silently smooth or change native
incentives. A fixed-step update has a discrete branch-trace derivative;
continuous-time event/saltation corrections belong to a different evaluator
and are not added by analogy. Empty cells and structural zero movements
need exact mathematical handling, without artificial density epsilons.

Gradient usefulness additionally needs the sign/ranking of actual feasible
advice changes and the resulting full objective, with scalar search as a
strong reference. Internal objective decrease alone does not establish
physical traffic fidelity or a benefit over the simpler optimizer.

## Evidence and status boundary

The current evidence consists of source reading, analytical proofs and
exact static hand arithmetic. No traffic trajectory, AD, finite-difference,
policy-training, calibration or cross-fidelity result exists for this joined
member. Complete-time derivatives are qualified only on regular traces;
source lane-incentive discontinuities remain part of the model.

Accepting JQ1 can establish a task/methodology candidate and evidence
obligations. It cannot mark numerical/physical validation passed or authorize
implementation. A broader state distribution, continuing arrivals, changed
geometry/outlet, advice timing or physical traffic law requires checking
the affected assumptions rather than inheriting the diagnostic certificate.
