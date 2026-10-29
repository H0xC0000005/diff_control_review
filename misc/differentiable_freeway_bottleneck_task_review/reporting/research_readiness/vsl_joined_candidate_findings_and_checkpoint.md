# A joined VSL candidate now has an information test and complete accounting

**Later analytical qualification complete, 2026-10-21.** The user approves
the methodology-only plan; VC1–VC3 are executed and delivered at JM1.
The source joins, complete accounting and sensitivity fit the same model.
A new analytical addendum gives finite regular advice intervals and the
free-flow zero-information limit. No new component or methodological
choice is required. Existing model equations and JQ1 evidence below are
unchanged. Numerical/physical and positive-action claims remain unproved.

[Current findings and JM1 checkpoint](vsl_methodology_review_findings_and_gate.md)

[Approved analytical plan and completion status](../../synthesis/research_readiness/vsl_joined_candidate_methodology_review_plan.md)

2026-10-21. **LF1 and LF2 are selected. The remaining bounded qualification
pass is complete at a review checkpoint. No new methodological fork is
opened.** The result is a conditionally complete elementary member and an
evidence contract, not a successful traffic/gradient experiment or automatic
replacement of the accepted report.

## The big picture

We can now describe one coherent task. A finite cohort occupies a short
three-lane approach. E ends at the downstream line; A and B continue through
two exit outlets. Drivers attempt to move over as they approach the end,
and continuing traffic can also redistribute between lanes. Traffic that
cannot change lanes may keep advancing in its present lane. At E's end it
must obtain A's receiving service or wait.

One common speed advice regulates the cohort. Subraveti supplies the
lane-density and incentive framework. The selected Han budget determines
how much traffic can move and how much receiving service is available;
the selected conservative allocator shares those quantities. **No new
physical traffic mechanism was needed in this pass.** The new work concerns
the task's boundaries, information comparison, full-cohort objective and
sensitivity of that objective.

The mathematical specification keeps the traffic model in its first two
pages; the remaining pages provide the qualification arguments. The local
conventions below make this a concrete review member. They are declared
defaults for this candidate, rather than claims that every detail appears
verbatim in the principal paper or that an experiment configuration is frozen.

## What the qualification establishes

| Core question | Direct finding |
|---|---|
| **Can the selected components form an admissible model?** | Yes on the common-FD member: H supplies nonnegative traffic/space budgets; the selected allocator respects them and conserves mass. Initial, exit and lookahead conventions are now explicit. Source calibration and wave-propagation equivalence do not transfer. |
| **Does concealed A/B loading still matter?** | Yes for realized service and the next aggregate state. Two root initializations with the same E profile and the same A+B profile give different E service and total exit flow under the same advice. |
| **Does this prove different useful speed advice?** | No. Different service is not a proof of different best actions or useful gradients. The full-cohort action-value question remains an empirical/analytical test, with zero information value allowed. |
| **Is full lane detail necessary?** | Not established. In the two-state diagnostic, one extra adjacent-lane density identifies the hidden mode completely. This is a strong mandatory rival, not an inconvenience to exclude. |
| **Can all unfinished traffic be counted?** | Yes for the closed finite cohort. It eventually enters a regime in which all movements receive service; its entire remaining population-time then has an exact expression. No mass is deleted at a numerical cutoff. |
| **Can the whole objective be differentiated?** | Yes locally on regular finite branch traces, including the exact remaining-time term. Native incentive switches still prevent a blanket smoothness claim. No AD or finite-difference agreement has been demonstrated. |

## Why the A/B example matters

The two initializations place the same ending traffic near the lane drop.
They also contain the same total continuing traffic at every road position.
Only the division between A and B changes: the last cell has densities
60/90 in one case and 90/60 in the other. The preceding row has the same
nominal critical density in all three lanes in both cases. These are prescribed root
initial states, not two histories asserted to have identical observations.

Under identical 60 km/h advice, the first case gives E **877.5 veh/h** of
merge service and the second **1,072.5 veh/h**. Their total exit flows are
**4,005 versus 4,350 veh/h**. The reason is the combination of state-dependent
receiving and continuing traffic's lane-changing requests. In particular,
the far lane can compete for A through redistribution. The contrast is not
captured by saying only that a busier adjacent lane must always be worse.

Because the total initial mass is the same, the different exit flows also
produce different next-step total remaining mass. Thus E plus A+B is not
an exact closed state for predicting this model. This example uses actual
source incentive values on their congested branch, the selected H budgets
and the selected allocation law; it does not merely posit arbitrary
incompatible movement requests.

The distinction is visible in aggregate flow after the update. **Concealment
is therefore not absolute.** The elementary member selects one constant
advice at the reset decision, before those future observations exist. If
pre-decision histories or later feedback actions are added, include them
for every eligible controller and reassess what remains hidden. Do not
transfer the snapshot result to a history-aware claim without that check.

The witness is specific to the selected redistribution and allocation law.
That law need not maximize unrestricted total flow, and its preference
sequence contributes to the contrast. This is not traffic-law-independent
or empirical evidence that every real lane drop has the same information
effect. The example does not rely on how the missing E lookahead is averaged:
its final E movement is compulsory, and both continuing origin lanes are
on the source's congested branch.

