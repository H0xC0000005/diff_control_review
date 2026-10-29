# Feedback 1: audit of the VSL starting model

Date: 2026-10-12. Status: **Requested starting-point audit complete; no model
replacement selected.** This answers feedback 1 before further review execution.

## Main finding

The traffic idea is clear: if much traffic still needs to leave the ending
lane, a lower common speed may buy preparation time and reduce difficult
merging at the narrow exit. That benefit has to exceed the extra travel time
paid by everybody. Retaining the amount of unfinished merging may therefore
change the useful speed perturbation.

We have a fully defined **conditional analytical model** of this tradeoff.
We do not yet have a fully justified, paper-ready applied lane-drop model.
The distinction matters: refining a missing implementation detail cannot supply
the physical justification of the tradeoff. The next methodological burden is
to qualify that joined mechanism as an elementary traffic task, not to keep
adding components until the pipeline becomes executable.

Your feedback does not show a fundamental misunderstanding. Two possible
readings of the outline do need correction. Literature support for its
ingredients is not equivalent to adopting a complete published model; and
the current framework has not been shown to lie outside established VSL models.
Much of it is already covered, including by continuous lane-aware models. Its
precise information/gradient comparison remains to be qualified.

## 1. Component-level recap and completeness

The forward chain is:

**fixed population and preparation → common speed response → travel and
conservative preparation transfers → unfinished merging at the choke → finite
receiving and departures → complete traffic time.**

Initial information determines what each predictor can initialize. Derivatives
and independent control evaluation interrogate the whole chain; they are not
additional traffic components. The current analytical sequence has one decision,
one preparation interval and one subsequent service interval. It is not a
streaming network rollout or a feedback controller.

| Component | Current input, function and output | What is actually complete |
|---|---|---|
| 1. Geometry, population and initial preparation | Fixed permanent three-to-two drop; one zone; finite total mass split between the ending lane and symmetric continuing group | Exact analytical scenario. No admitted finite release profile, spatial density distribution or traffic-domain calibration |
| 2. Common action and realized response | One bounded constant common speed advice; ideal response sets the traversal speed | Exact conditional action mapping. Compliance, acceleration and congestion-constrained speed are not included |
| 3. Longitudinal propagation | Common zone length and speed determine a common traversal duration and synchronized choke handoff | Exact travel-time reduction. No spatial LTM/CTM update, finite road storage or backward congestion-wave model |
| 4. Mandatory preparation transfer | Ending mass declines at a constant fractional rate per unit elapsed time; exactly the same mass enters the continuing group | Conservative, explicitly specified exponential member. No calibrated opportunity law or admitted density/receiving-dependent replacement |
| 5. Preparation receiving conditions | Target receiving is assumed nonbinding while traffic prepares | A regime assumption, not an implemented finite-receiving operator or an established physical bound |
| 6. Choke receiving and departure allocation | Remaining merge mass consumes extra receiving work; fixed finite work rate and proportional homogeneous batch service produce departures and final clearance | Exact conditional service law. Transient supply, spatial spillback and alternative service priority are not covered by the certificate |
| 7. Objective and terminal treatment | Count all cohort travel and service time until complete exit; total time or its fixed-mass mean | Complete inside that batch model. Its convenient mean-service expression is not valid for arbitrary arrival/allocation laws |
| 8. Observer and comparator initialization | Aggregate history alone; the same history plus initial ending-lane mass; equivalent explicit grouped state | Conditional history collision and exact scalar compression. Native reachability, scalar measurement and one concrete strongest aggregate predictor remain unqualified |
| 9. Sensitivity and decision evidence | Differentiate the physical common speed while preparation and labels remain fixed; test feasible perturbations | Accepted analytical action/gradient result. No AD implementation check or independent traffic-gradient evaluation has occurred |

This is not a pipeline of placeholder equations: components 2–4, 6–7 have exact
equations under the stated assumptions. Conversely, those exact equations do
not imply that the omitted spatial or behavioral interactions are negligible.
Do not read a full LWR/LTM backbone into the word “propagation” in this kernel.

The grouped model also does not retain discrete order. With fixed total mass
and homogeneous parameters, initial ending-lane mass determines the continuing
mass and its subsequent evolution. The scalar-augmented model can reproduce the
grouped model exactly. That is the correct minimum-information finding for
the current member, not a reason to make the task more complicated.

