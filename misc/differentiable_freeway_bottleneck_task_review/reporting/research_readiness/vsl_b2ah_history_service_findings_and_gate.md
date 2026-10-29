# A travel history can time the cohort; it cannot locate spare merge service by itself

The user selected A-H for the next review: retain a compact account of movement
through the upstream preparation area before considering a position-resolved
traffic model. This is a review-route decision, not adoption of A-H's state or
equations. The two-stage traffic task remains: ending-lane traffic seeks early,
service-limited merging while it travels through the area; any residual must
seek finite service at the permanent lane end and may wait. This review stops
at **VSL-B2AH-G1**, a new choice about what the compact upstream receiver
represents.

The useful finding is narrower than either an A-H success or failure.
**Physical travel can be compact for the inherited synchronized, free-flow
cohort. Local merge service is not yet compactly closed.** An entry/progress
history can prevent the unphysical slow-speed discharge tail identified in
B2-A. It does not tell one adjacent-lane stock how much own traffic and spare
receiving coincide with a donor at each early merge opportunity. A whole-zone
stock and a physically local R1 receiving budget are different objects. A-H
can remain the first route, but joining them requires an explicit traffic
restriction or an additional location interface, not a bookkeeping convention.

Date: 2026-10-13. Status: **A-H qualification executed to VSL-B2AH-G1.**
No cohort profile, pooled receiving law, internal service station, exact
speed response, choke law or MP6 operating domain is adopted. No simulator
construction or traffic experiment was opened.

## What A-H already buys, and where the difficulty begins

S13's analytical cohort enters one fixed preparation zone together and, on its
selected uncongested branch, travels at the same realized speed under one
common VSL action. For that special case, its entry time and physical distance
traveled determine when the cohort reaches the lane end. A history or progress
clock can express this without releasing an arbitrary fraction of the current
stock every time step. This is a conditional deduction about S13's motion
branch, not a new queue or merging law. If P1's finite receiving produces
longitudinal waiting or splits arrival times, the single common clock ceases
to be enough; those delays must enter the history and complete-time account.

Now consider the traffic encountered along the way. P1's R1-first rule says
that *at a physical opportunity* through-lane traffic claims feasible
receiving first, and a nearby ending-lane request uses only what remains. In
Carey's source this budget belongs to an identified target cell. A-H proposes
one compact adjacent-receiver stock for the preparation area. It still needs
to explain which local through demand meets a donor and whether spare service
there can be used. The source's local rule does not itself turn spare capacity
elsewhere in the area into service for that donor.

Imagine a donor currently beside an early merge location. If the adjacent
traffic is concentrated at that location, it may leave no room there, even if
the same total adjacent-lane mass would leave room when concentrated farther
downstream. A whole-area stock records equal amounts in these two cases. A
boundary history can recover some internal movement on a homogeneous link,
but once traffic changes lanes *inside* the link, the time and location of
that lateral inflow also affect later local receiving. This is a conditional
distinguishing example: it matters only if the first task admits such internal
heterogeneity. It does not disprove a deliberately homogeneous A-H member.

There is a second, more basic timing question even in the small S13 task.
S13 declares that the complete finite mass starts at the entrance at the
decision instant; its later choke is a deliberately homogeneous batch. A
finite **rate** of own-lane service during upstream merging requires either
a physical passage profile for that mass or a queue that releases the
instantaneous arrival over time. Total mass and a travel time do not specify
the local own-lane flow rate. For illustration, four units crossing an early
opportunity over two seconds demand two units per second; spread over eight
seconds, they demand one-half unit per second. At a three-unit-per-second
receiving budget, the room left for lateral receiving is one versus two and
one-half units of work per second. These are hand-calculated alternatives,
not measured traffic states or a claim that either passage profile applies.

## Why the LTM analogy helps, but does not close the merge

The original link transmission model uses cumulative entry and exit counts
to propagate a homogeneous link and allocates transfers at its nodes. It is
a strong precedent for compact *longitudinal* timing, including arbitrary
time-varying boundary demand. It does not directly provide service for
mandatory lateral moves spread through the interior of one link.

