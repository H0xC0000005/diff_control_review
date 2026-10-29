# T7 project-impact audit

Date: 2026-09-14
Status: Impact classification accepted on 2026-09-14, with revised P8 delegating service-order resolution to M3. Review closure is recorded separately.

## Finding

The approved V0–V4 task can be supported by the current architecture without discarding Milestone 1 or broadening Milestone 2 into bay/access behavior. It requires explicit handoffs to Milestones 3–6. This is a document/contract compatibility audit, not evidence that the unimplemented operators or experiments already work.

Sources inspected: `PROJECT_CONTEXT.md` (architecture, differentiation, validation); `PLANS.md` (Milestones 1–6); `temp_content/milestone_2_per_lane_interaction_zone/phase_B_revision.md` (closed G1–G6); `phase_B_component_question_register.md` (component owners and interfaces); and the approved T6 formulation, primary suite, baseline realization and adoption matrices. Project-wide status text still describes the last consolidated milestone state; the active M2 Phase-B archive establishes the current component-discussion status.

## Classification and handoff

| ID | Accepted task requirement | Existing basis / implication | Classification and owner | Required timing |
|---|---|---|---|---|
| P1 | Continuous mass, fixed routes/order metadata, aggregate propagation | Context §§5–7 and M1 architecture already supply the scientific basis; no evidence here warrants discarding M1 | Compatible/no change | Preserve throughout |
| P2 | Four-leg symmetry and four service groups | A scenario construction, not a demand to hard-code four legs or groups in reusable model APIs | Component-local question revision: C2.1-Q3 and C2.5-Q1 should preserve explicit permission/scenario maps and rotational testability | Before M2 Phase C; exact scenario values later |
| P3 | V0 neutrality before order/storage claims | G4 is movement-exclusive; G5 distinguishes split-domain equivalence from subdivision error | Clarification in active phase archive: V0 needs a physically matched comparator; do not confuse an unsplit M0 difference with selective-order benefit | Before M2 Phase C and V0 acceptance |
| P4 | V1–V3 shared lanes, bays and access | G4 deliberately excludes these behaviors from M2; G2 allows replacement of passive access later | Compatible M2 boundary; later M3 plan must define lane intent, realized access, bay storage, ordered service and their update order | M3 Phases A–C |
| P5 | Continuous control-to-objective path | G6 includes ledger masses/timing, projection, grid, storage, service and outputs; structural labels remain fixed | Clarification in active phase archive; C2.2-Q1, C2.3-Q2/Q3, C2.4-Q3, C2.6-Q2 must preserve the connected path and signatures | Before M2 Phase C |
| P6 | TST counts all physical mass once, including source waiting | U/Z series partition and C2.5-Q1/Q3 provide ownership/accounting seams; cached grid and ledger are views of the same traffic | Component-local question revision: expose disjoint source/U/Z/downstream/completion accounting; never sum duplicate ledger and grid masses | Before M2 Phase C; task objective/clearance runner frozen later |
| P7 | B0–B3 causal ladder plus independent R1 | Roadmap M4 mainly names macro–meso comparison; T6 adds structured queues and lane/storage aggregate controls | Later roadmap amendment: explicitly assign B1/B2 implementations, faithful reference checks and capability limits; C2.5-Q2 preserves dispatch seams | Architecture seams before M2 C; baseline equations before M3/M4 implementation |
| P8 | Selectively retained order at the approved model resolution | M3 owns exact FIFO versus intra-bin homogeneity, service policy and defragmentation | M3-owned modeling decision with subsequent task-definition synchronization; specify preserved/relaxed information and reference, resolution-sensitivity, conservation and gradient evidence; exact FIFO is not preselected as production behavior | M3 A–C, before choosing service policy |
| P9 | External perturbation evidence precedes full optimization | T6 evidence sequence requests richer-evaluator perturbations first; PLANS places M6 after M5 | Later roadmap amendment: reserve a bounded external-perturbation readiness/check stage before full M5 optimization, leaving final held-out action transfer in M6; no silent milestone resequencing | Before M4/M5 experiment plans freeze |
| P10 | One service-to-SUMO intervention mapping | Maintained SUMO software supplies execution, not a guaranteed equivalent continuum intervention under spillback | Later experiment decision: freeze common cycle/lost-time/service mapping, population accounting, calibration and paired seeds; report mismatch | Before external perturbation evidence is admissible |
| P11 | Stable-signature derivative validity | G6 and C2.6-Q2 already require AD/JVP/FD and signatures | Compatible/no change; retain event cases in forward reporting and keep numerical checking distinct from external usefulness | Component and integration validation |
| P12 | V4 held-out banks and fair budgets | M5 already includes fixed banks and held-out evaluation | Later experiment-plan clarification: keep order pairs together; freeze numerical settings before held-out evaluation; separate representation and optimizer comparisons | Before confirmatory experiments |
| P13 | V5 excluded | Former V5 was renamed conditional I1 in T6 drafts | Scope exclusion: neither V5 nor I1 is a review deliverable, acceptance requirement or authorized experiment | Effective immediately |
| P14 | Part II future tasks unapproved | T5 closure returned the map for further work | Deferred separate work; do not imply full Part-II approval when closing this Part-I review | Separate user instruction |

## Two decisions that must not be hidden in implementation

P8 was revised following user discussion. M3 owns service-order resolution, intra-bin homogenization and defragmentation. The task tests the usefulness of selectively retained order at the approved resolution; it does not preselect exact within-bin FIFO as production behavior. M3 must define preserved and relaxed information and appropriate reference, resolution-sensitivity, conservation and gradient checks. Exact FIFO remains a possible reference or candidate. Synchronize the detailed task/operator wording after the M3 decision. Earlier T6 descriptions of exact-order B3 are qualified by this accepted ownership decision. M2 retains its existing exact ledger and policy-neutral seam until M3 authorizes a service policy; this review does not activate lossy operations in M2. V0–V4 retain their causal purposes.

P9 is a scheduling mismatch between the approved evidence order and the provisional roadmap. The smallest proposed resolution is a bounded external perturbation check before full optimization, rather than moving the entire final transfer campaign. This audit proposes that classification and timing; it does not amend the roadmap. If external mapping cannot be established, external-usefulness claims remain blocked even if internal derivatives pass.

## What is not established

Exact ordered-access equations/Jacobians, the chosen B1 equation set, B2 storage augmentation, calibrated demand regimes, and the continuum-to-SUMO mapping still require their designated future plans and evidence. No new literature search or simulator run was necessary for this document audit. Citation/adoption claims rely on the already reviewed and archived T6 evidence.
