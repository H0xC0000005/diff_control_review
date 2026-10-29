# T6 dialogue

Date: 2026-09-10  
Status: T6 open

## Clarification of the proposed defaults

The user found the original one-line default list too compressed to convey the experiment's overall operation. The list in `../synthesis/experiment_formulation.md` was expanded into D1–D7. Each entry now explains:

- what the default means operationally;
- why it is proposed;
- how it contributes to comparison fairness or interpretability; and
- what evidence may revise it without silently changing task semantics.

No default was approved, rejected, or promoted to fixed status by this editorial clarification. The physical action remains the phase service fractions; optimizer logits remain internal coordinates only.

## TST occupancy notation correction

The user observed that Section 3 of the formal contract appeared to sum source and network queues, which would define queue/waiting time only indirectly rather than total system time. The intended network term was all in-network mass, including moving and queued traffic, but the symbol $Q^{\mathrm{net}}$ misleadingly suggested a queue variable.

The formal contract now uses $N^{\mathrm{src}}$ for released mass waiting at sources and $N^{\mathrm{net}}$ for all mass physically present in the modeled network. It explicitly states that the time integral of their sum is the area under the number-in-system curve and equals summed source-to-destination elapsed time when all released demand completes. Summing only stopped/queued mass would instead measure waiting or queue time and is not the proposed primary objective.

This is a notation and definition clarification, not a change from TST to a different objective.

## Formal task and variant-gradient amendment

The user accepted V0–V4 as the valid primary variants and requested removal of V5 because it is principally an integration and initial network test. The former V5 is now conditional post-suite test I1. It may be required after V0–V4, but it is no longer part of the first scientific campaign.

The user also requested an explicit colleague-facing definition of $f$, $x$, $df/dx$, the complete objective-to-control gradient path, and the additional propagation introduced by each variant. The formal contract now defines:

- $f$ as clearance-complete total system time;
- $x$ as the physical effective-service allocation $g$, not optimizer logits;
- a state-transition sensitivity recursion connecting service to the objective;
- V0's direct service/discharge path;
- V1's continuous ordered-prefix/residual-head path;
- V2's bay discharge/storage/admission/spillback feedback path;
- V3's exact order-conditioned accessibility path under a fixed structural skeleton; and
- V4's fixed scenario-bank average of scenario-level gradients.

The amendment preserves piecewise differentiation: continuous mass is differentiated within a stable scan/prefix/active-set signature, while route identity, labels, permissions, permutations, and branch changes remain structural.

## Symmetric four-leg default

The user rejected the underspecified asymmetric three-group starting point in favor of a regular four-leg intersection because rotational symmetry provides the clearest default. The suite now uses four protected effective-service groups: north–south through/right, north–south left, east–west through/right, and east–west left. Red clearance is not a service group because the task remains at the effective-service rather than executable-timing layer.

Core V0–V3 scenarios apply the same lane layout, demand profile, turning shares, order pattern, capacities, and downstream conditions to every corresponding approach under 90-degree rotation. This creates an additional validation invariant: rotating the scenario and permuting the four service allocations must preserve the objective and rotate the gradient accordingly. V4 may add predeclared asymmetric held-out strata, but they are labeled departures from the symmetric default.

## Definition of optimizer coordinate z

The user noted that $z$ was insufficiently defined at its use in the derivative contract. The formal and summary contracts now state that $z\in\mathbb{R}^4$ is an optional dimensionless internal logit/score vector mapped by the simplex parameterization to physical service allocation $g$. It is not the scientific input $x$ and is not compared across models. The text also records the softmax redundancy: a common additive shift to every logit leaves $g$ unchanged, so implementations may center the logits or fix one reference coordinate.

## Forward-sensitivity recursion explanation

