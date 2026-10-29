# Feedback 2: contribution priority for the elementary VSL task

Date: 2026-10-12. Status: **Contribution preference recorded and assessed;
no new traffic model or execution approved.**

## Verdict and the central distinction

Your priority is sound and fits this review. The elementary task should first
show whether a simulator sensitivity guides a worthwhile common-speed change,
and what traffic information makes that guidance reliable. It need not introduce
a new VSL application or a new modeling stack. This is a workable objective for
the current refinement, although an applied usefulness result is not yet
established.

One qualification is essential: **a gradient informed by an additional traffic
statistic beating a predictor without that statistic demonstrates the value of
information for control sensitivity; it does not, by itself, demonstrate the
superiority of gradient-based optimization.** The model and its initial
observations supply the information. Differentiation carries its consequences
through the traffic dynamics and objective. It cannot recover information that
the admitted observer cannot distinguish.

This distinction does not weaken the intended contribution. It identifies the
claim that is closest to the project's question: how little traffic information
can be retained while preserving useful control sensitivities? A minimal
continuous statistic can answer that question in VSL, while the urban task
separately investigates discrete movement order and access.

## The priority to use from now on

| Priority | Defensible target | Evidence boundary |
|---|---|---|
| Primary | Useful, information-sensitive control gradients: do the retained traffic mechanisms predict speed changes that reduce complete traffic time? | Correct derivatives are a prerequisite. Independent traffic evaluation is required for an external usefulness claim; the accepted analytical certificate remains explicitly conditional |
| Supporting attribution | Identify the minimum information needed for that guidance, including whether an aggregate model plus one scalar matches the grouped model | Match observations, physical action and accounting; separate added information from representation and model-form differences |
| Optional stronger result | Gradient-based optimization achieves better cost or efficiency than alternative optimization methods | Compare methods on the same information, prediction model, action, objective and declared resources. This is additional evidence, not a requirement for the first verification |
| Secondary | The precise information/gradient verification adds something beyond the closest existing studies | Qualify that exact comparison. A literature absence claim is not necessary to make a useful verification example |

I interpret your second priority, called “task novelty,” as novelty of the
**particular study or verification**, rather than novelty of the traffic-control
task itself. That resolves the apparent overlap with your excluded claims.
Newness of the lane-drop setting, VSL control, gradient optimization in general,
or the modeling stack will not be used as the contribution premise.

Claim priority and evidence order are different. Forward semantics, observations
and derivative correctness still have to be checked before downstream usefulness.
Keeping those prerequisites does not move usefulness below modeling novelty.

## One traffic example shows what the comparison means

Use the accepted S13 example: at the fastest allowed common speed, two
preparations have the same declared aggregate history. One has little traffic
left in the ending lane; the other has much more. In the certified regime,
a feasible small slowdown harms the first preparation but helps the second.
The first should remain at the bound; the second has an improving direction.
This is a conditional result of the stated preparation and service laws.

An aggregate observer restricted to that identical history cannot tailor its
initial direction to the hidden distinction. It may still choose a sensible
average or conservative action using its permitted prior. It is not necessarily
unstable, noisy or difficult to optimize. Even an exact optimizer of its
prediction cannot resolve information withheld by the observation contract.

Adding initial ending-lane mass allows the compact model to predict the
distinction autonomously. In S13 it has exactly the same objective and gradient
as the explicit ending/continuing grouped model. Finite differences or direct
search on that compact model can also exploit the information. Consequently,
the example supports an information-to-gradient finding and a compression
finding; it does not establish that full lane state or AD is necessary to find
the best speed.

The three tests therefore answer different questions:

1. **A versus A+E:** what is gained by the initial merge statistic beyond the
   full allowed aggregate history?
2. **A+E versus G:** does the explicit grouped representation add anything at
   equal information? Equality is required in the inherited member.
3. **Gradient methods versus alternative optimizers within one model:** does
   the way of finding the action add accuracy or efficiency? The analytical
   optimum and bounded direct search are strong references for this scalar task.

Published aggregate and lane-aware models remain separate, faithfully specified
challengers. If they use different traffic laws, their performance contrast is
a model-form result until a controlled comparison supports a narrower attribution.
No future reference merge state may be supplied to any predictor.

## How to interpret the proposed signs of contribution

