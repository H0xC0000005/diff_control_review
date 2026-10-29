# Standalone asymmetric VSL: Step 3 verification contract

Date: 2026-10-19. **AS1 and AS2 user-accepted; AS3 review delivered.
Proposed for original Step 3 closure at VSL-S3-G1. No numerical execution
or Step 4 is authorized by this record.**

The task asks whether knowing the adjacent-lane share of continuing traffic
changes useful common-speed advice, and whether a complete traffic gradient
carries that information correctly. The selected conditional model is the
current standalone evaluation world. A compact predictor with the same
initial adjacent information is a required equal-information peer.

This contract supersedes the historical symmetric-member protocol for the
intended task. It keeps the accepted mechanisms and evidence hierarchy while
using independent initial E/A/B loads and the Level 2-to-Level 3 comparison.
The historical protocol, its proofs and verification remain in place as
conditional references, not new asymmetric results.

**Global-assumption audit, 2026-10-19:** the separately approved preliminary
review is complete at GA-G1. The short statement below makes existing
premises explicit and the dependency audit qualifies their claims. No law,
admission bound, observation, objective or derivative meaning changes.

[Audited global-assumption statement](vsl_global_assumptions_statement.md)

[Audit findings and checkpoint](../../reporting/research_readiness/vsl_global_assumptions_findings_and_checkpoint.md)

## Fixed traffic world and complete accounting

Use the user-accepted AS1 domain and H1/T1, S-E-P, W-F, R-E and O-R laws.
Every true initial E, A and B load is independent; each lane remains uniform
along the same footprint. Count actual total E+A+B mass. Keep the terminal
and recovery account initially empty, no postdecision arrivals, finite
storage and the original bounded one-shot constant common advice.

Freeze initial traffic, geometry, physical coefficients, W-F reference
normalization and the one-vehicle-equivalent renewal mass while advice
varies. Do not regenerate initial state, refit work coefficients or change
the predecision history for a candidate action. Completion remains at the
choke. Complete local TST includes every initial lane's remaining travel
and both A/E waiting tails. Retiring recovery weight never removes traffic.

Admission is mathematical and conditional. Mark parameter provenance as
analytical, source-supported or empirically identified. No physical range
is inferred from a successful existence proof or numerical optimizer.

## Information, inference and representation

| Role | Inputs and required behavior | Attribution |
|---|---|---|
| **Level 1** | All admitted lane-blind longitudinal observations/history and lawful inference. | Context for the nested ladder; not the central new contrast. |
| **Level 2** | Level 1 plus initial E and combined continuing traffic, and every other actually admitted channel. Allow model-aware estimation, uncertainty or a disclosed prior. | The central omission is the initial A/B split. Do not force A=B or weaken the rival to a snapshot. |
| **Level 3** | The same common inputs plus individual initial E/A/B loads. Predict all later traffic and history autonomously. | The Level 2-to-Level 3 test concerns information, not an assumed representation/optimizer advantage. |
| **Compact equal-information peer** | Level 2 plus one initial adjacent mass, or an equivalent statistic. Reconstruct E/A/B under the common footprint and predict the same law. | It must agree with Level 3 in complete trajectories, objective and every defined derivative. Larger lane detail is not established as necessary. |

Shared physical coefficients and initialization-family knowledge do not include
the realized E+A load, which reveals A when E is known. Scenario/pair IDs,
reference lane traces, future service and post-action E/queue/recovery data
are evaluation records, not initial predictor inputs. Action-dependent
observations do not open a probing or feedback controller.

AS2's construction matches the entire predecision aggregate record and an
even richer E/continuing record. Its feasibility and exact channels are
explicit; it is not a field sensor specification or universal observability
theorem. Preserve identifying cases: strictly receiving-limited E decline
at known speed can identify A under the known law. Any other informative
actually admitted channel is honored. Priors/risk rules for ambiguous input
must be disclosed and fixed before the action comparison; the pairwise
certificate does not choose one for the rival.

Information present in complicated features may be harder to learn, but
that is a separate hypothesis. An identifying statistic computed from the
same permitted inputs is an equal-information transform and may be used
by either peer. A later extraction/training comparison needs matched tasks,
inputs and resources; it cannot be labeled an information-impossibility
result or opened as a new experiment by this review.

## Evidence layers and required outcomes

