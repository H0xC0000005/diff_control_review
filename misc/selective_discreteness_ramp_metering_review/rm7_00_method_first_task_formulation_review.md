# RM7.00 — Method-first ramp-metering task-formulation review

Date: 2026-10-01. Status: **Closed at RM7-UG1 / RMT-R1; Candidate A approved.**
Parent: [RM6 scope correction](reporting/rm6_35_method_first_scope_correction.md).

## Authority and purpose

The user explicitly rejected implementation-anchored reopening and instructed
the ramp branch to restart in the same method-first manner as the VSL line.

RM7 therefore asks which ramp-metering traffic task can test the core research
question before selecting any simulator architecture:

> What information omitted by a strong macroscopic ramp model could alter a
> useful infrastructure metering decision, and could that information later
> support a relevant control gradient?

Current project components, milestone progress and implementation cost are not
task-admission criteria. They enter only after a scientifically defensible task,
model family and evidence protocol exist.

## Evidence use and non-authority

The historical RM0–RM5 review remains useful for mature ramp-control baselines,
candidate mechanisms and known confounds. Its negative project-role decision is
not imported as a veto because it answered a different question: whether ramp
metering could be added as a strictly compatible orthogonal parallel task.

Likewise, S12–S13 finite-receiving work is one candidate mechanism family, not
the predetermined ramp model.

## Scope of this review

RM7 performs the ramp counterpart of the VSL line's initial task selection:

1. define candidate traffic/control tasks;
2. require one common infrastructure metering action and complete traffic
   accounting;
3. identify the candidate macro-hidden information in each task;
4. identify strong lower-resolution alternatives and confounds;
5. select one task for a later full predecessor/mechanism review; and
6. stop before model-family adoption, equations, implementation or experiment.

## Evaluation criteria

Each candidate is assessed on:

- operationally meaningful infrastructure control;
- a strong aggregate/multiclass baseline;
- a specific information omission that could change service or outcomes;
- an isolatable progression from aggregate to richer state;
- feasibility of matched actions/objectives and a richer independent evaluator;
- a plausible later differentiability path; and
- distinct research value beyond generic ramp optimization.

## Candidate task families

- **F1 — local on-ramp merge-opportunity control:** one meter controls entry to
  a multilane mainline where target-lane occupancy, usable gaps, merge stage or
  relaxation may be hidden by road-total aggregates.
- **F2 — ramp admission with downstream route-access/spillover:** metering changes
  the composition and timing reaching a fixed downstream exit or restriction.
- **F3 — coordinated multi-ramp control with localized merge states:** several
  meters interact through corridor propagation, ramp storage and local merge
  opportunity.

## Fixed task-selection guardrails

- The action remains infrastructure ramp metering; direct vehicle acceleration,
  lane-change, route or trajectory control is a different task.
- Ramp waiting and mainline delay must be counted for the complete affected
  population through common clearance.
- Candidate models must later share the same action, demand, objective and
  reference scenarios.
- Mature aggregate feedback, MPC and adjoint methods are baselines, not reasons
  to reject a richer-information question before it is formulated.
- A negative, compressed-state-sufficient or aggregate-sufficient result is
  admissible.

## Explicitly open after task selection

RM7 does not decide whether the eventual candidate should use lane-continuous
mass, ordered packets, safe-gap distributions, microscopic vehicles, a hybrid
reference or another representation. It does not assume exact gap state is
necessary or differentiable. Those are later evidence/model-family questions.

## Stop condition

Stop at [RM7-UG1 / RMT-R1](reporting/rm7_20_method_first_task_formulation_and_gate.md).
Task selection would authorize a later full review proposal, not equations,
implementation, simulation or gradients.

## Task-selection closure

The user approved Candidate A and retained Candidate C as a possible extension
after positive local results, subject to a separate decision. RM7 is closed.
See the [decision record](discussion/rm7_candidate_a_approval_and_extension_record.md)
and [remaining design inventory](synthesis/rm7_post_selection_design_inventory.md).
A bounded RM8 proposal is the next allowed step; execution is not open.

## Later continuation decision — 2026-10-01

The user approved open-loop G1.A and accepted the recommended initial review
approaches. Bounded RM8 literature/static review was authorized to its next
substantive discussion point and has reached RM8-UG1. Read the
[continuation record](discussion/rm7_open_loop_approval_and_rm8_opening.md) and
[active handoff](reporting/rm8_current_handoff.md). The earlier proposal-only
restriction above is superseded for this authorized RM8 pass; equation adoption,
experiments and implementation remain gated.
