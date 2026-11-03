# A published aggregate rival for the first VSL verification

**Current A status:** the user defers A while the matched B pair is
verified first. A's later review must preserve source core assumptions/
algorithm backbone and intended behavior under scenario adaptation.
A simpler established method is preferred if suitable; Zhang is not
locked in as A. The source-screen findings below remain historical
evidence, not an adopted or completed aggregate benchmark.

[Current B-first scope and specification](vsl_b_pair_elementary_verification_specification.md)

**Task-fit review executed:** the common B controller fits under its
declared adaptation. This does not qualify the aggregate predictor A.
A's density-bearing bottleneck cell needs an explicit counterpart at the
target's free choke exit. Work stops at whether A is required before the
first B comparison or stays pending for later qualification.

[Current task-fit findings and choice](vsl_zhang_task_fit_findings_and_choice.md)

**Latest comparison status, 2026-11-02:** the user selects per-case
optimization for the first elementary gradient verification. Its matched-B
contract is delivered separately. The aggregate CTM/enumeration remains
reference A's candidate source route, with exact task compatibility still
to be closed; later discussion below preserves the earlier chronology.

[Current per-case matched optimizer](vsl_per_case_matched_controller_contract.md)

2026-11-02. **Rival-selection review completed; recommendation at the gate.**
The reviewed lane-resolved plant remains the selected traffic model.
The rival recommended below is not yet adopted or ready for implementation.

**Discussion amendment:** the published aggregate reference is not sufficient
to identify a gradient benefit. A common controller with matched versions
using and not using simulator derivatives has not been selected. That gap
must close before the comparison can be finalized.

[Matched-controller clarification and current question](vsl_matched_controller_gradient_comparison_clarification.md)

**Recommend Zhang et al.'s aggregate CTM plus speed enumeration as the
source of the first rival.** It supplies a concrete precedent for choosing
VSL at a lane drop using an aggregate traffic model. Its search procedure
is simple enough for the one-advice task. A version using our common
advice and complete TST would be an explicit task adaptation, not a
reproduction of the published controller.

This is the first item of the agreed review plan. It identifies the most
promising source and the changes that would have to be justified. It does
not close the comparison protocol, elementary experiment or development
handoff.

**Matched-controller follow-up:** the next source/contract review has
opened and stopped at per-case planning-query access versus shared-
controller training. A simple scalar B0/B-gradient pair is a conditional
candidate; adopting this aggregate reference alone still does not close
the comparison.

[Current matched-controller findings and gate](vsl_matched_controller_review_findings_and_gate.md)

## What the rival would mean in traffic terms

Imagine the same amount of E traffic approaching the choke, with the same
combined A+B loading, but with the continuing traffic distributed differently
between A and B. The selected plant keeps that distinction. Its derivative
can follow the resulting changes in lane requests, receiving and discharge.

The proposed rival predicts traffic as aggregate road cells and chooses
among candidate speeds using that prediction. It does not explicitly
represent E's interaction with A and B separately. This is the kind of
published simplification relevant to the question about detail carried by
the gradient. An aggregate model can still predict congestion and capacity
loss; it must not be reduced to a fixed-capacity queue for convenience.

A fair eventual comparison would evaluate the rival's selected advice in
the **same lane-resolved plant and complete-TST objective** as the gradient
method. The published aggregate predictor supplies a competing decision
model, not a replacement evaluator.

## What the source actually supplies

Zhang, Chung, Sabar, Bhaskar and Ma study a three-to-two lane drop. Their
microscopic optimization uses a modified genetic algorithm. Separately,
Section 4.3 uses an aggregate CTM and enumeration to select the minimum
speed within a spatial profile informed by the microscopic optimization.
The source criterion is throughput over a study period [1].

**The recommended branch is CTM plus enumeration, not “GA plus CTM.”**
The two optimization procedures have different roles in the paper. The
source establishes a lane-drop application of aggregate prediction and
speed selection, without certifying our task adaptation.

This meets the requested literature requirement at the level of a
**published model/control method applied in the same scenario family**.
It is stronger support than citing a generic optimizer and inventing a
coarse traffic model around it. It does not establish a verbatim published
baseline for our finite-cohort task.

### Rule-based application and gradient compatibility

The later practical discussion (PDF p. 22, Figure 19) chooses profiles
according to demand and proposes half-interval feedback search for one
speed. This explains the rule-based appearance. The earlier GA and CTM
enumeration branches optimize by objective evaluations, not gradients.