[Yperman, Logghe and Immers, original LTM paper](https://www.mech.kuleuven.be/cib/verkeer/dwn/pub/P2005C.pdf)

[Jin, continuous LTM and initial/boundary conditions](https://arxiv.org/pdf/1405.7080)

Carey's R1 gives a precise local allocation and explicitly permits an
unfulfilled request to remain while traffic proceeds to later cells. This
supplies the transfer meaning, but its local occupancy and service are not
reduced to one whole-zone stock in that paper.

[Carey, Balijepalli and Watling, mandatory requests and R1](https://eprints.whiterose.ac.uk/id/eprint/77315/7/Carey%20et%20al%202013_with_coversheet.pdf)

A link-queue or reservoir approximation can relate total occupancy to demand
and supply without representing each interior position. It is a serious
compact rival, and it must be named honestly: Jin's link-queue work describes
an approximation with different internal traffic dynamics from CTM/LTM, not
an exact consequence of boundary-count LTM. Likewise, the inspected official
abstract for van der Gun, Pel and van Arem supports changing fundamental
diagrams and reconstructing within-link density for LTM with VSL; it does not
establish a one-stock law for distributed lateral transfers. Calling an
aggregate receiver “LTM-based” would not supply that missing derivation.

[Jin, link-queue model and its relation to LTM](https://arxiv.org/pdf/1209.2361)

[Van der Gun, Pel and van Arem, official article record and abstract](https://research.tudelft.nl/en/publications/the-link-transmission-model-with-variable-fundamental-diagrams-an/)

## What the current questions now say

| Question | Direct finding at this A-H checkpoint |
|---|---|
| **MP1: opportunity and speed** | On S13's no-queue common-speed branch, entry/progress timing can determine when the cohort traverses a fixed physical distance. It does not by itself specify how a rejected request encounters the next *local* service opportunity. Slower advice has no guaranteed sign of benefit. |
| **MP2: feasible early completion** | R1 allocates a *known local* receiving budget. One zone stock does not establish which local receiving budget a physically present donor can use. Pooled service would be an added analytical assumption. |
| **MP3: minimum information** | Adjacent-lane stock can expose a hidden future-receiving difference, but local own-demand timing and possibly transfer-location history can be consequential. A-H's exact minimum memory remains unselected. |
| **MP4: early and late costs** | The downstream compulsory lane-end service is retained. Any release queue or upstream holding created to make early service finite must contribute to total time. A spare aggregate budget cannot silently serve a request at an unreachable position. |
| **MP5: departures** | A physical progress history avoids the demonstrated geometric-tail shortcut in the admitted free-flow case. Changed within-cohort arrival or holding can invalidate S13's common handoff and proportional half-clearance mean. |
| **MP6: joined regime** | There is still no source-supported, single operating domain joining compact early receiving, common VSL motion, compulsory lane-end service and complete departures. A-H has a possible elementary restriction, not an admitted applied model or gradient result. |

The information comparison also remains honest only if every model receives
the same **declared aggregate entrance history**. If A-H is given an extra
initial lane-specific passage profile or receiver statistic, that addition
belongs in G2's observation ladder and the strong aggregate rival receives
everything recoverable from the same aggregate data. No post-action reference
receiving curve may be injected as a model input.

## VSL-B2AH-G1 — what does the compact receiver stand for?

**Problem statement.** A-H now needs a physical interpretation of finite
early receiving across the fixed preparation area. Is one receiver a
deliberately homogeneous interaction approximation, or must the model keep
separate local service interfaces to preserve P1's local R1 meaning?

**Assumed model-chain function.** An action-independent initial traffic
description and the common VSL determine physical arrival and own-lane
demand; the adjacent receiver limits early transfer after own-lane priority;
accepted traffic updates its later receiving; unmerged traffic reaches the
permanent lane end; complete departures determine total time. A solution
must close that chain autonomously for all compared actions.

**Core gap.** S13's simultaneous batch has no finite upstream passage
profile. The LTM papers determine boundary movement for homogeneous links,
while the R1 paper allocates receiving at identified locations. The sources
inspected here do not derive a whole-zone R1 budget from one stock plus
boundary/age history when lateral transfers occur throughout the area.
Whether a homogeneous restriction is acceptable for the paper's first task
is a global scientific choice, not an implementation detail.

**Candidate H1 — compact homogeneous interaction window.** Declare a fixed,
finite cohort passage profile, common across all advice actions. The
profile could be generated by a finite entrance release or an initial
co-moving footprint; these have different initial-state and waiting-time
meanings and are **not yet interchangeable or selected**. A declared
profile's history determines physical progress and own-lane demand. Treat
the adjacent preparation traffic as one representative receiver
whose finite stock and outflow determine one receiving-work budget; apply
own-lane-first allocation to physically present requests while the cohort
crosses the window. Accepted mass changes that stock, and the residual goes
to the separate compulsory lane-end service. **Pros:** retains one local
receiver account, finite physical timing and continuous mass; directly tests
whether this compact information suffices in a deliberately elementary
regime. **Cons:** a representative whole-window budget is an explicit
homogenization of Carey's location-specific R1, not an exact sourced
reduction. The entrance profile/footprint and its observability, absence of
consequential internal queues, downstream outflow and action-consistent
receiving law all require qualification. This changes G1 initial-traffic
meaning, G3 service/motion and potentially G2/G4, while MP6 remains open.

**Candidate H2 — a few local cumulative-flow interfaces.** Retain
physically fixed early opportunity locations. Between them, use compact
entry/exit histories; at each opportunity, keep the receiver information
needed for local R1 service. Unserved traffic can reach later opportunities
subject to the intervening travel clock. **Pros:** respects the spatial
meaning of the cited R1 rule and gives explicit locations for competition,
queueing and residual passage without requiring a dense CTM cell lattice.
**Cons:** it adds consequential position-indexed state and chooses how many
opportunities exist and where. A growing set of interfaces becomes the
short spatial B route in another representation. It changes G3 and G2/G4
interfaces, and the source record does not fix a principled finite number
of stations for this particular VSL task.

**Strong simpler rival — one-zone link queue.** A whole-zone occupancy can
drive a macroscopic demand/supply and pooled lateral service rule while a
separate delay account carries travel time. **Pros:** a compact, clear
comparison for how much local service information matters. **Cons:** its
internal dynamics and opportunity meaning are different from both exact
LTM propagation and Carey's local R1. It could be a separate model-form
baseline, but promoting it as P1's primary physical closure would reopen
G3 rather than preserve the accepted local interpretation.

**Provisional recommendation.** Keep A-H as the selected review route and
consider H1 only as an **explicitly adapted, restricted analytical member**
for one bounded qualification, with a fixed physical entrance profile and
no asserted congestion-location fidelity. This is a proposal for the user's
methodological disposition, not an approval or an MP6 admission. If local
receiving or queue location is consequential even in the declared member,
H2 is the smallest location-aware return; do not call an arbitrary pooled
budget the source's R1 rule. The original S13 conditional certificate
remains unchanged and can continue as an analytical benchmark.

This gate is Type 2 under G1/G3 and VQ3-P/T/S, with G2 information and G4
complete-time dependencies. Review stops here before selecting H1's profile,
receiver relation, source parameters, time law, or any implementation.

[Source reading, hand examples and evidence limits](../../extraction/research_readiness/vsl_b2ah_source_and_compactness_audit.md)

[Work and verification record](vsl_b2ah_work_report.md)

## Subsequent H1 choice and qualification — 2026-10-13

The user chose H1, emphasizing that intra-zone longitudinal heterogeneity
is premature while a homogeneous restriction remains viable. This closes
VSL-B2AH-G1's review-route choice in favor of homogeneous qualification;
it does not approve every possible profile, receiving or queue law.

The subsequent H1 pass formed a concrete conditional homogeneous upstream
candidate, including its rate-scale adaptations, physical arrivals and
ending-scalar sufficiency under initial continuing symmetry. It did not
disprove homogeneity. The remaining shared choice is consequential terminal
waiting and its upstream influence. The bounded pass is finished at the
original VSL-B2-G1 interface gate; the successor modeling-chain stage is
still open. H2/B remains deferred.

[Executed H1 qualification and specific remaining gate](vsl_h1_homogeneous_window_findings.md)

[Original-stage progress](vsl_review_progress.md)
