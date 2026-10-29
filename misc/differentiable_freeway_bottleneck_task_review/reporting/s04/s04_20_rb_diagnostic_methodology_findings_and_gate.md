# S04.20 — Route B diagnostic methodology findings and user gate

Sprint: [S04](../../00_review_sequence.md#s04) · Role: 20 findings / decision evidence · Predecessor: S03 / diagnostic planning · Gate: DG-MUG1.

Date: 2026-09-17. **Methodology-only pass closed; DG-MUG1 Candidate A approved.**
[Closure and next-sprint boundary](s04_99_rb_diagnostic_methodology_closure.md).
Subsequent explicitly authorized Candidate A execution is complete at
[the analytical findings/DG-AC1](../s05/s05_20_rb_certificate_findings_and_gate.md).
The original finding-stage recommendation and history below are preserved.
The finding-stage recommendation below is preserved; the user's subsequent
approval selects A, not a positive certificate or permission for numerical work.
No simulation, calibration, implementation or server configuration performed.
The user's latest instruction governs: review the diagnostic methodology, not
execute its previously described numerical passes. Server readiness is not a
review gate. No paper-access request is outstanding.

## Main finding

The information → common-advice decision → conservative refinement → useful
gradient direction remains worth investigating, but **two different scientific
claims must now be separated**:

1. Intrinsic information loss: identical declared aggregate/history information
   conceals configurations that require different useful decisions.
2. Model/observer inadequacy: a particular strong aggregate representation fails
   to predict/use decisions well, although its input history might contain enough
   information for another observer or compressed closure.

The exact-match design addresses the first. An approximate/history-aware model
comparison can address the second. They must not silently substitute for each
other. This review validates that distinction and the comparison logic, not
existence of the required traffic case. No match failed numerically; no residuals
or action scores have been measured.

## What the source check adds

History can, in principle, expose unmeasured state. General nonlinear observability
theory is relevant background, not a ready-made test for hybrid microscopic
driving. [Hermann and Krener, introductory framework](https://www.math.ucdavis.edu/~krener/1-25/10.IEEETAC77.pdf).

A concrete traffic observer estimates lane density, but requires lane-aware
probe quantities and boundary measurements—not just our lane-blind envelope.
Its result neither proves nor refutes recoverability from that envelope.
[Bekiaris-Liberis et al., accepted manuscript, II-B/II-E and III](https://acris.aalto.fi/ws/portalfiles/portal/28009519/ENG_Bekiaris_Liberis_et_al_Highway_traffic_state_estimation_Transportation_research_part_B.pdf).

Abstraction theory separates preserving dynamics, action values and decisions;
matching one of these need not preserve the others. Its general MDP results are
not a traffic theorem. [Li, Walsh and Littman, 3.3–3.4](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/camera-ready-9.pdf).

Approximate-abstraction guarantees constrain model/action-value errors, not merely
closeness of raw observations. They do not supply our traffic residual bound.
[Abel et al., 5.1–5.2](https://proceedings.mlr.press/v48/abel16.pdf).

These sources qualify the inference, rather than fill the direct traffic gap.
Existing [strong response/history studies](../../extraction/n2_source_studies/response_lane_derivative_frontier.md)
and [lane mechanism/counterevidence](../../extraction/rb_source_studies/new_lane_evidence.md)
remain relevant; no new global novelty or literature-absence claim follows.
[Source/access audit](../../extraction/rb_diagnostic_source_studies/observability_and_abstraction.md).

## Methodology audit

| Link | Defensible contract | Evidence still missing |
|---|---|---|
| Advice → response | Common desired-speed response; actual motion remains endogenous; same feasible actions. | Dynamic voluntary-advice response is not established by an available speed-factor interface. |
| Preparation → information | Reachable driving and the actual spatial/history/queue channel, with disclosed preparation differences. | No inspected traffic source certifies the exact paired full-history collision. |
| Information → decision | Compare complete acceptable-action sets and common-action regret, including unchanged advice. | No independent matched-pair action scores; finite samples cannot establish continuous or feedback-policy failure. |
| Decision → refinement | Try valid compressed statistics before fuller lane state; conserve mass and receiving/storage constraints. | No minimum sufficient state, class/order necessity or trusted transfer closure established. |
| Refinement → gradient | Separate forward/reference checks, internal derivatives and independent gradient-guided improvement. | None demonstrated by this review or by a sampled advice ranking. |

Three safeguards particularly matter:

- Full history is a strong comparator obligation, not proof of either hidden-state
  recoverability or irrecoverability. Bit-identical sampled arrays certify only the
  declared channel, not every possible aggregate observable, finer time sampling
  or sensor configuration. Grid audits limit—not eliminate—that qualification.
- Different preparation lane-entry patterns are different past forcing. If those
  assignments are withheld, the comparison also contains unknown-input ambiguity.
  Justify that information boundary; do not invoke a known-input observability
  result or claim the complete past scenarios were identical. A richer-state
  oracle diagnostic is not yet a deployable controller with an available observer.
- Forward differences or an inversion between two inferior actions do not prove
  useful decision loss. A common third action may remain acceptable. Small cost
  errors also do not by themselves bound derivative errors; later gradient
  evidence needs local sensitivity and independent outcome tests.

## Modeling priorities retained

First retain a strong spatial mass/mean-response/history baseline and complete
waiting/recovery accounting. Then, if the chosen claim earns evidence, assess
ending-lane mass by longitudinal group and continuing-lane imbalance as candidate
compressed statistics—not approved sufficient states. Full lanes come only after
a credible compression failure. Response classes and order remain deferred.

Adopt source concepts, not unaudited whole equations: deterministic paired
transfer and finite receiving/storage are candidates; branch budgets, empty-state
ratios and hard capacity switches still need methodological audit. No smoothing,
categorical moving-mass model, source repair or saltation exception is adopted.
Native microscopic behavior in an independent reference does not change Gap 7.

## DG-MUG1 — next substantive choice

The issue is **which claim to pursue next**, not installing SUMO or performing
another development phase. The expanded candidates, Pros/Cons and dependencies
are in [DG-R1 of the inventory](../../synthesis/s04/rb_diagnostic_question_inventory.md#dg-r1--which-information-claim-should-the-next-methodological-study-pursue).

**Provisional recommendation: A — retain the exact information-loss target and
seek a source-grounded analytical/constructive certificate in a tractable traffic
subcase.** Require admissible preparation, the declared history/input boundary,
the same advice and decision-relevant consequences. Merely assuming a lane-dependent
capacity penalty is not such a certificate. The construction may prove infeasible.

Candidate B is a genuinely different, viable model/observer-quality study, not
an automatic relaxation of matching. Candidate C is deferral. No candidate is
approved by execution of this review. Numerical diagnostics, if wanted later,
need separate authorization; their earlier run settings remain prospective design
material, not results or current work.

The method review is closed. The original exact-matching contract remains the
approved default; only choosing B would reopen its information/evidence meaning.
Next selected activity is Candidate A's methodology-only analytical construction.
No implementation follows, and that next sprint has not started in this turn.
