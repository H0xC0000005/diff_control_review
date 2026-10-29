# Milestone 2 supplementary modeling context: equal-binned cumulative-mass interaction zone

**Scope:** scientific and engineering context for the previously discussed local interaction-zone model.  
**Purpose:** preserve modeling decisions and direct implications that are more specific than the current project context.  
**Status language used here:**  
- **Agreed modeling fact** = explicitly established in the prior design discussion and consistent with the current project backbone.  
- **Engineering implication** = follows directly from the agreed representation but is not itself a new traffic-behavior assumption.  
- **Still parameterized/open** = the representation is fixed, while a numerical value or lower-level realization was not fixed.

---

## 1. Position of the interaction zone in the simulator

### Agreed modeling fact

The intended architecture is:

`aggregate LTM/Newell long-link region -> fixed downstream lane-local interaction zone -> node/signal service -> downstream LTM`.

Only a bounded inbound region near the downstream node is represented with lane-local mesoscopic detail. The rest of the link remains in the established aggregate LTM/Newell representation.

The local zone is therefore a **localized refinement of a physical downstream portion of the inbound approach**, not a whole-link lane grid.

### Engineering implication

The physical mass associated with the refined link has one ownership at a time. A natural decomposition is

`M_a = M_U,a + sum_l M_Z,a,l`,

where `U` is the upstream aggregate portion and `Z` is the lane-local interaction zone.

A local zone added on top of an already complete whole-link occupancy would double-count physical mass/storage. An extra vertical buffer appended to the link would likewise lengthen the modeled physical system unless the network geometry were explicitly changed.

### Still parameterized/open

The exact numerical span of the detailed zone and the exact partition of propagation delay between the upstream aggregate subdomain and the local zone were not fixed by the earlier conceptual agreement.

A previously discussed concrete example was approximately:

- inbound detailed span: `100 m`;
- representative vehicle-equivalent spacing basis: approximately `4 m`;
- about `25` local mass cells/bins in that illustrative setting.

These values were examples for reasoning about resolution, not universal constants of the method.

---

## 2. Per-lane, equal-binned cumulative-mass coordinate

### Agreed modeling fact

The interaction-zone grid is **per lane**, not per link.

For lane `l`, the ordered coordinate is cumulative traffic mass / FIFO rank rather than physical distance. Let `xi >= 0` denote queue-rank mass, with `xi = 0` at the downstream head / stop-line side and increasing upstream toward the tail.

A fixed mass resolution `Delta xi > 0` defines equal-width rank bins

`I_k = [k Delta xi, (k+1) Delta xi)`.

Thus:

- all ordinary bins have the same width in **vehicle-equivalent mass**;
- the bin index represents ordered mass rank, not a physical metre coordinate;
- changing `Delta xi` changes representation resolution, not physical lane length;
- fractional continuous mass is allowed inside every bin;
- no vehicle-count integerization occurs at bin boundaries;
- if geometry-derived lane storage is not an exact multiple of `Delta xi`, the structural storage boundary can truncate the final logical bin rather than altering traffic mass.

The local continuous composition state is

`W[lane, bin, movement] >= 0`

with units of continuous vehicle-equivalent mass.

For every lane,

`sum_{bin,movement} W = M_Z,lane`.

### Engineering implication

The grid has a fixed tensor shape for a configured local zone even though the traffic mass inside it is continuous.

If the physical lane storage is not an exact multiple of `Delta xi`, the last logical interval can be a partial structural bin or be represented with an explicit mask. Traffic mass itself is not rounded to the bin width.

Padding/masking for heterogeneous lane capacities is tensor-layout metadata and carries no physical traffic mass.

### Still parameterized/open

The numerical bin width `Delta xi` was not globally fixed.

A previously discussed example used approximately `4 vehicle-equivalents per bin`. This was an illustrative resolution, not a settled universal value.

The intended model class retains a **fixed mass-bin resolution within a configured zone**, with later sensitivity/convergence to zone span and `Delta xi` possible if needed.

---

## 3. Meaning of a mass bin

### Agreed modeling fact

A bin stores continuous **movement composition over an ordered mass interval**.

If the lane-local movement composition is represented conceptually by `c_l,m(xi)`, then

