# A minimal matched controller, and the choice before adopting it

**Timing choice resolved by the user, 2026-11-02:** start by optimizing
each initialized case. Current-case simulator queries are permitted before
committing its constant advice. Shared-controller training and runtime
optimization remain deferred. The original alternatives and source reasoning
below are preserved as the discussion record.

[Current per-case definition and contract gate](vsl_per_case_matched_controller_contract.md)

2026-11-02. **Matched-controller review opened and stopped at a methodological
choice.** A simple candidate pair can be formed. Whether it is the right
first verification depends on when simulator feedback is available.
No controller, query protocol or experiment is adopted by this report.

**The smallest candidate B is the advice value itself.** Both versions
optimize the same single constant-speed parameter for the same initialized cohort.
B0 compares candidate speeds using complete TST values from the detailed
simulator. B-gradient uses that simulator's complete speed derivative
to guide updates to the same speed parameter.

This is a source-supported direct speed-optimization approach, rather
than a newly invented controller architecture. It can be an elementary
test of simulator gradients. It is not automatically a test of training
an aggregate-observation controller for previously unseen traffic.

## What can actually be formed

| Part | Candidate specification | Source and qualification |
|---|---|---|
| **Common B** | One bounded speed parameter, applied commonly throughout the road and held fixed during each executed episode. | Direct speed-setting optimization is supported by [1], [2]. Restricting it to our task is an explicit adaptation. |
| **B0** | Repeated objective evaluations compare candidate values of that parameter. Include strong bounded scalar search; maximum advice is an additional reference. | [1] supplies speed enumeration and a separate fine-simulator objective-feedback workflow. Do not transplant its spatial profile or source optimum. |
| **B-gradient** | Use the complete derivative from the selected lane-resolved plant to guide a constrained first-order update of the same parameter. | [2] supplies a VSL gradient-optimization precedent; our existing model contract supplies the applicable derivative. Its traffic equations and gradient formula are not imported from [2]. |

Both B versions retain identical forward traffic dynamics, complete-TST
accounting, action bounds, initialization, and final constant-advice
application. Neither needs explicit lane features at a controller input.
The distinguishing feedback is objective values versus access also to
the simulator derivative. This does not make the richer derivative an
undeclared input; its availability is the intervention being studied.

The “aggregate information” in this simplest candidate is **scalar
performance feedback**. It is not a controller that reads a spatial vector
of E and A+B observations. That distinction must remain explicit.

The existing regular-branch sensitivity includes finite-trajectory effects,
residual-state effects and direct residual travel time. It allows this
candidate at the mathematical level; it does not establish numerical
gradient correctness, convergence or better advice. Native switches can
invalidate a two-sided derivative or defeat a finite step suggested by
a local derivative. No smoothing, density epsilon or changed traffic law
is proposed.

## What the source check establishes

Zhang et al. [1] explicitly optimize speed parameters using objective
feedback from Aimsun, and separately use aggregate CTM enumeration.
Delle Monache, Piccoli and Rossi [2] formulate direct VSL optimization
and compare search with a gradient method. Thus a new neural policy is
not required merely to give the simulator gradient a recipient.

There are important transfer limits. The latter source studies free-flow
outflow tracking and time-varying controls. Its random exploration uses
endpoint-valued speed sequences; that is not a suitably matched search
over our whole scalar interval. We retain the direct-optimization principle,
not that endpoint-only comparator or the source's PDE sensitivity.

For our one-dimensional action, B0 must be allowed to search the interior.
The continuous admissible speed interval is common to both versions;
a finite search approximates it at a declared resolution and budget.
Source search and gradient methods are evidence of applicability in VSL,
not a native reproduction of the proposed matched experiment.

## The choice that changes what the result means

Consider the existing pair of initial traffic states. They have the same
E and A+B profiles, but different A/B loading. Their local services differ;
different best advice has not been proved.

There are two ways to use a simulator when choosing advice for those cases.

| First verification | What the methods may do | What it could establish |
|---|---|---|
| **Optimize the current case — recommended elementary start** | Reset and query the current initialized case at candidate speeds before selecting its final constant advice. B0 gets TST values; B-gradient also gets derivatives. Both retain results of their admitted queries. | Numerical sensitivity and advice-optimization usefulness for that case, under measured query/computation budgets. |
| **Train one aggregate-observation controller across cases** | Use training cases and their permitted feedback to fit a shared rule; at evaluation, give the rule only the declared aggregate observations and no case-specific optimization queries. | Whether detailed simulator gradients help train a useful shared controller despite its coarse explicit inputs. |

