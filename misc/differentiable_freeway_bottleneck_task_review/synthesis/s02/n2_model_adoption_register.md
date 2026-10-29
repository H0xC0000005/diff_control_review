# N2 model-adoption register — provisional, not implementation authority

All candidates receive the same link-level advice schedule. Actions, traffic
population, closure/reopening and objective accounting cannot change with
resolution. No parameter values, class counts, lane partition or smoothing
selected. Source equations are referenced rather than retranscribed as a new
model. See individual [source studies](../../extraction/n2_source_studies/FB0013.md).

| Responsibility / source | Original I/O, state and source locations | Smallest proposed adaptation / conservation and derivative cautions |
|---|---|---|
| Strong B0 response/dynamics: FB0003/26; FB0013 | Advice plus segment density/mean speed and boundaries → lane-weighted flow/new state; density veh/km/lane, speed km/h, flow veh/h, origin mass. FB0026 II–III eqs 1–6/13–14; FB0013 pp 3–5 eqs 1–5. | Recalibrate homogeneous realized response for advice, not enforced limits. Retain necessary propagation/speed dynamics and shared storage; do not force urban LTM choices on freeway task. Continuous min/max kinks and inherited bounds need audit; whole METANET scheme not certified for positivity/storage. |
| Strong B0 speed-history alternative: FB0022 | Link cumulative inflow/outflow and entry-time speed histories → exit flow, average travel quantities; II/eq 10, III. | History may account for response delay without driver classes. Binary exit threshold/state-duration CD require audit; not ready-made differentiable backbone. Distinguish history cohorts from fixed population response classes. |
| Ideal aggregate bottleneck/recovery reference: FB0001/21 | Density/flow, demand, lane reduction/drop capacities, event timing → queue/wave paths and delay; FB0001 archive pp 6–8, FB0021 §2.1–2.3/Appendix A. | Use recovery-tail and no-benefit reference logic, not moving-front control. Fixed exogenous closure is allowed; endogenous discharge switches not automatically admissible. No discarded upstream delay. |
| B1 response composition: FB0005/26/33; FB0028 lead | Field aggregate speed response or microscopic individual speed factor; FB0005 §8.3; FB0026 III/13; FB0033 §3.3. FB0028 only primary abstract inspected. | Fixed exogenous membership, continuous class mass and deterministic response, if identifiable and decision-relevant. Reuse mean-law calibration as comparator; don't equate scalar alpha with class share. No control-dependent resampling. Need donor-class sending constraints and exact per-class conservation. An exact B1 closure law is still missing. |
| B2 endogenous lateral transfer: FB0024/30 | Per-lane/group density, adjacent/downstream receiving room, fixed lane end/route incentive → paired lateral flows/new occupancy. FB0024 eqs 7–11; FB0030 eqs 1–22. | Borrow constrained transfer and mandatory-merge incentive, preserve each class's mass if classes retained. Advice is shared; LC volumes endogenous, not commands. Need common donor/receiver budgets, group weighting, empty-state limits and branch continuity checks; no blind copy of published equations. |
| Lane/class accounting boundary: FB0004/20 | Lane-specific speeds plus commanded LC (and sometimes RM), CAV/class states → optimized traffic. FB0004 III/eqs 1–12; FB0020 §3.1–3.3. | Accounting/transfer insight only. Remove actuator and population mismatch before claiming relevance to state-only F1 contrast; no direct reuse of CAV actuation or joint-control gains. |
| Derivative/reference lineage: FB0002/RM0025 | Speed variation → outflow-tracking derivative in free-flow LWR; routing controls → numerical adjoint/FD checks in multiclass network. | Internal derivative checks only; target must be advice/objective matched. Transported jumps are deterministic event sensitivity, not random categorical mass. No new saltation/estimator research authorized. |

Priority: (1) strong baseline plus common advice/evaluator/accounting contract;
(2) evidence for one omitted-information decision contrast;
(3) only then select a justified response or lane refinement;
(4) gradient correctness and independent usefulness require later planned tests.
No automatic compliance-first ordering follows from this evidence.
