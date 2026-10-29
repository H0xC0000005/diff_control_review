# RM8 task, derivative and independent-reference screen

Date: 2026-10-01. No model equation or simulator selected.

## Task contract retained

One finite-storage ramp merges into a multilane mainline. The common decision
is a bounded open-loop rate schedule, initially inspected by small perturbations.
Demand-limited release and actual downstream receiving are distinct. A meter
permission cannot guarantee that ramp traffic physically enters the mainline.
Autonomous lateral responses are traffic dynamics, not a second control.

Count waiting on the ramp, mainline time, rejected/unserved arrivals and residual
traffic under a common clearance rule. An artificial benefit from parking
traffic beyond the horizon is excluded. Storage and merge safety constrain
feasibility. No rate values, time resolution, objective formula, merge priority
or terminal law are frozen by this review.

## Evidence matrix

| Product | Current status | Required bridge |
|---|---|---|
| Physical metering-to-merge mechanism | Source supported, with site/model restrictions | Select and justify a conservative local law |
| Rate-only action compatibility | Plausible, not fully transcribed | Same meter meaning, demand/receiving limits and feasible set |
| Hidden information beyond strong history | Not established | Exact realizable matched-history construction or explicit weaker-claim decision |
| Useful decision distinction with complete accounting | Not established | Feasible common perturbation/action comparison through clearance |
| Minimum sufficient retained state | Not established | Compare history, scalar closure, group contrast and finer interactions |
| Conceptual sensitivity chain | Identified | Rate → arrivals → merge state/service → queues → complete objective |
| Mathematical correctness of that candidate gradient | Not established | Adopt defensible laws/events, derive sensitivities and an independent check contract |
| Independent one-step usefulness | Not established | Same perturbations in a separately justified richer/reference model |
| Full controller/optimized research study | Deferred | Only after previous evidence; feedback/MPC/multi-ramp not automatic |

## Derivative discipline

An active receiving constraint can make a rate perturbation ineffective; a
breakdown threshold can change the mode. A correct derivative within one regime
may fail for a finite intervention crossing an event. Source branches, zero
states and hysteresis initialization require explicit semantics. Do not certify
the family merely because portions are continuous, or repair it with smoothing.

Later review must distinguish analytic derivative correctness, numerical
correctness of a future implementation, and one-step improvement in an independent
reference. Published macro adjoints are predecessors, not validation of an
as-yet unspecified local-lane derivative. This review performed none of those
numerical checks.

## Reference requirements, not software selection

A candidate reference must reproduce rate-induced local redistribution,
receiving limitations and any acceleration/capacity recovery being claimed.
It must share action mapping, demand/population, geometry, observations and
clearance accounting. Document which mechanisms were calibrated and against
what data. Holding out perturbations and avoiding shared imposed service penalties
are necessary to make a future transfer test informative.

Hybrid lane/particle models and calibrated microscopic models are candidates.
The qualifier 'microscopic' alone is insufficient. SUMO is not required to
complete this review; installation and execution remain outside scope.
A future research plan may select software only after its relevant behavior
and intervention mapping have been justified.
