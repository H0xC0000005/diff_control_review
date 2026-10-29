# S01.30 — N1 user decision gate — freeway lane-capacity-reduction task

Sprint: [S01](../../00_review_sequence.md#s01) · Role: 30 user gate · Predecessor: pre-review handoff · Gate: N1 user gate.

Date: 2026-09-16  
Status: **Candidate A accepted after discussion; N2 protocol drafting authorized;
N2 execution/implementation not authorized**

## Recorded user decision

The user agreed with the revised findings/gate and explicitly approved candidate
A when requesting the next protocol. Accepted scope includes Gap 7, the focused
Gap 8 novelty target, and shared link-level primary actions across B0/B1/B2.
The earlier matrix wording giving B2 lane-specific primary actions was an
inconsistency and has been corrected; lane-specific actions remain a separate
unapproved extension. Exact equations, class/lane state, calibration, and
experiment contracts remain open.

The following N1 findings and candidate alternatives are retained as the
decision's rationale. The current unapproved next plan is the
[`Historical N2 protocol proposal`](../../archive/planning/n2_phase_A_protocol_proposal.md).

## Outcome

Select a narrowed **F1 speed-advisory/VSL task** for a later full review. Stop
**F2 coordinated ramp metering** as the primary selective-resolution task.
Treat **F4 post-reopening recovery** as a required F1 scenario dimension, not a
third control task. Do not open F3 joint control or F5 lane-change control.

For the scientific evidence and modeling implications behind this outcome, read
the explanatory [`s01_20_n1_findings_report.md`](s01_20_n1_findings_report.md). The present
file remains the decision record; the findings report distinguishes direct
literature results, N1 inferences, and proposed adaptations.

## Findings in brief

- Aggregate LWR/link-queue VSL with capacity drop is already a strong baseline,
  and simple feedback can transfer between those aggregate formulations.
- First-order VSL derivatives and optimization already exist; differentiability
  by itself is not a novel result.
- Compliance and traffic composition matter operationally, but can initially be
  represented as continuous aggregate classes rather than individual vehicles.
- Mandatory lane changes and lane distribution can limit VSL-only performance,
  making lane-group state the strongest candidate addition. Existing studies
  usually entangle that state with lane-change commands or direct CAV control.
- No reviewed study isolates B0 homogeneous aggregate, B1 aggregate compliance,
  and B2 lane-group multiclass state under one matched action/objective/evaluator
  or tests which model produces more useful downstream action rankings.
- Coordinated ramp metering already has strong aggregate/multiclass derivative
  and control baselines; no analogous minimum-state gap was found.

The defensible F1 research question is not whether VSL can be optimized or
differentiated—both are established. It is whether the minimum retained
information needed to produce useful downstream speed-advisory gradients changes
from (B0) homogeneous link aggregate, to (B1) aggregate compliance classes, to
(B2) lane-group multiclass state with aggregate lateral transfer, when all
actions are judged in the same independent microscopic evaluator.

F2 stops because strong first-order, multiclass, feedback, fairness-aware, and
nonlinear-MPC baselines already cover its core action and constraints, while the
bounded search found no supported lane/order-state omission that changes the
coordinated-meter decision. Continuing it would test differentiable ramp
optimization again, not the repository's resolution question.

## Compact decision matrix

| Gate | F1 | F2 |
|---|---|---|
| Operational task | Supported | Supported |
| Strong lower-resolution baseline | Supported | Supported |
| Decision-relevant resolution gap | Qualified | Unsupported |
| Smallest added-state hypothesis | Qualified: B0 → B1 → B2 | Unsupported |
| Derivative-correctness contract | Qualified | Supported |
| Independent gradient-usefulness test | Qualified | Technically feasible but scientifically unmotivated |
| Distinct value/novelty | Qualified | Unsupported for this resolution question |
| Stop condition | None yet | Macro sufficiency + insufficient novelty |

The detailed task contract is in
[`candidate_task_matrix.md`](../../synthesis/s01/candidate_task_matrix.md); the minimum
evidence and boundaries are in
[`minimum_source_map.md`](../../synthesis/s01/minimum_source_map.md) and
[`explicit_exclusions.md`](../../synthesis/s01/explicit_exclusions.md).

## Fatal stops, uncertainty, and access

- F1 did **not** trigger a fatal stop. Its novelty and minimum-state claims are
  qualified, not assumed: a full review must try to falsify both.
- F2 triggered macro-sufficiency and insufficient-novelty stops for this
  particular resolution question. This is not a claim that ramp metering lacks
  operational value.
- The search did not locate a direct predecessor that compares B0/B1/B2
  differentiable speed-control action rankings in one richer evaluator. This is
  a bounded search result, not proof of universal absence.
- Seliman et al.'s lane-group VSL paper remained abstract-only (E1), but no
  access request is warranted: open decision-grade sources already support the
  lane-state hypothesis, and the present selection does not rely on its result.
- No distinct third candidate met the protocol's admission rule.
- **User clarification to Gap 7:** avoid control-dependent probability shifts
  over discrete outcomes and hybrid transitions requiring saltation/event-time
  corrections wherever possible. Prefer deterministic continuous traffic mass
  with fixed exogenous cohort/scenario structure. Such an extension requires
  evidence that adequate simpler alternatives are unavailable, explicit user
  approval, and additional gradient-fidelity and approximation/bias-variance
  validation. Ordinary deterministic branch kinks remain a separate issue.
  This clarification does not select F1 or authorize implementation.

## Decision requested

### Problem statement

Should the freeway branch invest in a full evidence review of the narrowed F1
task, revise the N1 framing, or stop the branch?

### Assumed model-chain function

The eventual study, if later approved, would generate continuous infrastructure
speed-advisory controls in B0/B1/B2, verify their numerical derivatives, and
replay matched perturbations or action rankings in one fixed richer evaluator.
It would isolate compliance and lane-group information before admitting any
vehicle-order or gap state.

### Core gap

N1 establishes feasibility and a plausible resolution-sensitive mechanism but
does not prove that B0/B1 misrank controls, that B2 fixes the ranking, or that no
direct predecessor already answers the complete cross-fidelity question. Those
are the next review's fatal gates, not assumptions for implementation.

### Candidates and recommendation

#### A — Select narrowed F1 for a later full review (**recommended**)

Authorize a separate planning task for a full F1 literature/evidence review,
centered on the B0/B1/B2 ladder, derivative correctness, and independent
gradient usefulness. This does not authorize implementation.

**Pros:** directly tests how much lane/compliance information is needed; keeps a
strong aggregate baseline; produces interpretable positive, equivalence, and
negative outcomes; has open decision-grade evidence and a plausible evaluator.

**Cons:** the key ranking failure is not yet demonstrated; calibration and fair
cross-fidelity matching may be substantial; lane-level VSL is already a crowded
control family, so novelty could still fail.

**Dependencies/consequences:** the full-review protocol must foreground direct-
predecessor novelty, matched objectives/populations/horizons, a fixed-seed
microscopic evaluator, and sequential B0/B1/B2 ablation. F4 recovery is required.

The novelty target is one causal resolution-to-gradient-usefulness result, not
new VSL, compliance, lane-changing, and gradient methods separately. Review
priorities are: **P0** direct-predecessor veto; **P1** supported decision gap plus
fair evaluator feasibility; **P2** minimum-state ladder; **P3** deterministic
derivative contract; **P4** matched downstream usefulness evidence. Gap 7's
admissibility restriction is screened early. Gap 8 in the findings report
defines supporting ingredients and excluded novelty directions. These are
review priorities, not authorized implementation or experiment stages.

#### B — Refine and rerun a bounded part of N1

Reject or alter the proposed actuator, disturbance, baseline ladder, or scope,
then issue a specific revised framing for another bounded sprint.

**Pros:** allows the branch to target direct CAV commands, a different closure
regime, or a different state ladder if those better match the intended science.

**Cons:** direct CAV or lane-change control changes the task and raises
entanglement; reopening F2 without a new resolution mechanism repeats a stopped
line; broadening the task increases evidence and calibration burden.

**Dependencies/consequences:** the user must identify the changed scientific
decision. Any F3/F5 or vehicle-specific actuator would need a new task contract
and should not inherit this recommendation.

#### C — Halt the freeway branch

Record that neither the qualified F1 opportunity nor the stopped F2 case
justifies a further review.

**Pros:** avoids a potentially expensive calibration/novelty program and keeps
the project focused on stronger established tasks.

**Cons:** leaves the plausible lane/compliance resolution question untested and
forgoes a task where negative/equivalence evidence could still be scientifically
useful.

**Dependencies/consequences:** no freeway simulator or task work should follow;
the N1 package remains a closed negative/qualified evidence record.

**Original recommendation A — subsequently accepted by the user.** F1 preserves
a small, falsifiable retained-information ladder while keeping primary actions
matched. Its selection authorizes proposing the separate N2 review protocol,
which now awaits approval. No N2 execution, implementation, or project-plan
change is authorized by the N1 selection or current drafting request.