| Layer | Evidence required | Interpretation boundary |
|---|---|---|
| **Mathematical/forward correctness** | Independent reference and hand cases; paired transfer and total mass conservation; finite receiving/storage; correct roots, marks and guards; complete clearance; equality of departure-integral and travel-plus-queue TST. | A failed forward layer blocks derivative interpretation. Differentiability does not repair it. |
| **Information and reconstruction** | Reproduce AS2's admitted complete-history equality and its identifying cases; verify compact/Level 3 equality under the same initial information. | Different predictions alone do not prove useful actions. An informative history is a sufficiency finding, not a failed test to hide. |
| **Complete-time action relevance** | Evaluate feasible changes and scalar near-optimality against full TST in the same selected law. Include endpoints, admitted event boundaries, positive and common-action cases. | The new conditional finite-action certificate is not a default parameter selection, proof of opposite infinitesimal slopes or applied traffic evidence. |
| **Gradient correctness** | Distinguish the continuous variational/event-aware reference, a converged independently checked forward model's directional differences, and its AD derivative. Record event signatures, cutoffs and all clearance tails. | AD/difference agreement on the same inaccurate discretization does not establish continuous-model accuracy. |
| **Within-task gradient usefulness** | Check predicted feasible directions against independently checked complete-TST changes and a strong scalar reference, with numerical error bounds. | A finite derivative or an internal training-loss decrease alone is insufficient. Correct local derivatives need not make a large finite step useful. |
| **Optimizer/learning advantage, optional stronger claim** | Same task, model/information, feasible interval, objective, starts and disclosed resources. Count derivative work and objective calls and compare attained accuracy. | Neither information value nor feature extraction difficulty establishes AD necessity, a representation win or a speedup. |

These checks concern the defined task; an independently coded reference
is not an independent traffic world. Applied MP6 and any SUMO transfer
require their own later admission/evidence. They do not block this user's
chosen standalone methodology closure.

## Reference jobs and case discipline

1. **Accepted asymmetric history/reconstruction reference.** Fixed E and
   continuing total, swapped adjacent/far loads, complete matched histories,
   and the compact peer. Also retain informative receiving-history cases.
2. **Current-law common-fastest control.** A nonzero additional-work interval
   gives free passage and identical travel-only complete TST in the new
   asymmetric pair. Positive E, positive mismatch coefficient and finite
   recovery are allowed. A no-E neutral case is supplementary, not its substitute.
3. **Exact fixed-work deletion.** The auxiliary arrival-aware E queue has an
   exact full pulse/tail objective on its declared sustained-queue branch.
   The new low-A/high-A calculation is a reference; it does not replace W-F
   mismatch or R-E/O-R recovery in the selected world.
4. **Selected-law finite-action existence.** The uniform objective bound
   transfers opposite finite slowdown utility and positive common-action
   regret to a nonempty positive-mechanism range. It may require large work,
   weak mismatch and fast recovery and keeps A free. It is not a moderate-
   work, calibrated, strong-A-delay or numerical-gradient certificate.
5. **Coupled-delay and history mechanisms.** Retain the archived complete
   A-delay/active-renewal witness as a separate reference. It checks behavior
   absent from a pure E queue; its preferred action and physical range are
   not supplied by the new action certificate.
6. **Regular and nonregular event cases.** Cover preparation switches,
   arrival front/rear, A/E birth/clearance, mismatch/profile changes, window
   fill and old-cutoff/source encounters. Retain admitted grazing/coincident
   cases and report actual side/finite-change behavior.

These are distinct analytical reference jobs, not a claim that one parameter
setting exercises every mechanism or supports every research outcome. A
future execution proposal must predeclare its cases and admission rules
without screening on hidden preferred actions, gradient signs or whether
the richer model wins. Retain the full admitted case accounting and negative
results. Keep empirical identification and held-out action evaluation separate
if applied parameter evidence is later introduced.

## Full gradient and numerical obligations

Hold all independent initial lane loads fixed. Differentiate preparation at
fixed progress, the moving lane-specific arrivals including B, current
service roots and speed marks, the recovery source and old-weight retirement,
and queue/event times. The W-F coefficient is physically fixed; it is not
renormalized with advice or a new search box. Preserve history through queue
clearance and do not reduce the dynamic state to the meter reading alone.

Use an action-independent horizon beyond the proved uniform clearance bound.
The differentiated departure integral and travel-plus-A/E-queue form must
agree. Zero queue endpoint values do not remove the timing effect on future
service/history. The new mathematical note gives the full independent-lane
reference and conditional regularity argument.

