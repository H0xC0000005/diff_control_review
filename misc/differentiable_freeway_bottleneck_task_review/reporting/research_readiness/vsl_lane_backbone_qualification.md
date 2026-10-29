# Lane-backbone qualification: joined candidate delivered at JQ1

Initial findings: 2026-10-20. **LF1 and H/LF2 selected; joined qualification
delivered at JQ1, 2026-10-21.** The remaining bounded pass is complete for
the declared closed-cohort member. It specifies the finite-domain model,
provides a genuine A/B service/next-state witness, proves complete finite
population-time with an exact residual value, and states the full regular-
branch derivative. This is conditional methodology qualification; numerical
and physical validation, strict action-information value and candidate
acceptance at this checkpoint are not established. Feedback 14 still applies:
the current VSL stack is a reference, not a functional-equivalence constraint.
The earlier recommendation to backtrack first remains withdrawn.

[Current joined-candidate findings and confirmation checkpoint](vsl_joined_candidate_findings_and_checkpoint.md)

[Complete member, information/accounting/sensitivity qualifications](../../synthesis/research_readiness/vsl_joined_candidate_contract_and_qualification.pdf)

[Current congestion/VSL findings and LF2](vsl_congestion_join_findings_and_gate.md)

[LF1 selection and approval scope](vsl_allocator_selection.md)

[Current allocator findings, complete candidate comparison and LF1](vsl_allocator_findings_and_gate.md)

[Proposed component, proof and hand cases, PDF](../../synthesis/research_readiness/vsl_allocator_contract_and_checks.pdf)

The native-source findings below retain their original scope. The new
allocator substitutes a flow-realization component; it does not repair the
printed source equations or certify the authors' unobserved implementation.

[Purpose clarification and corrected recommendation](vsl_feedback14_review_scope_and_allocator_response.md)

The lane-information direction remains sensible. The difficulty is now more
specific: **we cannot yet obtain a physically admissible forward model by
directly transcribing the selected paper's flow rules and adding VSL.** The
source specifies why traffic wants to change lanes, but its printed conversion
of those desires into actual simultaneous flows has unresolved problems.
This matters before gradients or information comparisons: a useful derivative
must refer to a valid traffic update.

The user's approval selects the published lane-model route for qualification,
including reconsideration of the earlier homogeneous-zone preference. It
keeps the concealed A/B lane-loading question. It does not approve arbitrary
source repairs, a finished replacement, or a change to the accepted report.
The option to backtrack is retained.

## Retained findings from the native-source check

There are two helpful findings from the author's later work. The thesis
contains a **three-to-two lane-drop application**, so our geometry has a
closer native precedent than the four-to-three field case previously checked.
It also presents a later receiving restriction that reduces lateral flow
continuously to zero as available space vanishes. That addresses one earlier
branch warning. The original chapter and later chapter differ; the later
formula is a source-supported clarification candidate, not an erratum we
can attribute to the original journal paper. [1], [2]

**The remaining obstruction is shared flow accounting.** Two independent
hand checks expose it:

- **Receiving after a lane change.** Consider a congested lane with little
  room for arrivals. A substantial amount changes out into a neighboring
  free lane. That departure should release space. The printed receiving
  adjustment instead subtracts the departing lateral flow. With admissible
  positive densities, the adjusted receiving value becomes negative, and the
  subsequent minimum rule therefore produces negative forward flow. The
  later thesis repeats this adjustment in its original-model chapter.
- **One donor, two destinations.** A more heavily loaded middle lane can
  have strong demand to change into either neighbor. Each direction is
  calculated from the same sending budget. In a positive free-flow example,
  the two lateral requests together exceed that budget. The printed
  conservation equation includes both directions, but the inspected
  formulas do not supply their joint allocation or a direction-selection
  rule. Applying the natural summed residual-demand interpretation also
  produces a negative forward demand.

These are deductions from the displayed equations, **not results of traffic
experiments or claims about the authors' actual implementation**. The main
receiving example uses one lateral direction, avoids empty lanes, avoids
the disputed full-receiver branch and stays outside the capacity-drop
discharge mode. The donor example is independently useful; its residual
interpretation is stated explicitly in the mathematical note.

[Hand calculations and exact source equations, PDF](../../synthesis/research_readiness/vsl_lane_backbone_flow_checks.pdf)

[LaTeX source](../../synthesis/research_readiness/vsl_lane_backbone_flow_checks.tex)

The public source search and selected thesis chapters did not resolve the
joint allocator. This is a bounded access/reading result, not proof that
no authoritative implementation or explanation exists. A verified source
algorithm resolving these issues could restore the native route.

## Why the VSL addition does not settle this

Han et al.'s sending restriction remains a plausible action interface: advice
limits how much traffic can advance; local lane state and geometry continue
to govern lane-changing preferences and receiving. Physical cells remain
fixed. That gives a clear role to the added component without adding a
separate recovery mechanism. [3]

