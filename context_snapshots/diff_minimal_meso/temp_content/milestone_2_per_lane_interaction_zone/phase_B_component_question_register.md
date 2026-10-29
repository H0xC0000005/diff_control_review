# Milestone 2 Phase B — complete component-question register

Status: **All component-local questions inventoried; Component 2.1 is the first active decision set**  
Parent record: `phase_B_revision.md`

## How to read dependencies

- A **decision dependency** means the parent choice must close first.
- A **forward interface constraint** means a later component already establishes data that an earlier interface must preserve, without allowing the later component to change an accepted scientific contract.
- An **implementation dependency** controls D/E order only; it does not prevent Phase B from reviewing all questions now.
- A conflict reopens the smallest named parent contract and its dependent questions explicitly.

## Complete inventory and cross-component dependencies

| ID | Core question | Decision dependencies | Forward consumers |
|---|---|---|---|
| C2.1-Q1 | Structural record and reconciliation owner | G1 | all components |
| C2.1-Q2 | Allowed per-lane physical heterogeneity | G1; Q1 | 2.3, 2.4, 2.5 |
| C2.1-Q3 | Lane order and permission completeness | inherited commitment; Q1 | 2.2–2.5 |
| C2.2-Q1 | Lane-ledger record boundary | 2.1-Q1/Q3; G2 | 2.3–2.6 |
| C2.2-Q2 | Commitment-map representation/validation | 2.1-Q3; G2 | 2.4, 2.5 |
| C2.2-Q3 | Exact merge invocation and telemetry | 2.2-Q1; M2/M3 seam | 2.3, 2.5, 2.6 |
| C2.3-Q1 | Bin width/count/partial-capacity schema | 2.1-Q2; G3 | 2.4–2.6 |
| C2.3-Q2 | Half-open overlap convention/signature | 2.2-Q1; 2.3-Q1; G6 | 2.4, 2.6 |
| C2.3-Q3 | Cached versus on-demand grid | 2.3-Q1/Q2; G3/G6 | 2.4–2.6 |
| C2.4-Q1 | Lane capacity and delay derivation | 2.1-Q2; G1/G2 | 2.4-Q2/Q3, 2.5, 2.6 |
| C2.4-Q2 | Commitment-feasible receiving algorithm | 2.2-Q2; 2.4-Q1; G2/G4 | 2.5, 2.6 |
| C2.4-Q3 | Zone eligibility representation | 2.2-Q1; 2.4-Q1; G2 | 2.5, 2.6 |
| C2.4-Q4 | Storage roundoff/failure policy | 2.3-Q1; 2.4-Q1/Q2; G6 | 2.5, 2.6 |
| C2.5-Q1 | Scenario/state/result/history schema | accepted 2.1–2.4 | 2.5-Q2/Q3, 2.6 |
| C2.5-Q2 | Mixed refined/unrefined orchestration | 2.1-Q1; 2.5-Q1; G5 | 2.6 |
| C2.5-Q3 | Boundary conservation context | 2.2-Q1/Q2; 2.5-Q1 | 2.6 |
| C2.6-Q1 | Independent scalar oracle floor | equations from 2.1–2.5; G5 | acceptance evidence |
| C2.6-Q2 | FD scan, tolerances, signature schema | signatures from 2.2–2.5; G6 | acceptance evidence |
| C2.6-Q3 | Artifact/provenance schema | 2.5-Q1; G5/G6 | integration and closure |

## Component 2.1 — lane/zone topology, geometry, and storage

Component 2.1 defines structural metadata only. It does not transfer traffic, construct ledgers/grids, or implement node behavior.

### C2.1-Q1 — structural records and reconciliation ownership

**Problem statement.** What exact meso-owned record boundary should carry geometry-authoritative primitives and prove that the `U_a + Z_a` decomposition describes the same physical link as the accepted M0 derived FD record?

**Assumed model-chain function.** Later components need one immutable lookup from a refined global link ID to its physical decomposition, ordered lanes, storage, permissions, and derived upstream LTM parameters. The accepted `NetworkDefinition` and `LinkFDParameters` remain unchanged.

