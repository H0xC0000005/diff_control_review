# Feedback 7 amendment: ordered packets, local lane balancing

26 October 2026. **The amendment resolves the remaining point.** You explicitly withdraw the frozen-starting-queue decision. The selected direction is now: process source packets in order, balance each packet across its legal lanes, and let later packets see the load assigned by earlier ones. This needs no global joint allocation of heterogeneous packets.

## What is agreed

For each homogeneous packet, project its current movement and identify its legal lanes. Use the queue-load estimate present when that packet is processed. Distribute its continuous mass to balance the eligible lanes as far as feasible, then add those assigned amounts to the estimate used by the next packet. Earlier committed waiting amounts must not disappear from that estimate merely because they are not yet physically inside the target lane.

With starting bay/other loads 0.2/0 and one new unit, equal-load balancing gives intended additions 0.4/0.6. This can be calculated for that packet in one operation. **Sequential across packets and simultaneous amounts within one packet are compatible.** My earlier word “joint” blurred those two levels.

“Perfect equality” needs one small qualification: adding new traffic cannot always equalize all lanes without moving existing traffic. If the same starting queues receive only 0.1, it all goes toward the empty lane, leaving loads 0.2/0.1. The intended rule is to fill the shortest queues up to the next queue level, then share further mass among the tied shortest lanes. No existing commitment is reassigned to manufacture equality. This description concerns matched legal alternatives; physical room, access and travel eligibility still determine actual entry separately.

When a packet's mass enters several lanes, append its children to each lane's ordered record in the parent source order. Later packets append after earlier ones in that lane. Logical assignment may proceed while mass waits, but physical admission cannot pass a genuine blocker on a common feeder. Pending records are views of physical upstream mass, counted once. No artificial order between the new targets inside one homogeneous parent packet is needed.

The ideal first version introduces no extra desired-lane preference. The imperfect preferences you mention remain deferred. A preference model might still admit a batch calculation; there is no need to decide that future algorithm now.

## Current movement is enough for the grid and allocation, while routes survive in the ledger

Your separation is appropriate if “route is not important” refers to the allocation criterion and movement grid. Those can use current movement without duplicating complete future paths. The existing route-table reference and route position must still survive in the ordered ledger and be carried by emitted packets.

For example, two packets can both go through this intersection but turn in different directions at the next one. Their grid contributions can share the same current-movement label; their future route identities cannot be discarded or reconstructed arbitrarily at discharge. Likewise, a movement-composition bin alone cannot recreate exact FIFO order. Emission consumes the retained ordered metadata, consistent with [the established route/grid distinction](../../../../context_snapshots/diff_minimal_meso/PROJECT_CONTEXT.md#L127).

## Equal lane loads do not by themselves justify collapsing the lanes

Your multiplied-capacity interpretation is a useful symmetric limit: identical permissions, propagation/storage, service, access and corresponding ordered states can make balanced parallel lanes behave like the matched aggregate model. It is an expected equivalence case, not a reason to abandon the per-lane representation.

Equal queue totals alone are insufficient. Two shared lanes can have the same mass but different front movements. If one has a left-turn head with zero effective service and the other has a serviceable through head, the second can discharge independently. A single FIFO lane with doubled capacity does not generally preserve those two heads. Bay length, accessibility and unequal residual storage also break the simple collapse. The current urban study retains those distinctions where present.

## Differentiability and current status

The continuous queue-balancing calculation can be piecewise differentiable. For fixed packet order, legal sets and active constraints, its additions, splits and min/max operations admit ordinary local sensitivities. Changes in which lanes receive mass or which constraints bind can produce kinks. Thus the presence of min operations is compatible with differentiation, but it does not establish differentiability at every point, correctness of a particular implementation or useful control gradients.

**No additional question remains in this batch.** Sequential packet processing with per-packet continuous balancing is now the selected direction. The route, symmetry and differentiability qualifications above preserve existing invariants; they do not open another choice round. The current batch is ready for explicit user closure. No next batch, implementation, new preference model or experiment is opened.

[Updated decisions](../../temp_content/research_readiness/review_decisions.md)

[Current lane-model discussion](../../temp_content/research_readiness/coupled_lane_access_and_service_discussion.md)

## Supporting work record

Read the amended feedback 7, the earlier point explanation and current decisions/candidates/source records, and `PROJECT_CONTEXT.md` §§5.2–5.5. This response defines the agreed traffic meaning without adopting a new external equation. Its examples are hand accounting and invariant checks; no simulation or numerical gradient evidence is claimed.

This is a separate amendment response. Live proposal, inventory, decisions, source and navigation are synchronized. The two old question notes and original feedback-7 response receive historical/navigation notices only. The mathematical companion receives a current-status correction, with displayed equations retained as earlier prototypes rather than silently reapproved normalized costs. The feedback inbox is preserved except for its answered heading marker. Root files, code/tests/configs, approved plans, earlier scientific answers and prior validation results remain unchanged. Exact results of the document checks and status-only PDF build follow below when complete.

The existing companion source/PDF pair remains at `reporting/research_readiness/urban_coupled_lane_model_candidates.tex` and `reporting/research_readiness/urban_coupled_lane_model_candidates.pdf`. Two passes with pdfTeX 1.40.25 / TeX Live 2023 build the status correction:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_feedback7_amendment_latex_20261026 misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_coupled_lane_model_candidates.tex
```

Scoped Python/pypdf and exact-fraction hand checks passed: 156 local links; all 15 question IDs, 34 high-level candidate definitions and eleven named directions retained; completeness tables, displayed equations and the original feedback-7 scientific answer body unchanged. The 103-file snapshot accounts for fifteen intended existing edits, 88 unchanged files and this one new response. The final six-page PDF matches its build, has text on every page and has no LaTeX warnings/box issues; no raster inspection is claimed. The result is `/tmp/urban_feedback7_amendment_check_20261026.json`. Read-only `git status --short` still lists only pre-existing tracked edits to `AGENTS.md`, `PLANS.md` and `memo.txt`. No traffic/gradient acceptance test is run, and the full model's later construction remains separate.
