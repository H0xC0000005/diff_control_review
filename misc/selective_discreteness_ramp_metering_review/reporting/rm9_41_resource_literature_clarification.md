# RM9.41 — Forward allowance and Candidate A's literature boundary

**Subsequent disposition:** [UG3.B approved](../discussion/rm9_resource_b_approval_and_continuation.md);
this gate is closed. The dated alternatives/evidence below are historical.
Current law and next gate: [RM9.50 / UG4](rm9_50_separate_resource_findings_and_observer_gate.md).


Date: 2026-10-02. Status: **UG3 discussion; neither A nor B newly approved.**
Parent: [resource gate](rm9_40_accepted_kernel_findings_and_resource_gate.md).

## Answer to the user's objection

The user questions why lateral arrivals cannot increase the recipient's forward
allowance, and asks whether A is literature-grounded. This is discussion, not
approval of B or withdrawal of the historical UG2 acceptance.

Forward allowance means permitted forward flow rate. Ordinary sending is an
occupancy- and speed-dependent traffic offer bounded by physical capacity, not
itself an independent physical service resource. More traffic can increase the
offer in uncapped free flow; realized flow need not increase if capacity or
downstream receiving already limits it. The lane's own receiving can decrease
as storage fills. These are distinct quantities. Lateral inflow is external to
the lane but internal to the road; neither fact requires the old sending cap.

## What the inspected literature supports

| Existing source | Inspected support | Limit for A |
|---|---|---|
| FB0030, Nagalur Subraveti/Knoop/van Arem | Printed 1765–1766, Eqs. 13, 20–22: ordinary sending is demand; modified sending adds lateral inflow and subtracts outflow. Eqs. 18–19 separately describe a capacity-drop extension. | Our recipient old-sending cap is not inherited from those equations. Full-source validation does not validate our changed coupling. |
| RM0018, Wright et al. | Section 3.1: input demands compete for downstream supply, with priorities and unused-supply allocation. | Supports the forward merge allocator, not a shared within-cell transverse/longitudinal budget. |
| RM8-P01, Laval/Cassidy/Daganzo | Section 2: bounded-acceleration lane changers introduce traffic-stream voids and reduce bottleneck discharge. | Mechanistic support for disruption, not a universal one-for-one debit for ordinary lateral transfer. |

Primary links: [FB0030](https://repository.tudelft.nl/file/File_2c4359e7-5e5a-4651-964f-6f3610ab89ae),
[RM0018](https://horowitz.me.berkeley.edu/Publications_files/All_papers_numbered/Wright_node_models_transportation_networks_Transportation_research_B_2017.pdf),
[RM8-P01](https://bpb-us-e1.wpmucdn.com/sites.gatech.edu/dist/f/3571/files/2023/03/merges.pdf).
Reused sources and selected sections, not an exhaustive search or a claim that
no supporting work exists anywhere.

## Strongest conditional rationale for retaining A

One possible abstraction allocates each step's movement opportunities only to
traffic eligible at its start. The donor divides its eligible traffic between
sideways and forward movement. A lane changer cannot also contribute to the
recipient's forward service during that update; it stays in storage and becomes
eligible later. This can explain the recipient cap as an explicit eligibility
or movement-service assumption.

This is a reviewer interpretation, not a sourced derivation of the exact kernel.
It needs a defensible relation between movement opportunities, cell length,
timestep and physical maneuver delay/interference. Demand is a rate offer, not
a count of such opportunities. Preventing duplicate mass use does not by itself
derive the rate subtraction. Saying arrivals wait until next step also does not
resolve the audit: its free-flow debit persists as timestep shrinks at fixed
cell state/length. It cannot simply be dismissed as a vanishing update lag.

**Pros:** A declared common movement budget is compact, conservative and
tractable for conditional information/sensitivity analysis.
**Cons:** Its exact service relation is an unvalidated hypothesis. A benefit
driven by that law cannot become physical evidence merely because other models
show lane-changing interference.
**Dependencies:** Specify and justify the resource/eligibility and cell/step
meaning before physical control-benefit claims; preserve strong observations
and full accounting. No extra speed-cost law is implied.

The adaptation was introduced to enforce conservative budget bounds. That was
its mathematical motivation, not physical validation. Earlier explanations
gave conservation too much weight as a reason for this particular coupling.

## Consequence for the pending choice

Retain A only for an explicitly conditional movement-exclusion/service study.
B remains provisionally recommended: recompute forward sending from the new
occupancy and retain actual capacity/receiving limits. B is also a reviewer
adaptation, not the full FB0030 model or proof that real lane changes are costless.
Any later acceleration/interference law needs its own evidence. X1–X3 remain
deferred. UG3 remains open; no accepted equation changes in this discussion.

## Work and verification record

Created this note and synchronized candidates, inventory, claim boundary,
handoff and dialogue. No formula/PDF change was needed for the semantic answer.
G1 geometry/observer, G3 exact-history/action and G4 gradient usefulness remain
incomplete. Next allowed action: UG3 discussion/decision.

Read-only inspection used `rg`, `cat`, `sed` and `git status --short`; primary
web open/find calls rechecked the three existing sources. Screenshot retrieval
failed; extracted primary text was checked, with no visual-verification claim.
No new search query/source/archive, implementation, experiment or environment
change. Existing CSVs and accepted PDF/TeX are preserved.

Document check command: `python /tmp/rm9_ug3_clarification_validate.py`.
It checks local links, CSV integrity/counts, accepted-PDF checksums and pending-gate
wording. Verification results are added after execution.

Verification passed with zero errors: six Markdown records, 41 local links,
11 existing queries, seven existing source/lead records, and both existing PDF
checksums unchanged. The accepted TeX sources were not edited. No scientific
numerical tests ran. One initial documentation patch failed its context check;
corrected the patch anchors and applied it without changing equations or scope.
