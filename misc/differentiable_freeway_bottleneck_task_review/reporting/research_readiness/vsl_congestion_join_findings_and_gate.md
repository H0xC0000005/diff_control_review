# The speed limit fits; the congestion sending-cap interpretation needs a decision

**Later user decision and result, 2026-10-21.** H is selected and LF2 is
closed. The remaining qualification is complete for the declared elementary
member at JQ1. The interpretation comparison below is retained as delivered;
its open-decision wording is historical. The original mathematical note
and diagnosis are unchanged, and neither old report nor source code is rewritten.

[H selection and exact scope](vsl_congestion_selection.md)

[Current joined-candidate findings and checkpoint](vsl_joined_candidate_findings_and_checkpoint.md)

2026-10-21. **LF1 selected and closed. The next interface check has reached
LF2, a new consequential choice. Full replacement qualification is incomplete.**

The selected behavior is now fixed for this continuation: traffic attempts
to change lanes, can continue in its current lane if the attempt fails and
forward space remains, and must merge or wait at E's actual end. This pass
checks what traffic and receiving budgets feed that allocator. It does not
reopen the lane-changing principle or return to backbone selection.

## The traffic meaning of the result

There are two different limits on a cell's departures. **The speed advice
limits how quickly its present traffic can advance. Congestion can impose a
lower service ceiling even when enough traffic is present.** Han's VSL rule
fits this structure: use the smaller of advice times density and the
congestion-dependent ceiling. Receiving space and the allocator's fixed
priorities do not acquire a separate direct dependence on the advice. [2]

The source check also explains how receiving can remain endogenous. For a
receiving A cell, its allowance depends on its own density and the preceding
A cell's density. E and A then compete for that one allowance. Joining E
traffic changes subsequent A states and hence later service. The rule uses
traffic already in the plant, rather than an externally supplied receiving
schedule. It does not independently impose the old model's slow-entry
recovery penalty. [1]–[3]

**The unresolved part is when the congestion sending ceiling applies.**
Subraveti's short summary says to use the modified demand and supply while
density decreases from the sending cell to the next cell, and ordinary CTM
otherwise. Taken literally for demand as well as receiving, this makes the
congestion ceiling disappear when the cell ahead becomes just slightly
denser. The cited original Han formulation keeps a cell's reduced ceiling
when its upstream neighbor is congested; it does not add that switch based
on the cell ahead. [1]–[3] A cell can still be fed by a dense queue behind it
even if density increases slightly between it and the next cell. That is
why the two interpretations need not describe the same service.

This difference is not a numerical tolerance. It can change realized flow,
lane-changing requests and sensitivities. The principal paper explicitly
refers to Han for the full formulation, but we found no author clarification
establishing which interpretation its implementation uses. The later thesis
repeats the summary. We should therefore select the completed law openly.

## A small example shows why it matters

Consider three consecutive cells in one lane. The first is jammed; the middle
cell has density 40 vehicles/km. The last is almost equally dense: either
39.9 or 40.1. Use the same illustrative fundamental diagram as the preceding
hand checks and the source's illustrative 10% maximum capacity drop.
Advice is 60 km/h, so the speed cap does not hide the issue.

| Sending-cap interpretation | Cell ahead at 39.9 | Cell ahead at 40.1 | What changed? |
|---|---:|---:|---|
| **G: mode-gated completion of the principal summary** | 2,025 veh/h | 2,198 veh/h | The receiving queue grew slightly, but the sending ceiling switched off. |
| **H: complete Han congestion budget, recommended** | 2,025 veh/h | 2,025 veh/h | The jammed upstream cell still determines the middle cell's reduced ceiling. |

As the two last densities approach 40 from either side, G's flow difference
approaches 175 veh/h. H has no corresponding jump in this example. The
mathematical note gives the source indexing and exact calculation. This is
a static one-lane reduction used to check the interface, not a traffic
trajectory, calibrated task result or claim about the authors' actual code.

## The two viable completions

**G — keep a distinct recovery mode as the principal summary states.**
Use the reduced sending ceiling while the sending cell is at least as dense
as its same-lane successor. Otherwise use ordinary sending. The receiving
formula and missing constants are completed from the cited Han source.
At the last E cell there is no same-lane successor; G additionally needs an
endpoint convention. The concrete candidate treats that compulsory merge
as having the reduced-ceiling mode enabled.

Its philosophy is that the extra sending restriction belongs specifically
to a density-decreasing recovery configuration. In the example, traffic
leaves that mode as soon as the cell ahead is denser, so the ceiling changes.
No new memory state is required, but a discrete mode boundary becomes part
of the traffic law.

