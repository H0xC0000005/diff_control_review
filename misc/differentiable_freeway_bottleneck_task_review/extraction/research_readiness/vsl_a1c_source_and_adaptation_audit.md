# Revised A1-C execution: viewed references and adaptation boundaries

Date: 2026-10-15. Selected-section source work, not a complete-paper or PDF
archive. The user selected revised A1-C; the new state-closure choice is
unselected. No source numerical illustration was run or used as calibration.

## Main references inspected

| Reference | Material actually inspected | Role and limit |
|---|---|---|
| [Jin, Gan and Lebacque (2013 preprint), *A kinematic wave theory of capacity drop*, arXiv:1310.2660](https://arxiv.org/pdf/1310.2660) | Reopened primary manuscript; §2.1 boundary/selection formulation, §2.2 unique Riemann solution and §6 merge allocation. | Selection of evolution is part of the source model. Neither its phenomenological drop nor its uniqueness theorem proves the proposed history/state-dependent work node. |
| [Leclercq, Knoop, Marczak and Hoogendoorn (2016), *Capacity drops at merges: New analytical investigations*, DOI 10.1016/j.trc.2015.06.025](https://repository.tudelft.nl/file/File_c424c1b3-7374-436b-a6a7-abdf69063aa6) | Rechecked §2 point inputs and §3.2's explicitly congested flow/speed relation; reused §5 limits. | Physical insertion/recovery interpretation; does not select initial free-to-queued transitions or supply this finite transient account. |
| [Chevallier and Leclercq (2009), *Do microscopic merging models reproduce the observed priority sharing ratio in congestion?*, TRC 17(3), 328–336, DOI 10.1016/j.trc.2009.01.002](https://www.sciencedirect.com/science/article/abs/pii/S0968090X09000096) | Primary publisher search-returned abstract and introduction. Direct publisher open failed. No complete rate/relaxation equations or empirical data inspected. | Insertion-rate and relaxation concepts must fit together. No native microscopic algorithm, continuous reduction or parameter set is adopted here. |
| [Jin and Zhang (2003), *On the distribution schemes for determining flows through a merge*, TRB 37(6), 521–540](https://www.sciencedirect.com/science/article/abs/pii/S0191261502000267) | Primary publisher search-returned abstract/introduction; direct open failed. | Demand-based fairness is a serious simpler allocation reference. Its demand-proportional rule is not the proposed equal-work rule and does not derive actual entry kinematics. |

The exact early H1 gap-work source, continuous-LTM backbone, empirical
relative-speed and congested-sharing findings are reused through the prior
audits, not reported as newly read full papers. The early work coefficient
is not transferred into the terminal without qualification.

[Earlier H1 work/source audit](vsl_h1_source_and_adaptation_audit.md)

[Feedback 7 empirical references and their limits](vsl_feedback7_traffic_state_source_audit.md)

## Deliberately screened neighboring formulations

These abstracts were viewed while testing whether a source already gives
the required unified transient law. They are retained in the reference list,
not treated as algorithm/equation qualification or adopted task models.

| Reference | Access and screening limit |
|---|---|
| [Chevallier and Leclercq (2007), *A macroscopic theory for unsignalized intersections*, TRB 41(10), 1139–1150, DOI 10.1016/j.trb.2007.05.003](https://www.sciencedirect.com/science/article/pii/S0191261507000537) | Primary publisher search-returned abstract; direct open failed. Temporary insertion availability and average-underload delay are relevant concepts. Its fictive alternating service is not adopted as a new clock/phase in this task. |
| [Chevallier and Leclercq (2008), *A Macroscopic Single-Lane Roundabout Model to Account for Insertion Delays and O–D Patterns*, CACAIE 23(2), 104–115, DOI 10.1111/j.1467-8667.2007.00527.x](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-8667.2007.00527.x) | Publisher bibliographic/abstract search record; author-uploaded abstract also screened. No full roundabout model/equations inspected or adopted. |
| [Chevallier and Leclercq (2009), *Microscopic Dual-Regime Model for Single-Lane Roundabouts*, JTE 135(6)](https://ascelibrary.com/doi/10.1061/%28ASCE%290733-947X%282009%29135%3A6%28386%29) | Primary publisher abstract and author-manuscript abstract returned in search. Distinguishes regime-dependent insertion descriptions; no microscopic roundabout process is imported. |

Incidental general search hits, secondary node reviews, Wikipedia and
uninspected papers cited inside the retrieved articles are not source bases
for the findings. No SUMO API, current binary or runtime correspondence was
newly qualified.

## What is borrowed, proposed and actually proved

| Status | Exact meaning |
|---|---|
| **Reused source ingredients** | Continuous mass, sending/receiving limits, conservative node allocation, explicit boundary selection and regime-conditioned speed interpretations. |
| **Proposed module** | Equal division of service work between competing ready streams, with unused work redistributed; traffic state changes unit admission work. This fairness convention is an explicit hypothesis, not a source theorem. |
| **Own analytical findings** | Unique fixed-input module flows; share/total-flow/residual-work identities; an exact arbitrary queue-birth diagnostic for a particular instantaneous completion; conditional storage/TST and bounded-work/finite-loss clearance criteria. |
| **Unresolved physical law** | Actual state-to-work coefficients, admission opportunity, speed transition/evolution, account/recovery overlap and the complete coupled initial-value problem. |

The diagnostic is not a source-derived empirical equation, a complete P-H
history model, a general nonuniqueness theorem for first-order nodes or a
new primary traffic scenario. Its role is to demonstrate why a missing
state-selection convention cannot safely be delegated to an integrator.

[Current traffic findings, alternatives and stop gate](../../reporting/research_readiness/vsl_a1c_service_work_findings_and_gate.md)
