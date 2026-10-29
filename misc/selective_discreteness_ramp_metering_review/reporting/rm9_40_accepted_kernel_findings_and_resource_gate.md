# RM9.40 — Accepted-kernel audit and physical-resource gate

**Subsequent disposition:** [UG3.B approved](../discussion/rm9_resource_b_approval_and_continuation.md);
this gate is closed. The dated alternatives/evidence below are historical.
Current law and next gate: [RM9.50 / UG4](rm9_50_separate_resource_findings_and_observer_gate.md).


Date: 2026-10-02. Status: **RM9-UG2.A accepted; authorized audit executed to
RM9-UG3. RM9 remains open.** RM9-X1–X3 remain deferred.

## Outcome

Recorded the user's handout acceptance and Candidate A adoption, preserved the
extension register, and continued the bounded static/mathematical review. The
accepted two-lane operator passes conditional mass/storage proofs and admits
an exact per-cell total-plus-one-lane reparameterization. Its ordinary strict
branches support sensitivity algebra, without a numerical gradient claim.

The audit also proves a previously unquantified consequence: the residual shared
budgets impose a one-for-one reduction in longitudinal flow for each unit of
lateral transfer on an otherwise unimpeded free-flow branch. This is a substantive
traffic-service assumption, not something established merely by conservation.
The receiving lane's old-sending cap prevents compensating forward service.

The [new mathematical PDF](../synthesis/rm9/rm9_accepted_kernel_semantics_audit.pdf)
and [TeX source](../synthesis/rm9/rm9_accepted_kernel_semantics_audit.tex) give the
proof, a hand-calculated unequal-speed example, a conditional strong-observer
reconstruction and a concrete alternative. The [claim audit](../extraction/rm9_accepted_kernel_claims.md)
separates derived facts from hypotheses. No accepted equation has been repaired,
no core history/action certificate has been manufactured, and no experiment ran.

## Findings and strict interpretation

| Question | Current result | Remaining limit |
|---|---|---|
| Is the operator conservative and storage-bounded? | Yes, under its step bounds and paired transfer/ramp/boundary balances | Entire geometry/ramp/boundary configuration is not yet frozen; physical validity is separate |
| Must two-lane information be stored as two independent lane masses? | Given each cell total, one additional lane coordinate is lossless | Not one scalar for an entire multi-cell region; not proof of hidden information or vehicle discreteness |
| Does the accepted coupling impose a lateral-movement cost? | Yes: a local forward-rate debit exists with no external receiving restriction | No independent justification for this particular one-for-one physical debit |
| Can the strong observer recover lane state? | Yes on a specified strict free-flow/passaged-speed diagnostic, including recovery of transfer direction | Speed map is diagnostic, not adopted; congested/mismatched-support cases remain open |
| Is there an exact hidden-history/useful-action pair? | Not established | Requires defensible forward law plus the complete observer/initialization contract |
| Are gradients correct and independently useful? | Piecewise composition is analytically differentiable away from ties | No whole-chain derivative check, action certificate or independent one-step usefulness |

**Semantic correction:** Earlier wording that A adds no capacity-drop penalty
meant no explicit acceleration/capacity-drop term. The audit now demonstrates an
implicit service debit from the resource coupling. The earlier explanation did
not make its magnitude clear enough. This is not the previously discussed
speed-dependent ramp multiplier; it acts on ordinary mainline lateral transfers
and persists even with distinct lane speeds and ample receiving.

The existence of a local flow debit does not prove complete total-time loss or a
metering advantage. Under unchanged final departure history, all-stream time is
unchanged. A meter-induced response may be specific to the stipulated resource
law, so correct internal gradients alone would not establish physical usefulness.

## Why RM9-UG3 is a new gate

The user accepted a candidate for review, including the explicitly described
shared-budget update. That acceptance is preserved in the [UG2 closure record](../discussion/rm9_handout_acceptance_and_ug2_closure.md).
The present audit supplies new evidence quantifying its physical consequence.
Any removal of the residual debits changes the accepted forward law; retaining
them needs an explicit resource interpretation and a suitably conditional claim.

The inherited G0 contracts prohibit an unexplained imposed capacity penalty as
the basis of a control-benefit claim. This does not make the equations
mathematically invalid. It does mean that a positive result cannot be promoted
as a physical ramp-control certificate without resolving the resource semantics.
RM9's source/adaptation stop rule and the repository's scientific change-control
workflow require a documented decision before changing that law. Reopen only
the residual donor/receiver resource part of **RM9-G2**; keep the adopted lane
count, bounded propensity family, metering action, accounting and UG1 Default
allocator. No new extension or successor is opened.

## RM9-UG3 — do lateral and longitudinal movements spend one flow-capacity resource?

**Classification / owner:** Type 2 review-global, user decision. Local proof and
source transcription are E1/E2 evidence. G1's actual observer/support and later
G3/G4 certificates depend on the resolved G2 law. Approval order remains global
resource contract before dependent full observer/action/gradient transcription.

**Problem statement:** Should within-cell sideways movement explicitly consume
the same finite sending/receiving rate budgets as forward motion, or should it
change occupancy/storage while longitudinal capacity is separately recomputed?

**Assumed model-chain function:** The bounded lateral operator moves mass across
lanes. The forward/ramp operator then determines accepted traffic at downstream
faces, using the Default allocator where mainline and ramp compete. The resource
coupling controls how lateral movement changes service, queues and sensitivities.

