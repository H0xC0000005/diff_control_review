# Route B diagnostic technical contract — approved

Date: 2026-09-17. Status: **Reviewed design; current execution is methodology only.**
Per user clarification, numerical settings/interfaces below are prospective
experiment-design material, not traffic-run authorization. Toolchain/server
configuration is outside this review and is not an open methodological gate.
No observed outcomes, functioning adapter or calibrated response is claimed.
Read the [mainline proposal](../../s04_00_rb_diagnostic_phase_A_proposal.md) first.
These settings are synthetic engineering defaults, not literature-derived
calibration or an accepted minimum model. Changes affecting meaning require
approval under the [question inventory](rb_diagnostic_question_inventory.md).

## 1. Reference and advice semantics

Proposed network: straight 2,400 m three-lane upstream road followed by an
800 m two-lane road, legal limit 100 km/h throughout. SUMO lane 0 is the
rightmost ending lane; declare connections 1→0 and 2→1 only. Inspect generated
connections, connector lengths and lane permissions: no heuristic extra path
from the ending lane is acceptable. Vehicles must merge through native behavior.
One advice zone covers upstream positions 800–2,000 m.

Use homogeneous passenger vehicles with native Krauss following and LC2013 lane
changing. Proposed type values: length 5 m, minimum gap 2.5 m, reaction parameter
tau 1 s, acceleration 2.6 m/s², deceleration 4.5 m/s², physical maximum speed
120 km/h, desired maximum speed 100 km/h, sigma 0, speed deviation 0.
Pin remaining native lane-change parameters to the supplied engine version;
record them before outcomes, without tuning to generate a lane advantage.
Effective response/bounds must be explicit in any later empirical design;
the current review does not inspect or configure local executable APIs.

Baseline advice is 90 km/h, including preparation. Response gain is 0.5:
desired free speed is 100 km/h minus half the difference between 100 and the
advice. Set an individual vehicle's desired-speed factor relative to the fixed
100 km/h road limit; outside the zone restore factor 1. Apply the same rule on
every lane before each simulation step. Audit zone-entry/exit timing.
Native following, lane changing, acceleration and safety determine actual speed.
Do not call actual-speed, forced-lane-change or relocation commands; do not change
road speed limits or disable native safety modes. This is a synthetic homogeneous
response to infrastructure advice, not direct CAV control or empirically measured
compliance. Keep its gain known to the aggregate information channel.

The continuous feasible advice range is 70–100 km/h. Evaluate nine open-loop
probes: unchanged 90; four early pulses of +5, −5, +10, −10 km/h over the first
60 s after decision; four identical-amplitude late pulses over the next 60 s.
Return to baseline outside each pulse. These sample a continuous control space;
neither traffic quantity nor the advice variable is integerized.

## 2. Reachable preparations and pair selection

Start every run empty. Generate deterministic intended departures:

| Intended entry interval | Rate | Population |
|---|---:|---:|
| 0–120 s | 900 veh/h | 30 |
| 120–480 s | 4,050 veh/h | 405 |
| 480–600 s | 2,700 veh/h | 90 |

Use regularly spaced timestamps within each half-open interval: 525 fixed IDs,
one common route, identical type parameters. Native safety-delayed insertion
must be retained and recorded; no maximum-departure-delay removal is permitted.
Intended departures, not successful insertions, define the scored cohort.

For each decision time 40, 60 and 80 s, try 16 predecision lane-entry patterns:
ending-lane quotas 1, 2, 3 or 4 of each six intended vehicles, with four cyclic
phase offsets; allocate the remainder alternately to continuing lanes. Freeze
the exact pattern arrays before runs. From decision time onward, intended
departures use the same two-per-lane six-vehicle pattern in every preparation.
No lane commands follow insertion. Earlier pending entrants retain their original
assignments, which are hidden preparation metadata and must be audited explicitly.

Select at most two exact-matched pairs, within identical decision time/context,
using predecision information only. Require a different lane occupancy vector in
the final upstream 400 m; prioritize its largest total absolute count difference,
then fixed lexical preparation IDs. No minimum positive contrast is invented:
report the actual counts and continuing-lane balance. Never select by action
benefit. Preparation also changes microscopic gaps/order; a positive result would
not prove occupancy alone is causal or sufficient.