**Core gap.** G1 fixes the physical meaning but not record granularity or which constructor owns cross-record reconciliation. Without one owner, constructors could derive quantities differently or accept a meso wrapper inconsistent with M0.

**A — normalized `MesoNetworkDefinition` wrapper with one authoritative constructor (recommended).** Store a reference to the accepted `NetworkDefinition`, a canonical tuple of refined-link/zone definitions, and the G1 physical primitives. The constructor derives upstream and lane quantities once, validates them against accepted whole-link values, and exposes normalized immutable downstream lookups.

- **Pros:** one validation boundary; no M0 interface change; normalized downstream records; central duplicate-ownership rejection.
- **Cons:** comparatively broad structural object; repeats provenance only indirectly present in M0; substantial constructor validation.
- **Dependency/consequence:** becomes M2's sole structural composition root; runtime traffic state remains separate.

**B — independently validated per-link `InteractionZoneDefinition` records.** Each zone references a global link ID and reconciles itself with M0; a thin collection validates uniqueness and ordering.

- **Pros:** smaller records; convenient local testing and reuse; less centralized construction.
- **Cons:** reconciliation can be duplicated; collection-level ownership validation remains; downstream code retains two peer objects.
- **Dependency/consequence:** equivalent to A only if derivation is shared, but produces a wider API.

**C — attach meso geometry to M0 records.** Extend `NetworkDefinition` or `LinkFDParameters` with optional lane-zone fields.

- **Pros:** one apparent network object and fewer lookups.
- **Cons:** reopens M0; couples aggregate users to M2; blurs independent macro/meso comparison.
- **Dependency/consequence:** conflicts with G1 unless G1 and M0 closure are reopened.

### C2.1-Q2 — per-lane heterogeneity contract

**Problem statement.** Which physical attributes may vary by lane, and should M2 enforce homogeneous lanes outside isolated short-lane geometry tests?

**Assumed model-chain function.** Lane geometry determines exact storage and grid masks. G4 limits principal neutral service fixtures to full-length movement-exclusive lanes, but Component 2.1 should not preclude future pocket geometry.

**Core gap.** The globals permit geometry-derived per-lane storage but do not say whether jam density is shared, repeated, or independently variable. That changes configuration size and whether lane differences mean geometry or distinct traffic physics.

**A — common FD primitives with explicit per-lane usable lengths (recommended).** Lanes share jam density, speeds, and nominal capacity convention; each lane carries its usable zone length. Principal G4 fixtures use full-length lanes; shorter lanes occur only in scoped structural tests.

- **Pros:** minimal and interpretable; avoids untested lane-specific physics; supports future bays and partial final bins.
- **Cons:** cannot express lane-specific density/saturation without extension; width/closure differences use usable length.
- **Dependency/consequence:** reconciles cleanly with homogeneous `U_a` and suffices for M2 acceptance.

**B — explicit length and jam density per lane.** Each lane independently defines both, with aggregate compatibility rules.

- **Pros:** most general storage representation.
- **Cons:** introduces heterogeneous-FD meaning M2 does not validate; reconciliation becomes conventional; larger test surface.
- **Dependency/consequence:** may reopen G1 if heterogeneity changes capacity or waves rather than storage alone.

**C — require identical lane lengths and density.** Defer all heterogeneous lane geometry.

- **Pros:** smallest implementation and simplest symmetry tests.
- **Cons:** prevents structural pocket fixtures; forces M3 migration; underuses G3 masks.
- **Dependency/consequence:** compatible with G4's principal fixtures but unnecessarily narrow.

### C2.1-Q3 — permission completeness and canonical lane order

**Problem statement.** How should lane order and movement permissions be authored and validated so every structural commitment has one stable, legal target?

**Assumed model-chain function.** Components 2.2 and 2.3 index lanes by canonical local order. Fixed commitment assigns every route transition to exactly one lane; G4 relies on movement-exclusive neutral fixtures.

**Core gap.** M0 orders movements but has no lateral lane order. Sorting arbitrary IDs need not be physically meaningful, while scenario-only validation can leave other legal routes unsupported.

