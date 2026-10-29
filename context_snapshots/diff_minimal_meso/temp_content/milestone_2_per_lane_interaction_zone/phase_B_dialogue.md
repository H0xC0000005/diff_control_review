# Milestone 2 Phase B dialogue

Status: **Phase B opened; Phase A proposal reworked; global contracts pending**  
Date: 2026-09-03

## Feedback intake

The latest Milestone 2 Phase B feedback states that the project-wide roadmap failed to preserve a previously agreed interaction-zone architecture. The user supplied:

`temp_content/feedback/sup_files/milestone_2/milestone_2_equal_binned_interaction_zone_context.md`

and requested that its agreed modeling approach be considered and merged into a reworked Phase A proposal.

The entire supplementary file was read. No other Milestone 2 supplementary file was linked from the feedback entry.

## Interpretation of authority

Statements explicitly labeled **Agreed modeling fact** are treated as inherited methodological decisions for this Phase B discussion, subject only to conflict checking against `AGENTS.md` and fixed `PROJECT_CONTEXT.md` invariants. No conflict was found.

Statements labeled **Engineering implication** are treated as strong consequences to transcribe into architecture and validation, while their exact implementation remains open where the file says so. Statements labeled **Still parameterized/open** remain Phase B questions.

The following are therefore no longer presented as candidates:

- downstream zone in series with an upstream aggregate LTM region;
- single ownership and additive partition of physical-link mass;
- per-lane equal-width cumulative-mass/FIFO-rank bins;
- rank zero at the downstream head/stop-line side;
- continuous mixed movement composition in `W[lane,bin,movement]`;
- partial structural final bins without traffic-mass rounding;
- synchronized grid and exact route-mass ledger, with ledger semantic/update authority;
- continuous prefix removal, rank shift, ordered tail append, and conservative rebinning;
- geometry/jam-density storage independent of mass-bin resolution;
- no-clipping spillback into the upstream LTM region;
- one exogenous structural lane commitment per route transition before behavioral allocation;
- no reactive reassignment, overtaking, or within-zone lane changing;
- fixed-structure piecewise differentiation without smoothing;
- exact FIFO service capability retained but behavior deferred to Milestone 3.

## Rework performed

`phase_A_proposal.md` was revised to:

1. cite the supplementary context as the recovered methodological input;
2. convert series decomposition, equal-bin semantics, ledger authority, and structural commitment from recommendations into inherited contracts;
3. remove overlay, appended-buffer, grid-only, dual-authority, and behavioral lane-choice alternatives from the ordinary decision inventory;
4. retain six responsibility-based components because they remain compatible with the recovered architecture;
5. replace the former G1–G3 questions with narrower decisions on physical parameterization, internal-boundary dynamics/indexing, and tensor realization/caching; and
6. update dependencies, mixed-question splits, Phase B closure order, and reopen conditions.

## Remaining milestone-global questions

- **G1:** physical primitives and storage/travel-delay partition;
- **G2:** internal-boundary propagation equations and interval indexing;
- **G3:** `Delta xi`, partial-bin/padding layout, and cached versus on-demand `W`;
- **G4:** neutral aggregate-authoritative node quota construction and replay;
- **G5:** matched split-domain reference and split-versus-unsplit evidence;
- **G6:** exact differentiated maps, active signatures, and gradient evidence.

No global decision is silently closed by this rework. The proposal’s recommendations remain provisional until user discussion/approval.

## Current gate and next discussion

Phase B is open. The next discussion should first confirm that the recovered agreed-contract list and revised question ownership are accurate, then close G1 and G2 before discussing grid-layout or component-local details. No Phase C plan or production implementation is authorized.

## Candidate-presentation revision

The user requested that every candidate in the problem list include explicit pros and cons, and that methodological candidates be explained in enough detail to support an informed scientific choice. The user also promoted this to a project-wide question-presentation rule.

Actions taken:

- updated `AGENTS.md` so every open-question candidate must state its resulting methodological/model-chain behavior, explicit **Pros**, explicit **Cons**, and relevant dependencies or scientific consequences;
- added a rule against compressing materially distinct candidates into a sentence or presenting a rejected option only as a weak strawman; and
- expanded every G1–G6 candidate in the Phase A proposal using that format without changing the candidate set, recommendations, or decision status.

