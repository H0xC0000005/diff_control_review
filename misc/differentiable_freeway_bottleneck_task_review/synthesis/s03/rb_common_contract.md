# Route B — common-contract recommendations at RB-UG1

Date: 2026-09-17. Review closed; Option A diagnostic planning approved.
Detailed contract recommendations remain inputs to the separate proposal,
not approved experiment equations or settings.
No numerical settings, exact equations, evaluator build or model selected.

## Strong comparator

First credible family: spatial homogeneous dynamics retaining continuous mass/
density, mean speed/response, upstream queues and finite downstream receiving.
Frejo2019 and Seliman2020 provide inspected dynamic-mean-speed precedents.
Entry/advice exposure history can matter; Wei2025 and the Raadsen/Bliemer2021
lead limit use of an instantaneous history-free comparator. A strong model
need not retain all imaginable past observations: specify its actual information/
memory and check competing credible aggregate families, rather than constructing
an undefined omniscient baseline.

Response calibration, capacity/discharge, propagation resolution and parameter
flexibility must not change unfairly with lane detail. Lane-group information
is a proposed addition, not an excuse to omit mean-speed/history physics from
the aggregate comparator. Aggregate observers inferred from past counts/speeds
are a potential simpler alternative; they are not proved sufficient either.

## Action and response

Same advice per spatial zone/update interval on every lane. Feasibility and
perturbation support match across representations. No optimized lateral flows,
lane-specific limits, vehicle-specific control targets or extra actuators.

Later design must declare whether advice is continuously available inside a
zone or retained after passing a sign; the model/evaluator must use the same
exposure semantics. This is a contract recommendation still needing later
approval, not evidence that a source's sign-limit law models voluntary advice.

SUMO official docs distinguish changing speedFactor/maxSpeed from setSpeed/
slowDown, and document endogenous strategic/cooperative/speed-gain lane changes.
This supports an inspectable desired-response interface; it does not validate
a dynamic human-advice response model. Mapping shared advice into desired-speed
parameters would remain an explicit synthetic modeling assumption. Safety,
car-following and lane-change realization must not be overridden to enforce
our target motion. Rolling online docs inspected2026-09-17; no installed version
or functioning adapter is verified.
[Vehicle-state docs](https://sumo.dlr.de/docs/TraCI/Change_Vehicle_State.html).

## Population, reference and accounting

Hold demand, routes, driver/vehicle population, geometry, incident and future
advice candidates fixed. Different preparation conditions must be disclosed.
Pair reference populations/randomness exogenously if later sampling is used;
do not resample control-dependent response/lane memberships in the candidate.

Use an independently implemented richer reference for action outcomes, not the
same lane equations as their own truth. Current sources support synthetic
microscopic evaluation as plausible, not a ready reproducible empirical bundle.
Calibration and held-out action evaluation must be separated. Match observation/
fitting opportunity and later optimizer budgets; grid/parameter variation is
an explicit robustness obligation.

Provisional primary metric: all-population time spent, including upstream
waiting from intended entry. For fixed routes/population, comparable delay
can be reported against a shared free-flow reference; no arbitrary policy
weights added. Also record discharge, storage, completion and failures.
Temporary closures require post-reopening clearance or an explicitly approved
complete residual-accounting rule. Stops/speed fit alone do not replace this.

Subraveti2020 equation12 includes both network occupancy and origin waiting;
this accounting is established, not novelty. SUMO TripInfo differentiates
departDelay from duration and normally omits unfinished trips unless requested.
Pending not-yet-inserted demand still needs an explicit external ledger.
[TripInfo docs](https://sumo.dlr.de/docs/Simulation/Output/TripInfo.html).

## Disturbance and unresolved feasibility

Fixed closure/reopening is not a differentiated decision. SUMO permission
closures can provoke emergency braking or route changes; these must not become
silent experimental confounds.
[Rerouter docs](https://sumo.dlr.de/docs/Simulation/Rerouter.html).
A static physical lane reduction avoids some transition-interface issues but
does not by itself answer temporary recovery. No scenario subclass is frozen.

The supplied Chen2025 predecessor uses a four-type-aware expected flow law,
not separately transported four-class masses; its NSGA-II/MPC VSL/no-VSL
comparison does not identify the benefit of added lane state. Source settings,
discrete speed choices and dual safety objective are not adopted. See
[verified source study](../../extraction/rb_source_studies/FB0040.md).

Open issues: dynamic advice-response validation, lawful parameter/data support,
reachable matched initialization/history and emergent discharge behavior.
Neither Chen2025 nor the new incident study supplies this whole common contract.
Installed-software
absence in the earlier selected environment is not host-wide unavailability.
No setup, calibration or traffic run was performed.
