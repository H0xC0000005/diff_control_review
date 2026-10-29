# Feedback 6: homogeneous allocation, physical spillback and average service

26 October 2026. The central clarification is that **splitting one homogeneous incoming block among accessible lanes need not create an artificial order between its lane targets**. Your example supports joint allocation and admission of that block. My earlier `A.pieces`/`A.curve` presentation imposed a choice before establishing that the traffic model needed it.

I record the internal opening, queue-based perceived congestion, elapsed-rate lane service and receiving reuse as your selected directions. The corrections below concern their physical meaning and the remaining concrete formulation; they do not reopen the earlier principles batch.

[Separate note: remaining model questions and batch closure status](../../temp_content/research_readiness/remaining_lane_model_questions.md)

## Keep the opening inside the detailed zone

Agreed: the opening and the interacting bay/main-lane storage belong inside the near-intersection zone. `G.internal` is selected; `G.mouth` is rejected for the current formulation. The original example remains required behavior: through mass 0.4 precedes left mass 0.6 on a single physical feeder. If the through destination accepts only 0.2, that much enters and the remaining through mass prevents the later left block from reaching the otherwise vacant bay.

Your spillback statement is sound **when the queue actually occupies the common path upstream of the opening**. A bay-bound queue extending into a single common feeder can obstruct traffic going to either branch. No extra signal-order rule is needed at that opening.

One qualification matters: a downstream lane being full, or its queue merely reaching the opening, does not automatically close every other path. If the common feeder's current traffic can reach the other lane without passing a blocker, that lane can still accept it. Conversely, later traffic cannot use that room by passing a genuinely blocked front on the same feeder. Thus the condition is physical occupation/access at the common path, rather than a blanket “any branch full means all branches closed” flag. Independent feeder lanes retain independent access.