If no valid exact pairs remain, stop before action runs. Report candidate counts,
component-by-component matching residuals, disappearing occupancy contrasts and
artifact failures. Do not silently add preparations or change native parameters.

## 3. Strong lane-blind information channel

Record every reference step from empty initialization through decision, including
the actual predecision observation and advice histories. Primary step is 0.5 s.
Use 16 longitudinal 200 m bins plus explicitly mapped internal connector bins;
bin geometry and membership are immutable structural metadata. Cover all active
traffic, not just an upstream detector. For each timestamp/bin store vehicle
count, density in veh/km, mean speed in m/s, empty-bin mask and cumulative entry/
exit counts. Density uses declared physical bin length; connector geometry must
be verified rather than guessed. Empty-bin mean speed is zero with a separate
mask, not an assumed free-flow speed.

Also provide total source waiting, cumulative intended/actual entries and network
exits, all advice history, geometry, route/type/response parameters, future intended
demand and its common lane-entry rule. Known initial condition is empty. Past
per-vehicle lane-entry choices, realized lane IDs, gaps and leader topology are
withheld from the controller but stored for audit. This deliberately specifies
an information-limited controller; it is not a claim about an observer given
those additional inputs.

Arrays have shapes time×bin or time×channel, float64 physical values, integer
counts/indices and Boolean masks, with explicit seconds/metres/vehicle units.
Matching means exact equality of canonical arrays and metadata, not rounding,
tolerance-based equality or a hash alone. Raw arrays accompany checksums.
Numerical audit tolerances do not turn near matches into information collisions.

Project the same records onto 100 m and 400 m grids. Report whether finer
observations distinguish the selected states. A distinction resolved at 100 m
cannot be advertised as grid-independent failure of aggregate information.
Store full histories; no post hoc shorter memory or omitted source queues.

The conclusion is limited to the declared initial open-loop decision channel.
An online feedback controller might later observe the difference and recover;
this experiment does not establish failure of all aggregate feedback policies.
No macro implementation, aggregate gradient or lane-refinement state is built.

## 4. Replays, robustness and hard budget

Replay original network/vehicle inputs from time zero for every action. Do not
branch by saved-state reload: official SUMO documentation warns that internal
lane-changing and some following state are not saved, and RNG/pending-input
handling needs additional care. Verify repeatability first. Disable explicit
probabilistic demand/type draws; record seed 23423 and the full version/build.
Same-seed repeats measure numerical reproducibility, not statistical replication.

Primary selected pairs get all nine probes at 0.5 s and 0.25 s; matching must
remain valid at both steps. Use four frozen held-out contexts, changing only one
feature from primary: response gain 0.25; response gain 1; tau 1.2 s; or peak
demand 4,950 veh/h. The last has 615 intended vehicles, other contexts 525.
Rebuild the full preparation bank and select pairs without action outcomes in
each context. A failed context stays in the report, not discarded as inconvenient.
Primary step and all future inputs are identical within each pair.

| Run category | Maximum invocations |
|---|---:|
| Readiness/development checks | 24 |
| Primary prefixes: 16 preparations × 3 times | 48 |
| Four held-out preparation banks | 192 |
| Actions: 2 pairs × 2 states × 9 probes × (2 primary steps + 4 contexts) | 216 |
| Total hard cap | 480 |

Unused budget is not permission to search new scenarios. Prefix and full replay
are separate invocations. Maximum end time is 2,400 s; require the entire cohort
to arrive. A failure to drain is reported and has no arrived-only finite score.
Readiness covers empty/free-flow accounting, generated connection inspection,
native merge behavior, source insertion delay, advice response/zone timing,
identical-input replay, and a zero-response-gain action-invariance sanity check.
Readiness fixes may correct harness conformance, not change native physics or
weaken acceptance. No field validation or detachment is proposed.

## 5. Accounting and decision evidence

Primary score: mean seconds per intended vehicle from its intended departure
to arrival. All source waiting is included. Audit completed trip duration plus
departure delay against arrival minus intended departure. Independently integrate
a presence ledger from input timestamps and runtime arrival events, separate
from trip output, counting pending
and all on-network vehicles, including connectors. Match IDs and event totals
exactly; floating score agreement tolerance is 1e-6 s/vehicle. Verify output
timestamp precision of at least 12 decimal places in the actual engine rather
than attributing rounded trip-output discrepancies to traffic error.