The Section 8 component-local table remains an ownership inventory rather than the component discussion itself. Under the new repository-wide rule, each local question must receive the same expanded candidate format when it is discussed serially after the global backbone closes.

## Core-gap revision

The user observed from G1 that its Core gap described an implementation symptom—the absence of primitive geometry fields—without first identifying the decision that creates the gap. The same audit was applied to G1–G6.

Each Core gap now states, in order:

1. the core scientific, physical, comparison, or differentiability question the item must answer;
2. why the currently agreed context does not answer it;
3. how the visible implementation gap follows from that missing contract; and
4. the scientific or engineering failure modes if it remains unresolved.

The candidate sets and provisional recommendations were not changed.

## Chitchat-question response

The latest feedback added explanatory questions for G1–G6 and a proposed intra-bin defragmentation rule. The detailed response is archived in `phase_B_chitchat_answers.md`; each feedback question was marked `(answered)` without otherwise editing the user text.

Key conclusions:

- reusing the LTM means retaining its equations for `U_a`, not retaining the original whole-link parameters and appending `Z_a`;
- equal mass bins are CTM-like as a fixed array/shift representation but are not spatial CTM cells and do not carry cell-level demand/supply;
- G2 covers internal physical timing/feedback as well as lane placement; first-available/load-balancing would contradict the agreed structural commitment;
- exact partial final-bin capacity is low-cost and should not be rounded, because bin resolution must not change physical storage;
- movement-exclusive full-length lanes are suitable neutral M2 fixtures, but bay overflow, equal lane distribution, and unused-quota transfer are additional allocation/service rules rather than automatic no-blockage consequences;
- G5 Candidate A is selected under delegated authority, conditional on the final G1/G2 contract, with all reference-only flow kept outside production;
- continuous ledger mass/timing and projected `W` values are on the gradient path; categorical route/movement/order metadata is not; and
- the initially described lossy intra-bin operation was interpreted as arbitrary reordering and was not approved for M2. A later clarification corrected that interpretation, as recorded below.

## Correction after partial-FIFO clarification

The user clarified that the proposed operation is not pre-service compression. It is a bin-scale partial-FIFO service model: movement-specific mass may be discharged from a homogeneous mixed bin without exact within-bin blocking, after which the ledger is reconciled to the realized discharge and canonically consolidated within the order resolution the model has intentionally relaxed.

The corrected audit finds this methodologically coherent and directly relevant to the project’s selective-discreteness question. It distinguishes two variants that still require a future decision: proportional partial-bin discharge and independently movement-quota-limited partial-bin discharge. The user’s numerical example uses the latter.

Under the current milestone boundary, M2 should construct the exact ledger/grid representation and leave an interface capable of atomic bin-discharge/ledger-reconciliation updates, but should not activate this lossy service rule in its neutral behavior. Exact FIFO versus bin-scale partial FIFO, including canonical order, route selection, representative timing, bounded error, fragmentation, and convergence contracts, belongs to the Milestone 3 behavioral decision unless the user explicitly reopens M2 scope.

## M2/M3 policy-mechanism boundary

In follow-up discussion, the partial-FIFO behavior was cleanly separated from M2 using a resolved-removal-plan seam. M2 owns exact representation, plan validation/application, ledger splitting/reconstruction, grid rebuilding, conservation, and telemetry. It does not decide which mass is behaviorally service-eligible. M2 exercises only movement-exclusive prefix plans where exact FIFO and bin-relaxed service coincide.

M3 owns exact-FIFO and bin-scale partial-FIFO plan generators. Only an approved M3 relaxed policy may select interior mixed-bin movement mass or authorize lossy within-bin canonicalization/timing consolidation. This preserves a usable M2 interface without importing M3 behavior.

The user accepted this reasoning and instructed that the question be recorded in Milestone 3 scope. `PLANS.md` now explicitly assigns to M3 the exact-FIFO versus equal-mass-bin partial-FIFO comparison, movement-discharge variant, ledger reconciliation/canonicalization, rank-error bound, fragmentation/convergence evidence, and forward/gradient-bias validation. M2 retains only the exact policy-neutral application seam and fragmentation telemetry.

## Candidate synchronization after chitchat

The user granted authority and established a default that candidate lists must be updated from later discussion unless explicitly waived. `AGENTS.md` now records that living-inventory rule while preserving approval/reopen status.