**Core gap:** The accepted update subtracts lateral flow from original forward
budgets. This both limits the donor and stops the recipient from using its newly
received mass to increase sending beyond its original offer. The resulting
forward debit is not a theorem of storage conservation or node priorities.
Inspected sources supply antecedents for these components, not independent
validation of this particular within-cell resource competition. Removing the
subtraction is a methodological amendment; adding a speed penalty is not needed
to decide this issue and remains deferred.

**Literature/terminology clarification:** Ordinary sending is a traffic-demand
offer bounded by capacity, not itself a fixed physical movement-service resource.
The recipient old-sending cap is our adaptation: FB0030's Eq. 20 adds lateral
inflow to modified sending. RM0018 supports the forward merge allocator, while
acceleration/void literature supports other disruption mechanisms. These
inspected passages do not establish A's exact one-for-one debit. The
[source and semantic clarification](rm9_41_resource_literature_clarification.md)
records the strongest conditional rationale and its limits.

### Candidate A — retain the accepted common-resource kernel with an explicit conditional claim

Keep the accepted equations exactly. Define sending and receiving as finite
movement-service resources shared by transverse and longitudinal transfers.
Lateral movement takes precedence and consumes the resource that would otherwise
serve forward traffic. Explicitly acknowledge the derived free-flow debit and
review it as a phenomenological hypothesis. Continue information/action analysis
under that declared kernel; require separate evidence before interpreting its
service cost or gradients as real merging behavior.

**Pros:** Preserves the accepted compact kernel and its proven conservation,
shared budgets and branch structure. Gives a tractable, transparent scarcity
model. A finite maneuver resource is a coherent modeling assumption; the audit
does not prove it physically impossible. Useful for conditional mechanism and
representation proofs even before calibration.

**Possible interpretation, not established evidence:** Only traffic eligible
at the step's start receives movement opportunities. Sideways movement consumes
the donor's opportunity; arrivals are not immediately eligible for the target's
forward flow. This could motivate the cap in a simplified model, but does not
derive the exact rate budget from ordinary sending or prove a physical delay.
Cell/step scale and service meaning need support. The debit persists as timestep
shrinks at fixed cell state/length, so next-step eligibility does not make the
whole effect a vanishing lag.

**Cons:** The one-for-one debit is built into the law, not independently established
here. An apparent metering benefit could rely on that imposed service relation.
It does not represent speed/acceleration-dependent disruption merely by being
conservative. Lateral-first priority and cell scale can affect conclusions, and
physical claims remain narrower until the resource is justified.

Full-source validation cannot be transferred to this different coupling.
Conservation motivated the adaptation; it does not physically require the old
recipient cap. A has literature antecedents for its components, but its exact
resource law is not established by the inspected literature.

**Dependencies / scientific consequence:** Freeze the conditional common-resource
meaning explicitly, then complete the strong observer/initialization contract.
Audit how results depend on the debit and compare a no-debit variation when
opened; do not call internal optimization or a model-correct derivative
independent usefulness. Source or reference evidence must justify the resource
before a field-relevant task is claimed. X1–X3 remain deferred.

### Candidate B — separate transverse occupancy transfer from longitudinal flow capacity (recommended)

Retain the bounded lateral transfer and its conservative mass/storage update.
After the transfer, calculate ordinary longitudinal sending/receiving from the
updated lane masses, without also capping them by original longitudinal budgets
minus lateral flow. The PDF gives the explicit replacement and positivity proof.
At each forward merge, mainline and ramp still share one longitudinal receiving
budget through the unchanged Default allocator. Actual accepted transfers remain
paired in mass conservation; both sequential stages respect finite storage.

This is a two-resource interpretation: sideways redistribution changes lane
occupancy, while longitudinal face capacity constrains forward traffic. It does
not claim that transverse plus forward arrivals share the original longitudinal
rate cap. The previous double-capacity concern is resolved only by explicitly
changing the resource contract, not by disguising a missing bound. Ordinary
receiving/storage can still matter; no new courtesy, short-lane urgency,
acceleration or capacity-loss mechanism is added.

**Pros:** Removes the unsupported automatic one-for-one forward debit while
preserving a bounded continuous lane model, finite storage and the Default merge
allocator. Forward effects follow changed occupancy, lane mobilities and actual
receiving constraints. Provides a cleaner first test of whether those mechanisms
alone carry hidden information and useful control sensitivity.

**Cons:** Amends the accepted resource semantics. The split process is still a
reviewer adaptation, not a fully calibrated source model; lateral scale and
update order still need interpretation. It may omit genuine maneuver interference
or show aggregate sufficiency/no useful metering distinction. It is not an
assumption that lane changing has no physical cost in every real setting.

**Dependencies / scientific consequence:** Explicitly reopen just G2's residual
rate coupling and rerun its analytic bounds/behavior audit after approval. Retain
all strong observable information and common action/accounting. Do not add an
extra service penalty after a negative result. Geometry, initial/history support
and a physical speed measurement map must then be transcribed consistently.
The X1–X3 register is unaffected; their later admission remains separate.

**Provisional recommendation: B.** It better isolates lane occupancy and finite
receiving without assuming a separate unit maneuver-service loss at the outset.
The cost is a declared resource-law amendment, not more algorithmic complexity.
A remains viable for a deliberately conditional common-resource study if that
is the intended physical abstraction. Neither candidate is a positive-result
promise or proof that lane detail is necessary.

## Current gate and next allowed action

UG2.A is accepted and recorded; G2's residual resource clause is explicitly
reopened at UG3 on new analytic evidence. No alternative is adopted automatically.
Discuss UG3. Continue the same bounded review only after its resource meaning is
resolved; do not begin RM10, implement, simulate or open deferred extensions.
[Current handoff](rm9_current_handoff.md) records the reading order and limits.