SUMO timeLoss is not the primary score: its ideal-speed reference depends on the
individual desired-speed factor being changed. Never use arrived-only output,
uncompleted trips, silent demand discard, collision, teleport, vaporization or
off-route outcomes as a successful low-cost run. Disable gridlock teleportation
where supported and audit every cause separately; disabling one cause does not
certify absence of teleportation. Invalid probes prevent certification of a full
menu comparison; do not simply optimize the surviving subset.

For each state report all nine scores and their excess over its best score.
Define an acceptable-action band as the larger of 0.01 s/vehicle and twice the
largest measured repeat/time-step disagreement across the paired menu. This is
a synthetic numerical resolution threshold, not a calibrated practical-value
threshold. Publish raw differences and the envelope; do not relabel tiny effects
as operationally important.

A decision distinction requires disjoint acceptable-action sets and positive
best-common-action worst-state excess above that numerical envelope. Thus a
common third action can invalidate an apparent two-action ranking reversal.
Require the distinction at both primary steps and at least two of four valid
held-out contexts for the proposed robust-positive label. Other context failures
and reversals restrict its domain and remain prominently reported. No averaging
across different populations hides a failure.

Labels: robust finite-menu distinction; common acceptable action in this bounded
domain; or unresolved due to matching, invalidity, integration or robustness.
None establishes continuous optimality, field benefit, minimum state, response
classes/order necessity, internal derivatives or independent gradient usefulness.

## 6. Future implementation interfaces and checks

Only after separate approval/freeze, create reference implementation/input files
under misc/differentiable_freeway_bottleneck_task_review/experiments/rb_diagnostic/:

- Immutable experiment JSON and generated plain-XML network/vehicle inputs.
- Reference runner: config/preparation/action IDs → versioned raw trajectories,
  insertion/arrival/invalidity events; no differentiated model.
- Observation module: raw trajectory/events → the fixed lane-blind arrays and
  hidden-state audit. No state modification.
- Diagnostic module: exact-match registry → outcome table, action bands/regret,
  failure ledger and report. No outcome-based preparation selection.
- Tests: independent bin/accounting examples, exact/near-match distinction,
  common-third-action case, full-history preservation and failure propagation.

A future run_diagnostic.py entry point will expose readiness, prepare, actions
and summarize stages. Summarize must never launch experiments. Unique output
directories refuse overwriting and record config/source hashes, command,
timestamps, versions, seed and stage failures. Exact commands are frozen after
the actual SUMO provider/version and runner have been verified; these are proposed
interfaces, not existing runnable commands. No dependencies or code are added now.
Use the existing package's extraction/ for rb_diagnostic_ matching/action/failure
tables and reporting/ for rb_diagnostic_ validation/findings/work/user-gate reports.
This continues RB-UG1 without merging numerical evidence into closed review logs.

## 7. Source/capability basis and methodological limitation

Official documentation supplies capability distinctions, not voluntary-advice
response calibration or reachable-state/action evidence. Server workability and
local provider/version configuration are excluded under the user's clarification.
Prior environment probes remain historical work records, not current blockers.

- Individual desired-speed factors and native bounds: [vehicle definitions](https://sumo.dlr.de/docs/Definition_of_Vehicles,_Vehicle_Types,_and_Routes.html)
  and [vehicle-state changes](https://sumo.dlr.de/docs/TraCI/Change_Vehicle_State.html).
- Explicit connections: [plain XML network input](https://sumo.dlr.de/docs/Networks/PlainXML.html).
- Saved-state limitations: [save/load documentation](https://sumo.dlr.de/docs/Simulation/SaveAndLoad.html).
- Departure delay, incomplete output and factor-dependent time loss:
  [trip information](https://sumo.dlr.de/docs/Simulation/Output/TripInfo.html).
- Repeatability and separate teleport causes: [randomness](https://sumo.dlr.de/docs/Simulation/Randomness.html)
  and [teleportation](https://sumo.dlr.de/docs/Simulation/Why_Vehicles_are_teleporting.html).

Native lane changes/discrete vehicle trajectories belong to the independent
reference, not the proposed differentiated meso stack. Their presence does not
waive Gap 7 or introduce moving categorical probability mass in a candidate.
