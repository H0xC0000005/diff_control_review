# S06 reference-first source and mechanism audit

Date: 2026-09-17. Scope: documentary review; selected primary methods/results,
not a comprehensive absence/novelty survey. New S06 IDs do not overwrite FB IDs.
Remote texts are inspected online, not newly archived or locally checksum-verified.
No source supplies this review's original preparation-timing deduction.

## S06-S1 — Erdmann2015, SUMO's Lane-Changing Model

[DLR primary manuscript](https://elib.dlr.de/102254/1/Springer-SUMOs_Lane_changing_model.pdf),
DOI10.1007/978-3-319-15024-6_7; 17-page manuscript. Inspected sections3–6 and10.1.
**Mechanism-only, full selected methods.** Strategic urgency uses distance,
speed history and lane occupation; blocked changes can alter ego/blocker speeds.
Safety gaps and cooperative adjustments couple longitudinal/lateral behavior.
Tactical change uses accumulated benefit with a threshold/reset, despite its
probability-like variable name. Evaluation changes lane-model behavior, not
common-advice information. Supports a native coupling basis, not our advice
benefit, exact collision or gradients. Authorship is Erdmann, not Krajzewicz.
Do not transplant its discrete mechanisms into the candidate mass model or
construe them as a Gap7 exception. No installed-version claim.

## S06-S2 — Knoop/Duret/Buisson/van Arem2010

Lane distribution of traffic near merging zones: Influence of variable speed limits;
DOI10.1109/ITSC.2010.5625034, IEEEITSC485–490.
[Institutional identity](https://research.tudelft.nl/en/publications/lane-distribution-of-traffic-near-merging-zones-influence-of-vari),
[author-uploaded primary paper text](https://www.researchgate.net/publication/224190648_Lane_distribution_of_traffic_near_merging_zones_influence_of_variable_speed_limits).
Inspected sectionsIV–VI; **field mechanism evidence, not a decision certificate.**
Lane-specific loops compare ramp/no-ramp locations and speed-limit conditions;
heavy congestion and rain are filtered. Lower limits increase right-lane use,
with competing utilization/gap implications. Net capacity effects are discussed,
not a matched-state advice experiment. Regulatory/on-ramp evidence does not
validate voluntary lane-drop advice. [Author erratum](https://www.victorknoop.eu/research/):
figure5 panels/headings swapped relative to captions; no panel-derived numbers used.

## S06-S3 — Zhang/Chung/Sabar/Bhaskar/Ma2023

Optimisation of variable speed limits at the freeway lane drop bottleneck;
DOI10.1080/23249935.2022.2033878.
[Institutional manuscript](https://ira.lib.polyu.edu.hk/bitstream/10397/92568/1/Zhang_Optimization_Speed_Freeway.pdf),
44pages; [published identity](https://research.polyu.edu.hk/en/publications/optimisation-of-variable-speed-limits-at-the-freeway-lane-drop-bo/).
Inspected sections2,4.1–4.3,5; **lane-drop regulatory mechanism/boundary evidence.**
Aimsun native interactions support optimized segment-wide limits; objective is
finite-horizon discharge. Calibration/validation uses100km/h; extrapolation to
low limits is qualified. Beneficial profiles include much lower minima than
our advice range. CTM crosscheck prescribes density-triggered capacity drop and
uses a micro-informed search domain. It is not an independent information-only
comparison or all-cohort clearance certificate. No derivative evidence adopted.

## S06-S4 — Reused FB0005 advisory experiment report

[Verified archived full text](../archive/full_text/FB0005.pdf), official
[Caltrans report](https://dot.ca.gov/-/media/dot-media/programs/research-innovation-system-information/documents/final-reports/ca18-2447-finalreport-a11y.pdf).
ReportUCB-ITS-PRR-2019-02; title dateSeptember25,2018. Reinspected PDFpp24–25,
34–36,39; prior N2 extraction retained. **Direct advisory outcome precedent,
not lane-information or merge-causality evidence.**

Aggregate occupancy/speed feedback feeds roadside common advice. Aimsun
calibration includes native lane-change cooperation and distance zones, alongside
existing ramp management. TTT explicitly includes entrance-ramp queues. Table3.2
reports−2.53%,−3.3%,−4.84% for nominal10/25/50% compliance; prose misassigns
approximately−3.5% to50%, while the table's average is−3.56%. Use table values
with this qualification. Calibration reproduction uses the same demand period,
not an independent held-out calibration test. Field before/after evidence does
not isolate merging or test equal complete histories.

Inference for this review: aggregate observations can already support useful
advice in a richer evaluator; their existence rules out neither hidden information
value nor a strong aggregate controller. Fixed homogeneous response0.5 is not
calibrated by these nominal compliance cases. Ramp-inclusive TTT is a useful
accounting precedent but not proof that every intended cohort is fully cleared.

## S06-S5 — Reused FB0039 Soriguera et al.2017

[Verified archived full text](../archive/full_text/FB0039.pdf),
DOI10.1016/j.trc.2017.01.024. Reinspected PDFpp5–6,10,16–17:
sections2–3,5.1,6–7. **Regulatory field mechanism/counterevidence.**

Three fixed, punctually enforced limit days at one measurement site do not test
dynamic voluntary advice. Importantly, lane-flow fractions are almost insensitive
to limit at the same aggregate occupancy in this dataset (reported differences
at most2.6percentage points), despite different distributions at the same flow.
Lower limits at moderate demand can increase lane changing. Stationary analysis
does not settle transient causality or recoverability from complete history.

Inference: even apparently lane-sensitive effects can partly track retained
aggregate variables. Do not claim information loss from a same-flow comparison;
occupancy, response, regime and histories belong in the strong comparator.

## S06-S6 — Reused FB0038 lateral-control study

[Prior full-method extraction](rb_source_studies/new_lane_evidence.md),
[verified archive](../archive/full_text/FB0038.pdf),
DOI10.1177/0361198120948055. **Boundary mechanism only; prior E3 reused.**
Spatial spreading and continuing-lane balance motivate candidate statistics,
but controlled lateral fractions with natural lane changing disabled do not
establish the common-advice actuator. The tested2→1 counterexample and source
waiting qualification remain intact. No source equation or branch is repaired.

## S06-M1 — Original reachability screen of the prospective design

Inputs are the [existing technical contract](../synthesis/s04/rb_diagnostic_technical_contract.md),
not observed trajectories: entry at the road start, upstream length2,400m,
contrast region2,000–2,400m, intended speed ceiling100km/h, acceleration2.6m/s²,
first intended entry0s and then every4s until120s. Entry position/speed were
not explicitly pinned in that contract. [Official vehicle-definition methodology](https://sumo.dlr.de/docs/Definition_of_Vehicles,_Vehicle_Types,_and_Routes.html)
documents base position (front at vehicle length) and default departure speed0;
these are a conditional screen, not adopted installed defaults.

With a5m front position, even instantaneous travel at100km/h cannot reach the
contrast region before71.82s. Therefore40/60s fail the region condition under
this intended entry/speed contract, regardless of insertion delay or merging.
At80s, ignoring acceleration permits at most three entrants (timestamps0,4,8).
With zero departure speed and continuous acceleration bounded by2.6m/s², the
earliest arrival bound is77.16188034s, leaving at most the first entrant by80s.
Advice-induced slowing, safety and insertion waiting only tighten these bounds.

These are continuous-time kinematic ceiling calculations, not exact discrete
SUMO predictions; time-step endpoint conventions can affect the tight80s count.
The robust40/60s exclusion remains. Native anticipatory lane changes may further
erase the ending-lane contrast, but no such erasure or matching failure was measured.
No decision-benefit impossibility follows from the sparse snapshot.

## Overall evidence boundary

Native coupling, speed-dependent redistribution and useful aggregate-observation
advice each have precedents. None of these inspected sources jointly establishes
a reachable consequential full-history collision, different useful shared advice
in the approved response/range, minimal sufficient mass state and independently
useful gradients. This is a bounded extraction result, not literature-wide absence.
No inaccessible paper is decision-critical to this stopping finding.
