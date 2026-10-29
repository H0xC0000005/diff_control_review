# Lane-backbone qualification: sources and interpretation limits

**Continuation, 2026-10-21.** LF1 and H/LF2 are user-selected. The joined
candidate is now conditionally qualified for its declared elementary member
and delivered at JQ1. Its information, accounting and derivative results
are review deductions, not inherited native certificates. The original
source equations and deductions below remain unchanged; numerical/physical
validation is not established.

[Current joined-member provenance and assumptions](vsl_joined_candidate_sources_and_assumptions.md)

[Current congestion/VSL source check](vsl_congestion_join_sources_and_adaptations.md)

[Current allocator findings](../../reporting/research_readiness/vsl_allocator_findings_and_gate.md)

[Allocator references, reading depth and adaptations](vsl_allocator_sources_and_adaptations.md)

**Interpretation clarified by feedback 14, 2026-10-21.** The deductions below
obstruct unrestricted direct transcription, not limited source-backed
adaptation. They do not establish that replacing the backbone is preferable
to qualifying an allocator. The next review priority is allocation; no source
equation, deduction or evidence limit changes in this clarification.

[Current purpose and recommendation](../../reporting/research_readiness/vsl_feedback14_review_scope_and_allocator_response.md)

Date: 2026-10-20. Supports the
[decision-facing findings](../../reporting/research_readiness/vsl_lane_backbone_qualification.md)
and [hand-reference mathematics](../../synthesis/research_readiness/vsl_lane_backbone_flow_checks.pdf).
The prior shortlist's recommendation is now user-selected for qualification;
the underlying complete forward model has not been admitted.

## References and actual inspection

**[1]** H. H. S. Nagalur Subraveti, V. L. Knoop, and B. van Arem, “First
order multi-lane traffic flow model – an incentive based macroscopic model
to represent lane change dynamics,” *Transportmetrica B: Transport Dynamics*,
vol. 7, no. 1, pp. 1758–1779, DOI: 10.1080/21680566.2019.1700846.
Repository/copyright 2019; article header 2020, preserved.

