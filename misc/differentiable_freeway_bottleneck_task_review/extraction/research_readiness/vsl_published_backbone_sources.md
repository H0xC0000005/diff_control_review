# Published-backbone assessment: references and source checks

**Follow-up, 2026-10-20.** The lane route is user-selected for qualification.
A subsequent source/hand-reference check turns the earlier budget cautions
into a concrete obstruction to direct transcription. The author's later
thesis also supplies a continuous receiving alternative and a three-to-two
case. Those selected readings and their limits are recorded separately;
the list below preserves what was actually viewed in the earlier pass.

[New source qualification and hand-check record](vsl_lane_backbone_source_audit.md)

Date: 2026-10-20. Primary-source assessment supporting the
[findings](../../reporting/research_readiness/vsl_published_backbone_findings.md).
This is the reference list for papers viewed in this pass, with full-method
reading distinguished from abstract/metadata access. Papers mentioned only
inside earlier review records are not represented as newly read.

## References and actual reading scope

**[1]** H.-Y. Jin and W.-L. Jin, “Control of a lane-drop bottleneck through
variable speed limits,” arXiv:1310.2658, 2013. The archived 31-page manuscript
is headed October 29, 2018; the arXiv record gives submission in 2013. These
dates are retained rather than assigning an unverified journal version.

