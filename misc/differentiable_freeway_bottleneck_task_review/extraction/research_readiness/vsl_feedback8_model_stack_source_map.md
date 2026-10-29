# Feedback 8: unified model, equation and source map

Date: 2026-10-16. This task consolidates the existing selected model. It
does not open another literature sprint or advance the pending protocol
reviews. **No new external paper was viewed.** The reference list below
reuses the previously inspected sources at their archived access limits.
No source calibration, native algorithm or published full-model theorem is
newly adopted.

[Plain-language recap, PDF](../../synthesis/research_readiness/vsl_feedback8_model_stack_recap.pdf)

[Full equations and mathematical work, PDF](../../synthesis/research_readiness/vsl_feedback8_full_mathematics.pdf)

## Component and proof coverage

Original component IDs are retained from the feedback-1/3 audits. The
recap's pages 2–3 map every original component; pages 4–8 explain the new
formulations. The added page 9 briefly introduces the literature rivals;
page 10 retains the reading/status guidance. The mathematical report uses
the section numbers below.

| Component / question | Current mathematical coverage | Archived authority used |
|---|---|---|
| C1–C2: initial geometry, finite cohort, common action and response | Sections 1–2 separate the S13 reference from the current footprint, A/E/B state, units and conditional domain. | [S13 contract](../../synthesis/s13/s13_m2_model_contract.tex), [S13 certificate](../../synthesis/s13/s13_m2_certificate_analysis.tex), [H1/T1 contract](../../synthesis/research_readiness/vsl_h1_t1_joined_contract.tex). |
| C3: travel, arrival timing, cutoff and physical terminal | Sections 4–5 give handoff and eligibility histories, physical versus eligible stock, vacancy protection and the monotone arrival pulse. | H1/T1 contract, subsequently retained in [WF-Q1](../../synthesis/research_readiness/vsl_wf_forward_qualification.tex). The superseded strict-priority one-queue server is excluded from the current law. |
| C4–C5: conservative preparation and adjacent receiving | Section 3 gives the opportunity-equivalent allocator, invariant free branch, scalar ODE, explicit donor/receiving branches and progress-coordinate speed effect; Section 4 gives population balances. | H1/T1 contract and [H1 source audit](vsl_h1_source_and_adaptation_audit.md). |
| C6a: speed/work relation and causal allocation | Sections 6–7 give fixed W-F work, the monotone implicit E root, current-state priority/cooperation and shortfall/clearance guards. | [S-E audit](../../synthesis/research_readiness/vsl_se_admission_and_transition_audit.tex), [S-E-P clearance audit](../../synthesis/research_readiness/vsl_sep_recovery_and_clearance_audit.tex), [W-F user selection](../../reporting/research_readiness/vsl_wf_selection_and_scope.md), [J4 coefficient audit](../../synthesis/research_readiness/vsl_j4_speed_response_audit.tex). W-A and the rejected allocation toggles are labeled historical diagnostics only. |
| C6b: E-only recovery, recent-mass renewal and complete evolution | Sections 8–10 give isolated loss derivation, profile properties, mass-rank/time-history forms, injection/aging/retirement, cutoff perturbation, local contraction, derived positive budget, event control and full clearance. | [O-R qualification](../../synthesis/research_readiness/vsl_or_recovery_qualification.tex), WF-Q1 and the selected R-E/O-R records linked there. Earlier advice-normalized work is replaced; it is used only at the exactly identical anchor in the witness. |
| C7: local completion and complete time | Section 11 derives full conservation and the population-time/queue-area identity. | H1/T1, O-R and WF-Q1. S13 mean time and current total TST differ by a declared normalization as well as the changed forward law. |
| C8–C9: initial information and sensitivity boundary | Section 12 gives compact reconstruction, retained conditional history ambiguity, negative controls, front threshold and activation-flux warning. | WF-Q1 and [closed S13 result](../../reporting/s13/s13_99_m2_certificate_sprint_closure.md). The current action/gradient protocol is not completed by this recap. |
| Nonempty analytical coupling | Section 13 reproduces the complete H1 A-delay/active-renewal construction, removes auxiliary zero parameters and records static feasibility. | O-R construction, preserved exactly at W-F's anchor. Its extreme-scale/uncalibrated limitations remain explicit. |
| Joint physical interpretation / MP6 | Section 14 collects tail/work identification, branch-product confounding, stationary correspondence and joint admission limits. | [MP6-Q1 mathematical note](../../synthesis/research_readiness/vsl_mp6_physical_identifiability.tex), [joint admission contract](../../synthesis/research_readiness/vsl_mp6_joint_physical_admission_contract.md). No applied range is inferred. |

The new reports write the shared budget as `mathcal B` and its reading as
`p_rec`; archived `B`/`p` have the same meanings. Far lane B, initial ending
fraction and the S13 coefficient are distinguished. H1 `f` remains an
opportunity-equivalent quantity; `f/h` is the lateral density source. No
coefficient, state, physical scale, observation or completion endpoint changes.

## Reused reference list and limits

