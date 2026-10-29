# Upstream merge space needs a travel clock before the lane-end boundary

The task has two connected stages. In the **upstream preparation area**,
ending-lane traffic attempts to merge as it advances; the adjacent
through lane can accept only what its traffic and receiving service
permit. At the **permanent lane end**, any remaining ending-lane traffic
must merge to continue, still subject to finite receiving. An
unserved request waits; compulsory need does not create immediate
service. P1 replaces the upstream completion assumption in component 4
and revises component 5's upstream receiving assumption. Component 6's
lane-end service and departures remain a downstream interface to
qualify, not the subject of this A gate.

The compact A route has a defensible upstream core: keep an accountable
amount of traffic in the adjacent lane's preparation-area receiver, let
its own through traffic use feasible service first, and allow early
merging only from what remains. Accepted merges add to that stock,
so later upstream receiving changes. This directly addresses
component 4's old assumption that a fixed share completes with
elapsed time regardless of adjacent service. Residual ending-lane
mass still reaches the separate compulsory lane-end stage.

The qualification finds a second requirement. **Knowing how much traffic is
in the upstream area does not generally tell us when it can reach an early
merge opportunity or the lane end under a lower speed limit.** A can stay
spatially compact, but only if it gives physical travel and arrival timing a
separate, justified account. Treating every vehicle in the stock as instantly
available changes upstream preparation. The source evidence does not yet
show that a compact timing account and distributed early merging can be
joined for this particular VSL task. This is the first new methodological
choice; the review stops here.

Date: 2026-10-13. Status: **B2-A qualification executed to VSL-B2A-G1.**
No receiver or motion law, extra state, task-role change, B2-B pivot or
applied MP6 regime is adopted.

## The strongest compact interpretation of A

Think of A as a compact account of the *upstream* preparation area, rather
than only a fixed-capacity gate at the lane end. Its adjacent-lane stock
helps determine how much early merge room can be offered now. Its own
through-lane traffic claims that room first; a physically present
ending-lane request can use the rest. The accepted mass leaves the donor
and enters the target exactly once. Any unmerged mass continues toward
the separate lane-end service. Target outflow and later receiving must
follow from traffic and a declared downstream boundary. A common VSL
acts on the same fixed road for every compared case.

This is the smallest plausible repair of component 4. The previous B2
counterexample showed why today's receiving number alone is not enough: two
different target stocks can yield the same present service and different
future service. Adding a stock can remove *that* ambiguity. It does not
automatically tell us which donor mass has reached a merge opportunity, when
the target's own traffic can advance, or when accepted traffic reaches the
exit. Those are movement questions, not bookkeeping details.

| Causal question | What one receiver stock can express | What remains to be justified |
|---|---|---|
| Why is target receiving different now? | Different occupied amounts can imply different free space and service. | A receiving relation and boundary valid for the admitted traffic state. |
| How much early merging completes now? | R1 can allocate a known upstream receiving budget after known own-lane demand. | Which donor traffic is physically available at the early opportunity, and what own demand reaches it. |
| Why does service change later? | Accepted mass changes target occupancy. | How outflow, arrivals and downstream restriction evolve under the same speed advice. |
| What reaches the lane end and exits? | Stocks preserve mass and identify residual unmerged mass. | When it reaches compulsory lane-end service and when all traffic exits; conservation alone does not supply mean complete time. |

### A simple travel-time check

Consider one fixed-length free-flow area initially holding one unit of traffic
uniformly along it. Traffic travels half the area's length per time step and
no more enters. Physical travel releases half the mass in the first step and
the other half in the second. A naive one-stock update that releases half of
*whatever remains* at each step gives a different answer:

| Exit interval | Physical movement | Naive half-the-current-stock rule |
|---|---:|---:|
| First | 1/2 | 1/2 |
| Second | 1/2 | 1/4 |
| Third | 0 | 1/8 |
| Still present after the second | 0 | 1/4 |

Both descriptions conserve mass, but only the first clears this free-flow
traffic on time. The second has a geometric tail, so it also gives the wrong
travel and complete-time trajectory. This is a **preparation-area motion**
check, not a model of compulsory merging at the lane end. Carey establishes
this issue for standard CTM cells
whose free-flow speed is below one cell per step and proposes a correction
that uses when traffic entered. The table is a checked special case of that
argument. It rules out this tempting stock-only motion shortcut, **not** all
compact traffic models.

