# JM1: source, interface and assumption audit

2026-10-21. **Analytical review evidence; no implementation or experiment.**
The existing selected equations are unchanged. New deductions concern their
joint analytical consequences, not a newly imported traffic mechanism.

**Source roles and inspection.** Reuse the six primary references below.
This pass rereads selected local primary text from [1], [2] and [5]. Han and
Wright methods are reused through the previously completed primary-method
audits, rather than claimed as newly read full papers. No new search,
download or source-family addition was needed. Exact reading scope from
earlier passes remains in the linked audits.

| Source | Actual role and source check | Adaptation or non-transfer boundary |
|---|---|---|
| **[1] Principal lane model** | Reread printed pp. 1759–1766: diagonal versus same-cell transfer, conservation, displayed additive incentives, keep-right/route/courtesy and Han-based congestion. | Retain lane-density states and preferences. Replace movement realization explicitly. Its warning about diagonal congestion propagation remains relevant; shared-state budgets do not prove equivalent waves. Its common-FD accuracy discussion prevents inheriting its field calibration. |
| **[2] Same-author thesis** | Reread chapter 4, PDF pp. 64–65, equations 4.4–4.11: 2:2:1 lookahead, density incentives, omitted bounded acceleration and revised receiving branch. | The weights clarify the framework. Missing E cells, outlet ghosts and the exact mode/direction conventions remain declared member definitions. The text does not supply the selected three-lane allocator. |
| **[3], [4] Han lineage** | Reuse the already qualified homogeneous ceiling, receiving slope and VSL sending cap; [1] explicitly cites [3]. | H is the selected complete source-lineage budget, not the unselected abbreviated mode-gated reading. One common receiver allowance is mapped to all arrivals. No empirical or wave-fidelity certificate transfers to diagonal lane movements. |
| **[5] Carey and colleagues** | Reread selected sections 5–6.1: diagonal receiving competition, intention versus realization, R3 demand caps/redistribution and residual original-lane progression. Its illustrative results also use unit headway ratio. | Support for transport/fallback and capped-share principles. No native complete three-lane, permanent-lane-end algorithm is claimed; our composition drops its cohort/FIFO bookkeeping. |
| **[6] Wright and colleagues** | Reuse prior reading of MISO priority/redistribution and distinctions from general MIMO/FIFO models. | Fixed nominal priorities support the allocation kernel; the whole composed rule is not the Wright general junction solver. Invariance and maximum-throughput guarantees do not follow. |

The principal paper's displayed additive equation is the selected member
convention. Its explanatory prose is not treated as an unambiguous author
implementation of every route/mode detail. Empty donors skip undefined
ratios. The geometry's final E-to-A connection is compulsory even when a
finite upstream incentive would produce no desire. These choices are already
explicit in the selected contract; this audit does not silently change them.

**Interface chain and analytical checks.**

| Check | Direct conclusion and dependency |
|---|---|
| Lane state to desires | Positive-donor lookahead gives a defined density ratio. Exactly empty donors generate no requests. Nominal mode thresholds and geometry are independent of advice. |
| Desires to donor requests | Joint normalization spends at most one sending budget, even when a donor wants both neighbors. This normalization is our interface completion. |
| Budgets to allocation | H is nonnegative on the common-FD physical domain. With the declared time/space bounds, sending cannot exceed old stock and receiving into a physical cell cannot exceed its old space. Free outlets have shared service limits but no physical stock. |
| Competing requests to shared flows | Capped sharing respects each request and the single common receiver budget. Unused nominal entitlement is redistributed; a fixed priority is not a constant realized merge rate. |
| First allocation to fallback | Each residual donor amount and target allowance is nonnegative. The one same-lane fallback is bounded by both; it adds no second lateral opportunity. |
| Flows to physical stock | Every internal movement is subtracted once and added once. All flows use old stock; newly arriving or newly released space is not reused in the same update. The stock remains within jam storage. |
| Terminal stock to completion | E has no continuing E outlet. Unserved E remains physical stock; only crossing an A/B outlet completes mass. No ghost value is counted as traffic. |
| No lateral requests | At an interior row the rule reduces algebraically to ordinary same-lane sending/receiving flow. This is a local limiting case, not aggregate-lane equivalence or continuum convergence. |
| Whole model to complete accounting | Positive advice, positive discharge budgets, a finite road, free outlets and no replenishing arrivals support eventual entry into the exact-tail regime. The proof does not require native incentive continuity. |
| Full objective to derivatives | A uniform finite prefix and finite rational branch formulas give regular advice intervals. The derivative includes both residual-state and direct-speed dependence; native switches remain. |

