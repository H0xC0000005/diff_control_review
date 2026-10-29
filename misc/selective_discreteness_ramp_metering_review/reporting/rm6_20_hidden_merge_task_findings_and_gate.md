# RM6.20 — Hidden-merge-information ramp task findings and user gate

Date: 2026-10-01. Status: **Gate withdrawn without disposition; superseded by RM7.**
Parent: [RM6 readmission plan](../rm6_00_hidden_merge_task_readmission_review.md).
Evidence: [source-transfer audit](../extraction/rm6_hidden_merge_source_transfer_audit.md)
and [admission matrix](../synthesis/rm6_task_admission_matrix.md).

> Scope correction: the user found that RM6 continued to anchor the task to
> current implementation progress and selected a model family too early. The
> RMA-R1 candidates below are historical and require no decision. Read
> [RM6.35](rm6_35_method_first_scope_correction.md) and the RM7 method-first gate.

## Provisional result

The reopened branch now has one defensible continuous-mass task family:

> one infrastructure-controlled on-ramp supplies lateral demand to a finite
> target-lane receiving resource shared with mainline demand; hidden target-lane
> merge pressure may change endogenous service and the useful metering action
> even when road-total mainline history and ramp queue history are identical.

The provisional verdict is **RMA-A — admit a narrow analytical task family for
separately gated formulation**.

This is a model-family admission, not an action certificate. It establishes that
the branch no longer fails solely because realistic merge effects must be
microscopic. It does not establish an exact matched-history pair, different
optimal metering actions, lane-state necessity, a useful gradient or traffic
validity.

## Current progress inherited from the old branch

The historical RM0–RM5 review was substantial and fully closed:

- it established the ordinary continuous ramp action, queue, storage and
  all-stream accounting requirements;
- it audited strong first-order and multiclass discrete-adjoint methods,
  ALINEA-family feedback, nonlinear/data-driven MPC and route-aware aggregate
  competitors;
- it inspected destination-aware ramp control and found both a strong aggregate
  comparator and an equation-level reproducibility concern;
- it formulated and audited B1-P, a one-meter/long-link/downstream-diverge order
  transfer case;
- it concluded that B1-P was at most an optional post-M3 transfer fixture rather
  than an orthogonal research task; and
- it produced an accepted colleague report and closed without implementation,
  simulation or gradient experiments.

Thus the branch was not halted for lack of review effort or because ramp
metering is operationally unimportant. It was halted because the reviewed
candidate did not supply the project-specific information-resolution question.

## Why ramp metering halted while VSL continued

| Issue | Historical ramp branch | VSL branch |
|---|---|---|
| Lower-resolution baseline | Aggregate/multiclass ramp control, storage, feedback and gradients were already mature. | Aggregate VSL was also strong, but omitted lane preparation had a more direct source-supported candidate role. |
| Missing-information hypothesis | No evidence showed that exact order or lane state changed a meter decision beyond route-aware aggregate/cohort alternatives. | Ending-lane preparation and mandatory transfer could be hidden from the strong aggregate observer. |
| Compatible candidate mechanism | B1-P avoided realistic merging through non-overlap and reused downstream ordered service; ordinary safe-gap/lane behavior appeared to require new physics. | Continuous mandatory transfer and finite receiving were admitted and eventually produced the S13 conditional certificate. |
| Distinct scientific value | Generic differentiable ramp optimization was established; the candidate repeated the signal task's order hypothesis. | The branch retained a specific information-to-decision question under a different common VSL action. |
| Result at stopping point | Compatible case too elementary; realistic case outside then-approved scope. | Source-bounded M2 member yielded exact observer collision, different actions and a conceptual gradient direction. |

The difference was therefore evidential and methodological, not a preference for
one controller type.

## What later VSL work changes for ramp metering

S12 and S13 do not prove the ramp result, but they add one missing bridge. A
conservative continuous lane-resolved model can represent lateral demand sharing
finite target-lane receiving with mainline traffic, including extra gap/headway
work, without tracking microscopic vehicles or exact gap sequences.

For ramp metering, the action-to-service path is potentially more direct than
for VSL: the meter controls lateral demand arriving at the finite receiving
resource. Hidden target-lane preparation can determine the marginal service cost
of that release. This is enough for task-family admission.

