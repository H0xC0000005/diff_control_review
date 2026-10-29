# What the standalone task can establish, and how its gradients should be checked

**Superseded for the intended task by the AS3 asymmetric review.** AS1
and AS2 are user-accepted. New fixed-E asymmetric action, full sensitivity
and final consistency results are delivered at the original Step 3 user
closure gate. This record preserves historical symmetric-member results;
they are not the new asymmetric certificate.

[Current asymmetric findings and final Step 3 gate](vsl_as3_findings_and_step3_closure_gate.md)

[Current asymmetric verification contract](../../synthesis/research_readiness/vsl_asymmetric_standalone_verification_protocol.md)

**Subsequent scope correction, 2026-10-19:** the user identifies initial
A/B imbalance, at fixed E and continuing total, as the intended hidden
information. This record's symmetric-member results remain conditional;
its intended-task closure recommendation/readiness is withdrawn. G2/G3
initial-family and information qualification must be reopened. The dated
delivery below is retained and does not prove the asymmetric contrast.

[Current correction and provenance](vsl_initial_ab_asymmetry_scope_correction.md)

Date: 2026-10-19. **Remaining Step 3 review completed; final user closure
gate VSL-S3-G1. No new methodological choice is proposed.**

The central question is now clear: **does knowing how much traffic is still
in the ending lane change a good speed decision, and can the model carry
that information correctly through to the complete travel-time gradient?**
The answer has two parts. One initial ending-lane measurement is enough to
predict the selected task. That information can matter for advice in a
conditional range of the selected law, but it need not matter in another.
The gradient must then follow the entire traffic evolution, including when
traffic becomes eligible, when queues switch mode and how recovery history
is replaced. Differentiating only the current merging formula misses part
of the decision problem.

The review leaves the chosen model intact. SUMO is an optional future
extension, as the user requested. This is a completed methodology review
and evidence protocol, not a report of numerical gradient tests or empirical
traffic performance.

## What the traffic information actually buys

Imagine two preparations with the same total traffic, common past speed and
complete lane-blind longitudinal history. In one, more traffic occupies the
ending lane. The accepted upstream loading construction can produce exactly
this pair, and it still works after the terminal model amendment: before the
decision, neither preparation has reached the terminal or deposited recovery.
Keeping a longer aggregate history cannot distinguish this constructed pair.

Once initial E mass is supplied, total mass and the initial A/B symmetry
reconstruct every initial lane density. The selected model then generates
its own arrivals, queue modes, speed marks and recovery history. Therefore
the compact aggregate-plus-E predictor and the explicit lane representation
have the same objective and sensitivities wherever those sensitivities exist.
We have a sufficient initial statistic, without establishing that full lane
state, vehicle identities or discrete order are necessary for this VSL task.

This sufficiency depends on the fixed preparation family, known parameters
and empty initial terminal/recovery state. It is not a sensing claim for a
general freeway. If a permitted observation already identifies E mass, the
aggregate peer gets to use it.

## When the distinction changes the advice

State ambiguity alone does not prove control value. This review now gives
two direct results for the selected law.

**There is an exact common-action range.** In the previously constructed
history-matched family, a nonzero interval of baseline maneuver burdens still
allows both streams to pass freely at every permitted advice. The mismatch
and recovery mechanisms stay dormant. Both preparations then have the same
complete TST and prefer the fastest advice. Their different lane contents do
not require different control decisions in that range.

**There is also a conditional range where the same slowdown helps one and
hurts the other.** This result is established for the selected model through
a new comparison argument. Start from the earlier H1/T1 reference in which
only fixed maneuver work is retained. In its declared large-work range,
the two preparations have different preferred advice. Restore the actual
mismatch and recovery formulas with small positive mismatch and sufficiently
fast, finite recovery. Their additional effect on complete TST can be bounded
uniformly over all advice. If that bound is smaller than the strict reference
cost gaps, the opposite usefulness of one fixed feasible slowdown survives.
An aggregate-only rule receiving the identical history must still choose
one common action and incur regret for at least one preparation.

