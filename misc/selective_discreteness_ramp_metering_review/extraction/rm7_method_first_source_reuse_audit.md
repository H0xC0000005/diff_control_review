# RM7 method-first source-reuse audit

Date: 2026-10-01. Scope: task selection using the existing ramp corpus and later
freeway mechanism evidence. The evidence cutoff is sufficient for initial task
framing; an approved successor must run a fresh targeted predecessor search for
the selected task.

## Evidence families retained without implementation constraints

### Strong aggregate and gradient baselines

- RM0002 supplies first-order ramp queue, metering, merge and total-time control
  structure with strong controller results under declared assumptions.
- RM0024 supplies a direct first-order coordinated-ramp discrete adjoint with
  finite-difference verification and freeway application.
- RM0025 supplies multiclass network adjoints with merges, diverges and buffers.
- FB0008/FB0009 supply fairness-aware feedback and nonlinear/data-driven
  coordinated control.
- FHWA guidance supplies finite storage, queue override and operational ramp
  management obligations.

These sources make generic ramp differentiation and queue control prior art.
They also provide the strong lower-resolution comparator required for any
method-first candidate.

### Local merge-opportunity mechanisms

- RM0004 and FB0030 supply lane-specific continuous conservation, lateral
  transfers and lane-dependent receiving/capacity behavior.
- RM0011 and the historical evidence debate identify acceleration, lane change,
  safe gaps and driver interaction as plausible nonaggregate merge mechanisms.
- RM0014 supplies empirical isolated-merge context.
- The S12 source family adds finite target receiving, gap-weighted lateral work,
  lane-change void/capacity effects and analytical active-merge capacity.

Method-first use: these establish several candidate representations of local
merge opportunity. They are not required to fit current project components and
no one family is selected by RM7.

### Downstream route-access and spillover mechanisms

- Cassidy's ramp/diverge analysis supports metering changing admitted route
  composition and downstream restricted-exit demand.
- RM0016 supplies destination-aware aggregate control, off-ramp queue/spillover
  structure and a strong route-aware comparator, while retaining the historical
  equation/reproduction qualification.
- FIFOQ and destination-aware aggregate states show that route memory can be
  retained without exact local order.

Method-first use: F2 is operationally coherent, but its proposed hidden
information must survive strong route-aware and storage-aware aggregate models.

### Coordinated corridor and mesoscopic evaluation

- RM0024, FB0008 and FB0009 show that multiple meters make scalable gradients,
  fairness and MPC relevant.
- Mesoscopic ramp literature reviewed in feedback 20 adds dynamic assignment,
  stochastic/event resolution, route/departure response and network scale.
- Hybrid/microscopic references can resolve local gaps and lane changes while a
  corridor model supplies propagation.

Method-first use: F3 has strong operational and gradient motivation, but network
coordination, forecasting and fairness can obscure whether local hidden merge
information caused any improvement.

## Task-selection implications

| Candidate | Supported opportunity | Strongest confound | Initial judgment |
|---|---|---|---|
| F1 local merge opportunity | Direct actuator-to-merge interaction; clear target-lane/gap/lane-state candidate; small matched setting | State may compress to merge pressure; model family and observable collision unproved | Best first task for isolating information value. |
| F2 downstream route access | Meter changes arrival composition/timing at fixed restriction | Route-aware aggregate memory and storage may already suffice; overlaps ordered-service question | Viable secondary task, weaker first choice. |
| F3 coordinated multi-ramp | High-dimensional gradients and interacting local merge states | Coordination, fairness, forecast and network spillback confound the local information contrast | Valuable extension after a local case, poor first isolation task. |

## Evidence boundary

The earlier review's incompatibility conclusions are not used as task-selection
stops. Conversely, removing those stops does not establish that microscopic or
lane-resolved detail is necessary. The selected task must next undergo a fresh
predecessor/mechanism review comparable to the VSL line's N2 stage.
