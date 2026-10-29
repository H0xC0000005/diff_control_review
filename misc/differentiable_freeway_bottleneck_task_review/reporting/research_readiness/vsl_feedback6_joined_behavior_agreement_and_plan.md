# Feedback 6: what the shared merge-service account should represent

**Latest checkpoint, 2026-10-19: AS1/AS2 accepted; AS3 delivered at the
original Step 3 closure gate.** The intended fixed-E/fixed-(A+B) asymmetric
task now has an accepted forward/information contract, a new conditional
complete-TST finite-action certificate, a nonzero common-fastest range,
the full regular sensitivity reference and a final consistency audit.
The compact extra-adjacent-statistic peer remains exactly sufficient.
The review is complete; formal user closure of Step 3 is pending at
VSL-S3-G1. Numerical gradients/usefulness and physical admission are not
established. SUMO is optional; Step 4, implementation and experiments stay
unopened. Earlier symmetric-member results remain historical references.

[Current asymmetric findings and final Step 3 gate](vsl_as3_findings_and_step3_closure_gate.md)

[New asymmetric action and full-gradient mathematics, PDF](../../synthesis/research_readiness/vsl_as3_asymmetric_actions_and_gradients.pdf)

[Current standalone asymmetric verification contract](../../synthesis/research_readiness/vsl_asymmetric_standalone_verification_protocol.md)

[Final Step 3 consistency audit](vsl_as3_step3_consistency_audit.md)

[Accepted AS2 information findings](vsl_as2_information_findings_and_checkpoint.md)

[Accepted complete-history and compact-peer proof, PDF](../../synthesis/research_readiness/vsl_as2_information_and_history.pdf)

[AS1 acceptance and AS2 authorization](vsl_as1_acceptance_and_as2_opening.md)

[Accepted AS1 traffic findings](vsl_as1_asymmetry_findings_and_checkpoint.md)

[Accepted independent-lane forward contract and proof, PDF](../../synthesis/research_readiness/vsl_as1_asymmetric_forward_contract.pdf)

[Current provenance, intended contrast and narrow correction](vsl_initial_ab_asymmetry_scope_correction.md)

[Earlier symmetric-member findings; closure recommendation withdrawn](vsl_step3_standalone_findings_and_closure_gate.md)

[Earlier symmetric-member comparison and evidence protocol](../../synthesis/research_readiness/vsl_step3_standalone_verification_protocol.md)

[Historical symmetric-member analytical results, PDF](../../synthesis/research_readiness/vsl_step3_standalone_information_and_gradient.pdf)

[Approved standalone scope and remaining questions](vsl_step3_standalone_scope_decision.md)

[Current physical findings and checkpoint](vsl_mp6_physical_findings_and_checkpoint.md)

[Joint admission contract and limits](../../synthesis/research_readiness/vsl_mp6_joint_physical_admission_contract.md)

[Selected W-F and approval scope](vsl_wf_selection_and_scope.md)

[Complete conditional forward argument and checkpoint](vsl_wf_forward_qualification_and_checkpoint.md)

[Selected renewal, analytical evidence and recovery checkpoint](vsl_or_recovery_qualification_and_checkpoint.md)

**Subsequent user decision and execution, 2026-10-15:** the user approved
the three-part chain below and confirmed conditional E slowing. The
source/analytical opening has begun and stops at M2-A1, a possible narrow
terminal-priority amendment. The full chain is not complete. The response
below retains its original delivery status; F/D's exclusive gate stays withdrawn.

[Current executed opening and admission choice](vsl_m2_admission_priority_findings_and_gate.md)

Date: 2026-10-15. Response and revised bounded review plan. **M2 remains the
user-selected direction; its exact law and the full Step 3 remain open.**
Here A is the continuing stream and E is traffic remaining in the ending lane.

## The central correction

Your main objection is right: compulsory merging and ordinary congestion are
compatible causes of waiting and slow discharge. They should be considered
together in one model, not offered as mutually exclusive choices. I withdraw
the F-versus-D selection gate and the recommendation to choose D first.

The traffic problem is to represent **how traffic gets through the forced
merge, and how that passage changes the service available to following
traffic**. The account must respond to the relevant traffic behavior. It does
not need an externally supplied first slowing event.