State conditioning and optimization method are separate questions. A
controller can react to traffic state while its parameters are optimized
with or without gradients. Here the published search supplies a
non-gradient rival; it does not establish a gradient-ready controller.

A gradient variant would optimize continuous speed/profile parameters
through a predictive rollout, rather than differentiate through GA or
enumeration. Source discrete choices and the density-triggered capacity
drop require a separate parameterization and regular-branch derivative
check. No smoothing or continuous relaxation is approved by this comment.
Potential compatibility is not a completed qualification. If paired
gradient/non-gradient versions become required, that check must precede
adoption of such a pair.

## Why this source is preferable for the elementary start

| Inspected work | Direct source finding | Consequence for our first rival |
|---|---|---|
| **Zhang et al. [1]** | Aggregate CTM with speed enumeration at a lane drop. | **Recommended starting source.** An open-loop scalar search is close to the chosen decision structure; the task changes below remain explicit. |
| **Han et al. [2]** | Rolling-horizon control optimizes intercell flows, converts them into VSLs and uses a quadratic population cost with a flow reward. | Strong aggregate alternative from our model lineage, but its controller is not supplied merely by reusing Han's sending/receiving budgets. Forcing one common speed changes the optimization formulation. |
| **Hegyi et al. [3]** | METANET-based predictive control repeatedly updates speed controls; its aggregate state includes mean speed. | Established control context, with more state and control machinery than needed first. Freezing the first feedback output would remove an essential part of the method. |
| **Jin and Jin [4]** | Lane-drop I/PI feedback acts through upstream inflow regulation; constant-control analysis concerns equilibria. | Poor direct fit to a cohort already inside the road with no later inflow. Applying its native boundary control there would not control the initialized traffic; moving its actuation would require adaptation. |
| **Wei et al. [5]** | Strong aggregate forward model; coupling it to MPC is proposed as future work. | Useful future predictor candidate, but the inspected paper alone does not supply the required published controller. |

The recommendation concerns the smallest credible first comparison.
It is not a finding that these alternatives are ineffective, or that
Zhang's model is the most accurate.

## What must be adapted, and what must remain fixed

| Interface | Proposed handling | Meaning and unresolved work |
|---|---|---|
| **Predictive traffic representation** | Start from the source's aggregate CTM, demand/supply and bottleneck law. | Retain its genuine traffic model. Do not replace it with our lane equations after deleting lane labels. |
| **Action** | Search one common constant advice within the reviewed task bounds, rather than a spatial profile parameter. | A different task-specific parameterization, not automatically a feasible subset of the source's sign constraints. It requires an explicit actuation map; source optimality/results do not transfer. |
| **Population and objective** | Use the same initialized cohort and evaluate complete TST through the agreed choke exit. | Replaces the source's demand-driven, finite-period criterion. The aggregate predictor's own complete accounting must be specified; our lane-model residual formula cannot simply be copied. |
| **Geometry, state projection and completion** | Preserve physical mass, spatial information and the plant's completion line. | Locate the source's bottleneck cell/service relative to the choke, specify aggregate initialization and separate predictor states from counted traffic. Do not silently add downstream trip time or a new physical restriction. |
| **Parameters and prior knowledge** | Use declared physical information and a common parameter-setting protocol. | Do not transfer a source optimum or obtain a speed profile from hidden test outcomes. Nominal quantities, model-specific calibration and parameter-transfer assumptions require disclosure. |

The last two rows are **scientific compatibility work**, not software
details to delegate unresolved to development. The current source reading
does not establish a complete baseline boundary/initialization contract.
If closing those interfaces requires an invented constitutive law, we must
reconsider this route rather than call that law borrowed.

Our plant, once-chosen advice, finite cohort and complete accounting are
the inputs to that next discussion. No change to them is recommended here.
The source's preferred low minimum speed does not establish a useful
choice inside our advice range. Its spatial metering mechanism cannot be
assumed to survive uniform advice throughout the road.

## What a comparison could establish

The source and plant have different congestion and VSL laws as well as
different lane resolution. Consequently, a performance difference would
initially be a **model-and-gradient comparison**, not proof that aggregation
alone caused the difference.

The direct comparison is useful as an overall performance reference.
For a simulator-gradient claim, specify an intermediate version of the
same eventual controller without simulator derivatives:

