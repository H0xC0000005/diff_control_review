# AS2: the past can conceal unused adjacent receiving

Date: 2026-10-19. **AS1 and AS2 are user-accepted. AS3 is subsequently
delivered at the original Step 3 user closure gate; formal closure is pending.**

[AS2 acceptance, learning-claim clarification and AS3 scope](vsl_as2_acceptance_and_as3_opening.md)

[Subsequent AS3 findings and final Step 3 gate](vsl_as3_findings_and_step3_closure_gate.md)

The core finding is that **the same observed traffic can conceal different
amounts of spare space in the adjacent lane**. If early E merging has always
been easy enough for every attempted transfer to succeed, observing E's
decline tells us how much it attempted, but not how much more A could have
accepted. A relatively empty A and a busier A can therefore leave exactly
the same aggregate and E histories.

That is a sound Level 2-to-Level 3 information contrast within the accepted
model. It survives the full predecision longitudinal record, not just a
snapshot. It is also conditional: if the observed past contains receiving-
limited merging, the richer traffic history may reveal A. The rival must be
allowed to use that information.

The other main finding limits how much representation is needed. **One
additional initial adjacent-lane load closes this information gap in the
homogeneous family.** Explicit per-lane initialization and the compact rival
then predict the same complete traffic evolution. This task has not shown
that a larger lane model, vehicle identity or discrete order is necessary.

## The traffic picture behind the finding

Reuse AS1's example: both preparations have 0.60 density units in E and
0.55 across A+B. One has A/B loads 0.20/0.35, the other 0.35/0.20.

Before the decision, load the road using the already reviewed recipe at a
common lower speed. It is feasible to make every early merge attempt succeed
in both preparations. Their E traffic then decreases in exactly the same
way. The continuing total increases by that same transferred amount, and all
traffic travels at the same speed. Their complete longitudinal histories
agree, including where traffic is present, density, flow, speed and counts.
Even an E-resolved history and the represented total early transfer agree.

At the decision, however, A is still more crowded in the second preparation.
Under the higher advice, AS1's local receiving test distinguishes them: one
can accept the full early offer while the other initially limits it. The
past did not test that difference in spare receiving. No observation window
was shortened, and no revealing history was removed to create the result.

This construction uses the same preparation law and previously disclosed
loading recipe, specialized to the newly accepted independent lane loads.
It reaches the required uniform initial footprint with an empty terminal
and recovery account. Loading ends at the decision, and its history is
independent of the future advice. It is an analytical existence example,
not a field calibration or a claim that every admitted history hides A.

## Direct answers to the AS2 questions

| Core question | Finding and implication |
|---|---|
| **Can fixed E and fixed A+B really conceal different A/B states?** | **Yes, in a nonempty admitted family.** Distinct positive A/B loads can have identical complete aggregate histories and identical E histories. The concealed split is genuine true state, not a label hidden over physically equal lanes. |
| **Does allowing all lawful history inference remove that ambiguity?** | **Not for this constructed family.** Its whole matched record is identical, so no deterministic filter can identify both states correctly. Level 2 may retain uncertainty or use a disclosed prior; it is not forced to assume A=B. |
| **When would Level 2 be sufficient instead?** | **When an admitted channel identifies A.** Exact E decline during strictly receiving-limited preparation can reveal adjacent load under the known law. Direct adjacent counts or equivalent information also suffice. Such cases must be reported as informative rather than excluded to preserve a positive result. |
| **What extra information matches Level 3?** | **One initial adjacent-load statistic.** E is already known, and total continuing traffic is known, so observing A determines B by subtraction. With the accepted unique forward law and empty initial terminal/recovery history, the compact and explicit per-lane predictors are identical. |
| **What does this establish for the research claim?** | **A conditional information gap, with a compact way to close it.** It establishes neither different best advice nor useful gradients. The whole traffic evolution and TST must still be compared in AS3. |

## What the predictors know

The true traffic always has independent E, A and B initial loads under the
accepted AS1 conditions. Every predictor shares geometry, physical
coefficients, the action interval, the preparation-family description and
the disclosed common loading recipe/past advice. A state-dependent E+A load
is not a common physical coefficient: supplying its realized value would
reveal A and change the information comparison.

| Predictor | Initial information and permissible reasoning |
|---|---|
| **Level 1** | The complete admitted lane-blind longitudinal record and all inference available from it. It remains context for the hierarchy. |
| **Level 2: central rival** | The same record, initial E and combined continuing traffic, and every other actually permitted history channel. It may infer A where the data allow, or retain uncertainty. The construction even matches a stronger E-resolved past. |
| **Level 3** | The same common information with initial E, A and B loads separately known. Future preparation, queues, service and recovery are predictions. |
| **Compact equal-information rival** | Level 2 plus one initial adjacent-lane mass, or an equivalent statistic. In this initial family it reconstructs the same state as Level 3. |

The action remains one advice choice at the decision. Observations obtained
after applying a candidate advice are outcomes, not inputs available before
choosing it. This does not open a feedback controller or an active probing
stage. A richer actual sensor channel must be honored; the proof covers
the stated matched channels, not every conceivable traffic measurement.

## What closes here, and what remains

AS2 supplies the true-state/input distinction, a feasible complete-history
collision, the circumstances that permit inference, and the compact rival's
exact initial-information sufficiency. **No new traffic law or observation
restriction was needed.** The accepted AS1 family and full permitted history
remain intact. The user has accepted this exact information contract.

The subsequent AS3 review examines whether the concealed split changes
complete TST, useful finite advice changes or defined gradients, then
recheck the complete sensitivity protocol and consistency before original
Step 3 closure. Different local receiving alone does not prove those results.
A common optimal advice, an informative history or compact-model equality
is a valid outcome. Strong history/inference, equal-information compact,
model-form and scalar-search rivals remain in scope.

Physical admission remains unestablished; SUMO is optional. No simulator,
installation, traffic rollout or numerical-gradient experiment was performed.
Step 4 remains unopened and the ramp/urban lines closed.

[Matched-history construction, inference and compact-peer proof, PDF](../../synthesis/research_readiness/vsl_as2_information_and_history.pdf)

[LaTeX source](../../synthesis/research_readiness/vsl_as2_information_and_history.tex)

[Channel audit, source reuse and inference boundaries](../../extraction/research_readiness/vsl_as2_history_channel_and_source_audit.md)

[AS1 acceptance and AS2 authorization](vsl_as1_acceptance_and_as2_opening.md)

[Work, exact checks and preservation](vsl_as2_review_work_report.md)
