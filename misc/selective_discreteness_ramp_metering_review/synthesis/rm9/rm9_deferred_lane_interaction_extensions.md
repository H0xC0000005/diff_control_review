# RM9 deferred lane-interaction extension register

**Current baseline:** UG3.B subsequently amended only the residual resource
coupling; post-lateral forward budgets are recomputed. X1–X3 remain Deferred,
including any new speed/acceleration state or receiving penalty. UG4's proposed
observation map is not adoption of X3. Read the
[current handoff](../../reporting/rm9_current_handoff.md).


Date: 2026-10-02. Status: **Deferred extension hypotheses; no execution or model
adoption.** RM9-UG1.A remains Default; RM9-UG2.A was subsequently accepted for analytic review. Parent:
[current physical-law candidates](../../reporting/rm9_30_allocator_contract_and_control_chain.md).

## User interpretation and scope

The user proposed two major lanes, movement away from a short merging lane to
avoid merging traffic, position-dependent merging urgency near that lane's end,
and speed-dependent equivalent service consumption. The user regards these as
secondary extensions unnecessary for the current review and asks whether that
positioning is sound. Interpret "short lane" here as the finite acceleration/
merge lane connected to the ramp, and "near/far" as the adjacent and inner
mainline lanes. No ramp vehicle is assumed to jump across a nonadjacent lane.

The existing proposal already retains two physical mainline lanes. Retaining
those lanes is baseline scope; adding merge-aware avoidance is an extension of
the behavioral law. An explicitly spatially resolved short acceleration lane is
not already fixed by the proposal's generic conserved ramp-to-node path.

## Living extension inventory

All listed questions are review-global Type 2, because they change the physical
forward law, state or comparison/evidence contract. The reviewer supplies source
and analytic evidence; the user owns adoption. Source extraction and local
conservation derivations are dependent Type 1 evidence, not independent approval.

| ID | Status | Mechanism / model-chain change | Dependency and admission trigger |
|---|---|---|---|
| RM9-X1 | Deferred hypothesis | Merge-aware mainline redistribution: adjacent-lane traffic moves inward in response to anticipated ramp interaction, subject to target receiving and donor budgets | Closed baseline law/observer; review if density-only response misses anticipatory lane interaction or for a later rule-family robustness comparison |
| RM9-X2 | Deferred hypothesis | Explicit finite short-lane cells and increasing mandatory merging propensity near the lane end | Defined geometry/entry eligibility, ramp propagation/storage and observer support; review if merge-location/remaining-distance effects matter to the chosen task |
| RM9-X3 | Deferred hypothesis | Speed/relative-speed/acceleration-dependent disruption or equivalent service requirement, separate from allocation priority | Define necessary speed information/state and supported receiving-resource law; review if the claimed mechanism requires acceleration or capacity recovery |

The two-mainline-lane layout itself is already in UG2.A. More major lanes would
need a separate state-reduction and joint donor/receiver audit; the bounded
one-adjacent-target proof is not inherited automatically.

## Semantic contracts that must remain explicit

**X1:** Avoidance may respond to expected merging even before current densities
strongly differ. That differs from discretionary density equalization. It is
still autonomous traffic behavior under common open-loop metering, not a new
lane-change actuator. Do not relabel this mechanism as density-only response.

**X2:** Greater desire to merge near the end is not guaranteed successful entry.
Actual receiving, gaps if represented, and donor availability still constrain
accepted transfer. Traffic with no feasible merge remains accounted for at the
end/in queue; it cannot be forced through or deleted. Introducing distributed
merging across several interfaces requires one consistent geometry and budget
contract, rather than appending several independent entry nodes.

**X3:** A service requirement larger than one describes consumption of a receiving
resource, not additional physical traffic mass. Accepted traffic remains counted
once in conservation and total-time accounting. The allocation parameter a is
not that requirement. Specify whether reduced effective supply or weighted
service consumption represents a disruption; avoid counting the same effect in
both without justification. A blanket "slower always costs more" rule is not yet
established: speed difference relative to receiving traffic, acceleration,
spacing and congestion regime may be relevant.

Ordinary density-based first-order cells do not automatically retain acceleration
history. An extension must declare whether speed is a derived observation, a
new dynamic state or a class/mode parameter, then assess aggregate reconstruction
under the same strong-information fairness contract. Structural distance-to-end
is known geometry; it is not itself new hidden information, although the traffic
mass/speed distribution along that geometry may be omitted by an aggregate model.

