# RM10 primary-source and transfer audit

Date: 2026-10-05. Methodology review only; A recovery/acceleration alone.
Interpretations below are reviewer deductions unless explicitly described as
source results. This packet reuses existing IDs, including the VSL branch's
S12A005, without transferring its earlier task admission. Source papers are
linked, not redistributed. New sources are RM10-P01–P05.

## Inspected primary methods

| ID / primary version | Inspected location and source support | Transfer boundary / reviewer inference |
|---|---|---|
| RM8-P01, Laval/Cassidy/Daganzo, 2005 proceedings/2007 chapter, [author-hosted paper](https://bpb-us-e1.wpmucdn.com/sites.gatech.edu/dist/f/3571/files/2023/03/merges.pdf) | Sections 2–4: lane-wise kinematic waves with bounded-acceleration inserting vehicles; voids and discharge reduction; metering interventions. | The ramp-queued versus unqueued comparison changes an admitted queue observation. It supports physical recovery and rate relevance, not identical strong histories or all-stream TST action ranking. |
| RM0011, Laval/Daganzo, 2004 working paper, [institutional original](https://escholarship.org/content/qt8w70q261/qt8w70q261.pdf) | Sections 2–3: hybrid lane-stream/particle dynamics and lane-changing interactions. | A richer physical reference, not automatically a continuous-mass reduction. Neither source particles nor a forward capacity improvement prove that identity is indispensable under our history contract. |
| RM10-P01, Leclercq et al., **2011 proceedings text**, [author-uploaded original](https://www.researchgate.net/publication/251530773_Capacity_Drops_at_Merges_an_endogenous_model) | Sections 2.1–2.2: inserting acceleration, entry speed and headway statistics enter an implicit effective-capacity calculation; actual entry flow and upstream regimes matter. | Body identifies Procedia Social and Behavioral Sciences 17, 12–26, DOI 10.1016/j.sbspro.2011.04.505. Landing metadata points to a related TRB journal version; that version was not method-audited. Stationary capacity is not a finite-storage metering rollout or its TST derivative. |
| S12A005, Leclercq et al., **2016 author manuscript**, [institutional original](https://repository.tudelft.nl/file/File_c424c1b3-7374-436b-a6a7-abdf69063aa6) | Section 2, equations 1–4; Section 4; Section 5/Figure 5. Mean-parameter approximations estimate active-merge capacity; heterogeneous traffic has different transient upstream flow. | DOI 10.1016/j.trc.2015.06.025; distinguish 2014 conference antecedent. Similar mean capacity is approximate, not exact state sufficiency or equal TST. Figure 5 flow trajectories differ: not a same-observed-history pair. Random characteristics require an explicit matched population/forcing contract. |
| RM10-P02, Leclercq/Marczak/Knoop/Hoogendoorn, **2016 published paper**, [institutional original](https://repository.tudelft.nl/file/File_d4844cb9-1115-47ab-ab36-443cc0ca7df4) | Printed pp. 1–3, Modeling Framework: two-mainline-lane starting point; recursively coupled effective-capacity and inserting-flow equations. DOI 10.3141/2560-01. | Direct two-lane mean-capacity precedent and strong aggregate/moment competitor. Spatial partitioning is a source assumption, not an adopted C geometry task. No dynamic finite-storage/full-history/action certificate is transferred. |
| RM9-L03, Srivastava, **2016 dissertation**, [institutional original](https://escholarship.org/content/qt7dx478g4/qt7dx478g4.pdf) | Chapter 3.3.1, printed pp. 27–28/PDF pp. 42–43, equation 3.3: congested demand decreases with density; ordinary supply, flux and conservation remain. Chapter 3.4 derives recovering discharge. | Explicit aggregate recovery competitor. Original reference is queue discharge at a signal; it is not an already validated ramp-merge law. Chapter 4 lane-drop material is not silently transferred. |
| RM0003, Cao/Nilsson/Coogan, **2021 arXiv v1**, [original paper](https://arxiv.org/pdf/2106.10347) | Section II.B, equations 3–6: density thresholds plus retained congestion mode; initialization specifies the mode in the intermediate band. | Known initial mode plus full admitted density history reconstructs the mode exactly. Controller gains from including hysteresis show model adequacy matters, not hidden history-conditioned state. An unknown initial mode is a different evidence domain, not universally excluded. |
| RM10-P04, Laurent-Brouty/Costeseque/Goatin, **2020 author version of 2021 SIAM paper**, [author-uploaded original](https://www.researchgate.net/publication/346438282_A_Macroscopic_Traffic_Flow_Model_Accounting_for_Bounded_Acceleration) | Section 2, equations 2.1–2.2 and Theorem 1; Section 3 interaction times; Section 5. LWR density is coupled to accelerating leader trajectories. DOI 10.1137/19M1268173; body identifies HAL-02155131v4. | Despite its title, it retains moving local constraints. With its complete initial density profile, source initialization fixes initial leaders/speeds. Coarse-observer identifiability is not proved. Existence of solutions is not a gradient theorem. Numerical examples are arterial signals, not our ramp-rate task. |

## Abstract-only and reused evidence boundaries

| ID / primary link | Permitted claim | Unavailable / not transferred |
|---|---|---|
| RM10-P03, Jin/Laval, 2018, [author institution](https://its.uci.edu/research_products/published-journal-article-bounded-acceleration-traffic-flow-models-a-unified-approach/) | Abstract presents bounded-acceleration continuum/car-following model relationships; DOI 10.1016/j.trb.2018.03.006. | Selected full methods not obtained. No exact closure, speed-observer or control-gradient theorem inferred. |
| RM10-P05, Srivastava/Jin, 2017, [publisher original abstract](https://journals.sagepub.com/doi/10.3141/2623-05) | Aggregate demand can be derived from microscopic acceleration models. | Full equations not inspected; RM9-L03 supplies the inspected concrete competitor. |
| RM8-P04, 2023, [publisher original](https://www.mdpi.com/2071-1050/15/3/2050) | Indexed primary text discusses aggregate density/speed models and capacity drop. | Direct HTML/PDF access failed; corroboration only, not a new full-method audit. |
| RM8-P05, 2013, [publisher DOI](https://doi.org/10.1016/j.trc.2013.02.006) | Existing abstract-level flow-ratio-dependent drop lead. | Not an exact transient/full-history closure theorem. |
| RM9-L04, Cho/Laval, 2020, [publisher original](https://ascelibrary.com/doi/10.1061/JTEPBS.0000350) | Existing combined RM/VSL bounded-acceleration control lead. | Additional actuator; abstract access only. Does not certify our rate-only task. |
| RM0014, [institutional report](https://escholarship.org/content/qt30s46939/qt30s46939.pdf) | Reuse RM8 extraction of Sections 3–5: restrictive-then-relaxed metering and occupancy-based recovery evidence. | No fresh full-text access claimed. Observable recovery feedback and throughput do not establish our hidden-information/TST certificate. |
| RM0024/RM0025 | Reuse [RM8 gradient audit](../rm8_source_studies/aggregate_and_gradient_alternatives.md). | Adjoint construction/internal optimization in different tasks is not independently useful acceleration-aware ramp gradients. |

## Coverage, not a universal absence claim

Sixteen targeted queries covered endogenous merge capacity, bounded acceleration,
heterogeneity, aggregate alternatives and ramp sensitivity/adjoints, followed by
the nearest primary methods above. Search results were screened for action,
objective and observation compatibility; unrelated emissions/VSL, autonomous
vehicle trajectory and reinforcement-learning tasks were not imported. The
query log and screening table retain failures and access grades. The source
frontier supports a bounded admission decision, not an exhaustive impossibility
claim about all ramp traffic or all future recovery models.

No C geometry search or C task formulation was conducted. Geometry present in
an A source was read only to delimit the source's validity. No joint A+C law,
geometry-dependent new case, private realization or extra-lane rescue was adopted.