## How complete accounting becomes simpler

Continuous mass may approach zero gradually, so “simulate until exactly
empty” is not a sound general stopping rule. Conversely, discarding the
small residual can bias the speed comparison.

Here a simpler exact solution is available. Once the entire remaining mass
falls below a fixed, geometry-derived threshold, all densities are low and
every receiving budget can accept all requests. Lane changes still occur,
but they no longer delay anyone. Every mass unit advances through each
remaining cell at the same advice-dependent rate. Its mean remaining
time in this discrete traffic model is therefore the remaining cell distance
divided by the advice. This gives the exact future population-time.

The proof also establishes that the finite initial cohort reaches that
regime. It uses forward progress on the finite road and strictly positive
service, even if the native lane-incentive modes change abruptly. This is
not a claim of exact finite-time emptying. It is not a result for continuing
external arrivals, a blocked downstream road or zero permitted advice.
Nor does the old claim that E cannot re-form a queue transfer: traffic can
arrive again from upstream cells in this spatial model.

The objective counts remaining population-time from the decision until all
mass exits at the lane-drop boundary. Any travel already completed before
the initialized episode is action-independent and is outside this remaining-
time objective. No downstream recovery or travel after that boundary is
quietly counted or claimed. The common free-exit boundary is an explicit
task assumption, following the earlier preference for completion at the choke.

## Scope and local defaults made explicit

The concrete member uses a 1 km approach split into ten 100 m cells with
6 s updates. Nominal free speed is 60 km/h, backward wave speed 20 km/h,
jam density 150 veh/km/lane and maximum capacity drop 10%. The once-chosen
common advice lies between 30 and 60 km/h. These are review defaults derived
from the existing illustrative FD, not site calibration or a chosen positive-
result parameter search.

The cohort is initialized inside the road, with no subsequent external
arrivals. The downstream A/B outlets are free boundaries with zero-density
ghost values; their shared allowances still respond to the last A/B cell
through H. All adjacent moves remain permitted while their receiving lane
exists; at the end only E-to-A is available to E. The model adds no downstream
spatial recovery zone.

Density preferences retain the principal source's displayed additive
incentives. The same-author 2:2:1 lookahead weights are used. At the end of
E, missing physical cells are omitted and the remaining weights renormalized;
no fictitious jam or traffic stock is inserted. The congestion keep-right
setting is the source's allowed zero choice. The free-flow keep-right,
route and courtesy rules, zero-mass handling and outlet conventions are
fully specified in the mathematical note and source audit. They remain
declared local adaptations/conventions, not inherited empirical validation.

## What the verification must compare

The information ladder remains link/row aggregate; E plus A+B; and separate
lane states, all at matched spatial locations. Use the same plant, feasible
advice and complete objective. Add the one-statistic rival, and allow a
model-aware aggregate controller to use the known distribution of hidden
states. Do not attribute model-law differences to information.

Separately compare gradient-based decisions with equal-information bounded
scalar search, as well as maximum-advice/no-control. This is deliberately
only one scalar action, so search is a demanding baseline. A finite search
is not automatically a certified global optimum. Neither an internal loss
decrease nor a nonzero derivative establishes usefulness. The exact tail
must be included in both the objective and its derivative.

Native lane-incentive branches can still change abruptly. On a regular
trace, propagate sensitivities through the finite update sequence and the
exact tail. At branch boundaries, report directional/finite perturbation
behavior; do not silently smooth the traffic law. This fixed-time-step
formulation does not import the old continuous-time saltation calculation.
Its derivative concerns the discrete evaluator actually defined here.

[Prospective comparison and derivative-evidence contract](../../synthesis/research_readiness/vsl_joined_candidate_verification_contract.md)

## Review position and stopping point

**The source-join qualification block is complete for this declared member.**
It now has a complete conditional forward definition, a same-observation
service witness, complete population-time accounting and a regular-branch
sensitivity contract. The final mathematical/member conventions are delivered
for review at checkpoint **JQ1**. This is a confirmation checkpoint, not
another newly opened choice between traffic stacks.

Remaining uncertainty concerns what the task will actually demonstrate:
whether useful advice differs, whether a compact statistic suffices beyond
the diagnostic pair, whether computed gradients are correct/useful and how
well this adapted model represents traffic. Those results are not filled in
by the review. There is no numerical or physical admission, and no claim
that this is the globally simplest possible backbone.

The accepted compact report and original Step 4 remain closed and unchanged.
This is the subsequent simplification branch's qualification result, not
retroactive closure of any historical pending gate. No new implementation,
experiment, SUMO requirement or urban work starts. The user's subsequent
scope clarification and completed analytical review are recorded above.
The current checkpoint is user review of the JM1 findings; future numerical
validation remains outside that review's closure criteria.

[H selection and exact scope](vsl_congestion_selection.md)

[Complete model, information witness, accounting and sensitivity — PDF](../../synthesis/research_readiness/vsl_joined_candidate_contract_and_qualification.pdf)

[Sources, global assumptions and local conventions](../../extraction/research_readiness/vsl_joined_candidate_sources_and_assumptions.md)

[Work record and checks](vsl_joined_candidate_work_report.md)