**Pros.** It retains the literal joint demand/supply mode sentence in the
principal paper. It gives congestion recovery a distinct status and could
serve a study that deliberately wants that mode-sensitive law.

**Cons.** Its extra sending switch is not present in the cited complete Han
formulation. It can introduce the abrupt service change above, and requires
an E-end convention. A conservation proof still holds, but gradient checks
crossing the new jump need an explicit discontinuous-model interpretation.
The inspected sources do not establish that this jump is an intended traffic
effect. G is an explicit completion of an ambiguous summary, not a certified
transcription of author code.

**H — use the full congestion budget from the already cited Han lineage.**
Each cell's ceiling depends on the preceding same-lane cell's congestion.
Its sending budget is the smaller of that ceiling and advice times its own
density. Its receiving allowance uses the full recovery-sensitive supply
rule, then all competing movements share that allowance through the already
selected allocator. No downstream density-order switch turns its sending
ceiling off. E's sending budget remains defined at its end because its
preceding E cell still exists.

Its philosophy is that congestion determines available service, while the
flow allocator decides which movements obtain it. It keeps the information
needed to distinguish a congested adjacent lane from a free one without
adding driver records or a second recovery mechanism.

**Pros.** The complete equations and constants can be traced to Han 2016;
Han 2017 supplies the consistent VSL extension. On a common fundamental
diagram they are continuous in the density inputs and satisfy the allocator's
sending, receiving and storage bounds. This removes the sending jump shown
above and avoids an extra E-end mode convention.

**Cons.** Selecting H explicitly supersedes the literal demand-gating reading
of the principal summary. It retains a phenomenological capacity-drop law,
not a calibrated explanation of every slow merge. The proof here covers a
common fundamental diagram; heterogeneous lane parameters need the source's
state-mapping treatment or a further qualification. Continuous budget maps
do not make the entire lane-incentive model smooth or establish useful
gradients.

**Provisional recommendation: H.** This is completion of an existing
congestion-model lineage, with VSL from the same supporting work already
under consideration. It does not add a new traffic mechanism or replace the
selected lane-change allocator. The reason is the explicit source formulation
and the avoided unexplained sending jump, rather than a preference for a
smoother optimization problem at any cost.

## What this establishes, and what remains

| Review question | Direct answer |
|---|---|
| **Does VSL fit the selected allocator?** | Yes, conditionally: advice caps donor sending; the same amount feeds forward and lateral requests. Cells, receiving physics and priority weights stay fixed. |
| **Can congestion-dependent receiving satisfy storage protection?** | Yes for the inspected common-FD Han closure. Its receiving allowance is nonnegative and no greater than the ordinary backward-wave space bound. Under the fixed time-step conditions, the selected allocator's earlier proof applies. |
| **Whose state defines the shared receiver?** | A's receiving allowance uses the preceding A cell and the receiving A cell. All arrivals share it once. It is not independently recomputed for E and A, nor automatically defined by the worst donor. This follows the principal lane indexing and the original source's mainline/shared-supply construction. |
| **Does this recreate the old forced-point recovery model?** | No. Congestion loss acts through the chosen cell-state law and shared service. An additional penalty from E's speed mismatch is not established or added. |
| **Are the joined congestion equations selected?** | No. The sending-mode interpretation is LF2. H is fully specified and conditionally checked on paper, but remains a recommendation. |
| **Is the complete replacement task ready?** | No. After LF2, finish the information witness/observability comparison, full population-time accounting and whole-model derivative contract under the selected law. No positive information gain, useful gradient or interior optimum is assumed. |

The principal model still supplies the lane-density/incentive framework.
Carey/Wright support the selected allocation component. Han already belongs
to the principal model's congestion lineage and supplies the VSL restriction;
H would make that budget component explicit rather than add another
independent engine. The resulting stack still requires qualification as a
whole. Citation count alone does not settle its simplicity.

**LF2 is Type 2 and user-owned:** whether to retain G's mode-gated sending
or use H's complete congestion budget. It affects flow requests, compulsory
merging and sensitivity, so it cannot be inferred as a source-notation fix.
LF1 stays closed. The present pass stops at this new methodological choice;
it does not claim the full interface stage or replacement task is closed.
The accepted report, closed VSL Step 4, closed ramp line and urban work are
unchanged. No simulator code or traffic experiment is involved.

[LF1 decision and exact approval scope](vsl_allocator_selection.md)

[Source equations, conditional bounds and exact hand case, PDF](../../synthesis/research_readiness/vsl_congestion_join_contract_and_checks.pdf)

[References actually inspected and source/adaptation boundaries](../../extraction/research_readiness/vsl_congestion_join_sources_and_adaptations.md)

[Work and verification record](vsl_congestion_join_work_report.md)