For example, suppose arrivals fit comfortably below undisturbed capacity.
An E group reaches the lane end, cannot yet enter A, and waits. If A continues
unaffected, this is E waiting, with no necessary loss of A service. If A yields
or brakes, or E enters slowly and obstructs following traffic, usable shared
service can fall. Arrivals can then exceed **current reduced service** even
though they never exceeded undisturbed capacity. A queue and subsequent slow
discharge can develop inside that same process. An independently heavy arrival
pulse can also produce a queue. Both influences can occur in the same episode.

The earlier calculation remains valid only for its stated completion: no
entry obstruction or maneuver burden, free crossing, empty initial history
and load below ordinary service. An undisturbed trajectory is then possible;
if that completion is uniquely causal, it follows that trajectory. This is a
useful benign-case check. It does **not** show that an actual forced merge
under ordinary underload needs an external seed or that congestion must be
introduced by exceeding the undisturbed ceiling. The mistake was the decision
inference drawn from the calculation, not its conditional algebra.

## The agreement I propose we use

Keep one aggregate point-service component, with enough internal traffic
information to update one effective service ceiling shared by A and E. Its
lane-specific admission and allocation rules still determine who can use that
service. Several physical influences may update the same account; they do
not require a separate service constraint for each past entry.

The following behavior belongs in the joined qualification. This is a scope
for review, not approval of an unspecified penalty or equation.

| Behavior | What the model needs to represent | What must not be inferred automatically |
|---|---|---|
| **E cannot yet enter A** | E waits; admission depends on usable adjacent service and the compulsory-entry rule. | Every waiting E group reduces A capacity, or every E entry must stop. |
| **A yields/brakes, or E enters slowly** | The actual interaction can change current shared service and the speed of departing traffic. | A fixed low insertion speed for all E, or a second charge for the same obstruction. |
| **A/E arrivals exceed available service** | Conservative queue growth and discharge; the available service may already be reduced by merging. | Queue size by itself is a new capacity-loss mechanism. |
| **A slow departure continues to affect followers** | Retained recovery information changes later service until the influence ends. Relevant A departures are assessed alongside E departures. | Every slow A departure has an independent extra penalty, or a crossed vehicle remains as unfinished traffic. |
| **Traffic passes without disturbance; the cohort clears** | Benign passage creates no artificial burden; residual influence recovers according to its physical interpretation. | Low observed outflow means low capacity, or every cohort must exhibit an interior optimum. |

Your lane-end example is a sound reason to examine compulsory slowing and
waiting. One qualification matters for this task: ordinary lateral merging
is forbidden within the terminal section before the forced point; upstream
H1 preparation still permits early merging. Therefore, reaching the point
without merging does not itself prove that no acceptable gap was available
earlier. We should model a possible forced wait or slow entry,
rather than make it inevitable for every residual E group. This keeps the
accepted restricted task and its later natural-SUMO transfer test distinct.

The literature supports the relevance of insertion/acceleration effects and
the feasibility of aggregate lane-interaction descriptions. It does not yet
supply our complete finite-cohort M2 closure. In particular, a source assuming
congested approaches does not establish that ordinary overload above an
undisturbed ceiling must be the cause of congestion in this task.

[References actually inspected, access limits and the source/inference boundary](../../extraction/research_readiness/vsl_feedback6_behavior_source_audit.md)

## The remaining modeling gap

There is no need to settle a single exclusive origin of slowing. We do need
to close the causal chain. An aggregate queue tells us that traffic is waiting
and constrains how much can leave; it does not uniquely determine actual
insertion speed, braking, acceleration or continuing recovery. Flow alone
also cannot distinguish light fast traffic from slow congested traffic.

The key question is therefore: **what small set of predicted traffic states
and rules makes admission, departure speed and the shared service account
consistent with each other?** Macro representation looks plausible; its
sufficiency remains a qualification result to establish. One account does
not prove that one scalar state is enough. We will not insert microscopic
gap trajectories or future SUMO speeds merely to close this gap.

## Recommended next review: one joined point-merge law

