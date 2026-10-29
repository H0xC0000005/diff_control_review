# Feedback 20 source and access record

Date: 2026-09-15  
Purpose: preserve the sources used to debate mesoscopic and differentiable ramp metering without repeated querying

## Source table

| ID | Source and persistent link | Access inspected | Claim supported | Boundary |
|---|---|---|---|---|
| RM0024 | Reilly et al. (2015), *Adjoint-Based Optimization on a Network of Discretized Scalar Conservation Laws with Applications to Coordinated Ramp Metering*, [doi:10.1007/s10957-015-0749-1](https://doi.org/10.1007/s10957-015-0749-1) | Public 23-page manuscript archived at `../full_text/RM0024.pdf`; publisher-version browser text also inspected | Discrete adjoint, sparse linear scaling, direct coordinated I-15 ramp-metering/MPC application, finite-difference scaling motivation | Manual discrete adjoint of a first-order model; no exact local order or automatic differentiation; reported controller result is model/data conditional |
| RM0025 | Goatin, Klar, and Mezquita-Nieto (2026), *Discrete adjoint gradient computation for multiclass traffic flow models on road networks*, [doi:10.1007/s11081-026-10122-4](https://doi.org/10.1007/s11081-026-10122-4) | Open 33-page version of record archived at `../full_text/RM0025.pdf`; full HTML/PDF method inspected | Discrete adjoint of multiclass Godunov network flow; merges/diverges/buffers; exact numerical-objective gradient on active branches; benefit with many controls | Numerical demonstration is general network/class control, not the B1-P task; class aggregation is not exact FIFO rank |
| RM0026 | Gu et al. (2022), *A Smoothing Method for Ramp Metering*, [doi:10.1109/TITS.2021.3123815](https://doi.org/10.1109/TITS.2021.3123815) | Author-institution bibliographic record and abstract inspected; full text not required for the high-level classification | Direct smooth CTM ramp-metering MPC; smoothing/convergence claim and alternatives | Abstract-level for this pass; no equation transcription; smoothing is a changed contract, not evidence for exact gradients |
| RM0027 | Lee et al. (2019), *Analyzing Simulation-Based Active Traffic Management Impact on a Large-Scale Regional Network*, [doi:10.1177/0361198119845650](https://doi.org/10.1177/0361198119845650) | Publisher abstract and cited DTALite basis inspected | Mesoscopic DTA plus ramp metering for large-scale/local-network impact and minute-scale interaction | Does not establish exact queue order or local merge fidelity; full text not needed for the reported abstract-level role |
| RM0028 | Wei (2001), *Analysis of artificial neural network models for freeway ramp metering control*, [doi:10.1016/S0954-1810(01)00019-X](https://doi.org/10.1016/S0954-1810(01)00019-X) | Publisher-indexed abstract and simulation-method sections inspected | Stochastic, event-based mesoscopic test bed covering mainline, entrance and exit vehicle operations | Controller and simulator contributions are coupled; no isolated exact-order result; no equation adoption |
| RM0029 | FHWA (2013), *Traffic Analysis Toolbox Volume XIV: Guidebook on the Utilization of Dynamic Traffic Assignment in Modeling*, [official section](https://ops.fhwa.dot.gov/publications/fhwahop13015/sec3.htm); NCHRP 03-114 literature review, [official PDF](https://onlinepubs.trb.org/onlinepubs/nchrp/docs/NCHRP03-114_LiteratureReview-Revised.pdf); final NCHRP Research Report 1120, [doi:10.17226/27871](https://doi.org/10.17226/27871) | Official pages and relevant full precursor-report pages inspected | Meso role in route/diversion and larger-scale analysis; micro role at detailed junctions; meso often omits lane-changing/gap acceptance | Practitioner/review evidence, not a model equation or proof that every tool follows the same taxonomy |
| RM0030 | Poole and Kotsialos (2016), *Second order macroscopic traffic flow model validation using automatic differentiation with resilient backpropagation and particle swarm optimisation algorithms*, [doi:10.1016/j.trc.2016.07.008](https://doi.org/10.1016/j.trc.2016.07.008) | Author-repository text and bibliographic/abstract metadata inspected | Automatic differentiation through METANET for freeway parameter calibration and sensitivity insight | Calibration, not ramp-control experiment; second-order macro model; used only to establish freeway-specific AD precedent |
| Cross-package T0001/R0014 | Seo (2026), *End-to-end differentiable network traffic simulation with dynamic route choice*, [arXiv:2604.11380](https://arxiv.org/abs/2604.11380) | Full preprint browser-inspected in earlier/current reviews; records remain in the sibling packages | Explains reverse-mode AD scaling and distinguishes Reilly/Goatin manual adjoints; ramp metering listed as future applicability | Demonstrated task is pricing, not ramp metering; no duplicate local archive created |

## Archived file verification

| ID | Local file | Identification | Pages | SHA-256 |
|---|---|---|---:|---|
| RM0024 | `archive/full_text/RM0024.pdf` | Public Berkeley manuscript; title/first page extracted with pypdf | 23 | `db07df20fcb9671a7e75b5a7e92dd113bcd3a5a05de6476862d7dd5d48dd747b` |
| RM0025 | `archive/full_text/RM0025.pdf` | Open Springer version of record; title/first page extracted with pypdf | 33 | `14b19ed4794e020fafa20709215cdf8785c9fbde5588c2dbdcf7f193a8055fb5` |

RM0024's first attempted URL returned an HTML client challenge despite a `.pdf` name. It was replaced with the valid PDF from Berkeley Connected Corridors before being entered in the manifest. RM0025's shell `file` output reported only the first internal page-tree count; pypdf verified 33 readable pages.

## Search groups added

- Differentiable/adjoint ramp metering: adjoint, sensitivity, gradient, automatic differentiation, CTM, LWR, METANET, MPC.
- Mesoscopic ramp evaluation: mesoscopic, DTA, stochastic event-based, regional/corridor, hybrid/multiresolution.
- Counterevidence: optimal/monotonic/linear-program ramp control, microscopic merge safety/lane dynamics, aggregate calibration.

The pass is targeted rather than exhaustive. It is sufficient for the role decision because it contains direct freeway gradient-control predecessors, direct mesoscopic ramp examples, official model-resolution guidance and strong aggregate alternatives. Absence of another mechanism in this corpus is not asserted as universal absence.
