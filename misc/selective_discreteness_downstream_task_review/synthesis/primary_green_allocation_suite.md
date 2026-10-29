# T6 primary green-allocation suite

Date: 2026-09-10  
Status: proposed scientific contract; awaiting T6 approval

## Technical summary

The primary experiment is a fixed-topology **effective-service allocation** task. A continuous vector allocates a fixed service budget among fixed phase groups. It does not claim to produce executable green intervals. The experiment progresses from a representation-neutral intersection to shared-lane order, finite turning-bay storage, combined access/order effects, and held-out variation. Every variant retains the same action meaning and objective; only geometry, traffic state, and activated mechanism change.

The primary causal contrast is not “with bay versus without bay.” It is whether increasingly informative representations predict different service and useful control directions under carefully matched states. The no-bay and bay variants separate head-of-line order, physical storage, bay accessibility, and network spillback rather than combining them immediately.

## Common symmetric four-leg intersection

Use a regular isolated four-leg junction with north, south, east, and west inbound approaches. Before a variant activates shared-lane or bay behavior, the geometry, fundamental-diagram parameters, saturation-flow convention, downstream receiving conditions, demand profile, and left/through/right route shares are identical under 90-degree rotation. This gives a symmetry check: rotating the complete scenario and correspondingly permuting the control vector must produce the same objective and permuted gradient.

The fixed topology has four protected effective-service groups:

| Group | Served movements | Conflict meaning |
|---|---|---|
| P1 | Northbound and southbound through/right | North–south through service |
| P2 | Northbound and southbound protected left turns | North–south left-turn service |
| P3 | Eastbound and westbound through/right | East–west through service |
| P4 | Eastbound and westbound protected left turns | East–west left-turn service |

Opposing left turns in P2 and P4 are assumed to be geometrically compatible protected movements. Right turns remain grouped with through traffic and receive no separate allocation. The four quantities are effective service fractions, not executable signal phases: their ordering within a cycle and yellow/all-red intervals are not modeled. Pedestrians, permissive turns, offsets, phase reordering, and actuated logic remain deferred.

## Common symmetric traffic construction

Each inbound approach has the same released demand profile and fixed route shares `(left, through, right)` in the symmetric core cases. Corresponding outgoing links have the same geometry and receiving conditions. Initial source queues and in-network occupancy are likewise rotationally matched. Route identity and ordered route-mass realizations are fixed before differentiation.

The variants alter all four approaches in the same way:

- V0 gives every approach movement-exclusive full-length lanes;
- V1 gives every approach the same full-length shared-lane arrangement;
- V2 and V3 give every approach an equal-length finite left-turn bay and the same feeder geometry; and
- V4 begins with these symmetric families and adds predeclared held-out asymmetry strata to test robustness.

For V1 and V3 aggregate-matched order pairs, the same order pattern is rotated onto all four approaches by default. The paired scenario changes that pattern everywhere while preserving approach demand, movement totals, geometry, initial aggregate occupancy, service allocation, and downstream supply. A later diagnostic may perturb only one approach to localize an effect, but such an asymmetric case is not the default evidence case and must be labeled separately.

## Common traffic allocation

Traffic is continuous vehicle-equivalent mass carried by fixed route records. Each scenario declares:

- a demand profile for every origin approach;
- fixed route/movement shares for left, through/right, and cross-street traffic;
- a fixed ordered route-mass realization on every inbound approach;
- fixed lane permissions and lane-choice intent;
- initial link, source-queue, lane-zone, and ordered-ledger state; and
- a fixed downstream receiving profile.

For an aggregate-matched pair, total approach mass, movement totals, lane storage, demand profile, signal action, and downstream supply are identical. Only the ordering of route/movement mass—or an explicitly declared accessibility state derived from that order—changes. Traffic is never resampled while differentiating or comparing models.

The common demand level is varied across undersaturated, near-capacity, and oversaturated regimes so all four service allocations are consequential. Numeric ranges remain defaults to calibrate after the relevant simulator interfaces exist. Symmetry is an initial construction and validation property, not an assumption that every held-out traffic state must remain symmetric.

## Variant V0 — isolated, movement-exclusive, no turning bay

| Property | Definition |
|---|---|
| Network | One isolated four-leg junction with source and sink links |
| Approach layout | On every approach, separate full-length through/right and left-turn lanes; no short bay; one movement class per lane |
| Traffic allocation | Fixed route shares assigned to their permitted exclusive lanes; order should have no behavioral effect |
| Mechanism active | Aggregate propagation and signal service only |
| Intended comparison | All conforming representations should agree in forward output and gradients |

**Intention:** establish task implementation, conservation, units, objective matching, and macro-limit equivalence before any selective mechanism is active. A selective-order advantage here is a defect or an unmatched realization, not a positive finding.

## Variant V1 — isolated, one shared stop-line lane, no turning bay

| Property | Definition |
|---|---|
| Network | Same isolated junction |
| Approach layout | On every approach, one full-length lane shared by left and through/right traffic; no auxiliary bay |
| Traffic allocation | Rotationally symmetric aggregate-matched ordered pairs place red-ineligible versus green-eligible movement mass at each lane head while preserving movement totals |
| Mechanism active | Exact shared-lane head-of-line order and signal eligibility |
| Intended comparison | Test whether order changes attainable service when aggregate composition is identical |