[Primary full text](https://arxiv.org/html/1310.2658)

[Archived manuscript](../../archive/full_text/FB0001.pdf)

Reread §§2.1–2.2, equations 1–11; source control discussion; §5.3, equations
25–27 and cumulative-arrival/departure accounting; §6, equations 28–29.
The upstream point queue is **native to §5.3**, not a component we would need
to invent. The modeled link excludes explicit spatial dynamics in the VSL
and merging regions. Threshold discharge is discontinuous. The native
link-average/spatial pair motivates our proposed information experiment;
the source does not establish our equal-history or action/gradient witnesses.

**[2]** H. H. S. Nagalur Subraveti, V. L. Knoop, and B. van Arem, “First order
multi-lane traffic flow model – an incentive based macroscopic model to
represent lane change dynamics,” *Transportmetrica B: Transport Dynamics*,
vol. 7, no. 1, pp. 1758–1779, DOI: 10.1080/21680566.2019.1700846. Repository
and copyright year: 2019; article header: 2020. Preserve that discrepancy.

[Primary article](https://doi.org/10.1080/21680566.2019.1700846)

[Archived final article](../../archive/full_text/FB0030.pdf)

Reread local full-text PDF pp. 5–11 (printed 1760–1766), native A12 lane-drop
case and discussion/limitations. Source equations 1–4 give lane conservation
and grid/CFL assumptions; 6–11 give lateral incentives; 13–19 give demand,
receiving and capacity drop; 20–22 couple lateral and longitudinal flow.
Native field case is four-to-three, not our three-to-two geometry. Continuing
traffic can move to other lanes. Advice-response is explicitly omitted from
the calibrated congested case; field lane-density evidence is not VSL-control
or gradient validation.

**[3]** Y. Han, A. Hegyi, Y. Yuan, S. Hoogendoorn, M. Papageorgiou, and
C. Roncoli, “Resolving freeway jam waves by discrete first-order model-based
predictive control of variable speed limits,” *Transportation Research Part
C: Emerging Technologies*, vol. 77, pp. 405–420, 2017,
DOI: 10.1016/j.trc.2017.02.009.

[Primary accepted manuscript](https://pure.tudelft.nl/ws/files/45432235/AAM.pdf)

**Targeted extension of the shortlist:** read §§2.2–2.3, particularly the
VSL paragraph on manuscript p. 7; checked the control-actuation discussion.
The paper limits sending demand using displayed speed times density while
retaining its receiving formulation. Its optimizer chooses flows and converts
them to speed advice. Importing that demand restriction into [2] would be
our adaptation; its full jam-wave/capacity-drop model is not proposed as a
second complete traffic engine. No compatibility or derivative proof for
the combination is claimed.

**[4]** L. Wei, Y. Han, and M. Wang, “A first-order link-based flow model
with variable speed limits and capacity drops for freeway networks,”
*Computer-Aided Civil and Infrastructure Engineering*, vol. 40,
pp. 3200–3217, 2025, DOI: 10.1111/mice.13492.

[Publisher full text](https://onlinelibrary.wiley.com/doi/full/10.1111/mice.13492)

[Publisher PDF](https://onlinelibrary.wiley.com/doi/pdf/10.1111/mice.13492)

Reread §§1.2–2.1, Algorithm 1, equations 1–12, and the scope of §§3.2–3.3.
Entry-time/speed history is needed beyond the two current cumulative counts.
The sign acts on new entrants, with faster cohorts constrained by slower
predecessors. No individual lane-changing model is supplied. Source forward
comparisons do not establish derivative fidelity. HTML and PDF text access
succeeded; attempted PDF screenshots failed. No rendered-page certification
is claimed.

**[5]** M. Carey, C. Balijepalli, and D. Watling, “Extending the Cell
Transmission Model to Multiple Lanes and Lane-Changing,” *Networks and
Spatial Economics*, vol. 15, pp. 507–535, 2015,
DOI: 10.1007/s11067-013-9193-7. Earlier online/submitted version: 2013.

[Primary author-repository record](https://eprints.whiterose.ac.uk/id/eprint/77315/)

[Primary manuscript, retrieval failed this pass](https://eprints.whiterose.ac.uk/id/eprint/77315/7/Carey%20et%20al%202013_with_coversheet.pdf)

Current pass: institutional abstract/metadata and publisher preview only.
Full manuscript retrieval returned tool errors; do not label its methods
as newly reread. Detailed comparison reuses the prior full-method inspection
at manuscript pp. 5–12, R1/R2/R3 allocation and Algorithm A2, recorded in the
[B1 source audit](vsl_b1_source_and_interface_audit.md). That record supports
receiving/mandatory-transfer lineage, not complete native common-VSL
permanent-lane-drop clearance. Carey's earlier provisional principal-anchor
role is preserved.

**[6]** C. Roncoli, M. Papageorgiou, and I. Papamichail, “Traffic flow
optimisation in presence of vehicle automation and communication systems –
Part I: A first-order multi-lane model for motorway traffic,” *Transportation
Research Part C: Emerging Technologies*, vol. 57, pp. 241–259, 2015,
DOI: 10.1016/j.trc.2015.06.014.

[Primary publisher preview](https://www.sciencedirect.com/science/article/pii/S0968090X15002296)

**[7]** C. Roncoli, M. Papageorgiou, and I. Papamichail, “Traffic flow
optimisation in presence of vehicle automation and communication systems –
Part II: Optimal control for multi-lane motorways,” *Transportation Research
Part C: Emerging Technologies*, vol. 57, pp. 260–275, 2015,
DOI: 10.1016/j.trc.2015.05.011.

[Primary publisher preview](https://www.sciencedirect.com/science/article/pii/S0968090X15001977)

[6]–[7] were checked at abstract/introduction/available preview level during
the targeted search for native multilane VSL. They are credible alternative
leads, **not full-method-qualified candidates** in this bounded assessment.
The 2014 predecessor's controlled lateral flows must not be used to assert
that every behavior in the 2015 forward model is externally controlled.
This pass neither rules out a simpler native Roncoli route nor asserts that
the shortlisted lane candidate is globally best. No need to exhaust such
leads before presenting the task choice exposed by the approved shortlist.

## Decision-critical qualifications and our deductions

| Item | Source observation versus review deduction | Consequence |
|---|---|---|
| Jin population accounting | Source §5.3 supplies the upstream point queue and cumulative counts. | Finite releases and common clearance accounting are task specifications; upstream holding itself need not be a new traffic model. No source numerical result is treated as our own. |
| Jin information contrast | LWR uses a density profile and boundary states; the link queue uses average density. **Our deduction:** equal average density need not fix the boundary density. | A possible spatial-information question; no matched-history, different-action or gradient-usefulness certificate yet. |
| Jin derivatives | Source discharge, equation 5 or 9, jumps at its density threshold. | Regular-branch sensitivities do not alone cover threshold-crossing trajectories. A sensitivity/event contract remains work, without changing the forward law by default. |
| Lane/VSL interface | [2] uses the same sending demand in its lateral-demand calculation, equation 14. [3] supplies a VSL sending restriction. | Whether and how the capped demand propagates into lateral transfer and the existing discharge branch must be specified consistently. Adding advice directly to merge preferences or a second capacity-drop penalty is not justified by this component proposal. |
| Lane source cautions | [2] has empty-density denominators, a special equation-17 branch at theta = 1, and coupled donor/receiver budgets. | Exact zero/limit conventions, conservation, storage and lane-end clearance require qualification. The printed special branch differs from its limiting lower branch; do not repair, clip or smooth it here. |
| Wei timing derivative | Eligibility after Algorithm 1 is a binary distance test; equation 6 sums entry-time inflow increments using that test. **Our deduction:** fixed eligibility decisions carry no ordinary derivative of departure timing, while bin changes may jump. | This is a timing-path limitation, not a claim that all gradients vanish; speed-dependent capacity provides other paths. Interpolation/event reformulation would need explicit justification. |
| Wei transcription | Extracted HTML and publisher PDF text both show the old speed in both branches of equation 9, despite prose distinguishing old/new leaving cohorts. | Record a source/transcription ambiguity needing visual or author/source-code clarification. Screenshot access failed; no typographical repair or fully verified printed-equation claim is made. |

These checks identify what a future model qualification must settle; they
do not certify complete source algorithms or invalidate a publication's
forward evidence. No mathematical replacement, source correction, new full
paper archive, simulation, calibration or differentiation experiment was
created. The narrower source list supports the recommendation, not a
literature-wide novelty or absence claim.
