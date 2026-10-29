# BP-R Stage 3 — selected upstream-admission interface

Date: 2026-10-06. **S3-G2-M.A approved; local boundary/accounting transcription.**
Source continuum–particle CM/local IT laws are now read; the mandatory merge
allocation is approved as S3-G2-N.A. See [supplied-original audit](../../../extraction/rm12/bp_r_stage3/supplied_originals_audit.md)
and the [post-priority joined-contract audit](joined_contract_and_reduction_audit.md).
The [PDF companion](accounting_and_reference_contract.pdf) gives the mathematical
accounting and selected release interface; its TeX source is retained beside it.

## Semantic task and data flow

Choose one common bounded open-loop ramp-rate schedule. Offered arrivals are
fixed across schedules. Unadmitted ramp traffic waits in a counted inventory;
admitted traffic travels through a finite KW approach. At its downstream end,
available ramp traffic competes with mainline traffic for receiving. Actual
entry generates the selected source family's accelerating disturbances.
Evaluate the complete inventory area, including upstream waiting, until clearance.

The rate grants permission to the **entrance of the approach**. It neither
sets instantaneous freeway entry nor commands a merge speed, lane change, gap,
priority or total freeway capacity. A ramp with stored traffic can therefore
have merge entry above the contemporaneous upstream permission. This is causal
release of already admitted mass, not violation of the meter cap.

## State, units and common inputs

| Item | Meaning and units | Contract |
|---|---|---|
| External waiting | Continuous vehicle-equivalent mass awaiting approach admission | Separate from ramp and road inventory; never deleted when receiving is exhausted |
| Ramp approach | Spatial continuous lane mass/density on a declared finite length | Longitudinal KW/CTM sending and receiving; storage from geometry and jam density; not a featureless queue |
| Mainline | Spatial per-lane continuous mass/density in the local source domain | Conservative transport and paired lane transfers; finite receiving |
| Disturbance descriptors | Source trajectory/event metadata: position, speed, target lane and history as required | Not an additional population counted on top of fluid mass; source field counts traffic; conservative event insertion/coupling still to transcribe |
| Rate, admission and entry | Vehicle equivalents per second; these are three different quantities | Only rate is optimized; admission and entry follow availability, propagation and receiving |
| Public physical input | Common initial traffic, disturbance state/progress, parameters and offered forcing | Each reduction receives its declared projection and memory; no future-reference correction or per-test fitting |
| Objective | Vehicle-equivalent seconds, optionally divided by common finite population | Same offered arrivals and complete waiting accounting in every model |

Exact geometry, discretization and parameter values remain task settings to
document after the qualified law. A declared finite spatial domain is required;
field reconstruction and a new acceleration lane are not selected. Extra lanes
cannot be added to manufacture information loss. A source-grounded geometry
must be used consistently by the reference and all reductions.

## Conservative release and update order

For a reviewable time-bin transcription, declared offered mass in the bin plus
previous waiting is available to the entrance. Actual admitted mass is the
minimum of that amount, the bin's rate permission and approach receiving.
This is a work-conserving transcription of the approved cap/availability
contract, not a physical red/green launch model. All rates and available amounts
are evaluated under one explicit common time-index convention.

Debit actual admission once from waiting and credit it once to the approach.
Compute source-compatible longitudinal, lateral and merge transfers from the
current road/ramp state, respecting available mass and finite receiving.
Apply each internal transfer with paired debit/credit, and count sink exits.
Advance coupled source trajectories and events consistently with those actual
transfers. Exact source allocation/event timing is the remaining E1/C obligation;
this ordering is an accounting interface, not a newly selected source solver.

Keep the offered-arrival, actual-admission, actual-entry and final-exit histories
separately inspectable. Disturbance creation follows actual transfer rather
than permission or offered demand. No speed is assigned merely because a rate
is low, and physical meter startup is not inferred from an aggregate queue.

After finite offered arrivals and the decision horizon, all models share one
declared positive draining policy and remaining boundary forcing. Clearance
requires a supported emptying or convergent-tail argument under the eventual
law; finite demand and positive permission alone do not prove all traffic clears.

## Strong independent comparisons and their obligations

All reductions share this physical action, geometry, population and objective.
Model-specific prediction may differ, but no comparator may move its meter to
the merge, drop external waiting or replay the reference's future flows.

| Reduction role | Public initial projection | Independent response that must be specified |
|---|---|---|
| Spatial first-order lane traffic | Spatial lane/ramp mass and external waiting | Own conservative sending/receiving/node flows; an inactive-disturbance equivalence control, not the sole strong active comparator |
| Congestion/entry memory | Same spatial state plus public queue/regime and qualified entry-speed memory | Own source-supported evolution under admission and merge events; no future queue/speed oracle |
| Speed/disturbance moments | Spatial state plus supported initial distribution statistics | Own transport, aging and entry-driven statistic closure; mean-capacity matching alone is insufficient |
| Selective trajectory/state | Declared subset/coarsening of public disturbance state | Own constrained evolution; ablate retained features with common action/accounting, without assuming full identity is necessary |

Lane state may be retained by any qualified aggregate competitor. The study is
about the information needed for intervention response, not forcing lane-blind
models or requiring an ideal-history ambiguity theorem. Comparator roles and
access obligations are explicit; exact dynamic closures cannot yet be frozen
while the reference law is unqualified.

## Static limits and current acceptance

- The release balance conserves continuous mass and cannot admit more than
  available traffic, permission or receiving. No integerization occurs.
- Upstream action affects already admitted traffic only through subsequent
  physical interactions; instantaneous merge flow is not capped by that action.
- Without binding disturbances, qualified reductions must recover matched
  underlying traffic behavior. Artificially retained disruption fails this limit.
- Identical complete exits imply identical TST despite different queue locations.
- Reference regime evidence does not prove useful rate gradients, irreducible
  hidden state or failure of qualified compact competitors.

Boundary selection and local accounting are complete. The joined source law,
specific compact closures and clearing/control response remain partial; the
bounded continuation now awaits [S3-G3 disposition](../../../reporting/rm12/bp_r_stage3/post_priority_findings_and_disposition.md).
See [supplied-original qualification](../../../extraction/rm12/bp_r_stage3/supplied_originals_audit.md)
and [current merge-allocation gate](../../../reporting/rm12/bp_r_stage3/merge_allocation_gate.md).