[Exact inherited equations and physical derivative](../../synthesis/research_readiness/vsl_successor_kernel_note.pdf)

[Accepted S13 result and limitations](../s13/s13_99_m2_certificate_sprint_closure.md)

## 2. Literature backing and what is already covered

“Adoption” needs three distinct meanings here: a borrowed traffic structure,
an exact published equation or algorithm, and a task-specific adaptation.
The current kernel mainly uses the first and third. Its information/action
certificate is an original review deduction, not a result attributed to the
component papers.

| Component or flow | Literature basis in the records | What was reused; what was not established |
|---|---|---|
| Lane mass conservation and mandatory transfer | Subraveti et al., FB0030, equations 1–4 and 6–22; Carey et al., lane/commodity accounting | Borrowed conservative lateral-flow structure and mandatory-lane motivation. Neither whole published system was transcribed into S13 |
| Common VSL at the permanent drop | Zhang et al., S06-S3; common-limit field studies in S06 | Domain and actuator precedents. They do not establish immediate ideal compliance or a constant transfer response |
| Finite receiving, extra spacing and allocation | Carey et al., §§4–5, gap factor and rule R2; alternative source priorities | Borrowed demand/receiving and spacing interpretation. S13's separate homogeneous batch stage is a reduction, not the complete source algorithm |
| Aggregate VSL and changing capacity | Jin–Jin; Wei–Han–Wang; METANET VSL/MPC and response literature | Established strong simpler explanations and control rivals. Aggregate models need not have fixed service or omit speed history |
| Complete traffic-time outcome | S13's explicit accounting; related source travel-time/origin-waiting objectives; closed urban contract | Consistent scientific comparison principle. The batch time formula follows the chosen departure law, not a universal VSL objective identity |
| Observer equality, distinct preferred speeds and analytical directions | Conditional S05/S13 construction and deductions | Accepted result for this member. No source jointly supplies its exact observer, transfer, service and derivative comparison |