## Inspected literature support and limits

- Existing **FB0030**, primary final PDF, printed 1764–1765, route/cooperation
  incentive sections: models lane-end urgency and mainline movement that
  facilitates merging. This supports a family-level antecedent for X1/X2;
  avoidance and courtesy need not have identical motivation or coefficients.
  Full source branch/coupling issues from RM9 remain unresolved. Do not directly
  adopt the printed functions as a validated conservative extension.
  [Primary lane-model PDF](https://repository.tudelft.nl/file/File_2c4359e7-5e5a-4651-964f-6f3610ab89ae).
- Existing **RM8-P01**, Laval/Cassidy/Daganzo, primary author-hosted chapter,
  Section 2 and merge tests: bounded-acceleration lane changers generate lost
  discharge through traffic-stream voids in its hybrid model. It supplies a
  mechanistic antecedent for X3, not proof of a universal per-ramp-vehicle
  service multiplier or a first-order speed-cost formula. The modeled site
  omits acceleration-lane length, so it does not establish X2's spatial law.
  [Primary merge-mechanism PDF](https://bpb-us-e1.wpmucdn.com/sites.gatech.edu/dist/f/3571/files/2023/03/merges.pdf).

Both sources and selected sections were rechecked in this discussion. Existing
IDs are reused, no new full-text archive or empirical gradient evidence added.
No new search query executed; direct primary open/find checks only.

## Suggested review placement and scientific interpretation

1. Resolve the existing UG2 baseline-law decision and transcribe the strong
   observer. Audit conservation/physical meaning, information reconstruction,
   action relevance and then the gradient chain. Do not assume a favorable result.
2. At baseline-result discussion, select extensions against an identified
   validity/mechanism gap, or as a declared robustness family. Keep X1/X2/X3
   separate so a behavior change is attributable. Tentative order is X1, then
   X2, then X3 if required; dependencies/actual findings can change this order.
3. If the restricted baseline is negative, report that scoped result. A deferred
   variant may be opened for a documented missing mechanism, not as an automatic
   way to manufacture positivity. If positive, inspect whether the distinction
   survives plausible alternative interaction rules and a sufficient scalar or
   strong aggregate-history reconstruction.

These mechanisms can be secondary to the current first analytic review while
being necessary later for a field-relevant acceleration-lane/capacity-recovery
claim. No claim of universal merge fidelity follows from deferral. In particular,
conservative shared budgets and lateral-first precedence still require physical
interpretation; adding a speed penalty does not retroactively validate them.

## Work record and next allowed action

Created this register; synchronized UG2.A/B candidate consequences, the active
inventory and handoff; archived the discussion. Commands: rg/cat/sed reads,
primary-source web open/find, Python standard-library document writes and local
link/status checks. No equations, PDF, source code, dependencies, simulations,
numerical gradients or approvals changed. Current task is positioning only.
The next allowed action remains discussion of the existing RM9-UG2 decision,
not execution of an extension or a new review stage.

## User-confirmed deferral — 2026-10-02

The user accepts the PDF handout and explicitly asks to stash these ideas as
agreed. X1–X3 remain Deferred hypotheses; none is an active requirement or an
approved physical law. Their record is retained here without git-stashing user
changes. The [UG2 acceptance](../../discussion/rm9_handout_acceptance_and_ug2_closure.md)
authorizes continuation of the restricted candidate, not extension execution.
Earlier next-action wording above describes the pre-acceptance discussion.

Current continuation: the accepted-kernel audit reached [UG3](../../reporting/rm9_40_accepted_kernel_findings_and_resource_gate.md)
on residual resource meaning. X1–X3 remain stashed/deferred; that gate neither
opens them nor converts their hypotheses to fixed traffic effects.

## Information-gap planning clarification — 2026-10-05

The [new discussion proposal](rm9_information_gap_review_plan_proposal.md)
positions physical merge geometry (IG-D2) and acceleration/readiness (IG-D3)
as possible evidence-led future directions related to X2/X3, with X1 only
where independently justified. These candidates remain Deferred; a negative
result for the present task does not automatically open them. Gap-aligned
release timing (IG-D4) is a separate proposed control task, not an approved
extension or the deferred multi-ramp Candidate C. RM9 remains open at UG4;
source-first versus idealized-first admission is still under discussion.