This distinction is consistent with the geometry-dependent blocking motivation of [Wright et al., *On node models for high-dimensional road networks*](https://arxiv.org/abs/1601.01054). That source motivates the qualification; its partial-FIFO coefficients are not adopted here.

The opening therefore needs spatial ownership, accessible paths, finite storage and causal propagation of congestion. It does not need an additional phase schedule. A branch departure frees upstream receiving according to the physical propagation law, not instantaneously throughout the feeder.

## Use perceived queue congestion without service-plan knowledge

I accept `L.queue` as the behavioral direction and set `L.work` aside for the current model. This is a clear information assumption: lane choice responds to congestion drivers perceive, without requiring knowledge of the average service allocation or a forecast of clearing time. We need not establish that service-aware reasoning never occurs in reality to justify this deliberately simpler model.

Your reference to approaching vehicles raises a small definition to make explicit. A congestion estimate can include visible or already committed approaching mass as well as the ready queue, without introducing a new microscopic motion model or predicting future arrivals. I provisionally retain the existing queue-plus-commitments estimate on that reading. Its exact visibility/counting window and normalization still need specifying. If you intend strictly stopped/service-ready traffic only, that would narrow the estimate; the underlying queue-based choice remains agreed either way.

Physical moving traffic still propagates in the existing backbone and counts toward TST. Omitting a forecast of its motion from the lane-choice cost does not remove that traffic from the simulator. Pending views and physical occupancy must also be counted once in the perceived backlog, rather than adding the same approaching mass twice.

The earlier [Gong, Bliemer and Raadsen lane-equilibrium source](https://doi.org/10.1016/j.trb.2025.103208) supplies conceptual precedent for allocating permitted flows jointly across lanes. Its decision concerns link-exit sending flows, so it does not establish our particular queue-entry cost, storage law or driver-information assumption.

## Your homogeneous example removes the artificial target-order choice

Take one new unit of homogeneous mass, legally able to use either lane. Initially the bay contains 0.2 and the other lane is empty. Assume equal queue-cost scales, both entrances physically accessible, and sufficient feeder sending. This is a static illustration in which receiving permits all available room and no tighter entry-rate/travel bound intervenes; storage alone would not guarantee those conditions in a dynamic step. “Capacity” here means **storage**, not saturation flow per second.

| Storage of each lane | Bay after admission | Other lane after admission | New mass remaining upstream |
|---|---|---|---|
| 1.0 | 0.6 | 0.6 | 0 |
| 0.5 | 0.5 | 0.5 | 0.2 |

The unrestricted equilibrium assigns 0.4 of the new mass toward the bay and 0.6 toward the other lane. In the second row the physical additions are 0.3 and 0.5. Both lanes fill; 0.2 remains upstream. There is no need to say “all newly bay-targeted pieces must go first” or the reverse. In this static example, the existing target totals and physical bounds are compatible with those admissions.

I therefore replace the required `A.pieces`/`A.curve` choice with **`A.joint`: joint splitting of the current homogeneous source block**. This names a transcription direction for your behavioral requirement, not a new principle to vote on. The allocator/admission law can return lane amounts together. A cumulative curve might eventually describe that result mathematically; it is not an additional traffic behavior that you must choose. Arbitrary packet cuts must not create a new blockage mechanism.

“Homogeneous” here means the same persistent route state, current movement, legal alternatives and applicable prior commitment. Different original route/movement blocks keep their source order; a later through block cannot pass an earlier obstructed left block merely because joint allocation is used. Once traffic occupies a realized lane, exact order within that lane remains. Previously fixed targets are not silently reassigned.

One distinction in your example remains important. I interpret “0.2 spilled back on the shared lane” as **0.2 physically waiting on the common upstream feeder**. It does not establish that all 0.2 is committed to the other destination lane. If the original intended amounts 0.4/0.6 were already frozen, the unadmitted target amounts are 0.1/0.1, both physically upstream. Making all 0.2 target the other lane would be a different allocation/commitment decision. Physical location and desired destination are separate.

Your example resolves the reason I introduced an artificial within-block order. It does not yet define the full dynamic operator: we still must specify partial admission when receiving changes, how frozen pending shares are retained, and compatibility with the existing single-target ingress records. Those are concrete formulation tasks. They need no invented within-block priority, no retargeting default and no relaxation of order between different source blocks. The precise assignment location in the internal feeder also remains a proposal; the example assumes a homogeneous block has reached an accessible fork.

## Use elapsed-rate service while preserving its intermediate constraints

`S.elapsed` is selected. The current resident head is served at its effective average rate; its service consumes elapsed time, and the next resident head can use the remaining time once exposed. Eligibility, lane capacity and receiving remain constraints. This directly expresses how fast the lane serves its ordered traffic.

The budget alternative can also enforce physical constraints, so skipping them is not an intrinsic defect of every budget formulation. The reason for your choice is the desired elapsed-rate meaning. The original hand comparison remains useful evidence that the two abstractions can give different departures under the same fractions. Neither comparison establishes empirical accuracy or useful gradients. `S.budget` is retained only as an unselected alternative.

## Reuse receiving without inventing phase order

`R.reuse` is selected. Average service does not prescribe “left phase first, through phase second,” and the model should not create such precedence through a lane-visiting loop. Another physically reachable head may use receiving room that the first cannot use, subject to its own average service and physical bounds. Receiving reuse does not transfer unused left-turn service to through traffic.

However, **no phase order does not mean no resource-sharing law**. Suppose two independent ready lanes each could send 0.8 into an exit with room for 1.0. Splits 0.5/0.5 and 0.2/0.8 both use all the receiving and respect the individual bounds. Reuse alone does not choose between them. A simultaneous sharing rule based on declared physical priorities or feasible demand is still needed; it need not represent anyone being served first in time.

Likewise, exact FIFO within an occupied shared lane remains a physical obstruction, not a signal schedule. The selected `S.elapsed` and `R.reuse` must be joined in one rule whose results do not depend on software traversal order. I retain that as a model-definition task rather than asking you to choose a numerical solver or invent priorities now.

[Updated concrete discussion](../../temp_content/research_readiness/coupled_lane_access_and_service_discussion.md)

[Decisions and remaining questions](../../temp_content/research_readiness/review_decisions.md)

## Supporting work record

Read feedback 6, repository review instructions/context/roadmap and the active discussion, decision, source and candidate records. A bounded primary check used Wright et al.'s arXiv abstract and the indexed primary publisher text for Gong et al.; the attempted author-hosted Wright PDF was inaccessible, so no full-paper verification is claimed. No new source equation or theorem is adopted. The numerical tables are conditional hand accounting, not experiments.

Edits synchronize this response, the active discussion/decision/guide/log, candidate inventory/source notes, overview/gap/completeness navigation and the existing mathematical companion's status and admission scope. Feedback is preserved except for the permitted `(answered)` heading marker. Root files, code/tests/configs, approved plans, historical records and previous validation results are not changed. Document checks and the PDF build are recorded after completion below. No package installation or traffic/gradient/optimization/SUMO run is performed.

The candidate source was compiled twice with the existing pdfTeX 1.40.25 / TeX Live 2023 toolchain, then the built PDF was copied beside its source:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_feedback6_latex_20261026 misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_coupled_lane_model_candidates.tex
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/urban_feedback6_check_20261026.py
git status --short
```

**Checks passed:** 132 local links/cited lines; all 15 question IDs and 34 high-level candidate definitions preserved; eleven named directions consistently covered; completeness/relationship/report-budget tables unchanged. The scoped 55-file snapshot has the twelve intended existing edits and 43 unchanged protected files; this response is the new artifact. The final six-page PDF matches the build output, has text on every page and has no LaTeX warnings or box issues. Existing pypdf checks text integrity; no new raster-inspection claim is made. The result is retained at `/tmp/urban_feedback6_check_20261026.json`. Git status still lists only the pre-existing tracked edits to `AGENTS.md`, `PLANS.md` and `memo.txt`.

[Updated mathematical companion](urban_coupled_lane_model_candidates.pdf)

[Retained LaTeX source](urban_coupled_lane_model_candidates.tex)
