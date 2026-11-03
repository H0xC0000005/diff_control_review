# Per-case VSL optimization: one controller, two tuning methods

**Handoff alignment complete:** the user accepts B first and confirms
that A is not required early. The local private entry, current-scope/timing
addendum and portable first-verification specification are aligned.
Original equations, source snapshots and implementation workflow remain.
The next development action is its first implementation proposal.

[Alignment outcome and boundary](vsl_b_first_handoff_alignment.md)

**Scope choice resolved:** the user selects the matched B pair first
and defers A. The review-side elementary specification is consolidated;
the current pass stops at that checkpoint before private handoff alignment.
The scientific outcomes and numerical implementation remain untested.

[Current first-verification specification](vsl_b_pair_elementary_verification_specification.md)

[Earlier task fit and source-boundary finding](vsl_zhang_task_fit_findings_and_choice.md)

2026-11-02. **Per-case optimization and the same-base-controller
requirement are user-fixed.** The active recommendation is one common
Zhang-derived speed-setting design, tuned without or with simulator
derivatives. Its common task adaptations and numerical methods remain
proposed, not an accepted implementation or experiment plan.

The earlier attribution of one overall source algorithm to each B arm
is withdrawn as the controller construction. It confused a controller
with the routine used to tune its parameters. No second traffic model
or task is introduced in B-gradient.

[Correction, shared-controller identity and source scope](vsl_shared_controller_correction.md)

The question is now concrete: **for the same initialized traffic case,
does access to the simulator's complete speed derivative help select
useful advice compared with objective values alone?** Runtime control and
training a shared controller are later possibilities, not this task.

The recommendation is a strong value-only search paired with a
value-checked gradient search. Both choose the same kind of advice;
the derivative supplies a local direction rather than a new traffic model.

## One decision variable, two feedback channels

B is one direct speed-setting controller, whose single continuous
parameter is the common advice in 30–60 km/h. Both versions use that
identical control map and execution rule. Recommend adapting Zhang's
speed-parameter representation as the common source design for both.

For any prescribed parameter value, the two versions issue exactly the
same speed throughout the same episode. Equal parameters therefore give
the same trajectory and TST from the same initialization. Different
tuning methods may ultimately select different parameters; that is the
intended optimization outcome, not a controller-family difference.

This first controller has no separate aggregate-state feature vector.
It follows the selected per-case direct-optimization setting rather
than introducing a learned feedback policy.

| Shared element | Contract |
|---|---|
| **Traffic case** | The same prescribed initial lane-cell stocks, independent of advice. No later arrivals; the selected free outlets and completion line remain. |
| **Forward evaluator** | The selected Subraveti/Han/Carey-led lane-resolved plant, with its existing update and boundary conventions. |
| **Objective** | Complete total system time (TST) for the whole initial cohort, including the exact remaining-time value. No residual deletion or extra E-merging penalty. |
| **Physical action** | One speed value applies throughout an executed episode. Optimization trials are counterfactual simulator resets, not repeated advice changes during that episode. |
| **Optimizer memory** | Each method may retain its own admitted query history for this case. It starts afresh for the next case. |
| **Final result** | The best advice actually evaluated under that method's budget, together with its measured complete TST. |

The evaluator retains separate E/A/B states internally. B0 receives costs;
B-gradient receives costs and, where qualified, the speed derivative.
Neither receives raw lane arrays, a hidden-case label or a teacher optimum
as an explicit controller feature.

This is the intended channel by which episode-specific traffic detail can
affect a gradient update. B0 also encounters its consequences through TST;
the comparison must not claim that objective feedback contains none of
that information.

## What feedback means here

B0 is not a no-feedback method. It receives complete TST values, which
allow it to compare candidates and retain the best one. Its proposed
fixed grid schedule does not use a supplied derivative to steer probes.
Comparing costs can still reveal useful finite-change information.