**A — explicitly authored lateral order with full structural coverage (recommended).** The lane tuple is authoritative under a documented viewpoint. Permissions reference canonical M0 movement indices. Every lane permits a movement, every structurally available movement has a lane, and every commitment resolves uniquely and legally.

- **Pros:** stable physically meaningful indexing; reusable validation; supports future adjacency-aware M3 behavior.
- **Cons:** authors must supply correct order; excluded movements must be removed structurally.
- **Dependency/consequence:** permutation tests permute all maps; G4 fixtures additionally restrict each lane to one movement.

**B — authored order with scenario-used coverage only.** Validate only transitions present in the current scenario.

- **Pros:** supports sparse experiments and incomplete prototypes.
- **Cons:** network validity becomes scenario-dependent; failures move later; creates a second validator.
- **Dependency/consequence:** every scenario constructor must revalidate permissions.

**C — derive order by sorting lane IDs.** Treat IDs as canonical sortable keys.

- **Pros:** deterministic, low-input, easy serialization.
- **Cons:** ID order need not be lateral order; renaming changes tensor semantics; unsuitable for adjacency.
- **Dependency/consequence:** requires later M3 migration.

**C2.1 closure order:** Q1, then Q2, then Q3. If Q2 selects independent heterogeneous lane FD physics, reopen G1 before Q3 closes. The dedicated working copy remains `phase_B_component_2_1_questions.md`.

## Component 2.2 — exact lane-local state and commitment

### C2.2-Q1 — lane-ledger record boundary

**Problem/function/gap.** A lane ledger must retain accepted M1 route, position, mass, and affine eligibility semantics while adding lane ownership and later zone eligibility. The open choice is whether this context belongs inside each accepted `LedgerEntry`, in an M2 wrapper, or only in parallel arrays. Modifying M1 would reopen a closed interface; detached parallel arrays risk misalignment.

**A — `LaneLedger` wrapper around unchanged M1 entries (recommended).** The wrapper owns refined-link/lane identity and a tuple of unchanged `LedgerEntry` values; M2-specific zone eligibility is represented by a synchronized wrapper/profile only where M1's existing downstream eligibility meaning is not identical.

- **Pros:** preserves M1; makes ownership explicit; supports reuse of split/merge primitives.
- **Cons:** nested records and explicit synchronization checks.
- **Dependency:** must expose mass/timing tensors needed by 2.3, 2.4, and G6.

**B — new M2 entry duplicating M1 fields plus lane/timing fields.**

- **Pros:** self-contained record and direct access.
- **Cons:** duplicates semantics and operations; drift risk; conversion boundary expands.
- **Dependency:** requires proof of exact equivalence at every M1/M2 crossing.

**C — modify `LedgerEntry`.**

- **Pros:** one entry type.
- **Cons:** reopens M1 and burdens unrefined ledgers with lane metadata.
- **Dependency:** inadmissible without explicit M1 reopening.

### C2.2-Q2 — commitment-map representation and validation

**Problem/function/gap.** Every reachable `(link, route, route-position)` state on a refined inbound link needs exactly one permitted lane. The scientific commitment is fixed, but lookup ownership and completeness remain open.

**A — canonical dense structural lookup built once (recommended).** Construct a CPU integer lookup aligned with route index/position, plus validation evidence against lane permissions.

- **Pros:** deterministic constant-time lookup; complete validation; easy signatures.
- **Cons:** stores entries for all relevant routes; rebuild required when structural routes change.
- **Dependency:** 2.1-Q3 supplies lane indices and permissions.

**B — immutable mapping keyed by route transition.**

- **Pros:** sparse and readable; simple serialization.
- **Cons:** repeated dictionary lookup; harder tensor-alignment checks; aliases must be rejected carefully.
- **Dependency:** must still validate full structural coverage.

**C — derive from current movement at runtime.**

- **Pros:** smallest authored map.
- **Cons:** ambiguous when several lanes permit one movement; silently introduces a lane-choice rule.
- **Dependency:** conflicts with fixed one-lane commitment.

### C2.2-Q3 — exact merging and fragmentation telemetry

