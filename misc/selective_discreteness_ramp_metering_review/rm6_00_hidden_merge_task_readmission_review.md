# RM6.00 — Hidden-merge-information ramp-metering task readmission review

Date: 2026-10-01. Status: **Withdrawn without disposition; superseded by the RM7 method-first reopening.**
Parent records: [historical ramp closure](reporting/closure_record.md),
[S13 M2C-A closure](../differentiable_freeway_bottleneck_task_review/reporting/s13/s13_99_m2_certificate_sprint_closure.md),
and the [post-S10 successor plan](../differentiable_freeway_bottleneck_task_review/synthesis/s10/s10_post_closure_next_step_plan.md).

## Authority and changed role

> Scope correction: this plan still anchored admission to the current project
> architecture and selected a finite-receiving family before task formulation.
> The user rejected that reopening basis. Its gate is withdrawn; see
> [RM6.35](reporting/rm6_35_method_first_scope_correction.md).

The 2026-09-15 ramp review rejected ramp metering as an orthogonal parallel
second task for the signal-control project. That decision remains valid for its
original role. On 2026-10-01, after accepting the separate VSL M2C-A result, the
user explicitly placed further VSL work on hold and reopened ramp metering as a
new task-admission question.

RM6 therefore does not revive the halted B1-P downstream-diverge task or claim
that the old closure was mistaken. It assesses the narrower successor hypothesis
recorded after S10:

> Lane- or gap-resolved receiving opportunity at an on-ramp merge may be hidden
> under the same strong aggregate mainline history and ramp queue, and that
> information may change a useful infrastructure metering decision.

## Review purpose

Determine whether one project-compatible, source-bounded continuous-mass model
family warrants a separately gated analytical task formulation. The review must
stop early if the proposed distinction requires microscopic safe-gap sequences,
explicit vehicle lane-changing trajectories, direct CAV control or a weak
aggregate comparator.

## Historical starting point

The closed RM0–RM5 review already established:

- operational ramp metering, finite ramp storage and queue override are mature;
- first-order and multiclass discrete-adjoint ramp-control methods exist;
- ALINEA-family feedback, fairness-aware control and nonlinear/data-driven MPC
  are strong lower-resolution competitors;
- the B1-P one-meter/downstream-diverge construction is coherent only as a
  narrow transfer fixture and reuses the ordered-service hypothesis already
  owned by the signal task; and
- realistic overlapping merges, lane access and safe-gap behavior were not
  supported by the then-approved physics without a substantial expansion.

No ramp simulation, controller implementation or gradient experiment was run.

## Fixed RM6 contracts

- **Geometry:** one infrastructure-controlled on-ramp merging into a multilane
  mainline with one explicit target lane or target-lane group.
- **Action:** one bounded continuous ramp-metering rate or fixed-shape release
  schedule. There is no speed control, lane-change command or vehicle trajectory
  control.
- **Traffic quantity:** continuous vehicle-equivalent mass with conservative
  mainline and ramp accounting.
- **Observer:** complete declared predecision history of road-total mainline
  density, flow, speed and cumulative counts, plus ramp queue/history and common
  known future forcing; no target-lane decomposition.
- **Outcome:** complete all-stream delay/system time including ramp waiting,
  mainline delay and residual queues through common clearance.
- **Comparator:** strong aggregate and multiclass ramp models, including finite
  storage and queue management; an aggregate-plus-merge-pressure statistic must
  be considered before attributing value to full lane state.
- **Evidence staging:** task-family admission precedes an exact decision
  certificate; a decision result precedes any useful-gradient claim.

## Explicit non-goals

RM6 does not formulate final equations, prove an exact matched-history action
split, implement a ramp model, run SUMO, calibrate traffic, optimize a controller
or claim novelty. It does not reopen route choice, stochastic vehicle events,
microscopic gap acceptance or the halted B1-P order task.

## Question inventory and ownership

All questions are Type 2 review-global because they define the task, observer,
mechanism, comparator and claim boundary.

| ID | Question | Dependency |
|---|---|---|
| G1 | Does the reopened branch seek a hidden-information task rather than generic differentiable ramp control? | Fixed by the user instruction and historical stop. |
| G2 | Is there a conservative continuous-mass merge/receiving family that can consume lane-resolved information without microscopic gap sequences? | Primary-source and S12/S13 transfer audit. |
| G3 | Can the metering action plausibly influence that receiving interaction under complete all-stream accounting? | G2. |
| G4 | What is the strongest fair representation ladder? | G2–G3; must include aggregate-plus-scalar. |
| G5 | Is the family strong enough for a later analytical formulation, or does the old macro-sufficiency stop remain decisive? | G1–G4. |

## Execution method

1. Reconstruct the frozen RM0–RM5 evidence and exact reason for closure.
2. Reuse the newer S12 finite-receiving source audit and S13 analytical result
   only where their mechanism transfers to an on-ramp action.
3. Test the chain `meter release → ramp/mainline target-lane competition →
   finite receiving/endogenous merge service → complete all-stream delay`.
4. Compare against aggregate, multiclass and scalar merge-pressure alternatives.
5. Return one admission verdict and stop at RM6-UG1.

## Admission verdicts

- **RMA-A — admit a narrow analytical task family:** a source-bounded
  continuous merge/receiving mechanism survives, but exact decision relevance
  remains for a later formulation review.
- **RMA-S — aggregate/scalar sufficiency at admission:** every consequential
  variable identified by the review is already available to a strong aggregate
  or one-scalar augmentation, leaving no justified lane-state task.
- **RMA-E — no compatible path:** the proposed distinction requires excluded
  microscopic or hybrid behavior, or no action-to-service path survives complete
  accounting.

## Stop condition

Stop at [RM6-UG1](reporting/rm6_20_hidden_merge_task_findings_and_gate.md). No
equation contract, implementation, experiment or successor review starts
without explicit user approval.