`W_l,k,m = integral over I_k of c_l,m(xi) dxi`.

A bin can therefore be mixed.

For example,

`W[l,k,T] = 4`, `W[l,k,L] = 1`

means that the corresponding rank interval contains five vehicle-equivalents, four currently mapping to through and one to left.

This does not identify whether the exact semantic order is `[T(4), L(1)]` or `[L(1), T(4)]`.

The bin is an aggregated continuous-composition representation, not an exact packet-order encoding.

### Agreed modeling fact

Mixed-bin composition is **not** interpreted as literal random overtaking.

It is an unresolved-order/mixing representation at the selected tensor resolution. Exact FIFO semantic order is retained separately.

---

## 4. Exact ordered route-mass ledger aligned with the grid

### Agreed modeling fact

The grid and the ordered route-mass ledger are two synchronized views of the same lane-local traffic mass.

Persistent route semantics are represented by ordered continuous route-mass entries, conceptually `(route_id, route_position, mass)`.

At node `n`, the current movement is obtained through the fixed structural projection

`movement = phi_n(route_id, route_position)`.

The full future route is not repeatedly stored in each local cell. Route identity remains in the route table / ordered ledger, and current movement is a local projection.

### Agreed modeling fact

The roles are intentionally separated:

- **grid** = continuous fixed-size physical/composition state;
- **ordered ledger** = exact semantic FIFO/route order.

The grid does not need to reconstruct exact route order.

The ordered ledger supplies exact order when later node service needs to distinguish states such as `[T(4),L(1)]` from `[L(1),T(4)]`.

### Engineering implication

A separate microscopic/raw-packet stop-line region is not required.

The combination

`equal-binned mass grid + aligned exact ordered route ledger`

is the intended local representation.

The route ledger can remain the semantic/update authority while the grid is deterministically projected/rebuilt from it. If both views are persisted, their mass equality is an invariant rather than two independent physical accounts.

---

## 5. Conservative projection from ordered mass to equal bins

### Engineering implication

Suppose an ordered lane-ledger entry `e` occupies cumulative-rank interval `[q_e^0, q_e^1)` and maps to current movement `m_e`.

For equal bin `I_k`, define overlap mass

`omega_e,k = length([q_e^0,q_e^1) intersect I_k)`.

Then

`W_l,k,m = sum_{e:m_e=m} omega_e,k`.

This produces a conservative grid:

`sum_{k,m} W_l,k,m = sum_e w_e = M_Z,l`.

Properties include:

- one ledger entry may occupy several equal bins;
- one bin may contain several ledger entries and several movements;
- partial bin overlap is represented by continuous mass;
- no rounding or integerization occurs at bin boundaries;
- lossless adjacent ledger merging does not alter the resulting physical mass.

For a fixed overlap topology, the numerical map consists of additions, subtraction, `min`, `max`, and linear overlap weights.

---

## 6. Queue evolution as prefix removal, shift, append, and rebinning

### Agreed modeling fact

The cumulative-mass coordinate was chosen partly because discharge can be represented as a continuous shift rather than integer vehicle dequeue.

Let the pre-service composition be `c_old(xi)`. If a continuous downstream prefix mass `q` leaves the lane, then the surviving composition is

`c_shifted(xi) = c_old(xi + q)`.

Thus service removes the interval `[0,q)` and shifts the remaining traffic toward the downstream head.

New accepted traffic is appended at the upstream tail in its ordered route-mass sequence.

The conceptual local update is:

`continuous prefix removal -> rank shift -> ordered tail append -> equal-bin conservative rebinning`.

### Engineering implication

The same fixed equal-bin lattice is retained after the update. The representation does not create or delete bins as traffic enters or exits.

The continuous service amount `q` changes interval overlaps continuously while the active structural overlap pattern is unchanged.

This is one source of the intended differentiability of the local representation.

---

## 7. Continuous traffic mass and selective discreteness

### Agreed modeling fact

Traffic quantity remains continuous throughout the interaction zone.

Continuous quantities include, when relevant:

- ledger/package masses;
- local bin movement masses;
- accepted ingress/egress mass;
- lane storage occupancy;
- LTM cumulative counts;
- continuous service capacities;
- later signal-control parameters.

