# AS1: where initial symmetry was used, and what replaces it

Date: 2026-10-19. **Initialization and complete-forward dependency audit
delivered at AS1's checkpoint.** This is original reasoning on the accepted
review model. No new paper was viewed or new physical mechanism selected.

The amended true state has independent initial E, A and B loads. Its
combined E/A load is derived from E and A, and total mass is derived from
all three lanes. Longitudinal homogeneity is unchanged. The mathematical
amendment is self-contained for its initialization/domain and states the
reused node/recovery laws and forward proof explicitly.

[Current exact contract and derivation, PDF](../../synthesis/research_readiness/vsl_as1_asymmetric_forward_contract.pdf)

[Plain findings and checkpoint](../../reporting/research_readiness/vsl_as1_asymmetry_findings_and_checkpoint.md)

## Dependency results

The source locations below identify logical dependencies; a text search for
“symmetry” alone is not the proof. Each carryover was checked against the
actual assumptions used by the equation or argument.

| Component or result | Existing source and actual dependency | AS1 conclusion |
|---|---|---|
| **Initialization** | Feedback-8 core, §2, `eq:initial`: explicitly sets A=B and writes total density as E+2A. | Replace by three independent initial densities and their sum. Retain common footprint, neutral terminal/account and finite cohort. This is the sole removed physical restriction. |
| **Admission** | Feedback-8 core, §2, `eq:domain`–`eq:workdomain`: separate E+A load, far-B load, total storage and root bounds. | Same inequalities with actual independent loads and total mass; no bound is weakened to manufacture an example. |
| **H1 free invariance and solution** | Core, §3, `eq:h1general`–`eq:h1receiving`: paired transfer conserves E+A; E+A fits critical density for every advice. | Carries. B is absent from this local interaction. Explicit branches and progress law do not use A=B. |
| **Handoff and conservation** | Core, §4, `eq:entry`–`eq:upstreammass`: common footprint clock, lane densities and paired lateral cancellation. | Entries carry unchanged. Total-density bookkeeping must use E+A+B. Individual balances already distinguish A and B. |
| **Terminal receiving and far service** | Core, §5, `eq:terminalcounts`–`eq:pulse`: entry rates below capacity, total mass below terminal storage, separate B receiving bound. | Carries with corrected mass. The monotone A/E pulse depends on E+A, not continuing symmetry. |
| **Work roots and allocation** | Core, §§6–7, `eq:root`–`eq:queuedynamics`: fixed coefficient, bounded current flows/marks, positive root derivative and current-mode guards. | Carries. No initial lane equality enters the root, service template or free/queued feasibility tests. |
| **Recovery and local coupling** | Core, §8, `eq:profile`–`eq:renewalupdate`; forward, §9, `eq:cutoffdiff`–`eq:contraction`: bounded E flow, mark Lipschitz estimate and retained-rank mass comparison. | Carries. The same E-only recent-mass account and local contraction are retained; no stateless reset or strongest-cap rule is substituted. |
| **Budget and rate bounds** | Forward, §9, `eq:budgetfloor`–`eq:budgetrate`: finite maximal E admission rate, positive recovery acceleration, youngest-age rearrangement. | Carries with common positive budget bound across the fixed-parameter family. This bound is derived, not added as a service floor. |
| **E and A event control** | Forward, §10, `eq:frontwork`–`eq:eventseparation`: ordinary E+A underload; decreasing E/increasing A pulse; neutral free E marks; selected guards; budget and offer rate bounds. | Carries. E's one-episode result remains conditional on these assumptions. A events have the same derived positive separation; no imposed dwell time is needed. |
| **Complete clearance and TST** | Forward, §§10–11, forward theorem, `eq:mass`–`eq:tstqueue`: complete eligibility by the rear; positive service while queued; total conservation; uniform initial positions. | Carries with actual three-lane total mass. B has zero eligible waiting under its retained service bound. The local completion boundary is unchanged. |
| **Ending-only reconstruction** | Forward, §12, `eq:scalar`: explicitly infers equal A and B from known E and total mass. | Does **not** carry. E and total now determine continuing total only. Whether permitted history identifies the split is AS2, not decided by this failure of the old formula. |
| **Symmetric witnesses** | Feedback-8 support, especially the A-delay/active-renewal family; standalone Step 3 matched-history/action constructions. | Valid historical special cases remain intact. They cannot be relabeled as fixed-E/fixed-(A+B) asymmetric certificates. AS1's new witness establishes admissibility and local receiving contrast only. |

## Sources actually reused

[Feedback-8 core equations](../../synthesis/research_readiness/vsl_feedback8_math_core.tex)

[Feedback-8 forward, event and TST arguments](../../synthesis/research_readiness/vsl_feedback8_math_forward.tex)

[Consolidated mathematics, PDF](../../synthesis/research_readiness/vsl_feedback8_full_mathematics.pdf)

[W-F whole-advice-range qualification](../../synthesis/research_readiness/vsl_wf_forward_qualification.tex)

[O-R local history and recovery qualification](../../synthesis/research_readiness/vsl_or_recovery_qualification.tex)

[Earlier finite-terminal/handoff derivation](../../synthesis/research_readiness/vsl_h1_t1_joined_contract.tex)

[Historical symmetric witness derivations](../../synthesis/research_readiness/vsl_feedback8_math_support.tex)

[Historical Step 3 information/action/sensitivity derivations](../../synthesis/research_readiness/vsl_step3_standalone_information_and_gradient.tex)

[Accepted literature and equation lineage](vsl_feedback8_model_stack_source_map.md)

[W-F source/adaptation audit](vsl_wf_forward_source_audit.md)

[Recent Step 3 viewed-reference list and reading limits](vsl_step3_standalone_sources_and_derivations.md)

The accepted traffic sources support their ingredients only to the extent
recorded in those source maps. AS1 does not claim a published paper supplies
this full model, its asymmetric extension or the illustrative coefficients.
No external-source claim is added by changing initialization.

## Evidence scope and checkpoint

The new exact algebra checks cover the three-lane mass identity, paired
transfer, progress branches, monotone offer bound, uniform-position travel
term, split parametrization and rational domain/receiving example. They do
not machine-prove the whole causal theorem, validate physical coefficients,
match predecision observations or evaluate a policy.

The conditional proof extension is complete at review scope. G3/VQ3-P's
exact amended initial family is presented for user acceptance; downstream
G2/MP3 and S3-Q1 remain AS2, and action/full-gradient consistency remains
AS3. AS2 cannot silently change the physical family to hide a revealing
observation; a necessary observation or mechanism change triggers its gate.