The Phase A proposal candidates were synchronized as follows:

- G1-A now explicitly defines `U_a` as the accepted LTM equations with upstream-subdomain parameters and `Z_a` as a delay-aware rank reservoir, not CTM spatial cells;
- G2-A separates homogeneous propagation, fixed structural commitment, and physical admission/timing, and excludes first-available/load-balanced lane assignment;
- G3 adds Candidate D for rounding storage to a bin multiple and records why it changes physical capacity; G3-A now shows the low-cost partial-bin capacity vector;
- G4-A now uses movement-exclusive full-length lanes for its neutral acceptance domain, capped/proportional cross-lane quota bookkeeping, and strictly limited short-pocket tests; dynamic pocket overflow and intermediate merge bays remain outside M2;
- G5 retains selected Candidate A and its validation-only comparator boundary; and
- G6-A now spells out the live continuous ledger-to-`W` gradient path and structural signature.

No open G1/G2/G3/G4/G6 candidate was converted into an approved decision by this synchronization. G5 remains selected conditionally under the earlier delegation.

## G1 grid-derived-length follow-up

The user proposed deriving zone length from maximum lane bin capacity times configurable occupied space per vehicle-equivalent, with the residual link assigned to `U_a` and a zero-length identity LTM when the zone covers the link.

This is recorded as new G1 Candidate D rather than folded into Candidate A. The audit established the dimensionally complete relation `L_Z = B_max * Delta xi * s_jam`, required `s_jam=1/k_j` under the approved vehicle-equivalent density convention, and distinguished physical design from resolution changes. Candidate A continues to author geometry and derive bin layout; Candidate D authors grid capacity and derives geometry.

For `L_Z=L_a`, the proposal now specifies omission/bypass of `U_a`, not construction of a zero-length accepted LTM record. `L_Z>L_a` is rejected because setting only `L_U` to zero would still overstate physical zone length/storage.

## Formula-readable G1 artifact

At the user's request, the G1 grid-derived-length answer was re-rendered as LaTeX/PDF for human readability. The server toolchain was verified as `latexmk` 4.83 with pdfTeX 3.141592653-2.6-1.40.25 (TeX Live 2023/Debian). Source and output are stored under `phase_B_artifacts/` as `g1_grid_derived_zone_length_answer.tex` and `.pdf`.

The user also established a project-wide default: answers containing multiple/complex formulas or substantial super/subscript notation should place the main mathematical explanation in a LaTeX-generated PDF and keep chat to a short conclusion/link. This rule is now recorded in `AGENTS.md`.

## G2 Candidate A pseudocode clarification

The user asked whether Candidate A scans available lanes in deterministic order and fills whichever has capacity. It does not. The proposal now includes pseudocode showing a stable scan over the upstream FIFO-eligible traffic tranche. Each entry uses exactly its structural `psi` lane; no alternative lane is searched and no load balancing occurs.

The question also exposed a previously implicit behavioral boundary. Candidate A now explicitly continues the scan after an entry is partly or fully blocked from its committed lane, allowing later entries committed to other lanes to use their own receiving capacity while preserving per-lane and residual subsequence order. This is the neutral M2 analogue of Milestone 1's passive accessible extraction. A strict global stop would create cross-lane head-of-line blockage and is deferred to M3. This clarification changes no lane commitment but makes the passive accessibility assumption explicit for user decision.

## G2 Candidates B/C algorithm expansion

At the user's request, G2 Candidates B and C now include numbered interval processes and pseudocode comparable to Candidate A.

- Candidate B explicitly owns per-lane cumulative LTM histories, computes lane receiving and sending through short-link LTM equations, replays node quotas only within lane sending tranches, updates per-lane counts, and requires equality among count occupancy, ledger mass, and grid mass.
- Candidate C explicitly uses only instantaneous lane storage plus entry/discharge capacity, makes all pre-update resident mass node-available without a geometry-derived zone delay, and relies on the scheduler's pre-update rule for only a one-step numerical delay.

The expansion does not resolve G2. It makes clear that Candidate B adds a full per-lane kinematic state authority that must be synchronized with ledger/grid state, whereas Candidate C omits physical within-zone propagation rather than merely simplifying its implementation.

## G4 neutral-domain clarification