The primary recheck confirms that Carey models mandatory demand and competing
finite receiving with several priority rules. Those are established components,
not a newly invented mesoscopic mechanism.
[Carey et al., author manuscript, §§4–5](https://eprints.whiterose.ac.uk/id/eprint/77315/7/Carey%20et%20al%202013_with_coversheet.pdf)

Wei–Han–Wang retains aggregate cumulative counts and speed-limit cohort effects,
with traffic-state capacity drop, while excluding individual lane-changing
behavior. It is a serious aggregate rival; service dependence alone does not
establish the need for additional lane information.
[Wei–Han–Wang, publisher methodology](https://onlinelibrary.wiley.com/doi/full/10.1111/mice.13492)

The local FB0030 primary pages likewise show lane conservation, density-dependent
transfer incentives and receiving restrictions. Its route incentive depends on
distance to the lane end. That supports auditing the adaptation; it does not
make S13's constant rate a faithful whole-model transcription.

[Accepted source-to-equation audit](../../extraction/s13_m2_source_to_equation_audit.md)

[FB0030 equation-level study and branch cautions](../../extraction/n2_source_studies/FB0030.md)

[Nearest-work screen, including VSL-gradient predecessors](../../extraction/research_readiness/vsl_successor_baselines_and_evidence_gaps.md)

### The defensible gap is narrower than “existing VSL models cannot do this”

An observer restricted to two identical aggregate histories cannot condition
its initial choice on their different hidden ending-lane fractions. That is
S13's conditional information limitation. It applies to an observation contract,
not to every model called macroscopic. A continuous aggregate model augmented
with the sufficient statistic defeats any claim that full lane resolution is
needed for this member. Established lane-aware models may already retain the
relevant information as well.

The still-open applied question is whether the minimum augmentation improves
prediction of independently useful common-speed changes after strong aggregate
and lane-aware alternatives are fairly specified. Existing VSL control and
VSL-gradient research rule out novelty from the actuator, differentiability or
optimization label alone. Conversely, different action/observation/objective
contracts in a source do not prove that the precise proposed comparison is
already answered. That needs a bounded comparison audit, not an absence claim.

At present, the kernel is defensible as a transparent verification example.
Publication novelty and externally useful gradients remain open claims. If the
eventual comparison is established already, its verification role can still
be stated honestly; a revised paper-contribution claim needs explicit discussion.

## 3. What needs revision or qualification

The first priority is the **speed → realized transfer → receiving/time** join.
Three simplifying assumptions currently make it work together: more elapsed
time gives more completed merging; early transfers encounter no binding
receiving restriction; remaining late transfers increase service work. Each
has traffic motivation, but the sources have not jointly validated that reduced
chain. This is the main methodological limitation, not an unfinished software
interface.

| Priority | Required refinement | Why it matters; scope boundary |
|---|---|---|
| First | Ground the action-to-transfer law | More time is not automatically more completed merging. Urgency can depend on distance, while opportunity depends on target traffic. Explain why the admitted common-speed change alters realized completion, rather than merely relabeling the travel clock. Retain the exponential as the accepted reference; do not choose a new law here |
| First, jointly | Justify preparation receiving versus choke receiving | Early merging is not modeled as causing additional interaction delay in S13. Its traversal time is counted, so this is not an accounting error inside the kernel. For an applied model, justify why preparation remains nonbinding while the choke binds, or use a sourced receiving law and count its effect. Moving merge work upstream is not automatically a whole-system saving |
| First, jointly | Audit service allocation and departures | A receiving-work factor does not specify mean delay by itself. Show that proportional co-clearance is appropriate for the intended regime, or compute full time under a declared alternative. Do not replace total time with clearance duration to avoid the priority issue |
| Within that same join | Justify the continuing-group reduction | At a physical three-to-two drop, the ending lane directly merges into its adjacent continuing lane. Treating both continuing lanes as one shared receiving resource requires a stated regime or reduction; common speed does not guarantee balanced receiving. Add an imbalance statistic or fuller lane state only if a concrete admitted case defeats the compact closure |
| Next, only if necessary | Qualify the cohort/arrival reduction | The synchronized batch avoids staggered arrival, finite road storage and spillback. State its physical regime and evidence limits. A small finite-arrival model may become necessary for an applied test, but it is a scientific scope change, not an automatic addition |
| Alongside the core | Specify observations and concrete strong rivals | Distinguish initial observed ending mass from inferred mass; retain the conditional full-history claim; identify an actual aggregate prediction law. Never provide future reference corrections or tune separate hidden-state capacities on held-out outcomes |
| After the core survives | Complete the derivative/evaluator contract | Stable-regime analytical/AD/difference checks and common independent perturbation evaluation need the admitted dynamics first. Evaluator availability cannot substitute for mechanism validity |

A pure prescribed completion schedule depending only on position, with no
speed-sensitive opportunity, would not improve preparation merely because travel
is slower. That is a useful analytical negative control, not a claim that the
published location-based demand laws have no speed effect: desired changes and
realized, receiving-limited changes are different. Similarly, slower speed can
change density and available receiving in ways the constant-rate member omits.
These are reasons to qualify the join, not new laws adopted by this audit.

Keep continuous mass, paired conservation, common action, complete time and
scalar compression as the reference contracts. Do not add identity/order,
heterogeneous compliance, acceleration kinetics, microscopic gap acceptance,
multiple controls or network propagation merely to make the result stronger.
Such additions have literature, but their existence does not make them needed
for this verification. A concrete failure of the admitted compact model must
precede an expansion.

[Living candidate record for core-model qualification](../../synthesis/research_readiness/vsl_feedback1_core_model_candidates.md)

## What changes in the review logic

The opening plan already named most of these limits, but arranged them primarily
as future work packages. This audit makes their scientific priority explicit.
Before proceeding deeper, one short argument must establish why the complete
reduced traffic mechanism is credible enough for the intended elementary task.
If that argument requires an independent model-construction program, stop and
return to task selection rather than turning every local gap into a new stage.

Every subsequent local study should say which uncertainty it resolves, how the
answer affects useful speed decisions or minimum information, why the simplest
existing rival is insufficient, and what result would end or narrow the study.
A locally plausible equation is not, by itself, a reason to continue construction.

The provisional continuation is therefore to retain S13 as the exact reference
and qualify the response/transfer/receiving reduction against one principal
source. It is not yet a decision to adopt a new model. The proposal and methods
outline are synchronized with this priority; the approved S13 and urban results
are unchanged. This requested audit ends here, before law selection or broader
review execution.
