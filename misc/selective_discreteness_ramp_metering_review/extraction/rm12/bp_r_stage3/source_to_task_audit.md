# BP-R Stage 3 — source-to-task qualification

Date: 2026-10-06. Selected original methods were freshly read. This is a
qualification record, not adoption of a new physical reference or a performance
certificate. Earlier source IDs and version qualifications are preserved.

Subsequent decision: the user selects S3-G2.A. This first-pass audit is historical;
read [post-approval qualification](reference_qualification_after_A.md) and
[current S3-G2-M](../../../reporting/rm12/bp_r_stage3/meter_boundary_gate.md)
for the remaining source/control boundary. This approval selects a route for
qualification, not a fully transcribed coupled task law.

## Nearest reference route

**RM8-P01**, Laval/Cassidy/Daganzo, 2005 conference manuscript / 2007 chapter,
[author-hosted original](https://bpb-us-e1.wpmucdn.com/sites.gatech.edu/dist/f/3571/files/2023/03/merges.pdf),
Sections 2–4: lane-wise kinematic waves, speed-incentive lane changes and
accelerating moving obstructions. The ramp is another KW lane, with point entry
because the site lacks an acceleration lane. Its 40% boundary adjustment raises
entry priority, not road receiving capacity. The stated acceleration bound is
speed dependent. Figure 6 distinguishes queued/unqueued ramp regimes at the
same actual ramp inflow; ramp state is therefore a strong compact competitor.
This is a direct local-merge route, but its intervention evidence does not bind
our open-loop permission law or complete-clearing TST comparison.

**RM0011**, Laval/Daganzo, 2004 working paper,
[institutional original](https://escholarship.org/content/qt8w70q261/qt8w70q261.pdf),
Sections 2–3, equations 1–10: continuous lane conservation with paired transfers,
finite sending/receiving and IT allocation. Section 3 generates integer disturbance
events from cumulative lane changes; deterministic floor crossings are possible
and Poisson sampling is optional. The obstruction starts at sending-lane speed,
has zero passing and is constrained by acceleration and downstream traffic.
The text does **not** justify the claim that flooring necessarily discards traffic
mass. Nor does this selected description fully resolve fluid/particle ownership
and coupling for a conservative ramp adaptation. Quantized event creation and
integerized traffic mass must be audited separately. This corrects an overly
broad possible reading of earlier cautions; it adopts neither interpretation.

The chosen route is this connected source lineage, not a splice of different
bounded-acceleration models. Qualification still needs the actual merge/meter
interface and conservative moving-constraint coupling. The working paper's
mandatory ramp-entry allocation is not supplied by its discretionary-lane-change
formula alone. A source priority parameter cannot be translated into an arbitrary
two-incoming node fraction without checking the node construction.

## Alternatives and accounting checks

**RM10-P04**, Laurent-Brouty/Costeseque/Goatin, HAL-02155131v4 (2020; journal
2021), [author-uploaded original](https://www.researchgate.net/publication/346438282_A_Macroscopic_Traffic_Flow_Model_Accounting_for_Bounded_Acceleration),
Section 2, equations 2.1–2.2 and Theorem 1: conserved density plus accelerating
moving constraints initialized at downward density jumps; constant acceleration
and a Cauchy problem on the line. This is macroscopic despite retaining finite
constraint trajectories. Its existence result supplies neither a metered ramp
node nor a rule for new merge disturbances or control gradients. Replacing the
merge source with this law requires a new boundary/event construction; changing
the acceleration law also changes the physics. It is not an already complete,
event-free alternative for our task.

**RM10-P01**, Leclercq/Laval/Chiabaut, **2011 Procedia proceedings body**,
DOI 10.1016/j.sbspro.2011.04.505,
[author-uploaded original](https://www.researchgate.net/publication/251530773_Capacity_Drops_at_Merges_an_endogenous_model),
Sections 2.1–2.2: endogenous mean merge capacity with insertion acceleration,
headway statistics and ramp congestion regime. Mainline congestion and an active
merge are assumed; the uncongested-ramp entry-speed prescription is an assumption.
This provides a serious compact service rival. A mean-capacity law is not an
established transient closure for queue onset, control changes and clearance.
No new event-free recovery ODE is inferred from it.

**RM0001**, Gomes/Horowitz 2006,
[original ACTM paper](https://horowitz.me.berkeley.edu/Publications_files/All_papers_numbered/80J_Gomes_TRC06.pdf),
Sections 2 and 4: permissions differ from actual entry, road/ramp inventories
are accounted, and storage/receiving matter. The source itself explains that
some discretizations empty only asymptotically and uses cooling. Therefore
``a long enough finite tail must be exactly empty'' is not a general acceptance
rule. This is accounting precedent, not authority to import ACTM equations into
the hybrid reference without qualification.

**RM9-L04**, Cho/Laval 2020,
[publisher abstract](https://ascelibrary.com/doi/10.1061/JTEPBS.0000350),
remains abstract-only for technical qualification. A targeted access search did
not produce the article's full methods. Its joint RM/VSL results cannot become
our common-rate-only representation result.

**RM12-S3-P01**, Laval/Xu, GDOT report FHWA-GA-20-1826 (2020),
[institutional report text](https://dlg.usg.edu/record/dlg_ggpd_s-ga-bt700-pr4-bm1-b2020-bv3-belec-p-btext),
printed pp. 9–16 selected: combined queue-controlled RM/VSL, GTsim calibration,
and separate system/freeway/ramp travel-time reporting. Ramp-only and joint-control
rows make the holding-cost tradeoff visible. Its fine reference, feedback tuning,
two-site scope and onset-period reporting are different contracts. It does not
establish our finite-cleared common open-loop reduction comparison. Institutional
OCR was read; exact formula transcription was not taken from damaged OCR.

## Access, bounded search and inference limits

Four actual queries in two batches are recorded in
[Stage 3 query log](../../../search/rm12_bp_r_stage3_query_log.csv).
Six inherited IDs plus one new report are qualified in
[Stage 3 screening](../../../screening/rm12_bp_r_stage3_records.csv).
The 2006 journal-paper CiteSeer fetch, two author-site fetches, report PDF link
and two PDF screenshots failed through the browser tool. Available original text
remains the method evidence; no new journal-version read or visual geometry
verification is claimed. Source URLs, selected locations and access grades are
explicit. Searches located other papers; unrelated controllers/actuators and
secondary summaries were not used as technical evidence.

**Conclusion:** the original hybrid route is concrete enough to present a
reference-adoption choice. It is not yet a fully bound task. Continuous conserved
mass does not itself forbid discrete disturbance metadata, and a macroscopic
label does not imply that such metadata is absent. The exact event-to-flow
coupling and meter mapping remain scientific qualification work; absence of a
ready continuous closure is evidence-limited, not proof of impossibility.