| Comparison | What it establishes |
|---|---|
| Published aggregate reference versus common controller without simulator derivatives | Whether the common controller is a credible performance baseline; model and controller effects are still present. |
| That same controller with versus without simulator derivatives, using the same forward plant and explicit inputs | Usefulness of the simulator-gradient pathway under the declared optimization/data budget. |

The common controller has not been fixed. Source [1]'s fine-simulator
objective-feedback optimization is a useful source-supported starting
pattern, not a qualified gradient counterpart. The scalar advice itself
could be the common parameterization; shared-policy training is a separate,
unselected possibility. No extra lane features need be supplied to the
controller just because simulation detail influences its gradient.

Objective-only feedback also reflects lane effects through TST.
Successful scalar search and a zero gradient advantage remain legitimate
outcomes. Competence relative to the published reference must later be
measured rather than assumed.

[Full explanation and source distinction](vsl_matched_controller_gradient_comparison_clarification.md)

## The decision at this gate

**Recommend taking Zhang's aggregate CTM plus enumeration into the next
comparison-design review as the principal candidate, with the adaptations
above visible from the outset.** The gate is acceptance of that source
route, not acceptance of an already completed baseline implementation.
Adopting that reference alone will not close controller selection.

The next review item must first qualify the common controller/parameterization
and its matched update methods, then resolve the proposed action,
cohort/objective, projection and boundary fit and simulator-detail access. It should stop if doing so requires a new traffic law
or a change to the selected task. Only after those scientific interfaces
are settled should the elementary verification and final development
handoff be consolidated.

No code, traffic experiment, simulator installation or private-repository
handoff update was performed. Numerical benefit, physical fidelity and
novelty of the precise comparison remain unestablished.

## References and reading record

[1] C. Zhang, E. Chung, N. R. Sabar, A. Bhaskar, and Y. Ma, “Optimisation of
variable speed limits at the freeway lane drop bottleneck,” *Transportmetrica
A: Transport Science*, vol. 19, no. 2, Art. no. 2033878, 2023,
doi: [10.1080/23249935.2022.2033878](https://doi.org/10.1080/23249935.2022.2033878).
[Primary manuscript](https://ira.lib.polyu.edu.hk/bitstream/10397/92568/1/Zhang_Optimization_Speed_Freeway.pdf),
Section 4.3; the exact source location for enumeration is PDF p. 21.

[2] Y. Han, A. Hegyi, Y. Yuan, S. Hoogendoorn, M. Papageorgiou, and
C. Roncoli, “Resolving freeway jam waves by discrete first-order model-based
predictive control of variable speed limits,” *Transp. Res. C*, vol. 77,
pp. 405–420, 2017, doi:
[10.1016/j.trc.2017.02.009](https://doi.org/10.1016/j.trc.2017.02.009).
[Primary manuscript](https://pure.tudelft.nl/ws/files/45432235/AAM.pdf),
Section 3, especially equations (11)–(19).

[3] A. Hegyi, B. De Schutter, and H. Hellendoorn, “Model predictive control
for optimal coordination of ramp metering and variable speed limits,”
*Transp. Res. C*, vol. 13, no. 3, pp. 185–209, 2005, doi:
[10.1016/j.trc.2004.08.001](https://doi.org/10.1016/j.trc.2004.08.001).
[Author report 03-016](https://www.dcsc.tudelft.nl/~bdeschutter/pub/rep/03_016.pdf),
Sections 3.1–3.2. Only its VSL/model-comparison relevance is used; the
closed ramp-metering review is not reopened.

[4] H.-Y. Jin and W.-L. Jin, “Control of a lane-drop bottleneck through
variable speed limits,” arXiv:1310.2658, submitted 2013.
[Primary manuscript](https://arxiv.org/pdf/1310.2658), Sections 2–4.
The inspected PDF is headed October 29, 2018; this version distinction
is retained.

[5] L. Wei, Y. Han, and M. Wang, “A first-order link-based flow model with
variable speed limits and capacity drops for freeway networks,”
*Comput.-Aided Civ. Infrastruct. Eng.*, vol. 40, no. 21, pp. 3200–3217,
2025, doi:
[10.1111/mice.13492](https://doi.org/10.1111/mice.13492).
[Publisher text](https://onlinelibrary.wiley.com/doi/full/10.1111/mice.13492),
discussion of control applications.

[References actually inspected, source locations and access limits](../../extraction/research_readiness/vsl_literature_rival_selection_sources.md)

[Work scope and document checks](vsl_literature_rival_selection_work_record.md)