**Problem/function/gap.** Exact adjacent merging is allowed, but M1's predicate includes route state and affine timing continuity. M2 must decide when to invoke it and what fragmentation evidence survives without importing M3 lossy compression.

**A — canonicalize after every completed transaction and report before/after counts (recommended).** Reuse the exact M1 predicate only when all timing meanings coincide; otherwise do not merge.

- **Pros:** deterministic bounded avoidable fragmentation; invariant state; useful M3 baseline.
- **Cons:** extra scan per transaction; wrapper timing equivalence must be explicit.
- **Dependency:** telemetry flows into 2.5 results and 2.6 artifacts.

**B — merge only on append/removal boundaries.**

- **Pros:** less work.
- **Cons:** state depends on transaction history; avoidable fragmentation persists; harder reproducibility comparisons.
- **Dependency:** later diagnostics must normalize counts carefully.

**C — threshold/lossy merge.**

- **Pros:** strongest size control.
- **Cons:** changes order/timing semantics and belongs to M3.
- **Dependency:** prohibited by the closed M2/M3 seam.

## Component 2.3 — cumulative-rank grid

### C2.3-Q1 — bin configuration and partial capacity

**Problem/function/gap.** G3 fixes equal mass width, padding, and partial final capacity, but the owning config level and literal tensor schema remain open.

**A — scenario-level bin width plus per-zone derived logical counts/capacity tensor (recommended).** Store one positive width in M2 scenario/config; derive counts and a padded float64 capacity tensor from 2.1 storage.

- **Pros:** resolution studies are explicit; physical storage remains authoritative; fixed shapes.
- **Cons:** one scenario cannot mix resolutions; padding follows the largest zone.
- **Dependency:** 2.5 scenario schema must carry the width without making it dynamic state.

**B — network-level bin width.**

- **Pros:** grid shape is intrinsic to the structural network.
- **Cons:** resolution sweeps require rebuilding network metadata; mixes numerical resolution with physical structure.
- **Dependency:** weakens clean experiment configuration.

**C — per-zone widths.**

- **Pros:** memory-efficient heterogeneous resolution.
- **Cons:** invalidates common-resolution comparison and complicates operators.
- **Dependency:** would reopen G3.

### C2.3-Q2 — overlap boundary and active signature

**Problem/function/gap.** Exact boundary incidence is nondifferentiable when an entry endpoint lands on a bin edge. A single ownership convention and signature are needed.

**A — downstream-closed/upstream-open half-open rank intervals with sparse incidence signature (recommended).** Use the already agreed head-at-zero half-open intervals; record, per entry, the first/last intersected logical bin and exact-edge flags.

- **Pros:** unique ownership; compact stable-regime signature; scalar-oracle friendly.
- **Cons:** exact-edge perturbations correctly invalidate FD comparisons.
- **Dependency:** 2.6-Q2 incorporates this signature.

**B — store a full boolean entry/bin incidence matrix.**

- **Pros:** direct diagnostics and vectorized comparison.
- **Cons:** memory-heavy; redundant with endpoints; larger artifacts.
- **Dependency:** affects cached state size.

**C — add epsilon to choose sides.**

- **Pros:** fewer apparent ties.
- **Cons:** changes mass allocation with numerical scale and hides event boundaries.
- **Dependency:** conflicts with G6.

### C2.3-Q3 — cached grid ownership

**Problem/function/gap.** G3 selects an atomic cache, but the cache can live inside immutable lane state or only in transaction results. The ledger must remain authoritative.

**A — immutable zone snapshot containing ledgers and validated cached grid (recommended).** Every constructor/transaction rebuilds both atomically; direct independent construction is private.

- **Pros:** consumers cannot observe stale data; grid is available to 2.4/2.5; clear invariant.
- **Cons:** rebuild/graph retention cost; snapshots are larger.
- **Dependency:** 2.5 state embeds the complete snapshot.

**B — cache only in operation results.**

- **Pros:** lighter semantic state.
- **Cons:** consumers can retain mismatched ledger/grid pairs; validation ownership is diffuse.
- **Dependency:** 2.4 would need repeated projection or cache plumbing.