B-gradient additionally receives a local derivative to guide a feasible
speed change. That derivative requires a rollout and sensitivity work;
it is not a direct live-traffic signal. Neither version updates advice
from traffic-state feedback during the executed episode: both commit to
one constant speed. The comparison concerns planning-time derivative
access, not open-loop versus closed-loop execution.

[Plain-language clarification and precise borrowing/adaptation boundary](vsl_matched_feedback_and_borrowing_clarification.md)

## The proposed matched pair

**B0: objective-only enumeration with global coverage.** Try candidate
speeds across the whole interval and retain the best result. Use a
deterministic nested uniform grid so additional budget improves coverage,
rather than assume the objective has one smooth minimum. Include interior
values and both bounds. The grid is a search approximation; it does not
turn the admissible speed into a discrete physical control.

**B-gradient: bounded first-order search with value checks.** At the
current candidate, use the complete simulator derivative to propose a
feasible speed change. Evaluate the proposed speed using the same full
objective; shorten an unsuccessful trial step. Retain the best evaluated
result, including when a trial crosses a traffic-rule switch.

These are two proposed tuning routines for the same controller, not
different controller models. Numerical step scales, grid resolution,
stopping tolerances and resource limits belong in the
later development/experiment plan and must be fixed before comparing
outcomes. There is no source-backed guarantee of global convergence or
superiority for either method on this adapted traffic task.

Use a common, case-independent starting speed; the midpoint is the proposed
default. Both methods receive the same initial cost probes, including the
bounds, charged to their budgets. The gradient search starts from the
shared prescribed candidate rather than a hidden-state-dependent warm start.

The first common probes do not depend on A, which is deferred.
An A-based warm start is a possible later variation requiring explicit
matching and cost accounting; it is not part of this first specification.
Both methods retain the best actually evaluated initial or trial candidate.

B0 does not use finite-difference or simulator-provided gradients in this
primary contrast. A finite-difference gradient optimizer is a legitimate
additional comparison, but must be named as gradient estimation rather
than derivative-free search.

## One base controller source, with gradient tuning added by us

**Common base candidate: Zhang et al. [1], Section 3.2.** The source
represents controls as speed-setting parameters and evaluates candidates
in a simulator. The shared adaptation uses one common continuous speed,
our selected lane-cell evaluator, closed cohort and complete TST.

The source's spatial/discrete settings and boundary constraints are
replaced identically in both versions. Continuous advice is already
part of this target task; B0's finite grid is a search approximation,
not a different physical action set. This is an adapted source design,
not reproduction of its native constrained speed profile.

B0 can retain enumeration as its value-only tuning method.
B-gradient adds first-order parameter tuning using the same controller's
complete simulator sensitivity. This gradient extension is our work;
the source need not have optimized its controller by gradients.

The user excludes Delle Monache from the active proposal, including
as an added optimization dependency. Historical reading records remain
for traceability. The common base is Zhang-derived; gradient-based tuning
is our extension, justified through our existing complete derivative.

The existing complete sensitivity and regularity results establish a
gradient path for this continuous common parameter on regular advice
intervals. There is no need to differentiate through a source optimizer,
or to prove approximate behavioral equivalence between distinct controllers:
the two control maps here are identical by construction.

[Shared-base identity, adaptations and ablation interpretation](vsl_shared_controller_correction.md)

## What a direction means, and where it can fail

At an interior speed on a regular branch, a nonzero derivative identifies
a sufficiently small local decrease direction. It does not certify a
large step across a switch, an improving feasible direction at a bound,
or a globally best speed. Zero derivatives and nonregular queries must
be reported, not repaired by changing the traffic equations.

An unqualified derivative is not an update direction. Stop that gradient
path and report the best candidate already evaluated, making the reason
visible; do not silently substitute a smoothed or different objective.

Keep derivative correctness and optimization performance separate.
Value checks can prevent accepting a worse trial, but do not prove that
the derivative was correct. Conversely, a correct local derivative can
give little search advantage in a scalar problem.

