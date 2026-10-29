# S07 reachable-preparation source and method audit

Date: 2026-09-29. Scope: the minimum primary/native material needed to review
entry semantics, insertion confounding and anticipation. This is not a new
lane-change literature survey and does not establish an installed reference.

## S07-S1 — official vehicle/type/route documentation

[SUMO vehicle definitions](https://sumo.dlr.de/docs/Definition_of_Vehicles,_Vehicle_Types,_and_Routes.html),
rolling official documentation inspected on 2026-09-29. Numeric `departLane`
selects a lane; `departPos="base"` places the vehicle fully on the lane with its
front at vehicle length; default `departSpeed` is zero, while `desired` requests
the desired insertion speed and delays an unsafe departure. Actual departure may
be later when space is unavailable. These semantics support making position and
speed explicit rather than inheriting a default.

The same page currently lists LC2013 defaults `lcStrategic=1`,
`lcStrategicLookahead=3000 m`, and `lcLookaheadLeft=2`. The rolling values are a
warning that native anticipation can span the whole 2,400 m approach, not a
version-pinned setting for a future run. S07 does not change any lane-change
parameter.

## S07-S2 — official insertion documentation

[SUMO vehicle insertion](https://sumo.dlr.de/docs/Simulation/VehicleInsertion.html),
official rolling documentation. Safe insertion checks leaders, followers,
intersections and stops; failed insertion enters a queue and is retried. Step
length and departure position/speed affect attainable spacing. Force insertion,
disabled checks and relocation exist but are inadmissible here because they would
change reachability and safety semantics.

Implication: preparation-specific lane load can change source waiting and actual
entry histories. Since both are retained by the strong comparator, unequal lane
quota patterns risk manufacturing an observable preparation difference before
the intended near-drop test.

## S07-S3 — official capacity methodology

[SUMO road-capacity documentation](https://sumo.dlr.de/docs/Simulation/RoadCapacity.html),
official rolling methodology. It gives the homogeneous Krauss headway relation
and illustrative insertion-capacity tables showing strong sensitivity to
departure speed, step length and placement. Default zero departure speed is the
weakest tabulated convention; desired-speed insertion increases capacity in the
documented examples.

The examples use their own speed and configuration and are not transferred as a
hard capacity bound. They support only the design conclusion that the old peak
quota rates—675/2025/1350, 1350/1350/1350, 2025/1350/675, or
2700/675/675 veh/h by lane—have very different insertion risk. A balanced block
is the least confounded preparation family.

## S07-S4 — reused Erdmann 2015 native model description

[Primary DLR manuscript](https://elib.dlr.de/102254/1/Springer-SUMOs_Lane_changing_model.pdf),
previously inspected in S06 and reinspected at Sections 3–4. Strategic changes
may occur well before a dead lane. The best-lane construction uses downstream
connectivity/occupation; urgency depends on remaining distance, current and
historical speed, required lane changes and occupation. Blocked strategic changes
can request speed changes from the ego and obstructing vehicles.

Implication: differing ending-lane assignments can affect the exact aggregate
speed/count history before the final 400 m. Literature cannot certify an exact
history collision for the native case. A later prefix feasibility run must test
equality first and stop before actions on failure.

## S07-M1 — original kinematic and preparation-bank analysis

The retained [analysis PDF](../synthesis/s07/s07_reachable_preparation_analysis.pdf)
and [LaTeX source](../synthesis/s07/s07_reachable_preparation_analysis.tex) derive:

- strict fastest-arrival screens of 71.8200 s and 77.1619 s;
- nominal advice-aware travel times of 74.0937 s (`desired`) and 79.4356 s
  (zero-speed start);
- nominal final-400 m residence of 14.4134 s;
- peak-arrival/full-region thresholds near 194.1/208.5 s and 199.4/213.8 s;
- nominal final-400 m populations of 17/16/17 at decisions 220/240/260 s under
  both screened insertion conventions; and
- a localized balanced six-vehicle contrast block producing 18 rather than 48
  prefix preparations.

These are continuous-time arithmetic screens. They do not include insertion
delay, following, lane changing, discrete step endpoints or bottleneck queues and
are not reference predictions.

## Evidence boundary

The review identifies one viable low-confounding preparation proposal but cannot
establish exact native history equality or decision relevance. No source supplies
a minimum sufficient lane state, useful advice split, or gradient claim. No
decision-critical source is inaccessible.
