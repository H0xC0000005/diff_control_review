# Pilot task-evidence codebook

Status: approved at T3 on 2026-09-10; full extraction has not begun

## Task class

- `green_fixed_service`: continuous green/service allocation with fixed topology.
- `green_realizable`: explicit phase durations with cycle and clearance feasibility.
- `adaptive_signal`: state-responsive timing or switching; contextual for the primary task.
- `network_control_other`: toll, gating, route, or other continuous network control.
- `diagnostic_only`: sensitivity/forward experiment without an optimization task.

## Target mechanism

- `aggregate_propagation`
- `signal_service`
- `movement_queue`
- `finite_lane_storage`
- `access_or_order_blockage`
- `network_spillback`
- `none_targeted`

Multiple mechanisms may be coded, but the paper's demonstrated mechanism must be distinguished from mechanisms merely mentioned.

## Signal-variable semantics

- `effective_fraction`: averaged service fraction, not directly a switching schedule.
- `duration_realized`: executable green duration with cycle/clearance semantics.
- `reference_trajectory`: high-level target passed to a lower controller.
- `categorical_or_adaptive`: phase/switching decision outside the initial continuous task.
- `not_signal`.

## Differentiation role

- `exact_or_piecewise_AD`
- `smoothed_or_surrogate_AD`
- `analytic_sensitivity`
- `estimated_gradient`
- `none`
- `unclear`

This code records the method claimed by the source; T4 will separately assess derivative validation and event-boundary qualifications.

## Baseline realization

For each retained task precedent, code:

- whether it can share the proposed control, objective, scenario, and budget;
- unavailable state or mechanisms;
- permitted neutral adaptation;
- gradient-bearing, forward-only, or evaluator role; and
- capability boundary that must remain visible.

## Evaluation evidence

- hand/reference forward case;
- finite-difference derivative check;
- internal optimization convergence;
- matched derivative-free comparison;
- held-out demand/geometry;
- stochastic replications or CRN;
- richer simulator comparison;
- field/empirical comparison;
- computational budget and wall-clock reporting.

## Task-quality fields

- traffic meaning and units;
- horizon and terminal/incomplete-trip treatment;
- parsimony;
- mechanism isolation;
- baseline matchability;
- external evaluability;
- negative-result interpretation; and
- uncertainty or inaccessible detail.
