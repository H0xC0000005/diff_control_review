# RM11 C0 — primary-source task and information audit

Date: 2026-10-05. Selected methods, not an exhaustive review. Source IDs are
deduplicated against the existing ramp/VSL records. The following are source
observations; the admission deductions are in the
[spatial/history/action audit](../../synthesis/rm11/c0_spatial_history_action_audit.md).
No source is required to prove our entire claim by itself. Combining sources
still requires an explicit, consistent methodological argument.

## Physical finite-lane evidence

**RM11-P01 — Marczak, Daamen and Buisson (2013), _Merging behaviour: Empirical
comparison between two sites and new theory development_.** Published TRC 36,
530–546, DOI 10.1016/j.trc.2013.07.007. [Original project-hosted paper](https://mocopo.ifsttar.fr/fileadmin/contributeurs/Mocopo/Documents/Other_documents/Article_-_Merging_behaviour_-_Empirical_comparison_between_two_sites_and_new_theory_development.pdf),
17 PDF pages. Selected Sections 3.1–3.3, 4.3–4.5, 5–6; printed pp. 536–544.

Bodegraven has a 283 m acceleration lane; Grenoble has a 210 m lane and arrival
platoons produced by a traffic signal 2 km upstream. That signal is not established
here as a local ramp-meter actuator. Trajectories describe positions and speeds;
Grenoble's analysed observation periods are discontinuous. In the logistic
gap-acceptance analysis, position is significant at Grenoble but not Bodegraven.
Neither site's analysis finds a merging-speed trend with position. Section 5
reports no observed vehicle unable to merge; it does not establish a universal
guarantee of successful merging. These findings support finite spatial behavior,
not an automatic end-of-lane blockage law. The fitted conditional probability is
not a conservative transient traffic/control model. The study does not establish
our exact aggregate/full-history information contract or common rate/TST action
distinction. Its trajectory recordings are research observations, not evidence
that a real controller knows every physical initial coordinate.

**RM11-P02 — van Beinum, Farah, Wegman and Hoogendoorn (2018), _Driving behaviour
at motorway ramps and weaving segments based on empirical trajectory data_.**
DOI 10.1016/j.trc.2018.05.018. [Accepted author manuscript](https://repository.tudelft.nl/file/File_c4adbb04-ba31-4286-91bb-6f15bfb7ba23),
25 PDF pages including cover; [institutional metadata](https://research.tudelft.nl/en/publications/driving-behaviour-at-motorway-ramps-and-weaving-segments-based-on/).
Selected Sections 2.5, 3.1–3.2, 5–6, especially manuscript Table 1 on p. 8.

The study observes fourteen sites in free flow. Its A59 Terheijden on-ramp is a
genuine two-through-lane plus acceleration-lane configuration, with a 320 m
acceleration lane. Thus two-lane finite geometry need not be invented. Helicopter
video provides trajectories over roughly 1.2–1.5 km, for thirty minutes at each
site; processing corrects tracking/measurement problems. The source distinguishes
trajectory behavior from what loop data capture at an individual level. It does
not supply a ramp-rate intervention study, the initial knowledge of a controller,
or a full-history observability result under our idealized channels. Free-flow
observed maneuvers alone do not validate congested end-of-lane receiving/storage
semantics. Availability of detailed research data cannot grant a comparator
unobserved fine initialization.

## Lane-macroscopic and rate-control competitors

**FB0030 — _First order multi-lane traffic flow model — an incentive based
macroscopic model to represent lane change dynamics_, 2019 online/2020 published
body.** [Institutional original](https://repository.tudelft.nl/file/File_2c4359e7-5e5a-4651-964f-6f3610ab89ae),
24 PDF pages. Selected modelling framework and incentives, printed pp. 1760–1764.

The model has longitudinal lane-cell conservation and lateral transfer constrained
by target-lane receiving. Route/end-distance, cooperation and downstream density
enter lane-changing incentives. It offers a spatial, continuous lane-state rival
to a point-merge description. Its field checks are not a complete ramp-rate,
finite-lane, hidden-history task. Retaining lane densities is already retaining
lane information; calling the model macroscopic does not make it an information-
hiding aggregate comparator. Public cell location and lane-end geometry are not
hidden traffic coordinates.

**RM0004 — _Lane Change Control Combined with Ramp Metering: A Strategy to
Manage Delays at On-Ramp Merging Sections_ (2021).** [Final original](https://repository.tudelft.nl/file/File_3728cefd-b910-49de-a341-d342fbbd5369),
13 PDF pages; selected Sections 2.1–3.1 and 4.

The model prioritizes entering ramp flow so mainline congestion does not spill
back onto the ramp and entering acceleration-lane demand can enter the mainline.
Its hypothetical acceleration lane occupies one 300 m cell. Lane-change control
is combined with D-ALINEA ramp feedback. The objective explicitly adds entrance
waiting to in-road traffic time. These are useful competitor/accounting precedents,
but guaranteed ramp entry, the extra lane-change actuator and hypothetical geometry
cannot be transferred into our finite-receiving, rate-only task as though they
were an empirical distributed-merge certificate.

**RM0001 — Gomes and Horowitz (2006), _Optimal freeway ramp metering using the
asymmetric cell transmission model_.** DOI 10.1016/j.trc.2006.08.001.
[Author-hosted published paper](https://horowitz.me.berkeley.edu/Publications_files/All_papers_numbered/80J_Gomes_TRC06.pdf),
19 PDF pages. **Access upgraded:** previous indexed excerpts, now selected full
methods. Sections 2, 4 and 5, printed pp. 246–250 and 255–256.

ACTM state includes mainline section inventories and ramp queues; ramp flow is
limited by demand, allotted mainline space and metering permission. Its optimization
counts road and ramp time and also rewards distance; equivalence to travel-time
minimization needs stated fixed-split/empty-terminal conditions. A cooling period
is used. The I-210 example is a twenty-meter corridor, not our isolated finite
merge lane. Its reported speed is calculated from model flow and intermediate
inventory, not independently measured non-equilibrium section speed. This is a
serious spatial/rate/accounting reference, with distinct merge-allocation assumptions;
it is neither a validated distributed-merging closure nor a hidden-history theorem.
Its conditional optimization result must not be copied to our task.

## Closest actual metering setting; transfer limit

**RM8-P02 — Klomp et al., _Ramp Metering with Microscopic Gap Detection Algorithm
Design and Empirical Acceleration Verification_, 2021 online/2022 issue.**
[Original paper](https://repository.tudelft.nl/file/File_c446bd9b-9a19-494b-9989-3d11f96fbb1a),
15 PDF pages. Fresh selected control/detector and site reads, printed pp. 92–96;
results/limitations previously extracted in RM8 and rechecked during the RM11
planning pass.

The A13 Delft-North setting has an existing meter, three mainline lanes, 135 m
from stop line to merge start and a 310 m merging area. Conventional control uses
averaged flow/speed; the proposed controller adds gap/class detection and releases
individual vehicles to selected opportunities. Its simulation also uses class-
dependent sampled acceleration and lane-demarcation assumptions. It provides
real aggregate-sensing control context, not evidence of exact cell mass sensing.
Its improvement comparison changes sensing and release timing, so it cannot
establish the unchanged common-rate/full-history claim. The source's three lanes
are real, but are not a reason to add lanes solely to obtain hiddenness. No timing
task, stochastic forcing or geometry adaptation is adopted here.

## Access-qualified leads and exclusion discipline

| Lead | Access actually achieved | Treatment |
|---|---|---|
| RM11-L01, Li (2016), _Modelling and Optimisation of Dynamic Motorway Traffic_ | [UCL metadata/abstract](https://discovery.ucl.ac.uk/id/eprint/1474219/) and indexed primary excerpt; direct/alternative PDF opens failed | Real M25 aggregate-control/initial-density lead. Indexed “detected density” passage is not a fully inspected initial-state contract. No negative theorem inferred from inaccessible methods. |
| RM11-L02, _Design, Field Implementation and Evaluation of Adaptive Ramp Metering Algorithms_ reports | eScholarship robot page; CDLIB full-report fetch failed; secondary index distinguishes 2005 and 2006 reports | Versions not conflated. No new full-method/source claim. The directly accessible RM0001 author paper supplies the selected aggregate comparator. |
| RM11-L03, Daamen/Loot/Hoogendoorn (2010), empirical on-ramp merging | Bibliographic/secondary abstract lead, not original full methods | No independent method claim or second count of the observations cited by P01. |
| RM11-L04, indexed 2026 King Fahd Road ODE–PDE ramp-impact lead | Author-upload search excerpt; direct open failed; publication/version not verified | Unresolved neighboring aggregate-model lead, not a refuted family. Not used to establish absence, closure or useful gradients. |
| RM11-L05, Grenoble collaborative ramp-metering thesis lead | Indexed author-upload lead; selected original methods not inspected | Multi-ramp neighbor, not an adopted single-ramp spatial/history certificate. No task conclusion based on it. |

RM8-P03 remains previously extracted timing/stability context, not a new C0
method result. Secondary search results locate originals only. Inaccessible work
is a coverage limit, never a scientific failure. Broad RL/CAV, joint VSL or
multi-actuator results were not expanded as substitutes for the unchanged task.

## Review boundary

The eighteen queries and twelve access-qualified source/lead records are in
[query log](../../search/rm11_query_log.csv) and
[screening record](../../screening/rm11_records.csv). Six originals received
selected method reads in C0; one earlier timing source is context; the remaining
five entries are limited-access leads (twelve records in total). No source binaries,
trajectory datasets or experiments were downloaded or redistributed. Primary
page/section references, rather than search summaries, support the findings.
