# Why the gradient comparison needs a matched controller

**Current continuation, 2026-11-02:** per-case optimization is now
user-selected. The proposed matched pair uses a scalar advice with value-only
global search or complete simulator derivatives and value checks. Its
methodological definition is delivered at the contract gate. This resolves
the feedback-timing choice; it does not adopt a shared learned controller
or establish numerical performance. The discussion below is historical.

[Current per-case contract](vsl_per_case_matched_controller_contract.md)

2026-11-02. **Discussion clarification, not an adopted controller or
experiment plan.** The literature-backed traffic stack stays fixed.
The source screen identified a published aggregate reference; it did not
finish selection of a controller with matched versions using and not
using simulator derivatives.

**Later execution:** the user approves opening the brief matched-controller
review. It identifies a simple conditional scalar pair but stops before
choosing per-case simulator queries or a shared controller trained across
cases. The original discussion below is preserved.

[Current findings and methodological gate](vsl_matched_controller_review_findings_and_gate.md)

## Direct answers

**The gradient-receiving controller is not fixed yet.** The review has
specified the plant's regular speed sensitivity and identified a
non-gradient published rival, but has not qualified a common controller,
its inputs, parameterization and two update methods.

**An intermediate version is needed for the intended gradient claim.**
Comparing the aggregate CTM/enumeration reference directly with an unrelated
gradient method could show an overall performance difference, but would
combine predictor, traffic-law, controller and optimizer effects. It would
not identify the contribution of simulator derivatives.

The user's proposed intermediate is therefore a substantive correction
to the comparison proposal. The previous same-plant objective-only
reference pointed toward this requirement but was not a fully specified
controller satisfying it.

## The comparison to formulate

| Method | What it uses | Its scientific role |
|---|---|---|
| **Published reference A** | The source-backed aggregate predictor and non-gradient control/search method, after accepted task adaptations | A credible traffic-control performance reference. |
| **Common controller B, without simulator derivatives** | A qualified controller/parameterization with the declared aggregate explicit inputs or feedback; objective feedback from the selected detailed plant | Establishes what that controller can achieve without simulator-provided derivatives. Its competence should be checked against A. |
| **The same B, with simulator derivatives** | The same controller structure, explicit inputs, action opportunity, objective and forward plant; updates additionally use the plant's derivatives | Compared with B without derivatives, tests the usefulness of the simulator-gradient pathway. |

The forward plant must retain the same lane detail in the two B versions.
Removing detail from its forward dynamics when derivatives are disabled
would change more than the optimization signal. Detailed state need not
be supplied as explicit controller features merely because it is used
inside the differentiated simulation.

Hold scenario/data access, initialization and the action problem fixed,
and account for forward evaluations, derivative evaluations and computation
when comparing optimization effort. The update algorithms can differ;
the point is a credible objective-only counterpart rather than an
intentionally weak optimizer. “Without gradients” should here mean
**without simulator derivatives**: a method could still use finite
differences, score-based policy gradients or gradients internal to its
own model. Those are distinct comparators and must be named accurately.
Finite differences remain gradient estimates and must not be labeled
derivative-free merely because they use objective queries.

B's performance without simulator derivatives is not known. Review can
establish methodological comparability and a defensible source basis;
development later measures competence and performance. Comparable quality
is a check, not an equality to stipulate or an outcome already proved.

## What the literature reading already contributes

Reference [1] has another useful branch besides the aggregate CTM:
Section 3.2 represents speed settings as parameters, evaluates candidates
in Aimsun and returns a scalar objective to its GA. This is a published
example of optimizing VSL from fine-simulator objective feedback [1,
PDF p. 12]. It supplies a possible source-supported pattern for B without
simulator derivatives.

It does **not** establish a published gradient counterpart, a learned
aggregate-state policy, compatibility with our complete-TST cohort,
or comparable performance in our task. Scalar objective feedback should
not be silently identified with an arbitrary spatial aggregate observation
vector. The admissible information contract remains to be specified.

Also, absence of a gradient optimizer in [1] does not mean its speed
parameters are intrinsically unable to receive a gradient. A gradient is
used to update the parameters; the GA or enumeration algorithm itself
need not be differentiable. If derivatives are taken through the selected
lane-resolved plant, it is that plant's qualified sensitivity that matters.
Differentiating the source CTM would be a different variant and would
need its own switching/parameterization checks.

For the current one-constant-advice task, the common parameterization
could be as simple as the scalar advice itself. A neural controller is
not automatically needed. Whether that elementary optimization is sufficient,
or a controller shared across episodes is needed, remains open. Neither
version of B is selected merely by identifying this possibility.

## What changes in the review recommendation

Keep [1]'s aggregate branch as a candidate external reference, but do not
treat its adoption alone as completing controller/rival selection.

The next bounded review question should be:

> Which source-supported common speed/controller parameterization can
> support a credible version without simulator derivatives and a matched
> version using the selected simulator's derivatives, under the same
> explicit aggregate information and action contract?

First examine the simplest speed-parameter optimization supported by the
source's objective-feedback workflow. A separate published learned
controller is needed only if that is the research object we choose.
Any proposal still needs explicit source/adaptation credit and the user's
decision where scientific meaning changes. No new architecture is
invented or approved in this clarification.

Finally, replacing a spatial profile, objective or completion boundary
changes the scientific decision/comparison contract. These are
**methodological task adaptations**, even while the selected traffic
stack remains unchanged. The user's acceptance in principle is not a
finding that the adaptations have no methodological effect.

## Supporting records

[1] C. Zhang, E. Chung, N. R. Sabar, A. Bhaskar, and Y. Ma, “Optimisation
of variable speed limits at the freeway lane drop bottleneck,”
*Transportmetrica A: Transport Science*, vol. 19, no. 2, Art. no. 2033878,
2023, doi: [10.1080/23249935.2022.2033878](https://doi.org/10.1080/23249935.2022.2033878).
[Primary manuscript](https://ira.lib.polyu.edu.hk/bitstream/10397/92568/1/Zhang_Optimization_Speed_Freeway.pdf),
Section 3.2, especially the speed-parameter representation and fitness
evaluation, and Section 4.3 for the separate CTM branch.

[Updated source-selection findings](vsl_literature_rival_selection_findings.md)

[Earlier comparison and sensitivity evidence contract](../../synthesis/research_readiness/vsl_joined_candidate_verification_contract.md)

No simulator, training, numerical experiment, dependency or private handoff
change is made by this response. The current gate remains open with the
matched-controller question explicit.