The major axis is **entry/waiting → actual discharge behavior → shared
service/recovery → effects on the remaining cohort**. This continues the
already selected M2 direction inside the existing G3 terminal return; it is
not a new roadmap stage or a proposal to improve several unrelated components.

| Review question | Concrete work and expected answer | Interface to preserve |
|---|---|---|
| **J1: When can E enter, and what makes it wait or disturb A?** | Qualify the smallest aggregate admission/interaction rule. Explain free passage, E-only waiting and an actual interaction with A through the same approaching-group example. Distinguish immediate blockage from later recovery. | H1 handoff/cutoff, finite terminal, current lane priority and physical sending/storage constraints; no new ordinary terminal lateral opportunities. |
| **J2: How does that traffic leave the point?** | Qualify a regime-aware departure-speed rule from predicted state and admitted traffic. Separate crossing speed from advice and the numerical value of service. Identify source assumptions and each adaptation. | Known initial state and causal prediction; no future reference-speed input or hidden vehicle trajectory. |
| **J3: How do these effects update one shared account?** | Form one candidate update with sufficient aggregate memory. Explain how current interactions and genuine continuing recovery enter once, how influences combine, and how they end. Examine A effects without presupposing an extra A penalty. | One effective shared-service output and conservative A/E allocation; local completion at the choke, with causal influence allowed to persist. |
| **J4: Does the joined candidate remain a sound elementary task?** | Check conservation, feasible service/storage, causal well-posedness, finite clearance and complete local total system time. Recheck MP6's joint operating domain, sufficient information and sensitivity paths; compare strong simpler rivals. | H1 homogeneity, continuous mass, the admitted observation/action contract and model → SUMO S-P → SUMO S-L evidence ladder. |

These questions are reviewed together because an entry restriction can create
a queue that changes discharge, which in turn changes service. Their order
organizes the explanation; it does not assume their equations are independent
or transfer M1's proofs. The eventual candidate must resolve any simultaneous
dependence causally and show that its departures are well defined.

The minimum analytical cases are benign passage; E waiting while A remains
unaffected; an actual slow entry/yielding episode; ordinary service shortage;
their combination; and recovery through full cohort clearance. No traffic
experiment is needed for this bounded source/analytical review.

**Expected deliverable:** one explicit candidate, a plain old/new component-6
comparison, the behavior cases it covers, source/adaptation limits, sufficient
state and interface, and its qualification evidence. Substantial equations and
proofs will have a LaTeX source/PDF. Retain M1, P-E's simpler capacity-drop
description, capable aggregate/history models, the ending-statistic rival and
equal-information search/sensitivity references. The candidate need not beat
them, make full lane state necessary or yield an interior optimum.

## What is settled enough to plan, and what still needs confirmation

**No further F-or-D preference is needed to prepare or conduct this joined
qualification.** The user's feedback and selected M2 direction give a clear
behavioral target. The exact entry/speed/recovery closure, its smallest
sufficient memory and its physical parameter provenance still require review;
they are not facts already established by agreeing on the mental model.

Keep model capability separate from the primary experimental domain. The
review can examine ordinary overloaded loading as an analytical case while
retaining the inherited no-ordinary-overload condition as a useful isolation
case. Feedback 6 does not silently approve changing the primary domain. If
the best candidate requires a changed bound, present that concrete G3
amendment with its attribution and baseline consequences when the candidate
is known, rather than demand a preliminary choice of slowing origin now.

Stop after the joined candidate and its qualification reach confirmation, or
earlier if source/equation work requires a genuinely new physical assumption,
spatial state, information input, allocation meaning or objective boundary.
Resolve ordinary source transcription and bookkeeping within the agreed scope.

**Current status:** feedback 6 answered and the review plan corrected. The
exclusive CP-M2-D1 framing is withdrawn, not closed by selecting F, D or an
unreviewed sum of their laws. CP-D2/M2, P-H, C-P, H1 and the SUMO ladder retain
their approved meanings. The exact M2 law, terminal amendment and Step 3 are
unfinished. This response does not claim execution of the new exact-law pass,
and opens no simulator construction, installation or traffic experiment.

[Progress and next allowed action](vsl_review_progress.md)

[Files, commands, preservation checks and remaining risks](vsl_feedback6_work_report.md)
