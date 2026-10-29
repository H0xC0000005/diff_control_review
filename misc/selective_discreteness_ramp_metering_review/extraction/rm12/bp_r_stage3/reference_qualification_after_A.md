# BP-R Stage 3 — reference qualification after S3-G2.A

Date: 2026-10-06. **Authorized A continuation performed; stopped at S3-G2-M.**
This is the historical reference-route continuation. The later user approval
closes S3-G2-M.A; [qualification after meter A](qualification_after_meter_A.md)
and the [source-input checkpoint](../../../reporting/rm12/bp_r_stage3/source_qualification_checkpoint.md)
give the current boundary. Unselected-placement language below records the
earlier source frontier, not the current approval status.
This records literature/static work, not an adopted complete task or experiment.
Read the [approved route and preceding evidence](../../../reporting/rm12/bp_r_stage3/findings_and_reference_gate.md)
and [current meter-boundary gate](../../../reporting/rm12/bp_r_stage3/meter_boundary_gate.md).

## Semantic finding

The supported family can keep aggregate lane traffic and explicitly tracked
accelerating disturbances. Its continuous lane conservation equations offer a
credible starting point for continuous-mass accounting; creating a disturbance
descriptor need not create another vehicle. The source nevertheless leaves an
important task interface unbound: **what does the selected rate permission
control, and where is traffic held before entering the freeway?**

Changing demand supplied to a ramp, limiting service at its downstream end and
operating a physical stop line with departure acceleration are different
models. The examined merge paper varies supplied ramp demands and discusses
discharge recovery. It does not specify an actuator law identifying all three.
The approved rate-only action is compatible with multiple cap placements.
Selecting one is a scientific task binding, not a harmless implementation
detail. The original A approval supplies no such placement decision.

## Primary evidence and what it establishes

