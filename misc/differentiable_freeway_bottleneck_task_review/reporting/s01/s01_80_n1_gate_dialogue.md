# S01.80 — N1 gate clarification record

Sprint: [S01](../../00_review_sequence.md#s01) · Role: 80 dialogue · Predecessor: pre-review handoff · Gate: N1 user gate.

## User note — Gap 7 probability-shift and saltation avoidance

The user clarified that the existing meso stack was deliberately designed to
avoid moving probability mass and saltation problems. Introducing random
discrete processes with control-dependent outcome probabilities creates extra
gradient-modeling/approximation and bias-variance burdens. Such processes should
be justified only when no adequate alternative exists, with dedicated
gradient-fidelity experiments under the relevant probability shifts.

### Interpretation and response

- Treat the note as an authoritative screening/design restriction for the
  ongoing review, not as approval of a freeway candidate or implementation.
- Distinguish deterministic time-discrete constraint kinks from stochastic
  probability redistribution and, separately, hybrid event-time/reset
  sensitivities. Saltation is not synonymous with a stochastic probability
  shift.
- Continuous traffic mass transfer and fixed compliance-cohort shares do not
  automatically create a discrete probability-shift problem. Prioritize these
  deterministic representations in B1/B2.
- Fixed seeds are useful for paired evaluation but do not eliminate missing
  derivatives of control-dependent categorical probabilities.
- Screen capacity-drop laws for genuine discontinuities rather than describing
  every activation as an ordinary kink. Do not approve a hybrid reset by
  implication.
- If a prohibited-by-default mechanism is indispensable, reopen the smallest
  derivative/model contract and its dependent questions; justify why adequate
  continuous/deterministic alternatives fail; then seek user approval of
  dedicated gradient-fidelity and estimator/approximation evidence.

### Synchronization and verification

Updated `s01_20_n1_findings_report.md` (Gap 7, B1/B2, derivative checks, and next-review
question), `s01_30_n1_user_gate.md`, `candidate_task_matrix.md`, and
`explicit_exclusions.md`. Read repository guidance/context and current review
records; used `apply_patch` for documentation edits. Verified relative Markdown
links and reviewed synchronized terminology. No scientific run or code test is
applicable to this documentation clarification.

No source, tests, configs, approved milestone plan, `PROJECT_CONTEXT.md`,
`PLANS.md`, or user feedback file was changed. Mainline methodology is not
amended. N1 remains at its user gate; the next allowed action is further gate
discussion or an explicit candidate/refinement/halt decision.

## User question — Gap 8 novelty focus and next-step priorities

The user asked how the scattered potential novelty areas relate to F1's
recommendation, which are addressed in which order, and which are outside the
recommended next step.

### Interpretation and response

- Clarify one central candidate contribution: a causal minimum-information
  result for useful cross-fidelity speed-advisory sensitivities. Merely combining
  existing ingredients does not establish novelty.
- Treat compliance and lane groups as successive explanatory variables; treat
  derivative verification, calibration, evaluator matching, and F4 recovery as
  evidence requirements rather than separate inventions.
- Prioritize direct-predecessor novelty and a supported decision gap plus fair
  evaluator feasibility before detailed model architecture. Screen Gap 7's
  restriction early. Then specify the minimum-state ladder, derivative checks,
  and matched downstream-usefulness evidence as one system.
- Do not demand B2 by assumption or rescue a failed novelty/motivation gate by
  inventing a controller or estimator. Simpler-model sufficiency is admissible
  but not automatically a publication contribution.
- Keep new control families, vehicle-level CAV actuation, microscopic behavior
  theory, stochastic/saltation estimators, safety theory, field deployment, and
  implementation outside the recommended immediate step.

Updated Gap 8, candidate A's dependencies, and the candidate task matrix using
`apply_patch`; checked the synchronized text and relative Markdown links. No
new literature search or scientific test was required. These edits clarify
existing scope and preserve decision status: N1 is still at its user gate. If
F1 is selected, the next action is a full-review protocol proposal, not review
execution, experiments, or implementation.

## Candidate A accepted; N2 protocol drafting authorized

After reading the revised findings and gate, the user agreed with them and then
explicitly referred to approval of candidate A in the protocol-drafting request.
Record selection of F1, not approval of any model/experiment implementation.
Synchronize the primary action as shared link-level advice across B0/B1/B2;
lane-specific actions are a separate unapproved extension. This corrects the
consistency audit's identified matrix mismatch under the approved clarification.

The N2 Phase A proposal/dialogue are in
`temp_content/differentiable_freeway_bottleneck_task_review/`. N2 stops at its
protocol-approval gate now, and, if subsequently executed, at the first
findings-dependent scientific routing gate or earlier access/fatal stop. No
closed review package, source, project plan, milestone, environment, or user
feedback was changed. Earlier statements in this dialogue record the status
at those discussion points; this entry is the current authorization boundary.