But reducing sending demand does not supply the missing allocation between
competing movements or determine how space is updated after a lateral
transfer. In the free-flow donor example, capping sending simply scales both
lateral requests together; their sum can still exceed the common budget.
The joined VSL/lane law therefore remains unqualified. Information witnesses,
complete-time/clearance and derivative checks depend on settling that law.

## Allocation assessment result; keep backtracking available

**Problem and model-chain role.** We need one rule that converts lane-change
desires and forward demand into nonnegative realized flows, sharing each
cell's traffic and receiving space consistently before densities are updated.
That flow-realization rule lies between the source's lane incentives and its
conservation update. It directly determines whether an A/B imbalance affects
E's access to service.

**Allocator gap and its resolution.** The printed source equations do not supply the
required complete rule. The authorized review now supplies a concrete
completion with common donor/receiver budgets, an explicit permanent-end
connection and a conditional stock/storage proof. It also exposes a genuine
behavioral choice: unsuccessful lane-change attempts may advance in the same
lane, or desired directions may become committed fractions that hold traffic
back. **The user selects attempts with forward fallback and closes LF1.**
The exact approval scope is recorded separately. Source transcription details
remain local only when they leave that behavioral contract unchanged. The
next check exposed a shared budget/gradient choice, LF2, now closed by user
selection of H. It did not reopen this allocation decision. Subsequent
conditional task qualification is delivered at JQ1.

**Allocator route — assessment complete at LF1.** Carey and Wright primary
methods provide diagonal transport, receiving-sharing and general-junction
leads. A small new three-lane composition can share donor requests, allocate
receiving space with fixed reference-capacity priorities and let residual
traffic use its own forward connection. A published fixed-fraction/FIFO
junction model is the stronger direct-reuse rival. Both require explicit
incentive/geometry mappings; neither inherits complete-task or useful-gradient
results from its sources. Ten available units generating seven toward each
neighbor now have a joint allocation candidate, not just a diagnosed gap.

**Pros:** preserves the principal density/incentive candidate while supplying
a concrete conservative component. **Cons:** the preferred completion changes
the transport stencil and service semantics; it is a new source-supported
adaptation, not a turnkey published three-lane algorithm. It need not maximize
unrestricted total flow. The current findings and PDF state its assumptions,
strong rival and proofs. The later user selection, rather than this earlier
assessment alone, approves the allocator as the qualification dependency.

**Backbone backtracking — fallback after assessing allocation.** Check a model
whose native lane-changing, flow allocation and VSL
control already form one coherent system. Roncoli et al.'s 2015 model is an
existing lead, not an admitted substitute: this review has only preview-level
evidence for its journal formulation. Its endogenous versus controlled lane
changes, permanent lane end and common-speed interpretation must be read
before judging suitability. [4]

**Pros:** directly serves the original aim of reducing newly joined traffic
rules and may avoid repairing this source's allocator. **Cons:** changes the
candidate traffic law and needs a bounded primary-method review; a simpler
admissible replacement is not guaranteed. The A/B question stays fixed, but
no existing information/action certificate transfers automatically.

**Selected continuation: attempts with forward fallback.** The completed assessment has not demonstrated
an excessive coupling burden, conflict with the RQs or a clearly better
backbone. Retain backtracking as a fallback to actual qualification failure.
Similarity to the accepted VSL framework and literal source identity are
preferences, not requirements to retain every old or source rule unchanged.
The original backtrack-first recommendation was premature and remains
withdrawn; a replacement allocator is selected, and no new backbone is selected.

## Progress and stopping boundary

The authorized qualification order is: establish admissible flow; then
qualify the VSL/native congestion interface on fixed geometry; then check
information, complete accounting and sensitivity. The first native-forward
check and the subsequent bounded allocator assessment are complete. LF1's
request-versus-commitment choice and LF2's Han sending/receiving budget are
closed by user selection. The remaining bounded qualification is complete
for the explicit member and delivered at JQ1. Its local/default assumptions
are stated for review; empirical claims and implementation are not admitted.
No silent source repair, alternate-backbone adoption, simulator development,
dependency installation or traffic experiment occurs. The
accepted conditional model/report, closed VSL Step 4, separate historical
Step 3 acceptance and closed ramp line retain their status. Urban work is
outside this pass.

[References, inspected pages and evidence limits](../../extraction/research_readiness/vsl_lane_backbone_source_audit.md)

[Newly inspected allocator references and adaptation limits](../../extraction/research_readiness/vsl_allocator_sources_and_adaptations.md)

[Work record and verification](vsl_lane_backbone_work_report.md)

[Allocator assessment work and verification](vsl_allocator_work_report.md)

[Joined qualification work and verification](vsl_joined_candidate_work_report.md)