The user asked whether G4 Candidate A actually constrains scenarios so that blockage beyond exclusive-lane behavior cannot physically arise, rather than merely describing a procedural quota replay. The candidate now explicitly defines its principal neutral acceptance domain: full-length node-reaching lanes, exactly one movement per lane, no lane start/end inside the zone, no lateral behavior or reactive allocation, demand only from resident eligible mass, and nonrestrictive same-movement quota replay.

This makes shared-lane head-of-line, pocket-access, intermediate-merge, and cross-movement blockage unrepresentable in the principal M2 service cases. It does not remove finite-storage, entry/discharge-capacity, signal-service, downstream-supply, or upstream-spillback constraints, which are required M2 physics. Short pockets may appear only in separate storage/ingress fixtures and cannot support a behavioral overflow claim.

## First global-decision-draft consistency audit

The user supplied a first decision draft selecting Candidate A for G1, G2, G3, G4, and G6, with G5 delegated. The selections form an almost consistent backbone, but two explanatory clauses prevent literal acceptance as written.

1. **G1 contains a source-of-truth contradiction.** The proposal's G1-A makes physical geometry and compatible FD primitives authoritative: author `L_Z` and jam density/spacing, derive exact lane storage, and then derive the full/partial equal-mass-bin layout. G1-D instead makes configured maximum grid capacity (`B_max * Delta xi`) authoritative for deriving physical zone length. The draft selects A while describing A as grid-authoritative. That description must be corrected to geometry-authoritative to retain A; choosing grid-authoritative geometry would instead select D and would conflict with G3-A's resolution-invariance rule unless additional quantities were recomputed to hold physical geometry fixed.
2. **G2 overstates what M3 substitutes.** G2-A's passive accessible extraction/no-cross-lane-blockage policy is deliberately replaceable by M3 behavior. Its upstream LTM propagation, fixed-commitment lookup seam, conservative U/Z transaction, delay eligibility, and spillback feedback are M2 infrastructure and should remain. A later node solver consumes/replaces the neutral G4 service policy; it does not replace the whole G2 physical-boundary contract.

With those corrections, the choices are mutually compatible:

- G1-A supplies geometry-derived storage/delay inputs to G2-A and geometry-derived capacity masks to G3-A;
- G3-A's partial final bin preserves G1-A physical storage while allowing `Delta xi` sensitivity without changing the road;
- G4-A's full-length movement-exclusive neutral domain excludes the M3 blockage mechanisms while retaining ordinary finite storage, capacity, signal, downstream-supply, and spillback constraints;
- delegated G5-A can close once the corrected G1/G2 equations and indexing are frozen, because its matched split-domain comparator must mirror them; and
- G6-A is compatible with the exact ledger-to-grid projection and fixed-structure piecewise differentiation boundary.

No new candidate was exposed by this audit, so the Phase A candidate inventory does not require revision. The global backbone remains pending only the two wording/contract corrections above; it is not yet consolidated into `phase_B_revision.md`.

## Global-backbone closure and Component 2.1 opening

The user accepted both audit corrections and authorized closure of the global questions. G1--G6 are consolidated in `phase_B_revision.md`; the Phase A proposal status now records that the global backbone is closed while component-local questions remain pending.

Phase B proceeds component-serial. `phase_B_component_2_1_questions.md` opens C2.1-Q1 through Q3 with full problem/function/gap/candidate/pros/cons/dependency treatment. No implementation or Phase C freeze is authorized by this closure.

## Complete component-question register and dependency audit

The user requested visibility of every component-local question before serial closure and raised concern about cross-component dependencies. `phase_B_component_question_register.md` now expands all 19 questions across Components 2.1--2.6, links each to its decision parents and forward consumers, and gives viable candidates with pros, cons, consequences, and recommendations.

The audit distinguishes decision dependency, forward interface constraint, and implementation dependency. The main forward constraints are: 2.4 requires 2.2 to preserve explicit zone timing and structural selection evidence; 2.4/2.6 require 2.3 to expose bin-incidence and storage-boundary signatures; 2.6 requires evidence fields from all earlier operations; and 2.5 must preserve unchanged execution for unrefined links. These constraints are considered while closing earlier interfaces, but cannot be used to silently change the already closed global scientific contracts.

At the user's request, the complete C2.1 problem/function/gap and candidate material was then copied into the master register. The register is now self-contained; the dedicated C2.1 file remains the working copy for the currently active component discussion.
