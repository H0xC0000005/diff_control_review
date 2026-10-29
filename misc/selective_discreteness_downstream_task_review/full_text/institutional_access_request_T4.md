# T4 institutional-access request

Status: fulfilled; T4 extraction completed  
Request date: 2026-09-10  
Batch: T4-01 (one decision-critical paper)

The requested PDF was supplied at the specified path on 2026-09-10. It was verified as a 14-page PDF and extracted locally with page markers. This request is retained as the access audit trail; no further user retrieval is required for T4.

Please retrieve the complete paper PDF through your institutional access and place it at exactly:

```text
/home/zpz/repos/diff_minimal_meso/misc/selective_discreteness_downstream_task_review/archive/user_supplied/T0007_Wei_et_al_2025.pdf
```

## Requested paper

### T0007 — *Hierarchical Predictive Control of Network Traffic Signals Using Link Transmission Model With Queue Dynamics*

| Field | Information |
|---|---|
| Authors | Lei Wei, Konstantinos Ampountolas, Angelika Hirrle, and Meng Wang |
| Year | 2025 |
| Venue | *IEEE Transactions on Intelligent Transportation Systems*, 26(10), 16391–16404 |
| DOI | [10.1109/TITS.2025.3568869](https://doi.org/10.1109/TITS.2025.3568869) |
| IEEE record | [Document 11010837](https://ieeexplore.ieee.org/document/11010837/) |
| Access state | Public abstract and metadata available; complete text remains closed-access |

**Abstract:** The paper proposes hierarchical model-predictive traffic-signal control using LTM-based queue dynamics at road-segment and turn levels. A network layer uses quadratic programming to determine effective green-time fractions for throughput maximization. A local layer uses a refined turn-level queue-transmission model and nonlinear programming to track those references while avoiding spillback. Arterial and grid-network experiments report improvements in throughput and queue length, particularly under oversaturation, and test robustness to demand-prediction error.

**Why the full text is decision-critical:** This is the closest located predecessor to the proposed task intersection: LTM signal control, continuous effective green fractions, turn-level queues, spillback, and a realization layer. T4 must determine precisely:

- whether effective green fractions or executable phase durations are the actual decision variables at each layer;
- the objective equations, units, horizon, constraints, and terminal treatment;
- how road-segment and turn-level queues represent finite storage and blockage;
- whether the lower layer merely tracks network targets or changes the realized intervention;
- which baselines, demand regimes, geometries, budgets, and robustness tests are used; and
- which aspects remain aggregate and therefore distinct from selective order/access semantics.

The abstract cannot support those extraction fields reliably. Omitting the paper would create a material blind spot in the primary-task and baseline formulation.

## What to supply

- The complete article PDF, including appendices and supplementary method pages bundled with the article, if any.
- No database export or bulk search is requested.

After placing the file, reply that the T4 material is ready. T4 will resume with local text extraction and quality assessment.