This is a deduction for a nonempty conditional parameter range, not a direct
transfer of S13's result. It supplies no calibrated setting and does not
recommend choosing evaluation cases for a favorable result. It proves a
finite-action contrast, not opposite infinitesimal gradients at the fastest
advice. The positive proof has free A traffic; the earlier case demonstrating
A delay and active renewal is a separate family. No single strong-delay,
information-action and physically admitted parameter set is claimed.

## What a correct gradient must follow

Lower advice changes more than the time spent on the road. It can alter
completed preparation; shift every arrival and the end of the arrival pulse;
change actual A/E service and crossing-speed marks; and change the loss
profiles that remain in the recovery window. Queue birth and clearance also
move. Even when a queue is zero at its endpoint, the shifted event can change
the following service and recovery history.

The new mathematical note gives the regular sensitivity chain for all of
these effects. Its main additions are explicit derivatives of moving
eligibility, the implicit service root, the moving queue events and the
recent-mass recovery account. For recovery, replacing old profile weight has
its own derivative term. Omitting it would compute a sensitivity for another
history rule. The calculation uses a fixed horizon beyond every admitted
clearance, so the final waiting tail is included.

An ordinary gradient is claimed only within regular event regimes. The
admitted forward task still includes queue thresholds, grazing or simultaneous
events, profile/root kinks and renewal-cutoff encounters. Those cases receive
their actual forward costs and feasible one-sided analysis. If a finite
derivative does not exist, report that fact and use the actual finite action
change; do not smooth the traffic law or interpret a jump quotient as a valid
gradient. This follows the existing event-aware contract and adds no new
modeling choice. Global continuity and minimum attainment for every coupled
parameter case have not been proved.

## Direct answers at the closure gate

| Review question | Core finding | What remains for later execution |
|---|---|---|
| **What initial information suffices?** | Initial E mass plus the shared aggregate inputs reconstructs the selected complete law. Exact aggregate-history ambiguity remains possible. | Verify the implemented observation/reconstruction interfaces and A+E/G equality. General sensing availability is unestablished. |
| **Can that information change good advice?** | Yes in a conditional positive-mechanism range, through a bounded comparison proof; an exact common-fastest range also exists. | Classify the declared evaluation cases without selecting only favorable ones. No measured performance gap is claimed. |
| **What is the full gradient?** | A regular-event sensitivity must include preparation, moving arrivals, service, queue events, recovery replacement and full clearance. | Compare independent references, converged forward differences and AD in double precision; retain boundary cases and undefined derivatives. |
| **What does a successful result mean?** | Within-task information-sensitive decision guidance. Compact equality is a sufficiency result; scalar search matching the gradient method is acceptable. | Optimizer efficiency or superiority needs its own matched-resource evidence. External traffic usefulness remains outside the present claim. |

The mathematical details, including the comparison proof and event/recovery
derivatives, are supporting material rather than prerequisites for reading
this report.

[New analytical results and complete sensitivity chain, PDF](../../synthesis/research_readiness/vsl_step3_standalone_information_and_gradient.pdf)

[Standalone verification protocol and outcome interpretation](../../synthesis/research_readiness/vsl_step3_standalone_verification_protocol.md)

## Closure recommendation and exact stop

**Recommend accepting the remaining standalone review and closing Step 3 as
a task/comparison/evidence-protocol review.** No primary equation, observation,
action, objective or gradient meaning needs a new selection. The consistency
audit finds no further methodological gate. Numerical settings, parameter
cases and actual implementation/gradient evidence remain for a separately
approved execution proposal; applied MP6 and external transfer stay unpassed.

This is the planned final user checkpoint, not automatic user acceptance.
Step 3's review work is complete and its final closure is awaiting review.
Step 4 has not opened. The ramp line, simulator construction, installations
and traffic experiments remain closed or unopened as before.

[Final consistency audit](vsl_step3_standalone_consistency_audit.md)

[Papers viewed, reused literature and own-derivation map](../../extraction/research_readiness/vsl_step3_standalone_sources_and_derivations.md)

[Work, commands, tests and preservation record](vsl_step3_standalone_review_work_report.md)