[Primary article](https://doi.org/10.1080/21680566.2019.1700846)

[Existing archived final PDF](../../archive/full_text/FB0030.pdf)

Reread PDF pp. 5–11, printed 1760–1766: conservation 1–4; incentives 6–11;
demand/receiving and lateral realization 13–17; capacity-drop mode 18–19;
adjusted forward flows 20–22. The physical checks reproduce these rules,
not a guessed author implementation. No code, normalization or simultaneous
allocation algorithm was recovered from the selected source material.
Institutional article metadata was opened; current publisher access failed.
Existing local PDF text remains the primary equation evidence.

**[2]** H. H. S. Nagalur Subraveti, *Lane-specific Traffic Flow Control*,
Ph.D. dissertation, Delft University of Technology, TRAIL Thesis Series
T2021/13, 2021, DOI: 10.4233/uuid:e405a549-b1fe-4fa1-8090-4429612359d9.

[Primary institutional record](https://repository.tudelft.nl/record/uuid:e405a549-b1fe-4fa1-8090-4429612359d9)

[Institutional PDF used](https://pure.tudelft.nl/ws/portalfiles/portal/87432341/Lane_specific_Traffic_Flow_Control_Repository.pdf)

Downloaded to `/tmp/vsl_lane_backbone_qualification/` after the browser
rejected the large PDF and an un-escalated shell fetch failed DNS. The
requested minimal network escalation succeeded. This is source reading,
not a dependency or repository archive addition. The PDF contains 189 pages;
**selected methods were read**, not the entire dissertation. Extracted the
text and searched for allocation/normalization/code clarification.

Inspected chapter 3, PDF pp. 39–45 (printed 26–32), especially equations
3.6–3.9, 3.13–3.17 and 3.20–3.22; chapter 4, PDF pp. 64–65 (printed 51–52),
equations 4.4–4.11 and the three-to-two scenario paragraph. Chapter 3 repeats
the original receiving-adjustment sign and special receiving branch. Chapter
4 presents a continuous receiving multiplier with its unrestricted case at
theta = 0; it also supplies lookahead weights 2:2:1 and a native three-to-two
case. These are useful same-author source clarifications. They do not supply
the missing joint flow allocation in the inspected summary. No statement
that chapter 4 is an official erratum to [1] was found or inferred.

The hand checks use bounds valid for any convex lookahead weights, avoiding
dependence on adopting chapter 4's particular weights. No ramp task or ramp
construction is reopened by reading this dissertation.

**[3]** Y. Han, A. Hegyi, Y. Yuan, S. Hoogendoorn, M. Papageorgiou, and
C. Roncoli, “Resolving freeway jam waves by discrete first-order model-based
predictive control of variable speed limits,” *Transportation Research Part
C: Emerging Technologies*, vol. 77, pp. 405–420, 2017,
DOI: 10.1016/j.trc.2017.02.009.

[Primary accepted manuscript](https://pure.tudelft.nl/ws/files/45432235/AAM.pdf)

Rechecked §2.3, manuscript p. 7, the displayed-speed sending restriction and
its conversion from optimized flows. It is an actuation component, not a
replacement lateral/longitudinal allocator. Native receiving and capacity-drop
rules are not imported wholesale. The joined lane/VSL law remains open.

**[4]** C. Roncoli, M. Papageorgiou, and I. Papamichail, “Traffic flow
optimisation in presence of vehicle automation and communication systems –
Part I: A first-order multi-lane model for motorway traffic,” *Transportation
Research Part C: Emerging Technologies*, vol. 57, pp. 241–259, 2015,
DOI: 10.1016/j.trc.2015.06.014.

[Primary publisher preview](https://www.sciencedirect.com/science/article/pii/S0968090X15002296)

Current search returned abstract/metadata; no full-method qualification is
claimed. The earlier 2014 controlled-flow predecessor does not establish all
semantics of this 2015 forward model. It is a backtracking candidate only.

**[5]** H. H. S. Nagalur Subraveti, V. L. Knoop, and B. van Arem,
“Multi-lane Traffic Flow Model: Speed Versus Density Difference as Lane
Change Incentive and Effect of Lateral Flow Transfer on Traffic Flow
Variables,” in *Traffic and Granular Flow 2019*, Springer Proceedings in
Physics, vol. 252, pp. 547–553, 2020,
DOI: 10.1007/978-3-030-55973-1_67.

[Primary institutional PDF](https://repository.tudelft.nl/file/File_ee0df66b-7f68-4639-b1d8-f782bbecc9b3)

Read §67.3 and its two-step transfer description while looking for clarification.
This brief summary confirms the transfer philosophy; it does not give the
joint budget or receiving-adjustment resolution needed by the hand checks.

**[6]** H. H. S. Nagalur Subraveti, V. L. Knoop, and B. van Arem, “Improving
Traffic Flow Efficiency at Motorway Lane Drops by Influencing Lateral
Flows,” *Transportation Research Record*, 2020,
DOI: 10.1177/0361198120948055.

[Primary publisher full-text page](https://journals.sagepub.com/doi/full/10.1177/0361198120948055)

Opened to identify the source of thesis chapter 4; detailed evidence here is
from the selected thesis pages above. No separate complete-algorithm reading,
controller adoption or reproduction is claimed.

## What the mathematics establishes

The diagnostics are review-created exact-arithmetic examples, not source
case results or fitted parameter choices. All tested densities are strictly
positive and below jam storage; the first check uses one lateral direction,
and both avoid the disputed full-receiver branch. Densities rise downstream,
so the stated source discharging-mode condition is inactive at the cells
needed for the examples. No rollout or random sampling is performed.

| Check | Conclusion | Boundary of the conclusion |
|---|---|---|
| Printed receiving adjustment, equations 21–22 / 3.21–3.22 | A permitted lateral departure can make adjusted receiving negative, forcing negative forward flow under the printed minimum. | Refutes unrestricted direct transcription of these equations. Does not certify or falsify an unobserved author implementation. |
| Two lateral desires from one donor | The pairwise rules can request more than the common sending budget. Summing residuals yields a negative forward demand. | A source rule selecting one direction or allocating both could resolve this, but must be recovered or specified rather than assumed. |
| Later receiving multiplier | A continuous, space-respecting alternative occurs in the author's later chapter. | An exact source-version change to record, not evidence that all original flow equations are thereby repaired. |
| Han sending cap | Provides a plausible control interface but no shared allocator. | Not an admissible joined VSL model or a numerical-gradient result. |

Clipping, changing the receiving sign, restricting to one transfer direction
or adding priorities would alter the forward contract. No such repair is
made. First assess source clarification or a qualified allocator. Backtracking
remains available if that assessment reveals a substantive problem; no current
finding proves that a small allocator adaptation is infeasible.