**C — on-demand only.**

- **Pros:** no stale cache.
- **Cons:** contradicts selected G3 and repeats graph construction.
- **Dependency:** requires reopening G3.

## Component 2.4 — internal physics and feedback

### C2.4-Q1 — lane capacity and characteristic delays

**Problem/function/gap.** G1 gives physical primitives but does not fix whether zone flow capacity is copied per lane, divided from aggregate capacity, or authored independently. Delay values must describe the zone length consistently.

**A — derive lane delay from shared speeds and lane length; use an explicit per-lane capacity rate reconciled to the link convention (recommended).** Full-length neutral lanes default to equal shares whose sum matches aggregate input capacity; deviations are structural and must pass a declared reconciliation rule.

- **Pros:** dimensional clarity; supports heterogeneous lengths; prevents accidental capacity multiplication.
- **Cons:** requires an explicit share/reconciliation field; equal sharing is a convention, not geometry alone.
- **Dependency:** if independent lane capacities are desired scientifically, reopen G1/G4.

**B — give every lane the whole link capacity.**

- **Pros:** simple and resembles parallel physical lanes.
- **Cons:** multiplies aggregate capacity relative to accepted M0 and breaks neutral comparison.
- **Dependency:** incompatible with G5 unless the baseline is changed.

**C — infer capacity only from storage and step length.**

- **Pros:** no extra field.
- **Cons:** storage is not flow capacity; timestep-dependent physics.
- **Dependency:** scientifically invalid under the FD contract.

### C2.4-Q2 — commitment-feasible receiving

**Problem/function/gap.** Scalar aggregate receiving cannot summarize lane accessibility independently of the ordered, committed eligible tranche. The implementation must realize G2 without calling a lane solver.

**A — stable committed-entry scan with lane residual capacities (recommended).** Scan the upstream eligible tranche once, split affinely as needed, continue across blocked commitments, and return accepted-by-lane, residual upstream, and selection signature.

- **Pros:** exactly transcribes G2; conservative; linear complexity; no reassignment.
- **Cons:** aggregate accepted mass depends on ordered commitment composition; not reducible to one precomputed scalar.
- **Dependency:** consumes 2.2-Q2 and emits signatures for 2.6.

**B — group eligible mass by lane before limiting.**

- **Pros:** vectorizable totals.
- **Cons:** can lose ordered residual/split timing unless reconstructed; grouping topology is complex.
- **Dependency:** only viable with proof of identical ledger result to A.

**C — sum lane room and accept a global prefix.**

- **Pros:** trivial aggregate interface.
- **Cons:** accepts mass for a full committed lane using unrelated space; violates G2.
- **Dependency:** inadmissible.

### C2.4-Q3 — zone eligibility representation

**Problem/function/gap.** Newly admitted mass needs a geometry-derived node-facing eligibility profile distinct from M1's existing link-arrival meaning, without same-step service.

**A — explicit M2 eligibility profile synchronized with lane entries (recommended).** Derive front/tail node-eligibility times affinely at admission and retain them through exact splits/merges.

- **Pros:** semantics are explicit; supports exact interval queries and gradients; avoids overloading M1 fields.
- **Cons:** extra synchronized tensors/wrapper logic.
- **Dependency:** must be part of 2.2-Q1's wrapper and 2.5 state.

**B — reinterpret M1 eligibility fields inside the zone.**

- **Pros:** no new timing fields.
- **Cons:** one field changes meaning by location; merge equivalence and diagnostics become ambiguous.
- **Dependency:** would reopen M1 semantics.

**C — integer eligible-step index.**

- **Pros:** simple scheduler logic.
- **Cons:** quantizes exact delays and detaches timing gradients.
- **Dependency:** conflicts with G2/G6.

### C2.4-Q4 — numerical storage boundary policy

**Problem/function/gap.** Floating arithmetic may produce tiny residuals around full storage, but repair must not conceal real overfill or alter behavior.

**A — scale-aware assertion tolerance plus zero only for a proven signed roundoff residual (recommended).** Compute unconcealed residual, fail beyond tolerance, and permit a zero-valued numerical guard only within the recorded tolerance/signature.