Structural/non-differentiated quantities in the initial model include:

- route IDs;
- route-position labels;
- current movement labels;
- lane identities and permissions;
- topology;
- phase sequence;
- exact semantic order skeleton of a fixed scenario.

No floor/round operation converts continuous flow into integer vehicles.

Packets/cohorts are divisible continuous mass, including at bin boundaries and accepted-flow boundaries.

---

## 8. Physical storage is separate from mass-bin indexing

### Agreed modeling fact

The equal-bin grid is not a physical-space discretization.

Physical lane storage comes from road geometry and traffic density, conceptually

`K_Z,l = L_Z,l * k_j,l`

or an equivalent vehicle-equivalent storage formulation consistent with the fundamental diagram.

The number of mass bins does not by itself determine metres of road or physical queue length.

The earlier illustrative relation

`100 m` and `4 veh-eq/bin` -> roughly `25 bins`

was a convenient example only after assuming a representative jam-spacing conversion. The physical storage contract remains geometry/density based.

### Engineering implication

Changing `Delta xi` refines or coarsens movement-composition resolution without changing the physical storage of the lane.

---

## 9. Spillback when the detailed zone fills

### Agreed modeling fact

The local zone is not a finite buffer that clips traffic when it fills.

The causal relation is

`lane/local-zone storage fills -> local receiving decreases -> upstream admission decreases -> excess mass remains upstream -> LTM/Newell propagates the queue upstream`.

Thus a queue longer than the detailed zone remains physically representable:

- the downstream portion occupies the lane-local interaction zone;
- excess queue remains in the upstream aggregate region;
- receiving feedback links the two.

No traffic mass disappears because the local detailed tensor has reached its storage boundary.

### Engineering implication

The local zone and upstream LTM require a conservative internal-boundary coupling.

A full lane can block additional mass committed to that lane even while other lane storage is available if no behavioral reassignment is active at this model stage.

---

## 10. Lane commitment before behavioral lane allocation

### Agreed modeling fact

The per-lane representation requires traffic to be committed to lanes, but behavioral lane allocation is a separate model layer.

For the interaction-zone construction stage, lane commitment is exogenous/structural rather than a learned or equilibrium behavioral choice.

A conceptual mapping is

`psi(link, route_id, route_position) -> lane`.

Once traffic is committed to a lane in the initial model:

- no explicit within-zone lane changing is modeled;
- no overtaking operator changes exact lane FIFO order;
- no reactive reassignment around a full lane is implied by the grid itself.

A blocked designated lane therefore leaves unaccepted mass upstream rather than automatically redistributing it to another lane.

### Agreed modeling fact

This structural commitment is distinct from the later behavioral chain

`perceived lane resistance -> desired allocation -> finite accessibility/storage -> realized occupancy`.

The latter belongs to the later lane-allocation/realized-accessibility model and was intentionally not collapsed into the interaction-zone representation itself.

---

## 11. Exact FIFO service is enabled by the representation but is a later behavior layer

### Agreed modeling fact

The representation was designed so that later service can consume an exact service-eligible ordered prefix without integer vehicle discharge.

Example:

`[T(4), L(1), T(3)]`.

If through is service-eligible and left is not, an exact ordered-prefix service operator can discharge at most the leading `T(4)` before the red left-turn mass becomes the head-of-line blocker.

The equal-binned grid alone cannot infer this exact stopping point when order is mixed inside a bin; the aligned ledger supplies it.

### Scope distinction

The ability to represent this state is part of the interaction-zone design.

The actual order-dependent signal/FIFO service rule, shared-lane blocking behavior, turn-pocket overflow effects, and partial-FIFO behavior form a later behavioral layer rather than being intrinsic to the equal-bin grid definition.

---

## 12. Differentiability of the equal-binned grid

### Agreed modeling fact

The differentiability strategy is **fixed-structure piecewise differentiation**, not smoothing of structural semantics.

Within a fixed route/lane/order/bin-overlap structure:

- continuous masses participate in ordinary tensor arithmetic;
- prefix service amounts change overlap lengths continuously;
- conservative rebinning uses linear overlap contributions;
- storage and service limits use piecewise `min/max`-type operations.