Both options can retain one constant advice per executed traffic episode.
Their difference is **how the advice is obtained**, not whether vehicles
receive repeated speed changes during that episode.

In the first option, each method may discover features of the current
case through simulator queries. Different hidden lane splits may therefore
lead to different choices even when the original aggregate observations
agree. This is legitimate under a declared planning-query protocol, but
it is no longer the old observation-only decision comparison.

In the second option, a deterministic shared rule must give the same action
to identical evaluation inputs. Fine simulator gradients can help learn a
better shared decision, but do not create a distinguishing input at deployment.
This does not preclude a training-efficiency or performance benefit.
A concrete literature-supported common controller for this option has not
been qualified by the current source reading.

Scalar per-case optimization must not silently stand in for shared-policy
training. Conversely, shared training should not be added just because
the term “controller” suggests a neural network.

## Why this is a methodological decision

The earlier evidence contract allows one advice chosen before future
traffic reveals the split. Per-case simulator queries can reveal it before
the committed advice through predicted costs or derivatives. The user's
clarification explicitly permits simulator detail to influence optimization,
but does not settle whether that happens during training or during planning
for the current evaluation case.

That timing/access choice changes the information channel and the
scientific claim. It is not a numerical implementation convention.
The traffic stack, finite cohort, completion line and physical advice
action can remain unchanged under either option.

The review therefore stops here, as authorized, before assuming either
query access or a shared-policy architecture.

## Relationship to the published aggregate rival A

Zhang's aggregate CTM/enumeration remains a candidate external performance
reference. A versus B0 measures the combined effect of the predictive
representation, query access and decision method; B0 versus B-gradient
is the matched simulator-derivative comparison once the protocol is fixed.

A comparison with A must state what predictor information and offline
data it receives, how it is adapted to the common task, and its own
query/computational costs. It is not automatically an equal-oracle-access
comparison merely because every final advice is evaluated in the same plant.

B0's competence relative to A is a future empirical check, not a review
acceptance condition requiring experiments now. No equality or inferiority
is stipulated. Successful scalar search, maximum-advice optima and zero
gradient benefit remain valid outcomes.

## Recommendation and stop

**Recommend the per-case scalar pair as the first elementary optimizer/
gradient verification**, explicitly limited to that role. It has a clear
literature-supported control parameterization, uses the already reviewed
plant sensitivity, and requires neither a new traffic model nor a new
learned policy architecture.

If the required first result is instead about a shared controller that
uses aggregate observations on new cases, choose the second option and
qualify its published controller family before calling B fixed.

The decision at this gate is which of those first verifications is intended.
After that decision, finish the selected B contract, data/query rules and
comparison with A, then formulate the elementary development target.
Neither the experiment protocol nor private development handoff is frozen.

[Primary readings and precise transfer limits](../../extraction/research_readiness/vsl_matched_controller_review_sources.md)

[Work scope and document checks](vsl_matched_controller_review_work_record.md)

## References

[1] C. Zhang, E. Chung, N. R. Sabar, A. Bhaskar, and Y. Ma, “Optimisation
of variable speed limits at the freeway lane drop bottleneck,”
*Transportmetrica A: Transport Science*, vol. 19, no. 2, Art. no. 2033878,
2023, doi: [10.1080/23249935.2022.2033878](https://doi.org/10.1080/23249935.2022.2033878).
[Primary manuscript](https://ira.lib.polyu.edu.hk/bitstream/10397/92568/1/Zhang_Optimization_Speed_Freeway.pdf),
Sections 3.2 and 4.3.

[2] M. L. Delle Monache, B. Piccoli, and F. Rossi, “Traffic regulation via
controlled speed limit,” arXiv:1603.04785, 2016.
[Primary manuscript](https://arxiv.org/pdf/1603.04785),
introduction and Sections 3.2–3.3. The 25-page v1 manuscript is the version
inspected here.

[Selected plant, complete objective and regular sensitivity](../../synthesis/research_readiness/vsl_joined_candidate_contract_and_qualification.pdf)

[Existing prospective comparison/evidence contract](../../synthesis/research_readiness/vsl_joined_candidate_verification_contract.md)

