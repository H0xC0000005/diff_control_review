# S11 temporary-closure recovery source audit

Date: 2026-09-30. Scope: bounded methodology-only review under the approved
[S11 plan](../s11_00_temporary_closure_recovery_admission_review.md). No traffic
execution, model construction or gradient calculation was performed.

## Audit question and evidence rule

The target is not whether reopening, VSL, lane changing or recovery discharge
exists separately. The target is a defensible chain:

`common lane-uniform advice → preparation → hidden lane/gap/order state at a
fixed reopening → transient service → useful decision`,

with the same declared strong aggregate history available to the comparator.
Direct full-method evidence can support a link. Evidence transferred across a
different actuator, geometry or phase remains qualified. A favorable
state-dependent discharge term is not evidence merely because it could be placed
in a model.

Evidence grades follow the existing pack: E3 is inspected full method/result
material; E2 is inspected primary abstract or selected primary content; E1 is a
discovery lead. The bounded search and access trail is in
[the query log](../search/s11_temporary_closure_recovery_query_log.csv) and
[access log](../search/s11_temporary_closure_recovery_access_log.csv).

## Reused sources

| Source | What it establishes | Boundary for S11 |
|---|---|---|
| [FB0021 full-text audit](n2_source_studies/FB0021.md) | An aggregate kinematic-wave model removes a severe exogenous bottleneck, restores capacity, counts delay through complete queue clearance and derives analytical parameter sensitivities. | Reopening, recovery-tail accounting and aggregate sensitivity are established prior art. The control uses moving fronts and the state has no hidden lane/gap/order information. |
| FB0006, archived official incident/ramp-closure report | Control effects during blockage and after clearance can differ. | The actuator is ramp closure and the study does not condition recovery on hidden mainline lane/gap/order state under a common VSL. |
| FB0011, archived FHWA work-zone ITS guide | VSL upstream of lane closures is operationally coherent. | Operational guidance does not establish a recovery-state mechanism or useful-action distinction. |
| [S06-S2 prior extraction](s06_reference_mechanism_source_audit.md#s06-s2--knoopduretbuissonvan-arem2010) | Field lane-specific measurements associate lower regulatory limits with changed lane use near merging zones. | On-ramp/regulatory evidence supplies an advice-to-lane-distribution link, not a fixed-reopening decision certificate. |
| [S06-S1 prior extraction](s06_reference_mechanism_source_audit.md#s06-s1--erdmann2015-sumos-lane-changing-model) | Strategic urgency, safety gaps, leaders and speed adjustment form a plausible coupled microscopic mechanism. | Simulator mechanism documentation is not independent traffic evidence for a beneficial sign or a minimum state. |

## New S11 sources

### S11-S1 — Banks, Amin, Cassidy and Chung (2003)

[Final California PATH report](https://escholarship.org/content/qt550516vw/qt550516vw_noSplash_b3bc47e74e7827dbbe911b1f12119b31.pdf),
UCB-ITS-PRR-2003-14, 93 pages; E3. The report studies lane-by-lane traffic and
incident recovery. It records post-clearance recovery that was gradual over
12–30+ minutes in some cases and abrupt over 2–5 minutes in others. It reports
individual-lane and total flows and speeds and notes that downstream and ramp
flows can affect the observations.

This directly establishes that restored lane availability need not imply an
instantaneous return to one fixed capacity. It also makes lane-resolved recovery
an empirically meaningful diagnostic. It does **not** establish that a particular
pre-reopening lane distribution, gap pattern or order caused the observed
recovery differences. The report found several tested behavioral-theory
predictions oversimplified or unverified, including distinct downstream capacity
and discharge states. It contains no VSL comparison and no matched aggregate
history.

### S11-S2 — Fudala and Fontaine (2010)

[Official VTRC/FHWA final report](https://rosap.ntl.bts.gov/view/dot/20237/dot_20237_DS1.pdf),
VTRC 10-R20, 47 pages; E3. The field system operated around changing work-zone
lane closures. The field evaluation was inconclusive because closure location,
demand, work activity and system activation varied, compliance was poor and the
algorithm could react late. The calibrated VISSIM study compared four-to-one and
four-to-two closures. VSL algorithm and compliance affected lane-change counts;
the milder closure produced mobility benefits in the studied simulation, whereas
the severe closure did not. Runs continued until congestion cleared.

This establishes that lane-uniform VSL is a coherent actuator in the selected
closure domain and can be associated with preparation/lane-change differences.
It does not isolate an in-run lane reopening or condition post-reopening service
on hidden state. Its lane-change result is a simulation output with calibrated
microscopic behavior, not proof that lane changes caused the travel-time result.
It supplies no strong-observer comparison or gradient evidence.

### S11-S3 — Oh and Yeo (2015)

[Published primary record](https://doi.org/10.1016/j.trb.2015.03.017),
Transportation Research Part B 77:88–102; E2 because only the publisher abstract
and selected indexed primary content were available. Individual trajectories at
active bottlenecks associate stop-and-go severity and lane-change behavior with
recovery discharge. Lane changers can create a transient flow increase before
relaxation, while their disturbance can create waves and later reduce discharge.

This is the closest direct lane/gap/order-to-discharge mechanism found. It is not
an exogenous closure-removal study, does not use VSL, does not hold aggregate
history fixed and does not establish a favorable advice-dependent sign. It can
support a cross-context hypothesis, not the joint S11 chain under G4-A.

### S11-S4 — Chen, Knoop, Liu, Li and Wang (2023)

[Final published institutional full text](https://pure.tudelft.nl/ws/portalfiles/portal/142225723/How_gaps_are_created_during_anticipation_of_lane_changes.pdf),
Transportmetrica B 11(1):958–978; E3. Drone trajectories at three merging
bottlenecks show that lane-change anticipation can cause the target-lane follower
to create a gap and reduce speed. The response depends on relational quantities
including relative speeds, the lane changer–follower headway and the follower's
initial reaction state.

This supports the scientific meaning of hidden gap/leader/history variables and
shows why lane occupancy alone is not a complete microscopic mechanism. It does
not link those variables to service after a fixed reopening, test a common VSL,
compare aggregate observers or rank actions.

### S11-S5 — Knoop, Hoogendoorn and Adams (2009)

[Primary journal record](https://journals.open.tudelft.nl/ejtir/article/view/3318),
European Journal of Transport and Infrastructure Research 9(4); E2. Across 90
incidents, a blocked driving lane was associated with substantially reduced
per-open-lane queue discharge during the incident.

This supports the physical importance of lane blockage and incident-specific
capacity. It concerns the blockage phase rather than hidden-state-dependent
service after reopening.

### S11-S6/S7 — FHWA performance-measure guidance

FHWA's [TMP effectiveness findings](https://ops.fhwa.dot.gov/wz/resources/publications/fhwahop12043/s3.htm)
and [work-zone delay/queue primer](https://ops.fhwa.dot.gov/wz/resources/publications/fhwahop11033/estimating.htm)
are E3 official guidance. They treat delay, travel time, throughput, speed, queue
length and clearance time as distinct measures. Queue and delay describe related
but nonidentical consequences. These sources justify retaining a metric set; they
do not identify which measure proves hidden-state control value.

## Claim-level result

| Required claim | Evidence result | Status |
|---|---|---|
| Fixed exogenous closure/reopening is operationally coherent | FB0006, FB0011, FB0021 and S11-S1 support the event and recovery phase. | Established. |
| Lane-uniform VSL is coherent for a temporary mainline closure | S11-S2 and FB0011 directly support the domain/actuator pairing. | Established, with field-effectiveness qualifications. |
| Common advice can alter lane preparation | S06-S2 field evidence and S11-S2 simulation evidence support lane-distribution or lane-change response. | Supported across related closure/merge settings; exact S11 response law absent. |
| Lane/gap/order state can alter transient discharge | S11-S3 and S11-S4 support lane-change gap/relaxation mechanisms; S11-S1 shows transient lane-resolved post-clearance flow. | Mechanism supported across separate contexts; direct fixed-reopening link absent. |
| The pre-reopening hidden state determines post-reopening service after conditioning on aggregate queue/state | No inspected source performs this conditioning. | Unresolved. |
| A strong aggregate history cannot recover the relevant distinction | No inspected source compares exact aggregate histories or observer sufficiency. | Unresolved. |
| The hidden-state effect changes the useful common-VSL decision | No source supplies a matched action-ranking comparison with complete accounting. | Unsupported. |
| A combined useful gradient exists | FB0021 supplies aggregate analytical sensitivity only. No lane-aware reopening decision gradient or independent usefulness test was found. | Unsupported. |

## Bounded-search conclusion

The search found a physically credible **composed hypothesis**: common VSL can
change preparation; lane-change anticipation and relaxation depend on relational
gap state and can affect discharge; post-incident service can recover gradually.
The critical joins are unverified. No inspected primary source shows that the
state present at a fixed reopening changes transient service after conditioning
on a strong aggregate history, or that this changes the best common VSL action.

Therefore the evidence does not satisfy the default G4-A admission threshold.
This is a bounded evidence gap, not proof that the mechanism is absent. Admitting
a later protocol would require either explicit acceptance of cross-context
transfer (G4-C) or new direct evidence. Requiring a complete certificate in S11
(G4-B) would also fail and would exceed the approved admission-review scope.