It is not enough for a positive controller result. Under complete all-stream
accounting, an aggressive common release policy may still dominate unless merge
interference changes effective service. A future analytical formulation must
derive that result or return an obstruction rather than select favorable
parameters.

## Representation and novelty boundary

The consequential hidden state may compress to one merge-pressure or receiving-
work statistic. The fair ladder must therefore compare:

1. strong aggregate/multiclass ramp state and history;
2. aggregate state plus the scalar merge-pressure statistic;
3. target-lane versus remaining-mainline grouped state; and
4. fuller lane state only if the compressed closure fails.

A scalar-sufficiency result would answer the minimum-information question but
would not support a full lane-resolved simulator. Likewise, because the finite-
receiving mechanism is shared with S13, the ramp task currently offers a new
actuator/causal-path test rather than an independent mechanism novelty claim.

## Remaining gaps before a research task exists

- No ramp-specific exact reachable pair has identical complete aggregate and
  ramp-queue histories while differing in consequential target-lane state.
- No continuous action family and complete objective have been shown to yield
  disjoint optimal meter actions.
- The transfer, receiving-priority and merge-work equations and parameter
  quantifiers are not frozen.
- Strong aggregate-plus-scalar sufficiency has not been tested.
- No implementation derivative or independent usefulness evidence exists.
- Traffic calibration, field prevalence and reference-evaluator design remain
  outside RM6.

## RM6-UG1 / RMA-R1 — branch disposition

### Problem statement

Should the reopened ramp branch proceed to a narrow analytical formulation,
remain only a cross-actuator extension of the deferred VSL study, or close again
under the historical macro-sufficiency result?

### Assumed model-chain function

The infrastructure meter changes continuous ramp release. Ramp demand and
mainline target-lane demand share finite receiving at the merge. Hidden target-
lane merge pressure changes endogenous service and may change complete all-
stream delay under the same aggregate observer history.

### Core gap

A source-compatible mechanism now exists, but its ramp-specific exact observer
collision, action distinction, minimum sufficient state and gradient relevance
have not been established. The next step would need to formulate and attempt
that analytical certificate without microscopic gaps or weak baselines.

### Candidate A — admit and plan the narrow analytical ramp task (recommended)

Open a separately gated formulation review for one on-ramp/target-lane finite-
receiving model. It must freeze the observer pair, action family, complete
objective, representation ladder, equations, parameter quantifier and aggregate
countermodel before any derivation.

**Pros:** Uses a source-bounded continuous mechanism, directly targets the old
missing resolution question, retains a strong baseline and can return a clean
positive, scalar-sufficient or obstruction result without simulation.

**Cons:** The mechanism overlaps S13, the result may collapse to one scalar, and
generic ramp gradients remain prior work. A later positive analytical result
would still lack empirical validity.

**Dependencies and consequences:** Requires a new RM7 plan and user gate. No
equation, implementation, simulator or gradient work is implied by admission.

### Candidate B — retain ramp metering only as a VSL cross-actuator extension

Do not create an independent ramp sequence. Place one metering variant inside
the deferred VSL Stage-1 model-family/robustness study after colleague review.

**Pros:** Avoids duplicating the finite-receiving theory, permits direct
cross-actuator comparison and keeps the minimum-information ladder unified.

**Cons:** Delays the ramp question, gives it less independent scope and couples
its interpretation to reopening the VSL continuation that the user has chosen
to set aside.

**Dependencies and consequences:** The ramp package remains at this admission
record. The deferred VSL roadmap would need an explicit later amendment before
including the cross-actuator case.

### Candidate C — close the reopened branch

Retain the historical conclusion that mature aggregate/multiclass ramp control
and the lack of demonstrated lane-state necessity do not justify another task.

**Pros:** Lowest scope and avoids a likely compressed-state or repeated-mechanism
result.

**Cons:** Does not test the newly available continuous finite-receiving bridge
and treats an unproved ramp-specific action obstruction as sufficient to stop.

**Dependencies and consequences:** RM6 closes with the original negative role
verdict intact. Ramp metering remains only an optional correctness or transfer
fixture.

**Provisional recommendation: Candidate A.** The claim is narrow enough to avoid
repeating generic ramp optimization and the continuous receiving family is a
material new input relative to the historical stop. The next burden is an
analytical formulation, not implementation.

## Gate question

Select **RMA-R1 Candidate A, B or C**. No successor review starts automatically.