- **Pros:** robust without hiding errors; preserves physical decision away from the boundary.
- **Cons:** requires centralized tolerance and diagnostic residual.
- **Dependency:** 2.6 reports tolerance and near-boundary status.

**B — strict exact comparison.**

- **Pros:** simplest semantics and catches every discrepancy.
- **Cons:** brittle after long floating-point accumulation; can reject physically valid states for tiny noise.
- **Dependency:** may make integration impractical.

**C — unconditional clipping.**

- **Pros:** operationally robust.
- **Cons:** silently destroys/creates effective room and hides conservation bugs.
- **Dependency:** prohibited by project invariants.

## Component 2.5 — rollout composition

### C2.5-Q1 — scenario/state/result/history schema

**Problem/function/gap.** The independent meso stack must expose enough immutable state and evidence for replay and gradients without making diagnostics behavioral state.

**A — explicit M2 dataclass family parallel to M0/M1 (recommended).** Separate structural scenario/config, dynamic upstream/zone/ledger state, step transactions/signatures, and full rollout histories.

- **Pros:** clear ownership and reproducibility; no accepted API mutation; all component evidence retained.
- **Cons:** more records and conversion glue; memory-heavy reference histories.
- **Dependency:** fields must be frozen before 2.6-Q3.

**B — extend M1 route rollout records with optional meso fields.**

- **Pros:** fewer top-level entry points.
- **Cons:** reopens M1; optional-state combinations proliferate; macro/meso comparison boundary blurs.
- **Dependency:** inadmissible without M1 reopening.

**C — minimal terminal state plus ad-hoc diagnostic callbacks.**

- **Pros:** lower memory.
- **Cons:** poor auditability and replay; callbacks risk behavioral coupling.
- **Dependency:** fails G5/G6 evidence needs.

### C2.5-Q2 — refined/unrefined link orchestration

**Problem/function/gap.** Only selected inbound links use U/Z decomposition; all other links must retain the accepted path with one owner for every boundary.

**A — immutable refined-link ownership map with explicit dispatch (recommended).** Precompute per-link mode and boundary owner; use unchanged M1 operations for unrefined links and M2 operators only for refined links.

- **Pros:** auditable single ownership; mixed networks supported; no hidden adapter.
- **Cons:** orchestration branches structurally; coupling tests required.
- **Dependency:** 2.1-Q1 supplies canonical refined IDs.

**B — wrap every link, using a zero-zone special case for unrefined links.**

- **Pros:** uniform loop.
- **Cons:** changes the unrefined execution path and weakens exact regression/equivalence evidence.
- **Dependency:** conflicts with the unchanged-path contract.

**C — run macro and meso copies then reconcile.**

- **Pros:** easy side-by-side diagnostics.
- **Cons:** double physical ownership and ambiguous authoritative mass.
- **Dependency:** prohibited.

### C2.5-Q3 — conservation validator context

**Problem/function/gap.** Local totals alone cannot detect route mass placed in the wrong location. Validation needs route-aware generation, source, U, Z/lane, downstream, and completion partitions without entering the differentiable behavior path.

**A — immutable boundary-accounting snapshot assembled from authoritative states (recommended).** Record per-route/per-link/per-lane location totals and cumulative transitions; validate global and local identities after every step in reference mode.

- **Pros:** localizes leakage/misrouting; no second state authority; supports artifacts.
- **Cons:** aggregation cost and larger histories.
- **Dependency:** consumes 2.2 identities and 2.5-Q1 histories.

**B — aggregate network mass only.**

- **Pros:** cheap.
- **Cons:** cannot detect route swaps, wrong lanes, or double ownership with offsetting errors.
- **Dependency:** insufficient for M2 acceptance.

**C — maintain independent cumulative accounting state.**

- **Pros:** fast incremental checks.
- **Cons:** creates another mutable authority that can drift.
- **Dependency:** violates the evidence-only role unless derived and cross-checked.

## Component 2.6 — reference and evidence harness