| Reference | Role in the recap | Existing source record |
|---|---|---|
| Nagalur Subraveti, Knoop and van Arem, Transportmetrica B, DOI [10.1080/21680566.2019.1700846](https://doi.org/10.1080/21680566.2019.1700846); archived record preserves the 2019/2020 version discrepancy. | Per-lane continuous conservation and constrained mandatory transfer. Its complete CTM/incentive algorithm is not the selected H1 law. | [FB0030 inspected sections and limits](../n2_source_studies/FB0030.md), [S13 source audit](../s13_m2_source_to_equation_audit.md). |
| Carey, Balijepalli and Watling, *Extending the Cell Transmission Model to Multiple Lanes and Lane-Changing*, author manuscript labeled 2013, DOI [10.1007/s11067-013-9193-7](https://doi.org/10.1007/s11067-013-9193-7). | Receiving-work and allocation ingredients. The selected homogeneous law, equal-work cooperation and history reduction are adaptations. | [Primary-source join audit](vsl_r1_primary_source_join_audit.md), [W-F source audit](vsl_wf_forward_source_audit.md). |
| Jin, *Continuous formulations and analytical properties of the link transmission model*, published 2015; [primary preprint](https://arxiv.org/pdf/1405.7080). | Boundary-count travel, stock and vacancy context. Its general node theorem is not attributed to our history-dependent node. | [H1/T1 source register](../../synthesis/research_readiness/vsl_h1_t1_joined_contract.tex), [O-R source audit](vsl_or_qualification_source_and_adaptation_audit.md). |
| Yperman, Logghe and Immers (2005), *The Link Transmission Model: An Efficient Implementation of the Kinematic Wave Theory in Traffic Networks*, [primary paper](https://www.mech.kuleuven.be/cib/verkeer/dwn/pub/P2005C.pdf). | Link/node separation and a specified merge allocation. It does not calibrate the present work or recovery law. | H1/T1 source register. |
| Leclercq, Knoop, Marczak and Hoogendoorn (2016), *Capacity drops at merges: New analytical investigations*, DOI [10.1016/j.trc.2015.06.025](https://doi.org/10.1016/j.trc.2015.06.025). | Isolated insertion/recovery basis and restricted congested speed interpretation. The capped profile and recent-mass account are further deductions/adaptations. | [P-H source audit](vsl_ph_source_and_adaptation_audit.md), [MP6 physical source audit](vsl_mp6_physical_source_audit.md). |
| Marczak, Daamen and Buisson (2013), *Merging behaviour: Empirical comparison between two sites and new theory development*, DOI [10.1016/j.trc.2013.07.007](https://doi.org/10.1016/j.trc.2013.07.007). | Archived empirical caution on gap/speed interpretation. No fitted coefficient or universal sign is imported. | [J4 reading scope and cautions](vsl_j4_speed_response_source_audit.md). |
| Wei, Han and Wang (2025), *A first-order link-based flow model with variable speed limits and capacity drops for freeway networks*, DOI [10.1111/mice.13492](https://doi.org/10.1111/mice.13492). | Strong aggregate history/capacity-drop rival, introduced on recap page 9. No new benchmark adoption. | [Baseline screen](vsl_successor_baselines_and_evidence_gaps.md), [history/response qualifications](../n2_source_studies/response_lane_derivative_frontier.md). |
| Jin and Jin, *Control of a lane-drop bottleneck through variable speed limits*, [arXiv:1310.2658](https://arxiv.org/abs/1310.2658), archived manuscript dated 29 October 2018. | Compact aggregate discharge/capacity-drop rival; its idealized limits qualify generic VSL-benefit claims. | Baseline screen and history/response qualifications. This is distinct from Jin–Gan–Lebacque's arXiv:1310.2660 capacity-drop paper. |
| Hegyi, De Schutter and Hellendoorn (2005), METANET-based predictive VSL control; [author report](https://www.dcsc.tudelft.nl/~bdeschutter/pub/rep/03_016.pdf). | Dynamic aggregate speed/control rival. Repeated predictive control differs from the primary one-shot constant advice. | Baseline screen; its previously recorded abstract/Section 3 scope is retained. |
| Delle Monache, Piccoli and Rossi, LWR speed control and cost variations; [arXiv:1603.04785](https://arxiv.org/abs/1603.04785). | Analytical-gradient reference with a different control/objective, not an already matched lane-drop benchmark. | [Derivative qualification record](../n2_source_studies/response_lane_derivative_frontier.md#fb0002--rm0025--seo2026-derivative-target-must-match-the-claim). |
| Zhang, Chung, Sabar, Bhaskar and Ma, *Optimisation of variable speed limits at the freeway lane drop bottleneck*, 2023 publication; DOI [10.1080/23249935.2022.2033878](https://doi.org/10.1080/23249935.2022.2033878). | Task/action precedent inherited through S13. Its finite-horizon discharge and native calibration are not this objective or information contract. | [S06-S3 source record](../s06_reference_mechanism_source_audit.md#s06-s3--zhangchungsabarbhaskarma2023). |
| Official SUMO, [Road Capacity](https://sumo.dlr.de/docs/Simulation/RoadCapacity.html), as rechecked in the prior MP6 pass. | Stationary headway correspondence and its limits only; no runtime/API or amended bridge qualification in this task. | MP6 physical source audit. |

The strong capacity-drop/model-form rivals and optimizer alternatives remain
in their existing [baseline record](vsl_successor_baselines_and_evidence_gaps.md).
They are not silently folded into this primary model. No claim of modeling
novelty or full-lane-state necessity is made.

The requested brief rival section reuses that record: Wei, Jin–Jin, Hegyi,
Carey and Nagalur Subraveti are traffic-model candidates; Delle Monache is
also a gradient-method precedent. A+E/G equivalence and scalar search remain
separate information/optimization controls. Zhang and the screened ramp-merge
applications are context rather than newly qualified matched baselines.

## Delivery status

Feedback 8 is answered by the two PDFs and their retained TeX sources.
This consolidation is not a new scientific gate and does not close applied
MP6 or Step 3. The next protocol reviews remain unopened by this task.
No simulator, dependency installation, traffic/ODE experiment, calibration,
numerical gradient, optimization or SUMO execution occurred.
