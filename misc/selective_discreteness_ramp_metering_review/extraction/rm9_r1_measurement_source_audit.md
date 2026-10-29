# RM9-R1 measurement source audit

Date: 2026-10-05. Status: **Bounded evidence pass finished to UG4-O; no observer adopted.**
Authority: accepted [brief plan](../synthesis/rm9/rm9_next_review_brief_plan.md).
Method: existing source reuse plus targeted primary-source searches and selected
method-section inspection. This is not an exhaustive measurement review.

## Source records and exact claim limits

| ID | Inspected material | Supported observation issue | Limit for RM9 |
|---|---|---|---|
| FB0030, reused | Existing final PDF, printed 1768–1769, PDF pp. 13–14; primary web PDF rechecked | One-minute lane detector flow/speed supplies estimated density; authors distinguish measured time means from model space means and acknowledge congestion bias. | Density in that calibration is not independently measured exact cell inventory; their simplification does not validate our congested cell-to-face passage map. No source algorithm is repaired or adopted. |
| RM9-O01 | FHWA Traffic Monitoring Guide 2022, Traffic Data Collection: Speed; Lane Occupancy; Headway and Gap | Dual-loop transit timing can measure vehicle speed separately from count. Occupancy is the percentage of detector-zone time occupied. | Neither occupancy nor a point count supplies true spatial cell mass automatically. Vehicle event/lane records are richer than the admitted road-total aggregate channel and are not silently supplied to the comparator. |
| RM9-O02 | FHWA Data Quality White Paper, Section 4.3.2 Speed | Passage time means use flow weights; section space means use density weights. | The point-sample harmonic interpretation does not warrant replacing a transient section mean with any arbitrary face-flow/cell-density ratio. Hardware error/noise is not used to manufacture exact hiddenness. |
| RM9-O03 | Jamshidnejad/De Schutter 2015, author report 15-035, PDF pp. 2–3, Sections I–II | Loop time means differ from generalized time-space means; traffic retained inside a section over several sampling cycles needs accounting. | This is an estimation precedent, not an exact inverse for our lateral CTM. No NGSIM experiment or estimator was executed here. |
| RM9-O04 | Jamshidnejad/De Schutter, author report 17-001, 2018 publication version identified on cover; Sections 2.1, 4.1–4.2, 5; PDF pp. 4, 9, 12–14 | Generalized variables share a space-time region; initial internal traffic and trajectory assumptions enter point-to-section reconstruction. | Section 4.2's multilane extension assumes no lane changes. Section 5 adds a trajectory approximation. These are serious transfer boundaries, not a source theorem identifying RM9's lane state. |

Primary links:

- [FB0030](https://repository.tudelft.nl/file/File_2c4359e7-5e5a-4651-964f-6f3610ab89ae)
- [RM9-O01](https://www.fhwa.dot.gov/policyinformation/tmguide/tmg_2022/traffic-data-collection.cfm)
- [RM9-O02](https://ops.fhwa.dot.gov/publications/fhwahop08038/04infoshare.htm)
- [RM9-O03](https://www.dcsc.tudelft.nl/~bdeschutter/pub/rep/15_035.pdf)
- [RM9-O04](https://www.dcsc.tudelft.nl/~bdeschutter/pub/rep/17_001.pdf)

New sources were inspected through public primary web pages/PDFs; no new binary
archive was downloaded. Reused FB0030 locally with pypdf. Versions, locations
and URLs are recorded in [screening](../screening/rm9_records.csv); executed
searches are in the [query log](../search/rm9_query_log.csv). The initial Edie
search returned indirect leads; definitions are supported here by the inspected
author research texts, not claimed as a fresh inspection of Edie's original.
The Berkeley CTM page is metadata orientation only, not a new method claim.

## R1 evidence/observer/task matrix

| Channel / context | Physical meaning and support | What the current law supplies | Disposition |
|---|---|---|---|
| True cell total | Traffic mass in a declared road section at an instant, summed across two lanes | Sum of stored lane masses | Retain as a strong idealized observation; do not claim ordinary loops measure it exactly. Density uses the declared section length/normalization. |
| Accepted face flow / cumulative count | Passage over a labeled mainline face in a completed interval; counts integrate actual flow | Sum of accepted longitudinal lane flows, with merge/ramp contributions labeled | Can transcribe exactly in the discrete benchmark. Do not confuse total downstream passage with donor-mainline service alone. |
| Detector occupancy | Fraction of a detector window covered by vehicles | No detector-length/vehicle-length realization in the current kernel | Do not substitute for exact cell inventory. Not an added hidden-state or noise mechanism. |
| Passage time-mean speed | Arithmetic mean over actual passing traffic at a station/window; lane means need passage weights | Accepted lane flows, but no fully justified physical crossing-speed map in congestion | Physical metric grounded; current state-to-measurement closure remains unresolved. Historical UG4.A is an explicit approximation, not source validation. |
| Instantaneous section speed | Density/mass-weighted longitudinal speed of traffic present in a road section | A representative equilibrium lane speed can be assigned from the existing FD parameters | New candidate C: avoids an upstream-cell-to-detector identification, but cell homogenization/equilibrium is still a declared modeling approximation. |
| Generalized time-space speed | Distance traveled divided by time spent over the same space-time region | Conserved occupancy and face counts do not alone prescribe internal traveled distance without a reconstruction | Legitimate metric, but not automatically accepted face flow divided by instantaneous cell density. Not recommended as an extra model extension in R1. |
| Ramp history | External waiting, pre-meter storage, actual releases, post-meter storage and actual merge entries, where present | Allocator and local conservation; exact ramp layout remains to transcribe | Keep each physical compartment/boundary identifiable. Meter permission is not automatically actual release or downstream merge flow. |
| Initialization / forcing | Common history begins at a stated epoch; all model inputs and boundary allocation rules are public | Deterministic update with structural lane parameters | Fully known initial full state plus public forcing is trivially reconstructible. Any initial uncertainty must respect every admitted observation, not arise from private prehistory/forcing. |
| Control timing | A common future open-loop schedule chosen after the admitted history | Lateral stage followed by forward/meter stage | Completed observations only; no candidate future flow or repeated feedback decision is added. |

## Reviewer inferences and limits

1. There is no source-backed universal identity equating physical point speed,
   true instantaneous cell density and accepted boundary flow in transient merge
   conditions. The inspected definitions have different supports.
2. Same-region generalized flow/density/speed obey their own identity. That
   does not make passage speed redundant with our face flow and cell mass.
3. A section-average observer can be defined without the historical passage
   approximation, provided its speed closure is explicitly admitted. It is a
   new viable G1 candidate, not a modification of approved G2 traffic dynamics.
4. Under that candidate's free-flow FD closure, exact section mass and speed
   already identify a two-lane split when known lane speeds differ. This is a
   diagnostic consequence of the proposed observer, not a field theorem or
   an R2 full-history classification. It does not favor a positive hiddenness result.
5. Source-specific estimation assumptions and access limitations cannot be
   converted into a necessity proof or a reason to run SUMO.

Mathematical definitions and stage/history/ramp accounting are in the
[R1 PDF](../synthesis/rm9/rm9_r1_observation_contract_audit.pdf). The full
scientific decision and smallest alternatives are in the
[UG4-O report](../reporting/rm9_60_r1_observation_findings_and_gate.md).