[Carey, variable-speed CTM, accepted manuscript](https://pure.ulster.ac.uk/ws/portalfiles/portal/85807280/TRB_2018_842_R2_as_uploaded_to_TR_Part_B_on_2020_04_29.pdf)

An arrival or boundary-flow history is one way to retain travel timing
without many spatial cells. The link transmission model is a serious compact
precedent: for homogeneous links it calculates sending and receiving at
boundaries using cumulative traffic counts. But that source does not give a
one-stock law for mandatory transfers made *inside* a VSL preparation zone.
If we need a separate history at every internal merge opportunity, the
result may merely encode B's spatial state in another form.

[Yperman, Logghe and Immers, link transmission model](https://www.mech.kuleuven.be/cib/verkeer/dwn/pub/P2005C.pdf)

Carey's R1 lane-change source likewise allocates receiving at an identified
upstream cell: through-lane traffic enters first and lateral traffic receives
residual space. It does not say that all ending-lane mass in a whole
preparation area can request the same local space at once. Collapsing
*all upstream attempts* into one point would move those opportunities
and may remove S13's progressively completed preparation mechanism.
Modeling only the **later forced lane-end merge** as a point would not
remove upstream preparation; it would leave the present upstream
motion/receiving question unanswered.

[Carey, Balijepalli and Watling, R1 and local cells](https://eprints.whiterose.ac.uk/id/eprint/77315/7/Carey%20et%20al%202013_with_coversheet.pdf)

## What this establishes for the existing questions

| Question | Direct answer from this A qualification |
|---|---|
| **MP1: upstream opportunity** | A can make early requests conditional on traffic reaching declared preparation opportunities. One stock does not itself supply a physical arrival clock for requests spread along the area. The residual request at the lane end is a separate downstream boundary. |
| **MP2: feasible completion** | Given *actual* donor availability, own demand and target receiving, P1/R1 supplies the local priority allocation. A has not yet predicted all three autonomously under common VSL. |
| **MP3: required information** | The receiver stock can fix the B2 hidden-stock ambiguity. Movement may additionally need entry/exit timing information; the minimum such memory is unselected. Full spatial positions are not thereby proved necessary. |
| **MP4: early and late cost** | Early transfers use upstream receiving; any remaining mass later requests compulsory lane-end service and can wait. Neither stage may assume free service. Their joint cost check waits for upstream timing and downstream boundary conditions. |
| **MP5: departures and mean time** | The one-stock speed shortcut fails even a free-flow clearance example. Complete time requires the actual departure chronology; S13's proportional batch remains conditional. |
| **MP6: joint regime** | No source-supported compact VSL lane-drop regime is admitted. The local R1 rule and the variable-speed travel correction have not been joined with the same preparation, lane-end and exit conditions. |

Strong simple rivals survive. A point queue with a justified arrival curve,
an aggregate or history-based VSL model, and a compact boundary-count model
can all be consequential comparisons. This review supplies no reachable
equal-full-history information witness, gradient accuracy result, optimizer
advantage or measured traffic validity. S13's conditional certificate and
the closed urban task remain unchanged.

## VSL-B2A-G1: what must compact upstream preparation remember?

The choice is about upstream traffic meaning rather than a parameter or
numerical step. The **terminal choke is present in every route**: residual
traffic must obtain finite service there. The A/B choice concerns how
early attempts and adjacent receiving evolve before it. A compact
preparation area can work only if some state or justified restriction
carries the travel information lost by collapsing positions.

| Route | Core idea and resulting task | Pros | Cons and dependency |
|---|---|---|---|
| **A-H: compact upstream travel history** | Keep early merge attempts across a finite preparation area, one compact adjacent-receiver account and the minimum entry/exit or age information needed for physical availability. Pass residual ending mass to the compulsory lane-end boundary. | Best chance to preserve S13's two-stage question while staying spatially compact; homogeneous-link boundary-count theory is a precedent for motion memory. | No inspected source closes distributed R1 merging with one receiver stock and this history. Added information may become as extensive as a small spatial model; G3 state/motion, G2 information fairness and G4 time meaning need approval. |
| **B: short spatial upstream merging region** | Represent the consequential upstream lane positions and move traffic through them before each early R1 allocation; pass leftovers to the same lane-end boundary. | Directly expresses location-dependent early arrival, blockage and target occupancy as in the principal lane-change source. | Larger state/timing stack. It still needs a sound fixed-geometry VSL movement law and lane-end boundary; spatial detail alone does not cure those shared gaps. |
| **Point-only early preparation (simpler rival, outside the accepted target)** | Replace *all upstream early attempts* by one point encounter, then use the same later forced lane-end service. | A transparent reduced baseline for seeing what distributed preparation contributes; speed can still change arrival time at that one encounter. | Changes component 4's preparation meaning and needs a separate G1/G3 task-role decision if ever proposed as the primary task. A point model used only for the terminal boundary has no such implication but does not resolve this upstream gate. |

**Provisional recommendation.** Keep the two-stage task fixed and give
A-H one bounded qualification: identify the minimum upstream
travel/arrival memory and show that R1 can use it at early merge
opportunities under a common advice range, with residual traffic
reaching the compulsory lane-end boundary. If that requires
consequential internal positions or unsupported instant mixing,
return to B with that concrete reason. The point-only upstream
version remains a simpler rival, not a silent replacement of the
primary task. This recommendation does not approve new state or
a new choke law.

The pass stops at this new Type 2 G3/VQ3-P/T/S choice, with G1 task-role,
G2 observation and G4 complete-time consequences. No dependent model,
experiment or simulator work follows until it is resolved.

[Source locations, reference list and inference limits](../../extraction/research_readiness/vsl_b2a_compact_closure_source_audit.md)

[Work and verification record](vsl_b2a_work_report.md)