Ordinary AD therefore propagates through the continuous physical quantities inside a stable active structure.

Nonsmooth changes can occur when:

- a ledger boundary crosses a mass-bin boundary;
- a lane reaches exact storage saturation;
- an ordered active prefix changes;
- another `min/max` constraint becomes active.

These are active-structure boundaries rather than a reason to integerize traffic or make the binning stochastic.

No smoothing of the equal-bin map was part of the agreed V1 representation.

---

## 13. Neutral interaction-zone behavior before later lane/FIFO behavior

### Engineering inference

The equal-binned interaction zone can exist before order-dependent lane service is activated.

In such a neutral state:

- the zone represents continuous lane occupancy/composition;
- storage constrains ingress;
- the accepted aggregate node/signal model can remain the authority for how much movement flow is served;
- local route/lane state conservatively identifies and replays the corresponding mass;
- exact lane-order information is retained without yet using it to reduce node service.

This separates:

`Can the lane-local state be represented and coupled conservatively?`

from:

`Does exact order/storage change realized signal service?`

The second belongs to the later mesoscopic-behavior layer.

---

## 14. Macro-equivalent interpretation of the local refinement

### Engineering inference

When local lane distinctions are behaviorally neutralized, the detailed state represents the same underlying traffic mass/kinematic-wave physics rather than a new traffic process.

Two distinct notions therefore exist:

1. **representation neutrality** — lane/grid bookkeeping does not invent or lose mass or create order-dependent service when those effects are disabled;
2. **numerical equality to an unsplit LTM trace** — may additionally depend on the chosen temporal/spatial decomposition.

A series decomposition of one physical link can change finite-step indexing or active constraints even if total physical length and storage are preserved. That is a numerical/discretization issue rather than a change to the equal-binned representation itself.

---

## 15. Fixed versus still-parameterized parts of the model

### Agreed representation

The following modeling choices are established:

- detailed state exists only in a fixed downstream inbound interaction zone;
- the grid is **per lane**;
- the ordered coordinate is **cumulative vehicle-equivalent mass / FIFO rank**;
- `xi = 0` is at the downstream head/stop-line side;
- bins are **equal-width mass bins** for a configured resolution;
- bin values store continuous movement composition;
- fractional/partial bins are allowed;
- traffic mass is never integerized to the bin width;
- exact route/FIFO order is retained by an aligned ordered route-mass ledger;
- the grid does not replace route identity;
- there is no separate raw microscopic stop-line packet region;
- queue evolution can be represented by continuous prefix removal, rank shift, ordered tail append, and conservative rebinning;
- physical storage is derived from geometry/jam density, not from bin count alone;
- a full detailed zone feeds back to upstream LTM rather than clipping excess queue;
- lane commitment at this construction stage is structural/exogenous;
- no within-zone overtaking/lane changing is implied;
- structural labels are not differentiated;
- continuous masses/storage/service remain on the AD path.

### Still parameterized/open numerical details

The following were not globally fixed by the earlier modeling discussion:

- exact physical interaction-zone span for each test network;
- exact mass resolution `Delta xi`;
- exact padding/mask layout for heterogeneous lane capacities;
- exact storage/travel-time partition between the upstream LTM subdomain and the downstream local zone;
- exact internal-boundary time indexing;
- exact tensor caching policy for whether `W` is persisted or deterministically materialized from the ledger.

These choices affect engineering/numerical realization without changing the equal-binned cumulative-mass representation itself.

---

## 16. Compact model summary

The agreed local representation is:

`physical downstream lane-local zone`
+
`continuous equal-width FIFO-rank mass bins W[lane,bin,movement]`
+
`aligned exact ordered route-mass ledger`
+
`geometry-based finite lane storage`
+
`conservative coupling to upstream LTM`.

Its local evolution is conceptually:

`LTM-eligible ordered mass -> structural lane commitment -> tail append -> equal-binned state -> continuous prefix removal -> rank shift/rebin -> downstream transfer`.

Excess traffic remains in the upstream LTM region when local storage is unavailable.

The representation is deliberately neither a homogeneous macroscopic link nor an integer-vehicle microscopic queue. It preserves continuous physical traffic mass while retaining the discrete semantic ordering needed by later lane/FIFO/blockage behavior.