The user asked why $S_{k+1}=A_kS_k+B_k$ holds and whether integrating its right-hand side with respect to $g$ simply recovers $F_k$. A separate explanatory note derives the recursion from the chain rule applied to $X_{k+1}(g)=F_k(X_k(g),g)$. It emphasizes that $B_k$ is only the direct partial derivative holding the incoming state fixed, while $A_kS_k$ transports all control effects already accumulated in that state. The recursion computes a total derivative; it performs no integration.

The note includes a scalar recurrence, a finite-turning-bay traffic interpretation, the objective-gradient chain, initial-state qualification, and nonsmooth-event boundary. Its source and rendered PDF are `forward_sensitivity_recursion_explainer.tex` and `.pdf`.

## Suppressing the fixed model index

The user preferred not to carry an unchanged model superscript/subscript through every within-model formula. The formal formulation now fixes an arbitrary realization $M$ once in a notation-convention paragraph and suppresses it throughout the subsequent within-model definitions and derivations. Thus $X$, $F$, $J$, $f$, $S$, $A$, and $B$ are understood to belong to that fixed model.

Model labels are retained only in genuinely cross-model statements, such as comparing directions proposed by models $M_i$ in richer evaluator $R$. This is a notational simplification only: choosing $M$ still determines the state, transition equations, Jacobians, and resulting gradient.

## Literature and engineering adoption behind the baseline ladder

The user observed that the realization matrix defined baseline roles but did not show which literature could be adopted methodologically or engineeringly. This omitted the practicality and literature-affinity argument important to colleagues.

The matrix now contains a literature/adoption overview and links to `../synthesis/literature_adoption_matrix.md`. The new audit distinguishes faithful equation transcription, bounded methodological adaptation, engineering-pattern reuse, direct software reuse, forward-reference reproduction, and contextual citation.

The resulting adoption position is:

- B0 retains the accepted project macro backbone while using T0001/T0005/T0011/T0012 for AD patterns, signal equations, and independent checks;
- B1 selects a principal published turn-queue formulation from T0015, with T0014/T0007/T0010 supplying explicit alternatives, task affinity, and physical checks;
- B2 uses T0030 as the principal lane-allocation anchor and an explicitly sourced finite-storage augmentation from T0008–T0010;
- B3 is a project-owned, component-provenance composition rather than a claimed reimplementation of one paper;
- R1 reproduces independent published forward behavior; and
- R2 directly reuses SUMO, with T0025/T0022/T0027 informing controller/evaluation practice.

Current public-source verification found UNsim and diff-hybrid-traffic-sim useful as licensed differentiable-engineering references but not task-compatible drop-ins. SUMO is the strongest direct software adoption. No decision-grade public drop-in implementation was verified for the exact B1/B2 equations, so transparent transcription and published-case reproduction are required.

## Status of the gradient framework versus operator derivatives

The user understands the formal formulation as a logically complete framework-level gradient chain, while the exact derivatives of variant-specific operators—especially ordered access—remain coupled to the exact milestone design. This understanding is accepted with the following boundary.

The T6 formulation fixes the required dependency path, scientific input and output, structural nondifferentiated variables, piecewise/stable-signature interpretation, and evidence obligations. It does not yet prove that every future operator is differentiable in every state, nor does it prescribe Jacobians before the corresponding equations and update ordering are approved.

Later milestone planning must treat this task/gradient contract as a design and acceptance anchor:

- Milestone 2 interfaces must preserve continuous state paths, conservation, and the lane-zone/ledger observables needed downstream;
- Milestone 3 must define the exact lane-allocation, finite-storage, ordered-access, and service operators and establish their local Jacobians or AD behavior within approved stable signatures;
- later sensitivity and optimization plans must compose those component paths into the T6 objective gradient and validate them hierarchically; and
- an implementation convenience may not sever the required path, introduce an unapproved surrogate gradient, or differentiate structural route/order choices.

The contract is an equal scientific design pillar, not authority to override repository invariants or closed milestone decisions silently. If an approved component design cannot realize a required gradient path, the smallest affected task or milestone decision must be reopened explicitly.