The conservation and local-budget proofs are sufficient for those claims.
They do not imply maximal throughput or calibrate traffic behavior. The
existing 15-versus-20 allocator counterexample remains a limitation, and the
X/Z service contrast depends in part on the selected preference/allocation
sequence. It is not a traffic-law-independent information theorem.

**Assumption ownership.** JA1 (continuous stocks/common FD) and JA5 (old-state
diagonal allocation with positive priorities) support admissibility. JA2
(closed initialized cohort), JA3 (free completion outlets), JA4 (positive
constant advice) and JA6 (all remaining population-time) additionally support
clearance/accounting. JA7 qualifies derivatives and evidence claims. The
new regularity deduction also uses the finite number of rational branch
formulas in this specific member. These assumptions are jointly consistent;
their field validity is not thereby established. Numeric member values remain
illustrations, not frozen experimental settings.

**Reference list.**

[1] H. H. S. Nagalur Subraveti, V. L. Knoop, and B. van Arem, “First order
multi-lane traffic flow model – an incentive based macroscopic model to
represent lane change dynamics,” *Transportmetrica B*, vol. 7, no. 1,
pp. 1758–1779, doi: 10.1080/21680566.2019.1700846. Repository/copyright
2019; article header 2020, as already recorded.

[Archived primary article](../../archive/full_text/FB0030.pdf)

[2] H. H. S. Nagalur Subraveti, *Lane-specific Traffic Flow Control*,
Ph.D. dissertation, TU Delft, 2021,
doi: 10.4233/uuid:e405a549-b1fe-4fa1-8090-4429612359d9, ch. 4.

[3] Y. Han, Y. Yuan, A. Hegyi, and S. P. Hoogendoorn, “New extended discrete
first-order model to reproduce propagation of jam waves,” *Transportation
Research Record*, vol. 2560, pp. 108–118, 2016, doi: 10.3141/2560-12.

[4] Y. Han et al., “Resolving freeway jam waves by discrete first-order
model-based predictive control of variable speed limits,” *Transportation
Research Part C*, vol. 77, pp. 405–420, 2017,
doi: 10.1016/j.trc.2017.02.009.

[5] M. Carey, C. Balijepalli, and D. Watling, “Extending the cell transmission
model to multiple lanes and lane-changing,” *Networks and Spatial Economics*,
vol. 15, pp. 507–535, 2015, doi: 10.1007/s11067-013-9193-7. Method reading
uses the institutional 2013 author manuscript.

[6] M. A. Wright, G. Gomes, R. Horowitz, and A. A. Kurzhanskiy, “On node
models for high-dimensional road networks,” *Transportation Research Part B*,
vol. 105, pp. 212–234, 2017, doi: 10.1016/j.trb.2017.09.001.

[Earlier principal-source and dissertation reading locations](vsl_lane_backbone_source_audit.md)

[Earlier Han primary-method qualification and links](vsl_congestion_join_sources_and_adaptations.md)

[Earlier Carey/Wright reading scope, versions and links](vsl_allocator_sources_and_adaptations.md)

[Global assumptions and local definitions](vsl_joined_candidate_sources_and_assumptions.md)

[JM1 findings](../../reporting/research_readiness/vsl_methodology_review_findings_and_gate.md)
