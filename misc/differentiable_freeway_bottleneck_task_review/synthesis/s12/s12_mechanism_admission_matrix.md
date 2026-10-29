# S12 mechanism-admission matrix

Date: 2026-09-30. Status: completed under G1-A/G2-A/G3-A and working-default
G4-A; final G4 decision pending at S12-UG1 / AMR-R1.

## Common screen

Every family is tested against the permanent three-to-two lane drop, one common
lane-uniform upstream VSL action, exact strong aggregate history, conservative
mass flow, finite receiving/storage, complete affected-cohort accounting and the
S05 fastest-action obstruction.

| Family | Source-bounded state and service mechanism | Advice reachability | S05 escape | Strong-observer result | Boundary verdict |
|---|---|---|---|---|---|
| **M1 — lane-change void/relaxation** | Particle or relational gap/relaxation state temporarily reduces discharge; S12-S1/S5 and S11-S3/S4. | Common VSL may alter lane-change timing, but no adopted continuous-mass action law. | Breaks fixed service. | Gap/relaxation state is finer than totals, but exact consequential collision absent. | **AMR-E for this family:** credible mechanism; adaptation too substantive for bounded admission. |
| **M2 — conservative mandatory transfer with finite receiving/gap cost** | Per-lane mass, mandatory lateral demand, target receiving shared by longitudinal/lateral entrants, and extra lane-change spacing; S12-S2, FB0030, S12-S3. | Common VSL changes lane-wise sending/density; S06-S3/FB0039 show lane-preparation response is possible but variable. | **Yes:** service becomes endogenous to lane state and action; arrival-only dominance no longer follows. | Lane-wise nonlinear receiving cannot generally be computed from totals alone; S05 supplies information-side non-injectivity. Exact near-drop pair remains future work. | **Provisional AMR-A under G4-A.** |
| **M3 — optimized spatial merging/lane balance** | Directly chosen lateral fractions spread merging and balance continuing lanes; FB0038. | Requires lateral-flow command rather than common VSL. | Breaks fixed service under its own actuator. | Lane state matters, but benefit is entangled with added control. | **AMR-C:** actuator mismatch. |
| **M4 — perceived-density lane-drop capacity** | Lane-change intensity raises perceived density; downstream acceleration law lowers demand; S12-S4. | Compatible in principle with VSL. | Breaks fixed capacity. | Consequential input is a compressed intensity/density variable and may be augmentable in an aggregate observer. | **AMR-B/E:** aggregate-equivalence unresolved; not selected. |
| **M5 — aggregate capacity drop/hysteresis** | Cumulative link state and queue-triggered reduced capacity under VSL; FB0022 and S06-S3 CTM crosscheck. | Direct common-VSL compatibility. | Breaks fixed service and can make slower VSL useful. | Required state is explicitly aggregate; no hidden lane information is needed. | **AMR-B:** strong aggregate countercandidate. |

## Why M2 passes the lightweight structural threshold

M2 has a source-bounded input/output contract:

- **inputs:** per-lane mass/density, mandatory ending-lane demand, longitudinal
  sending, target-lane receiving, lane-change spacing factor and common VSL;
- **outputs:** conservative longitudinal and paired lateral flows plus realized
  downstream service;
- **invariants:** nonnegative flows, donor-mass bounds, target receiving/storage
  bounds and exact cancellation of lateral transfers in total mass;
- **aggregate limit:** with zero mandatory transfer, nonbinding receiving or
  identical lane states, it reduces to an ordinary aggregate first-order flow
  description;
- **falsification:** reject the family for this branch if common lane-uniform VSL
  cannot affect its transfer/receiving inputs, if lane-wise service is determined
  by the declared aggregate history, or if complete accounting restores one
  common best action for all admissible hidden states.

The structural escape does not use a fitted favorable number. In the ordinary
regime with positive mandatory ending-lane demand and binding finite target
receiving, lateral and longitudinal entrants compete for the same space. Any
admissible positive extra spacing requirement changes that allocation and makes
service depend on lane state. Common VSL can change the time-varying sending and
receiving inputs. Consequently the fixed-service premise of S05 is absent.

This argument proves neither the sign nor the size of a useful control effect.
It establishes only that fastest-arrival dominance is no longer a theorem of the
model class.

### Admission ladder

| Level | Question | M2 result | Meaning |
|---|---|---|---|
| L1 traffic legitimacy | Is the mechanism source-supported and conservative? | Pass. | Per-lane CTM transfer and finite receiving/gap acceptance are established modeling devices. |
| L2 task compatibility | Can it represent a permanent lane drop with common VSL as the only action? | Qualified pass. | Geometry and action are compatible; the exact common-VSL response join remains to be frozen. |
| L3 obstruction escape | Does it remove fixed advice-independent service without choosing a favorable coefficient? | Pass. | Binding receiving makes service depend on mandatory lateral demand and lane state. |
| L4 information relevance | Is consequential state plausibly lost by lane aggregation? | Conditional pass for admission. | Lane-wise nonlinear allocation precedes aggregation; the exact full-history near-drop pair is missing. |
| L5 decision result | Does hidden state change the useful common-VSL action? | Open. | Requires an exact witness and complete-accounting ranking. |
| L6 gradient result | Is the resulting gradient correct and useful? | Open. | Only the piecewise/active-set derivative boundary is classified. |

AMR-A is reached at L1–L4. It authorizes planning the work needed for L5; it does
not claim that L5 or L6 passes.

## Observer-separation audit

The aggregation map preserves lane totals only after summing. M2 applies finite
receiving constraints and mandatory-transfer demand before that sum. Because
lane-wise minimum/priority operations do not commute with aggregation, two lane
allocations can share the same totals yet request different lateral receiving and
realize different service.

That is a coherent information-separation argument, supported by S12-S2's
multi-lane/surrogate comparison and S05's early-history collision. It is not the
later certificate. A full plan must still construct reachable preparations with
the same entire strong aggregate history and show that the lane-wise difference
survives near the drop under the same action set.

## Strongest-action and accounting audit

M2 removes the logical step that made the fastest action universally best: the
service sequence can now change with advice-conditioned lane evolution. It does
not establish that slower advice wins. A later certificate must include the
fastest feasible action, count upstream waiting and all affected cohorts through
common clearance, and accept these null outcomes:

1. all hidden states still choose the fastest action;
2. a slower action helps both states equally, so hidden information has no value;
3. hidden service differs but the complete outcome ranking does not; or
4. an aggregate capacity-drop model reproduces the same ranking.

## Derivative boundary

For continuous lane masses and fixed active constraints, demand/supply and
receiving allocations are piecewise differentiable. Minimum, priority and
capacity-activation changes create nonsmooth active-set boundaries. Exact lane
identity, lane permission and topology remain structural metadata. No smoothing,
gradient formula, derivative correctness or downstream usefulness is admitted by
S12.

## Provisional verdict

Under working G4-A, M2 satisfies the lightweight admission criteria and yields
**AMR-A — admit one family for a separately approved analytical model-contract
and derivation plan**. M5 confirms that advice-dependent service alone is
insufficient for a hidden-information claim. The final verdict remains pending
the user's deferred G4 decision.