| Proposed indication | Assessment and fair interpretation |
|---|---|
| Better performance than an aggregate peer | Useful evidence if the same physical actions are evaluated under complete accounting. With unequal initial information, attribute the advantage to information-sensitive prediction/control; with different laws, identify the model-form contribution. It is not automatically an optimizer advantage |
| Less unstable or noisy optimization, or fewer local-optimum failures | Potentially publishable additional evidence, but not implied by omission of merge state. Separate model bias, derivative estimation noise, numerical conditioning and optimization behavior. There is no present evidence of these failures, and this one-action analytical member does not require such a claim |
| A peer needs a deliberate repair | Investigate the repair as a serious rival. One initially observed merge scalar is an economical sufficient state in S13, not an unfair engineering trick. Record its information, sensing/calibration and complexity cost. A rule fitted separately to hidden test outcomes, or using future reference state, violates fairness; a lawful compact augmentation may settle the question positively |
| No peer model has been found | A reason for a bounded nearest-work check, not evidence of usefulness or proof that no rival exists. The analytical/scalar/direct-search references already exist for this member. Even a genuinely new comparison still needs forward and downstream evidence |

The framework also allows a gradient to be **useful without being uniquely
necessary**. It may correctly explain and guide a speed change while direct
search finds the same optimum. That is an honest first verification. Claiming
superior optimization, stability or sample efficiency requires the additional
comparison in the table; it should not drive an expansion of the elementary
task merely to create a harder optimizer problem.

The present task optimizes one constant speed action. Optimization behavior is
therefore the relevant process; learned-policy training is not specified.

Your caution about numerical gradients is appropriate. A derivative estimated
from objective evaluations, such as a finite-difference gradient, belongs among
gradient-based precedents and comparators. Some zeroth-order algorithms perform
direct search without producing a gradient; they remain optimization rivals.
AD supplies a way to compute a derivative, not a separate novelty exemption.
Delle Monache, Piccoli and Rossi already studied analytical control variations
and numerical-gradient descent for VSL, alongside random exploration. That
precludes a blanket “first gradient-based VSL optimization” claim, while leaving
the exact proposed information/usefulness comparison to be audited.

[Delle Monache et al., primary abstract and manuscript](https://arxiv.org/abs/1603.04785)

Aggregate VSL predictive control is also established: Hegyi et al. use METANET
and a total-time objective. Different controls and dynamics make that a source
challenger to qualify, not a matched derivative experiment already performed
for this task.

[Hegyi et al., author report](https://www.dcsc.tudelft.nl/~bdeschutter/pub/rep/03_016.pdf)

## Is this workable for the present refinement?

**Yes, as a contribution target, with an honest conditional fallback.** S13
already supports the analytical possibility of different useful directions and
the sufficient-scalar result. It does not yet establish a physical task in which
those directions transfer to independently evaluated traffic. The joint
speed/realized-transfer/receiving qualification identified in feedback 1 remains
the first modeling burden. This priority does not authorize selecting a new
transfer law, service allocation, observation contract or evaluator.

A prospective applied claim is:

> In a declared elementary lane-drop regime, retaining a minimal merge-
> preparation statistic improves prediction of useful common-speed changes
> relative to the specified aggregate observer, and a compact augmented model
> reproduces the grouped model's sensitivities. Usefulness is checked through
> independent complete-time evaluation of common physical perturbations.

That is a **target statement, not a reported result**. Today the defensible
result is narrower: under the accepted analytical assumptions and conditional
observer construction, initial merge preparation can change the improving
direction, and one continuous scalar suffices. No empirical performance gap,
optimization-process advantage or external gradient transfer has been measured.

These outcomes remain acceptable and have different meanings:

| Eventual finding | Claim to retain |
|---|---|
| Correct independent perturbation guidance; compact model equals grouped model | Useful sensitivities with a minimal sufficient statistic; no full-lane necessity |
| A strong aggregate challenger gives equally useful guidance in the admitted cases | Aggregate sufficiency in that tested domain; narrow any additional-information claim |
| Gradients and direct search perform equally well | Gradient verification may succeed; optimizer superiority is unsupported |
| Internal derivatives are correct but independent perturbations are harmful | Derivative correctness without external usefulness; report a negative transfer result |
| Credible physics requires a substantial new traffic stack | Revisit the elementary companion role before construction; retain S13 only within its analytical boundary |

No positive result is required to justify adding complexity. The local review
question is whether the smallest defensible mechanism carries the contribution
target. If it does not, narrow the claim or return to task selection. The urban
task and project hypothesis remain unchanged; VSL does not become a certificate
that discrete ordering is necessary.

## Recorded disposition and stop

The opening plan, methods outline, nearest-work screen and living core-model
candidates now use this priority. Candidate A remains the conditional reference;
B's bounded physical qualification remains unselected; C does not become the
default route to a stronger claim. Feedback 2 is answered and its preference is
recorded. This is a contribution-priority discussion, not approval to execute
the successor review or any experiment.

[Current opening plan and ownership](../../vsl_successor_00_opening_plan.md)

[Core-model candidates, still unselected](../../synthesis/research_readiness/vsl_feedback1_core_model_candidates.md)

[Work report and document checks](vsl_feedback2_work_report.md)
