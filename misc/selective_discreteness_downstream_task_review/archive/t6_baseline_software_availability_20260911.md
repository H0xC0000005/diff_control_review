# T6 baseline software and method-availability verification

Access date: 2026-09-11  
Purpose: prevent repeated querying and support `../synthesis/literature_adoption_matrix.md`

## Verified public engineering sources

### T0001 / UNsim

- Repository: https://github.com/toruseo/UNsim
- Status observed: public; MIT license; Python/JAX; `pip install unsim` documented.
- Relevant advertised content: LTM, incremental node model, dynamic route choice, JAX autodifferentiation, tutorials/examples.
- Repository qualification: README explicitly labels the project early development and warns that code/API, especially AD, may change.
- T6 use: independent B0 engineering/reference source, not a drop-in replacement for the accepted PyTorch/project semantics.

### T0003 / differentiable hybrid traffic simulation

- Repository: https://github.com/SonSang/diff-hybrid-traffic-sim
- Status observed: public; MIT license; PyTorch; paper experiment scripts include macro/micro/hybrid intersection signal-control examples.
- Relevant content: differentiable simulation organization, signal-control experiment scripts, gradient-versus-gradient-free patterns.
- T6 use: B3 engineering-pattern and experimental reference only; its microscopic state and macro/micro conversion are scientifically different.

### T0032 / Eclipse SUMO

- Repository: https://github.com/eclipse-sumo/sumo
- Official documentation: https://eclipse.dev/sumo/docs/Simulation/Traffic_Lights.html
- TraCI traffic-light API: https://sumo.sourceforge.net/docs/TraCI/Change_Traffic_Lights_State.html
- Status observed: maintained public source; EPL-2.0 with declared secondary-license conditions; downloadable/installable packages and source documented.
- Relevant content: explicit lanes/routes, signal programs, phase state/duration, `setPhase`, `setPhaseDuration`, and `setProgramLogic`; TraCI and compatible libsumo interface.
- T6 use: direct R2 external-evaluator software reuse. The effective-service-to-program mapping remains a project scientific contract.

### T0025 / sumoITScontrol

- Repository: https://github.com/DerKevinRiehl/sumoITScontrol/
- Status observed: public; GPL-3.0; Python framework for standardized SUMO traffic-controller evaluation.
- Relevant content: intersection/group configuration, lane or detector state measurement, controller benchmarking patterns.
- T6 use: evaluation/controller-wrapper pattern only unless a later license and semantic review approves direct dependency. Its controller tasks do not replace Candidate A.

## Verified open methodological sources without a drop-in implementation claim

### T0014 / partial-FIFO node model

- Public specification: https://arxiv.org/abs/1601.01054
- T6 use: equation-level partial-FIFO/mutual-restriction implementation or sensitivity alternative for B1.
- Availability conclusion: no decision-grade maintained drop-in implementation verified in this check.

### T0015 / turn-level queue transmission

- Publisher record: https://www.sciencedirect.com/science/article/pii/S0968090X24004583
- Preprint record: https://arxiv.org/abs/2310.12249
- T6 use: principal candidate equation source for B1 turn-level cumulative queue transmission.
- Availability conclusion: full methodological description is publicly locatable; no decision-grade official reference implementation verified.

### T0030 / extended macroscopic multilane node

- DOI/publisher: https://doi.org/10.1016/j.trb.2025.103208
- Authors: Xiaolin Gong, Michiel C. J. Bliemer, and Mark P. H. Raadsen.
- Status observed: open-access article; lane-based formulation, equilibrium principle, generic solution algorithm, numerical examples.
- T6 use: principal equation/algorithm anchor for B2 aggregate lane allocation.
- Availability conclusion: no verified official code; adopt by transparent transcription and reproduce published numerical cases.

## Interpretation boundary

“No verified implementation” means none was located during the bounded T6 availability check. It is not a claim that no private, supplementary, or later implementation exists. A later component plan should recheck the selected source and record the exact accessed version before implementation.