| Source / inspected location | Positive evidence | Transfer limit |
|---|---|---|
| RM0011, [2004 working paper](https://escholarship.org/content/qt8w70q261/qt8w70q261.pdf), Sections 2.1–3, equations 1–10 | Lane-wise continuous conservation; paired transfers; finite sending/receiving; current-state allocation; cumulative actual transfers can trigger deterministic disturbance events. A particle begins with sending-lane speed and is constrained by acceleration and downstream traffic. | Its IT discussion addresses discretionary changes and explicitly leaves mandatory changes outside the paper's treatment. Full endogenous CM/IT coupling and ramp ownership are not thereby completely transcribed. |
| RM8-P01, [original merge manuscript](https://bpb-us-e1.wpmucdn.com/sites.gatech.edu/dist/f/3571/files/2023/03/merges.pdf), Section 2; Sections 3.2–4/Figure 6 | Ramp modeled as another KW stream; transfer to mainline occurs at a point because there is no acceleration lane. A boundary adjustment increases entry priority without allowing ramp flow above the lane capacity. Supplied ramp demands are varied; queued/unqueued ramp regimes can have different modeled discharge at the same ramp input flow. | Input demand/flow is not an explicit cap-to-release-to-entry actuator law. Figure 6 does not prove complete-TST benefit or exclude a queue/speed-memory reduction. Meter placement, ramp travel and source entry-speed mapping require binding. |
| RM12-S3-C01, [2003 PATH moving-bottleneck original](https://escholarship.org/content/qt69r4t5pp/qt69r4t5pp.pdf), Sections 2.3–4 | A continuous KW stream can obey moving trajectory/flow constraints. The numerical construction approximates their effect using fixed restrictions and CTM; source convergence concerns cumulative counts under its assumptions. | Its convergence result takes trajectories/capacities as exogenous. It cannot certify the endogenous merge-birth, metering or sensitivity chain. The browser title is erroneous; cover/body identify the actual PATH report. |
| RM0001, [2006 ACTM original](https://horowitz.me.berkeley.edu/Publications_files/All_papers_numbered/80J_Gomes_TRC06.pdf), Section 2, equations 8–13 | Meter permission, available ramp traffic and mainline receiving jointly constrain actual entry; ramp/mainline inventory balances count the same transfer consistently. | ACTM's merge allocation differs from the source hybrid. Its permission/accounting principle is a precedent, not permission to import its blending or node equations as the hybrid law. |
| RM12-S3-A01, [2006 journal publisher preview](https://www.sciencedirect.com/science/article/pii/S019126150500055X), indexed introduction/snippets; [institutional record](https://its.berkeley.edu/node/4685) | Confirms the CM model is described in the journal appendix and that its particle trajectories account for mechanical and downstream restrictions. This identifies the exact remaining method source. | Direct publisher and CiteSeer full-text opens failed. The appendix was not newly read; cached introductory text cannot qualify its equations. This is a distinct version/access record, not a replacement for the working paper. |
| RM12-S3-A02, [1997 IT institutional record](https://experts.arizona.edu/en/publications/a-simple-physical-principle-for-the-simulation-of-freeways-with-s/), abstract/metadata | Identifies the incremental-transfer lineage cited by the working paper and its Riemann/Godunov claim. | Full methods not obtained. No concrete mandatory-ramp allocation can be inferred from the abstract. |
| RM12-S3-A03, [1995 gridlock institutional record](https://its.berkeley.edu/publications/nature-freeway-gridlock-and-how-prevent-it), metadata; RM8-P01 reference 25 | Identifies the report related to the 1996 gridlock chapter actually cited for the merge boundary. | Only metadata read. Do not misidentify RM8-P01's merge-boundary citation as the 1997 IT paper or silently claim its priority construction was transcribed. |

Full text and PDF screenshots were sought through the available browser. The
two screenshots were unavailable; direct full journal opens failed. Thus no
new visual geometry verification or exact appendix transcription is claimed.
Ten executed targeted queries in five batches are in the
[continuation query log](../../../search/rm12_bp_r_stage3_A_qualification_query_log.csv);
version/access decisions are in the
[continuation screening](../../../screening/rm12_bp_r_stage3_A_qualification_records.csv).
Only nearest source coupling/allocation citations were followed. Secondary
results and unrelated model families were not used as technical evidence.

## Conservative ownership: what is now justified, and what is still open

**Source-supported structure:** the continuous field has paired lane transfers.
Constraint descriptors restrict admissible flow; they do not appear as an
additional population term in that conservation equation. The moving-bottleneck
antecedent independently establishes a flow-constraint construction for a KW
field. This is adequate evidence that continuous accounting and moving
disturbances are compatible in principle.

**Proposed adaptation contract:** count traffic once, in the conservative road/
ramp/waiting inventories. Describe selected disturbances with event metadata,
without adding their count again to the population. For example, a transfer of
2.4 vehicle equivalents debits/credits 2.4; two deterministic threshold births
create two descriptors, while the fractional traffic remains accounted for.
This illustration proves bookkeeping under that contract, not exact behavioral
equivalence to every version of the source's particle treatment. Sub-unit and
event-phase sensitivity remain real approximation/gradient questions.

**Unqualified detail:** the complete endogenous source motion/flow algorithm,
birth location/time within a step, interactions between restrictions, source
mandatory-ramp allocation and any represented vehicle exclusion/spacing rule.
Do not declare the original implementation's mass ownership fully verified or
substitute a guessed acceleration/downstream-speed clamp. An accepted conservative
overlay must be checked against that actual method before freezing its equations.
If the source requires a different physical ownership/trajectory rule, present
the smallest amendment rather than silently integerizing G1 or changing physics.

## The actuator distinction is physically consequential

For a ramp with finite travel between its upstream entrance and the point merge,
a tighter cap at the entrance holds new traffic upstream. Traffic already beyond
that cap can still reach the merge. A cap at the merge can directly restrict that
traffic's entry and can make the approach queue instead. Finite propagation alone
establishes that the control maps differ; no simulated witness is required.

The donor state matters because the source initializes a new moving obstruction
using sending-lane speed. This does not authorize assigning zero speed to every
metered entrant or deriving a stop/start law from a rate cap. Both alternatives
must use a qualified traffic state/speed definition. A physical signal/launch
model would be a further refinement with its own support requirements.

This distinction already appears in the Stage 2 transfer audit and the Stage 3
envelope. It has not been decided by earlier open-loop approval, which selects
the control variable and excludes a separately optimized release phase. A/B
at [S3-G2-M](../../../reporting/rm12/bp_r_stage3/meter_boundary_gate.md) are two
concrete model boundaries for that same rate-only permission, not verified real
signal locations, a reopening of the
source-family choice or adoption of BP-U gap-targeted timing.

### Meter-boundary clarification evidence

The user asks whether B's exact-merge cap would change ramp metering into another
task. Re-read RM0001 Section 2, equations 8–13: metering rate bounds actual ramp
entry alongside demand and mainline-space constraints; unserved traffic remains
in the onramp inventory. That validates the aggregate ramp-entry-cap category,
not a physical stop line at the merge or the proposed spatial donor-speed law.

Two official layout sources were read at the selected locations: RM12-S3-M01,
[FHWA Handbook Section 10.4.1](https://ops.fhwa.dot.gov/publications/ramp_mgmt_handbook/manual/manual/10_1.htm),
and RM12-S3-M02,
[Caltrans Ramp Metering Design Manual Sections 1.6–1.7](https://dot.ca.gov/-/media/dot-media/programs/traffic-operations/documents/ramp-metering/rmdm-a11y.pdf).
Both distinguish queue storage before the stop line from acceleration distance
after it, before merging. They support physical layout semantics, not a new
traffic closure, actuator-delay equation or gradient result. The Caltrans PDF
edition date could not be confirmed in the retrieved text; do not assert the
search-snippet date as a verified edition. A cover screenshot was unavailable.

Reviewer inference: B collapses part of the physical signal-to-merge path if its
effective entry permission is treated as an immediate signal command. A stopped
pre-meter queue cannot alone set speed at the later merge. Since this review
studies entry-speed-dependent disturbances, command timing and entrant-state
adequacy require explicit qualification. A's KW propagation also does not prove
a launch law. Correct the candidates' physical-placement wording without
selecting either. Search and source records are supplementary to the completed
A-continuation inventory; historical query/access counts are unchanged.

## Dependent comparison and static disposition

All reductions must share the selected actuator, road/ramp geometry, initial
physical scenario and complete waiting accounting. A lane-aggregate rival may
retain ramp density and entry-speed memory. A rival with a different meter
placement would change the physical task and confound representation adequacy.
Source mean-capacity values do not supply a closed dynamic comparator; no
exponential closure or reference-fed moment update is adopted.

Finite receiving and paired transfers prevent arbitrary creation of service.
The source's priority adjustment is an allocation detail, not a capacity bonus.
Complete TST charges both placements' holding inventories; queue relocation with
identical complete exit histories still cannot improve it. No globally best
rate, admitted positive complete-TST scenario, compact insufficiency or useful
gradient has been established by this continuation.

**Disposition:** reference family/conservative coupling supported in principle;
exact coupled source law still partially qualified; actuator placement is now a
concrete user-owned task decision. S3-G2.A is closed, **S3-G2-M is open**, Stage 3
is incomplete and Stage 4 is unopened. Once placement is selected, bind its
boundary/state interface and complete the named source/comparison obligations,
stopping again if a new physical law or indispensable access need is exposed.
