# K2: forced-merge sources, interface qualification and limits

Date: 2026-10-14. Scope: one bounded compact terminal qualification under
approved K2, retaining H1 as the upstream candidate. This is a paper-reference
list and evidence audit, not a downloaded-paper archive or simulator pass.

## Papers actually viewed

| Reference | Material inspected | Direct support and limit |
|---|---|---|
| [Carey, Balijepalli and Watling (2013), *Extending the Cell Transmission Model to Multiple Lanes and Lane-Changing*, DOI 10.1007/s11067-013-9193-7](https://eprints.whiterose.ac.uk/id/eprint/77315/7/Carey%20et%20al%202013_with_coversheet.pdf) | Primary manuscript §5, R1 and Algorithm A1, R2 and Algorithm A2; residual lane-change discussion. | Local own-lane priority, receiving-work factor and proportional rival. It does not give this arrival-aware permanent-lane-end server or calibrate its priority/work factor. |
| [Jin (2015), *Continuous formulations and analytical properties of the link transmission model*, arXiv:1405.7080](https://arxiv.org/pdf/1405.7080) | Primary preprint §3.1, equations (23) and empty-link special case; §3.2 boundary-flow conditions; §3.3 equations (28)–(30). | Eligible queue, physical vacancy and demand/supply from boundary histories. A queue amount differs from link occupancy; junction behavior must be specified separately. The weighted forced-merge rule and terminal partition here are adaptations, not Jin's general junction theorem. |
| [Yperman, Logghe and Immers (2005), *The Link Transmission Model: An Efficient Implementation of the Kinematic Wave Theory in Traffic Networks*](https://www.mech.kuleuven.be/cib/verkeer/dwn/pub/P2005C.pdf) | Primary conference PDF §§2–4, especially sending/receiving conditions and §4.2 merge nodes. | Link/node decomposition and distinct merge priorities. No native mandatory gap-weighted lane-end queue or H1 lateral-source reduction. |
| [Tampère, Corthout, Cattrysse and Immers (2011), *A generic class of first order node models for dynamic macroscopic simulation of traffic flows*, DOI 10.1016/j.trb.2010.06.004](https://www.sciencedirect.com/science/article/pii/S0191261510000846) | Publisher abstract/introduction extract returned by search. Direct page access then failed. | Only the general need to specify allocation between competing demands and downstream supply is used. No full algorithm, priority calibration or generic-node admission is inferred. |

Other search results were leads, not substantively inspected papers or evidence
for this gate. The exact source reading limits above apply. Earlier H1 source
and timing audits are reused in place:

[H1 source/adaptation list](vsl_h1_source_and_adaptation_audit.md)

[Earlier source-to-equation audit of S13](../s13_m2_source_to_equation_audit.md)

## The source join that is and is not established

The local allocation supplies a receiving-work budget and priority. Empty-link
boundary histories supply finite physical travel/storage. Their restricted
composition forms a terminal candidate whose arrivals, queue and departures
are autonomous under a common action. The proof applies to an initially empty
terminal reach, fixed advice within each action evaluation, no internal lateral
sources there, a continuing stream that fits its first-priority service, and
receiving at the upstream interface that never binds.

No claim is made that the complete native Carey CTM, general Jin junction
model, or an arbitrary lane-drop site has been reduced exactly to this server.
The terminal work factor, R1 extension to compulsory merging, strict own-lane
priority and exclusion of further early transfers are explicit adaptations.
They are not established lane-end gap-acceptance or zipper calibration.

## Compact storage and positive waiting can coexist

For a finite terminal reach, incoming and outgoing cumulative mass determine
physical stock. A delayed incoming history minus outgoing mass determines
the eligible queue. Receiving uses a further backward delay and jam storage,
so physical stock and the eligible queue cannot be exchanged casually.

The primary note supplies the empty-link receiving condition at early times
and after the backward delay. A strict sufficient bound puts the entire
cohort below one terminal lane's jam storage, with incoming rates below link
capacity. It makes receiving at the H1 handoff nonbinding for every admitted
action without granting infinite storage.

At the same time, the node's weighted receiving-work requirement can exceed
its available rate even when its ordinary continuing stream fits. An ending
queue then forms while the storage bound remains satisfied. The note gives
compatible open inequalities rather than parameter values selected to create
an interior optimum. If the receiving inequality fails, the one-way H1
handoff is invalid; no adapter or clipping restores that admitted branch.

The physical construction requires a terminal section of the existing road
length, with early transfers ending at its entrance. This is the smallest
specific new geometry/opportunity choice found here. It is proposed at the
gate, not silently adopted under K2 route approval.

## Analytical reference checks and stage-level speed result

The two-second pulse reference uses ending and continuing mass four each,
receiving four work/s and late work factor two. Own traffic takes two work/s;
forced flow is one mass/s during arrivals. Queue grows linearly to two and
drains in one second after own arrivals stop. Queue-area delay is three
veh-eq s. Eligible-arrival-time sum is eight, complete-time sum eleven.
The four-second pulse has no queue, arrival-time sum sixteen and complete-time
sum sixteen. This demonstrates the distinction between queue reduction and
complete TST; it is not an H1 reachability or traffic-experiment result.

The batch-priority reference uses ordinary and forced mass two each,
receiving two work/s and late factor two. Both allocations finish after three
seconds. Own-lane-first gives five veh-eq s of TST; proportional batch service
gives six. The shared final work does not decide mean completion time.

For unchanged preparation outcomes, fixed service/work factors and nonbinding
longitudinal sending, the note proves an earlier-arrival dominance property
for the one-queue own-lane-first member. Faster free-flow arrival cannot worsen
whole-cohort TST on that branch. This is a derived diagnostic limitation,
not a theorem claimed by the cited sources and not a claim for arbitrary
priorities, speed-dependent capacities, or changed preparation.

## Baselines and scientific admission

The aggregate-plus-initial-ending-statistic rival reconstructs the proposed
upstream state and predicts the initially empty terminal queue itself. It
receives all fixed geometry, response/work parameters and available aggregate
history. No initial terminal state, future receiving curve or extra lane
observable is withheld from it. Full longitudinal state and discrete order
remain unnecessary for this restricted candidate's prediction.

Proportional/cooperative terminal service, the original S13 batch reduction,
and an explicit virtual point queue are separate model-form rivals. The
strong aggregate/history/capacity-drop rivals from the opening remain relevant;
this pass neither reruns their survey nor weakens them to memoryless service.

MP6 has a concrete conditional physical construction with finite waiting,
storage, conservation and complete clearance. Adoption of its partition and
priority remains open. Applied lane-end behavior, H1 opportunity-scale and
speed-response provenance, a fresh observer witness, derivative correctness
and independent usefulness remain unqualified. A positive queue or an interior
minimum internal to an eventual model is not independent traffic evidence.

[Conceptual forced-merge model, stage finding and terminal adoption gate](../../reporting/research_readiness/vsl_k2_forced_merge_findings_and_gate.md)

[Mathematical candidate and bounded reference proofs](../../synthesis/research_readiness/vsl_k2_forced_merge_contract.pdf)

## T1 selection and joined qualification — 2026-10-14

The user selected the finite physical terminal section and its described
restricted one-queue member. The continuation re-viewed the three fully
accessible primary papers in the reference table: Jin's empty-link
demand/vacancy and boundary-count relations, Yperman's link/node separation
and merge allocation, and Carey's R1/R2 context. Jin's arXiv abstract record
and publisher search extract were also inspected to verify publication
metadata: the preprint was submitted in 2014 and the paper appeared in
2015, DOI 10.1016/j.trb.2014.12.006. No additional paper was
substantively viewed. Tampère's earlier abstract-only access limit remains.
This table, together with the linked H1 audit, remains the sprint reference list.

[Jin's primary preprint record](https://arxiv.org/abs/1405.7080)

[Jin's publisher publication record](https://www.sciencedirect.com/science/article/pii/S0191261514002239)

The final consolidation supplies an exact H1/T1 forward contract, including
paired upstream balance, finite terminal receiving, scalar reflected-queue
well-posedness, full clearance and travel-plus-queue TST. These are deductions
for the declared restricted member, not theorems or calibration attributed
to the source authors. In particular, its weighted node is not asserted to
inherit Jin's theorem for general invariant junction models.

The joint example now includes active early receiving limitation as well as
positive compulsory waiting. It uses scaled algebraic coefficients and exact
preparation branches, not time-stepped traffic runs or a selected empirical
parameter set. Fixed exit-work ceilings also fit the slowest action's lane
capacity; this conservative domain refinement ensures receiver compatibility
without adding a new downstream state or mechanism.

The terminal handoff, absence of lateral sources inside that section,
own-lane-first forced priority, constant work factors, H1 opportunity scale
and ideal common-speed response remain explicit task assumptions. T1's
selection closes physical versus virtual interpretation; it does not provide
field support for those assumptions. The exact assembled contract is at
confirmation before freeze. Analytical MP6 has a nonempty joined domain;
applied MP6, gradient correctness, reachable information/action contrast and
independent control usefulness remain unestablished.

[Current joined conceptual model and MP conclusions](../../reporting/research_readiness/vsl_t1_joined_model_and_gate.md)

[Single combined contract and algebraic example](../../synthesis/research_readiness/vsl_h1_t1_joined_contract.pdf)