For fixed smooth event sequences, use double precision, feasible perturbation
and forward-refinement ladders, event signatures and error accounting. At
action endpoints use feasible one-sided comparisons. Separate continuous
model error, numerical forward error, difference-estimation error and AD
error. Solver/resolution settings, tolerances, perturbation sizes and budgets
must be fixed in a concrete later execution plan using reference conditioning
before its held-out outcomes; no unsupported numeric thresholds are adopted
in this method-only review.

For a nonregular case, first determine forward value and continuity/side
behavior. Report finite ordinary/one-sided derivatives only where they
exist; otherwise report the undefined/nonfinite derivative and actual finite
cost change. Keep the case in scalar action assessment. No smoothing, frozen
event, weaker gradient criterion or generalized-gradient controller is chosen.
If later execution requires a changed derivative meaning, reopen its smallest
affected global contract.

The global scalar reference must not presume every coupled objective is
smooth or its infimum attained. Give certified bounds/near-optimality where
available, including endpoints and events. Report a grid minimum at its
actual resolution rather than as an exact global optimum.

## Strong simpler rivals

| Rival | Why it matters | Fair claim |
|---|---|---|
| **Level 2 with all lawful history/model-aware inference** | It may identify A or make a good common/uncertainty-aware decision without an extra sensor. | Test omitted information under the exact admitted record, not an intentionally ignorant aggregate model. |
| **Exact compact adjacent-statistic predictor** | It reconstructs Level 3's initial state and matched law. | Require equality; no full-lane-state necessity or automatic representation win. |
| **Analytical sensitivity, finite differences and bounded scalar search at equal information** | One bounded constant advice is a strong setting for direct references. | Useful gradients need not be uniquely necessary, faster or better than search. |
| **Fixed work/receiving and stationary recovery reductions** | They can explain part of the same behavior with simpler constitutive state. | Preserve their limits and label model-form changes; do not attribute a pure information effect. |
| **Accepted literature challengers** | Wei–Han–Wang, Jin–Jin and Hegyi/METANET supply capable aggregate/history/control mechanisms; Carey and Nagalur Subraveti supply continuous lane-aware alternatives. | A faithful later source-model adoption needs its native equations/action and parameter contract; no weak hybrid is labeled a published baseline. |

Existing VSL cost-variation work remains prior art. No novelty of VSL,
gradients or lane-aware continuous traffic is assumed. A successful result
must explain its information, physics and optimizer attribution separately.

## Outcome interpretation and final gate

| Outcome | Conclusion |
|---|---|
| A permitted history identifies A | Allow its reconstruction; Level 2 is sufficient for that record. |
| Matched histories, different predictions, common best advice | Prediction ambiguity without required control value in that regime. |
| Matched histories and incompatible near-optimal actions | Conditional value of the omitted adjacent information in the defined law. |
| Compact peer and Level 3 agree | One extra initial adjacent statistic is sufficient; larger representation need not win. |
| Recoverable information is hard for a learner to extract | A separate learning/conditioning result only after matched-input/resource evidence. |
| Continuous reference, refined differences and AD agree | Correct implemented sensitivity in the declared regime, not automatically useful finite advice. |
| A predicted feasible step improves independently checked full TST | Within-task usefulness bounded by the step, event regime and numerical error. |
| Scalar search or a simpler model matches the result | Retain the simpler explanation; no stronger optimizer/state-necessity claim. |
| A boundary has no finite derivative | Report the limit and actual finite cost; do not remove the forward case. |
| No physical/external evidence is supplied | Keep the conditional standalone result; applied MP6/SUMO transfer unestablished. |

AS1–AS3 and the final global consistency audit are now complete at review
scope. Stop at VSL-S3-G1 for acceptance/correction and formal user closure of
the original Step 3. Step 4, implementation and experiments do not begin
automatically.

[Plain findings and closure gate](../../reporting/research_readiness/vsl_as3_findings_and_step3_closure_gate.md)

[New asymmetric action and complete-gradient mathematics, PDF](vsl_as3_asymmetric_actions_and_gradients.pdf)

[Final consistency audit](../../reporting/research_readiness/vsl_as3_step3_consistency_audit.md)

[Source reuse and claim limits](../../extraction/research_readiness/vsl_as3_derivation_and_claim_audit.md)
