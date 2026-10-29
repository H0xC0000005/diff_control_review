# N2 common-evaluator feasibility screen

Date: 2026-09-16. **Plausible but not established.** Documentary/API inspection
only; no traffic run, installation, calibration or evaluator choice frozen.
Selected Python environment 3.11.9 has neither `traci` nor `sumolib`; `sumo`
is not on this session's PATH. This is not a claim of host-wide unavailability.
Official online documentation is rolling, inspected this date; no installed
SUMO version/build is verified.

| Contract | Evidence / unresolved condition |
|---|---|
| Advice, not pedal or regulatory actuator | [SUMO VSS docs](https://sumo.dlr.de/docs/Simulation/Variable_Speed_Signs.html) change lane limits. Native VSS alone does not establish voluntary-advice behavior. Proposed common per-driver response map may update desired-speed parameters, while CF/LC decides realized motion; later implementation audit required. No optimizer-per-vehicle actions. |
| Fixed population response | [Vehicle type docs](https://sumo.dlr.de/docs/Definition_of_Vehicles,_Vehicle_Types,_and_Routes.html) distinguish fixed individual speedFactor from type-level distribution mean/spread; default spread need not vanish. [TraCI vehicle state docs](https://sumo.dlr.de/docs/TraCI/Change_Vehicle_State.html) distinguish speedFactor/maxSpeed from setSpeed/slowDown. FB0033 supports calibration, but fixed-limit fit does not identify dynamic advice response. Freeze paired exogenous population draws later; do not sample control-dependent membership. |
| Closure/reopening | [Rerouter docs](https://sumo.dlr.de/docs/Simulation/Rerouter.html) support time-interval lane permissions; rerouting-equipped vehicles can change routes. Keep demand/routes and closure schedule fixed, audit taper/warning and occupied-lane handling. Abrupt permissions can induce emergency braking. Native capability is not validated realistic closure behavior. |
| Storage/discharge/recovery | CF/LC interacts with lane closure; cannot assume desired capacity drop emerges or equals an aggregate FD. Need shared observable targets for onset, discharge, duration and post-reopening clearance. FB0021 supplies analytical accounting, not microscopic calibration values. |
| Objective/population/horizon | Count upstream insertion delay and unfinished traffic, not arrived-only mean travel time. [TripInfo docs](https://sumo.dlr.de/docs/Simulation/Output/TripInfo.html) describe arrival-based output and `--tripinfo-output.write-unfinished`; departDelay is distinct from duration. Pending demand and teleport/drop/error cases need explicit conservation/accounting policy. Extend recovery until clearance or approve a complete residual accounting rule later. |
| Independence and resources | SUMO is independently implemented and documented, but calibrating every model to the same fitted micro outputs is not independent empirical truth. Separate calibration from held-out action evaluation. FB0013 uses VISSIM; its data are by request and its optimization confounded. No VISSIM installation/license checked or assumed. |
| Access | Supplied FB0013/21 resolve batch 1. FB0033 data by request, not a downloaded dataset. FB0027 full text/FB0023 version and other abstract leads remain gaps, not mandatory dependencies for Route B. No second access request issued. |

Minimum next cost: separately approved contract/design review must choose the
claim's empirical versus synthetic-reference level, identify lawful parameter/
data support, define faithful advice realization, and specify a held-out
perturbation/accounting test. If existing materials cannot support this bounded
contract, return for access/scope choice rather than silently installing,
collecting field data, changing the actuator or fitting everything to one curve.