Every query resets to the identical initial cohort and retains the same
complete accounting. Query and numerical failures are recorded; neither
method may obtain an artificial low cost by truncation, lost mass or an
unqualified remaining-time approximation.

## Scientific comparison and first verification

| Question | Future evidence required | Interpretation |
|---|---|---|
| **Is the derivative correct?** | Complete-objective differences at regular speeds, with an inspected stable trace and declared numerical accuracy. | Tests differentiation, including the residual; no optimizer advantage follows. |
| **Does it indicate useful changes?** | Independently evaluate feasible advice perturbations and accepted search steps in the same plant. | Local within-model decision guidance; not physical or runtime validation. |
| **Does derivative access help search?** | Best observed TST versus computational budget for the matched pair, with forward/backward/query counts. | A possible quality or efficiency benefit; equal performance or a B0 win is valid. |

Begin from existing reference cases: reproduce the analytical service
contrast, examine the matched X/Z initial states as separate optimization
cases (they differ in A/B loading), and retain
an unconstrained case where maximum advice is correct. Do not assume the
X/Z pair has different best advice or discard it if both favor the maximum.

Report wall time and forward/derivative work rather than iteration counts
alone. Count rejected trials, initialization probes and final verification.
Use the same precision, physical scenario and numerical accounting.
Resource budgets are prospective development choices, not unrun review
results or fixed numerical thresholds supplied here.

## What the per-case decision changes

The user selects case-specific planning feedback. Different advice may
now be chosen for X and Z after simulator queries, even if the original
aggregate observations coincide. The old best-shared-action versus
separate-action bound is not the interpretation of this optimizer pair.

This explicitly amends decision-information timing, not the traffic
equations. Both methods may use information entangled in their admitted
query histories. The treatment being studied is access also to the simulator
derivative, not equality of all returned information.

The user's observation that a gradient can provide a current optimization
direction motivates a possible later runtime study. This report establishes
no state-estimation method, live replanning rule, real-time feasibility or
physical transfer result. Those remain deferred.

## Current status and development entry

The user accepts the consolidated B-first specification and authorizes
the private handoff alignment. That transition is complete. Its wrappers
now identify the selected model and per-case query comparison, and a
portable local specification carries the reference/evidence target.

The physical model, complete objective and regular derivative are unchanged.
Twenty original exports, initial provenance and the implementation workflow
are preserved. Numerical settings and executable checks remain for a
development proposal; no simulation or gradient result is established.

A is not required early and remains deferred under the user's stricter
source assumptions/backbone/intended-behavior criteria. Zhang is not fixed
as A; no A model or new source survey is opened.

The next development task is Phase A planning under the retained workflow.
It owns architecture, numerical settings, checks and component sequence.
This review/handoff pass stops before that proposal, implementation or
scientific execution.

[Handoff outcome and responsibility boundary](vsl_b_first_handoff_alignment.md)

## Sources and supporting records

[1] C. Zhang, E. Chung, N. R. Sabar, A. Bhaskar, and Y. Ma, “Optimisation
of variable speed limits at the freeway lane drop bottleneck,”
*Transportmetrica A: Transport Science*, vol. 19, no. 2, Art. no. 2033878,
2023, doi: [10.1080/23249935.2022.2033878](https://doi.org/10.1080/23249935.2022.2033878).
[Primary manuscript](https://ira.lib.polyu.edu.hk/bitstream/10397/92568/1/Zhang_Optimization_Speed_Freeway.pdf),
Sections 3.2 and 4.3.

[Primary reading scope and transfer limits](../../extraction/research_readiness/vsl_matched_controller_review_sources.md)

[Complete plant, objective and regular derivative](../../synthesis/research_readiness/vsl_joined_candidate_contract_and_qualification.pdf)

[Earlier timing alternatives, now resolved for the first verification](vsl_matched_controller_review_findings_and_gate.md)

[Work and document checks](vsl_per_case_matched_controller_work_record.md)