### C2.6-Q1 — independent scalar oracle floor

**Problem/function/gap.** End-to-end self-comparison cannot establish correctness. The minimum independent oracle set must cover new geometry, overlap, and boundary logic without building a second simulator.

**A — small standard-library scalar functions for each primitive plus hand cases (recommended).** Independently calculate physical partition/storage, ledger-bin overlaps, committed admission, eligibility, and one-step conservation; compose only tiny cases.

- **Pros:** catches shared tensor implementation errors; auditable; low dependency cost.
- **Cons:** some duplicated equations; limited scale/performance relevance.
- **Dependency:** oracle formulas freeze only after owning component decisions close.

**B — hand-calculated constants only.**

- **Pros:** minimal code and maximally independent.
- **Cons:** sparse coverage; awkward parameter sweeps and edge cases.
- **Dependency:** useful supplement but insufficient alone.

**C — compare only with production functions in float64.**

- **Pros:** cheap.
- **Cons:** not independent and cannot detect shared mistakes.
- **Dependency:** fails the mathematical-reference gate.

### C2.6-Q2 — derivative scan and active signature

**Problem/function/gap.** Existing M1 tolerances are a useful baseline, but M2 adds overlap, commitment, storage, and eligibility event surfaces. Evidence must distinguish numerical disagreement from regime changes.

**A — reuse M1 scan/tolerances initially and extend a compositional signature (recommended).** Combine node constraints with ledger split/selection, bin incidence, full-lane/storage, eligibility, and refined-link dispatch signatures; accept FD rows only when plus/minus/baseline signatures match.

- **Pros:** comparable to accepted evidence; correctly excludes event crossings; diagnoses which topology changed.
- **Cons:** signature schema is larger; stable rows may be scarce near boundaries.
- **Dependency:** every earlier operation must emit structural evidence.

**B — objective-value FD agreement without signatures.**

- **Pros:** simple output.
- **Cons:** can mislabel event-crossing disagreement as AD failure or accidentally accept cancellation.
- **Dependency:** violates G6.

**C — smooth events for checking.**

- **Pros:** easier numerical derivatives.
- **Cons:** validates a different model.
- **Dependency:** prohibited by G6.

### C2.6-Q3 — artifact and provenance contract

**Problem/function/gap.** Closure evidence must be reproducible and non-overwriting, but the exact artifact floor and naming owner remain open.

**A — one versioned run manifest plus machine tables and concise Markdown summary (recommended).** Include resolved config, hash, git state, Python/PyTorch/platform/device/dtype, seeds, exact commands, tolerances, signatures, assertion outcomes, artifact paths, and non-overwrite run ID.

- **Pros:** complete and inspectable; supports deterministic reruns; keeps human and machine evidence aligned.
- **Cons:** schema/runner work; strict versioning required when fields evolve.
- **Dependency:** consumes final 2.5 record schema and G5/G6 evidence.

**B — reuse M1 artifact schema unchanged.**

- **Pros:** minimal work and familiar layout.
- **Cons:** cannot represent lane/grid/storage/signature evidence without opaque extensions.
- **Dependency:** viable only as a base schema, not unchanged.

**C — logs and pytest output only.**

- **Pros:** simplest.
- **Cons:** not durable or sufficiently machine-readable; incomplete provenance.
- **Dependency:** fails the milestone evidence contract.

## Closure sequence and cross-component checkpoints

1. Close 2.1-Q1 to Q3.
2. Close 2.2-Q1 to Q3, checking that 2.4-Q3 timing and 2.6-Q2 signatures fit the wrapper.
3. Close 2.3-Q1 to Q3, checking 2.4 consumption and 2.6 signature needs.
4. Close 2.4-Q1 to Q4 against accepted 2.1–2.3 interfaces.
5. Close 2.5-Q1 to Q3, preserving unchanged unrefined-link execution.
6. Close 2.6-Q1 to Q3 and audit that all required evidence fields already exist upstream.
7. Run the final global/component consistency audit before Phase C.

This sequence is serial for closure, but the complete inventory is visible now so early interfaces can reserve later-required outputs without importing later behavior.
