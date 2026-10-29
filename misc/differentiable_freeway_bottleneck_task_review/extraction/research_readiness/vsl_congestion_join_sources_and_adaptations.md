# Congestion/VSL join: inspected references and interpretation limits

**Later status, 2026-10-21.** The user selects H and closes LF2. The source
interpretation evidence below is retained; candidate G remains unselected.
Subsequent qualifications and explicit member conventions are recorded separately.

[Joined-member sources and global assumptions](vsl_joined_candidate_sources_and_assumptions.md)

[H selection](../../reporting/research_readiness/vsl_congestion_selection.md)

Original pass, 2026-10-21. This pass reuses the accepted allocator evidence and makes one
targeted full-method extension to its principal model's cited congestion
ancestor. It does not select another backbone or introduce a second recovery
mechanism. At delivery, candidate closures remained subject to LF2.

**[1]** H. H. S. Nagalur Subraveti, V. L. Knoop, and B. van Arem, “First
order multi-lane traffic flow model – an incentive based macroscopic model
to represent lane change dynamics,” *Transportmetrica B: Transport Dynamics*,
vol. 7, no. 1, pp. 1758–1779, doi: 10.1080/21680566.2019.1700846.
Repository/copyright 2019; article header 2020, retained as previously noted.

[Archived final university PDF](../../archive/full_text/FB0030.pdf)

Reread PDF pp. 6–11, especially printed 1761–1762 (same-cell versus diagonal
transport motivation) and 1765–1766 (demand, receiving, capacity drop and
the joint discharging-mode sentence). Equations 18–19 are a short summary
explicitly referring to Han 2016 for detail. Their receiving branches,
primed critical-density coefficient and sending index require care. The
new example isolates a literal application of their mode sentence to demand;
it does not establish the authors' intended algorithm or unseen code.

**[2]** Y. Han, A. Hegyi, Y. Yuan, S. Hoogendoorn, M. Papageorgiou, and
C. Roncoli, “Resolving freeway jam waves by discrete first-order model-based
predictive control of variable speed limits,” *Transportation Research Part C:
Emerging Technologies*, vol. 77, pp. 405–420, 2017,
doi: 10.1016/j.trc.2017.02.009.

[Primary accepted manuscript](https://pure.tudelft.nl/ws/files/45432235/AAM.pdf)

Extended the earlier sending-cap reading to §2.3's full budget description,
PDF pp. 6–9 (manuscript pp. 5–8), equations 5–10 and the VSL paragraph/Fig. 5.
The ceiling is capped by nominal capacity and depends on the preceding cell;
VSL changes sending. The common-FD min-form in our note is a reindexed
translation, not a separate new empirical model. Source screenshots failed;
the mathematical reading uses the primary PDF's extracted text and equations.

**[3]** Y. Han, Y. Yuan, A. Hegyi, and S. P. Hoogendoorn, “New extended
discrete first-order model to reproduce propagation of jam waves,”
*Transportation Research Record*, vol. 2560, pp. 108–118, 2016,
doi: 10.3141/2560-12.

[Primary institutional accepted manuscript](https://pure.tudelft.nl/ws/files/10502816/New_Extended_Discrete_First_Order_Model_to_Reproduce_Propagation_of_Jam_Waves_TRR.pdf)

[Publisher record](https://journals.sagepub.com/doi/10.3141/2560-12)

New targeted method reading: §3.2, PDF pp. 8–10 (printed pp. 5–7), especially
the homogeneous derivation, equations 3–8; the heterogeneous-state mapping
and shared-supply paragraph were checked as scope boundaries. The primed
critical density in the recovery coefficient is the maximum-drop endpoint.
This resolves a coefficient omitted from the abbreviated principal source.
The shared-supply construction informs using one receiving budget, not
separate allowances per donor. Reading that generic merge treatment does
not reopen the closed ramp task or import its controller. Neither the
heterogeneous mapping nor the source's empirical comparisons are qualified
or rerun for our new allocation component.

The title/abstract, selected explanatory paragraphs and methods were read,
not all experiments or all 20 PDF pages. Institutional record/file browser
requests initially failed; the public `pure.tudelft.nl` manuscript worked.
No shell network fetch, full-paper archive addition or installation was needed.

**[4]** H. H. S. Nagalur Subraveti, *Lane-specific Traffic Flow Control*,
Ph.D. dissertation, TU Delft, 2021,
doi: 10.4233/uuid:e405a549-b1fe-4fa1-8090-4429612359d9.

[Institutional dissertation](https://repository.tudelft.nl/record/uuid:e405a549-b1fe-4fa1-8090-4429612359d9)

Reused local text for chapter 3, PDF pp. 44–45, equations 3.18–3.19 and the
repeated mode sentence; chapter 4, PDF p. 65, receiving/capacity-drop summary.
No author erratum or code resolving the sending-mode interpretation was found
in these selected materials. That is a bounded reading result, not proof
that no clarification exists.

## What is extracted and what is proposed

| Item | Evidence status |
|---|---|
| Full homogeneous recovery slope, density-dependent ceiling and receiving form | Primary Han 2016 equations, with capped no-drop branch explicit in Han 2017. |
| Advice times density as a sending cap, receiving otherwise unchanged | Primary Han 2017 VSL description. |
| G's extra density-order gate on sending | Explicit completion of one literal reading of the principal summary; author intent not verified. |
| G's enabled sending gate at final E | Proposed endpoint convention needed because that lane has no same-lane successor. Not selected. |
| H used lane by lane and all arrivals sharing one target budget | Proposed interface mapping consistent with principal lane indexing and shared-supply precedent; no source calibration transfers. |
| Algebraic storage bounds and the flow-jump example | New analytical deductions under the displayed common-FD assumptions. No trajectory or empirical claim. |
| Entire task, A/B information advantage, complete-time sensitivities and useful gradients | Not established or closed by this pass. |

The selected allocator PDF remains unchanged and its former unselected label
is historical; the separate LF1 decision record now governs. The principal
backbone still anchors the candidate; the native summary's demand gate and
the full source-lineage budget are not silently treated as identical.

[Earlier allocator references, Carey/Wright methods and limitations](vsl_allocator_sources_and_adaptations.md)

[Current traffic findings and LF2](../../reporting/research_readiness/vsl_congestion_join_findings_and_gate.md)

## 2026-10-22: what Subraveti explicitly adopts, and what remains our choice

Reread the existing primary article, printed pp. 1765–1766 (PDF pp. 10–11),
and selected simulation/calibration/validation passages on PDF pp. 12–17.
The capacity-drop section explicitly states: “The approach used by Han et
al. (2016) is used to incorporate CD in the model.” It then gives a short
formulation and refers to the original paper for details. The dissertation
chapter 3 repeats this adoption; chapter 4 also states that it employs Han's
approach. This is explicit model ancestry/adoption, not merely a background
citation or our conjecture that the two works could be combined.

The article reports simulation, calibration and validation of its described
lane model. This supports reported use of a Han-based congestion component
in the authors' numerical study. It does not establish code-level identity
between their implementation and our selected H closure. We have not audited
author code or recovered an erratum resolving the printed joint mode gate.
The complete H budget without G's extra sending switch, the explicit Han
2017 VSL restriction, and the shared-target mapping into our new allocator
remain declared selections/adaptations. No inspected author statement
endorses that exact assembled variant.

Consequently, “continuation of Subraveti's Han-based congestion lineage” is
supported. “Our exact Han/VSL/allocator variant was certified or implemented
by Subraveti” is not established. The existing H selection and all of its
qualification limits remain unchanged; no new methodological gate is opened.