**Intention:** isolate pure head-of-line order without short-lane storage or bay-entry mechanics. This determines whether exact order adds information beyond a mixed movement-composition or partial-FIFO baseline.

## Variant V2 — isolated, finite left-turn bay, storage emphasis

| Property | Definition |
|---|---|
| Network | Same isolated junction |
| Approach layout | On every approach, one full-length feeder/through lane plus one equal-length finite auxiliary left-turn bay beginning within the downstream interaction zone |
| Traffic allocation | Left-turn intent and total bay demand are fixed; arrival ordering is homogenized or chosen so all intended bay users reach the opening whenever storage permits |
| Mechanism active | Bay storage, occupancy, overflow, and resulting upstream restriction |
| Intended comparison | Test whether lane/storage-aware aggregate state explains the effect before exact order is needed |

**Intention:** isolate finite physical storage from ordered accessibility. If the lane/storage aggregate baseline matches the selective model here, that is the expected result and validates the baseline ladder.

## Variant V3 — isolated, finite left-turn bay, access/order emphasis

| Property | Definition |
|---|---|
| Network | Same geometry as V2 |
| Approach layout | Same symmetric four-bay geometry as V2 |
| Traffic allocation | Aggregate-matched pairs rotate the same fixed left/through order pattern onto every approach; intended bay users are reachable in one member and obstructed in the other while totals and nominal lane intent remain identical |
| Mechanism active | Realized bay accessibility, ordered blockage, finite storage, and movement-specific service |
| Intended comparison | Determine whether exact order improves forward and gradient predictions beyond aggregate lane/storage state |

**Intention:** provide the main selective-discreteness test. It must include pairs where order matters and controls where it does not. A positive claim requires the selective model to distinguish the pair and predict the richer evaluator's response more usefully; internal divergence alone is insufficient.

## Variant V4 — isolated combined and held-out family

| Property | Definition |
|---|---|
| Network | Same isolated-junction family; both V1 and V3 layouts may be sampled as declared strata |
| Approach layout | Shared lane or finite bay, with geometry fixed within each scenario; symmetric core plus labeled held-out asymmetry strata |
| Traffic allocation | Fixed scenario bank varies common demand regime, movement share, initial queue, bay length/storage, order pattern, and downstream supply; held-out combinations and controlled asymmetric perturbations are reserved before optimization |
| Mechanism active | Combined storage, access/order, blockage, and signal competition |
| Intended comparison | Test robustness and identify where simpler representations remain sufficient |

**Intention:** prevent one hand-constructed pair from carrying the conclusion. Results must be reported by mechanism stratum, including equivalence and failures, rather than only as an aggregate win rate.

## Historical proposal I1 — excluded from this review

Scope override (2026-09-14): T6 is approved for V0–V4 only. The user excluded V5, including its renamed I1 form, from this review. The description below is retained solely as proposal history; it imposes no review requirement or authorization.

| Property | Definition |
|---|---|
| Network | Two signalized junctions connected by one aggregate long link; only the downstream focal junction's service allocation is optimized |
| Focal layout | Downstream junction uses the V0, V2, or V3 focal approach; upstream signal and all nonfocal controls are fixed arrival shapers |
| Traffic allocation | Same fixed route shares/order logic as isolated variants, with upstream release patterns and downstream receiving states fixed per scenario |
| Mechanism active | Long-link propagation, arrival platooning, local bay/order behavior, and upstream spillback from the focal zone |
| Intended comparison | After V0–V4 close, test whether the isolated mechanism survives its intended aggregate-long-link/local-detail architecture |

**Intention:** serve as a later integration and initial network test, not as a primary scientific variant and not as general corridor signal coordination. It tests compositional relevance without adding offsets or a second optimized controller. It is opened only if needed after V0–V4; failure or incompleteness in V0–V4 cannot be rescued by I1.

## Variant ordering and stop logic

The primary execution order is V0, V1, V2, V3, then V4. Each later variant depends on the earlier relevant distinction:

- stop representation claims if V0 equivalence fails;
- do not attribute V3 differences to order unless V2 has isolated storage;
- do not optimize before forward and derivative checks pass in the applicable stratum;
- retain negative results: if lane/storage aggregates match richer behavior, exact order is unnecessary in that regime.

I1 is outside this primary order. A later implementation or integration gate may require it after V0–V4 are complete, but T6 does not pre-authorize it as part of the first scientific campaign.

## Decision-status ledger

| Item | Status at T6 proposal |
|---|---|
| Candidate A and effective-service claim level | Fixed by T5 user decision |
| V0–V4 hierarchy and intended causal roles | Accepted by the user during T6 review; formal gradient paths remain under review |
| Rotationally symmetric four-leg, four-service-group construction | Proposed default following user direction |
| Identical corresponding approach geometry, demand shares, and receiving conditions in core cases | Proposed default following user direction |
| Fixed route shares and fixed order during differentiation | Fixed by project invariants |
| Exact numeric link lengths, bay lengths, demands, capacities, and horizons | Default pending implementation calibration |
| Conditional corridor integration/network test I1 | Deferred until V0–V4 complete or a later integration gate requires it |
| Executable phase timing, offsets, cycle choice, actuated control | Deferred |
