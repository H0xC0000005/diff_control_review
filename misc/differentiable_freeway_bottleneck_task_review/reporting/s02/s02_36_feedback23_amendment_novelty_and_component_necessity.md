# S02.36 — Feedback 23 amendment — novelty and component necessity

Sprint: [S02](../../00_review_sequence.md#s02) · Role: 36 feedback amendment · Predecessor: S01 · Gate: N2-UG1.

Date: 2026-09-17. Status: bounded supplementary review/discussion at N2-UG1.
User feedback is preserved. Task plausibility is not route, model or implementation
approval. The approved shared link-level advice actuator and Gap7 constraints remain
unchanged. This is a brief targeted review, not an exhaustive priority search.

## 1. Short answer

The broad ingredients are established. Neither “lane-aware speed control” nor
“a differentiable macroscopic traffic model” is a defensible standalone novelty
claim. The candidate is scientifically plausible, but the previous response did
not yet supply a demonstrated missing contribution. Its strongest potential
contribution is **task-specific information sufficiency for useful control
gradients**, established against strong simpler models.

Lane dependence is plausible, not evidence that every proposed component is
necessary. In particular, lane occupancy does not establish a need for intra-lane
FIFO order, individual vehicles, response groups or microscopic car-following.

## 2. What the brief review establishes

- **Multi-lane control is established:** Roncoli, Papageorgiou and Papamichail
  (2014) formulate continuous lane-resolved traffic control with speed, lateral-flow
  and ramp actions. Their longitudinal/lateral flows are controller decisions;
  this is not endogenous lane changing under shared infrastructure advice.
  [Primary paper](https://skoge.folk.ntnu.no/prost/proceedings/ifac2014/media/files/1657.pdf).
  The [2015 journal extension](https://research.aalto.fi/en/publications/traffic-flow-optimisation-in-presence-of-vehicle-automation-and-c/)
  was checked at institutional metadata/abstract level, not treated as newly
  inspected full methods.
- **Speed-control gradients are established:** Goatin, Göttlich and Kolb
  (2016; online 2015) calculate discrete-adjoint gradients for time-dependent
  speed limits and ramp controls in aggregate LWR networks. Their method uses
  smoothing; it is not a certificate for the exact nonsmooth proposed closure.
  Their discussion also identifies discretization-dependent optimization results.
  [Primary author copy](https://d-nb.info/1265990972/34), section3.2 and section5.
- **Automatic differentiation of aggregate freeway dynamics is established:**
  Poole and Kotsialos (2016) use ADOL-C with METANET for parameter calibration.
  That differentiated target is calibration, not our proposed advice-gradient
  transfer question. This claim was inspected through primary indexed
  abstract/author-repository information; the full methods were not retrieved.
  [Publication](https://doi.org/10.1016/j.trc.2016.07.008).
- The already reviewed [Seliman et al. (2020)](https://doi.org/10.1061/JTEPBS.0000395)
  is closer to the lane-drop application, but its macro/micro optimization
  comparisons change objectives/search and sometimes actions. The existing
  [multiclass discrete-adjoint study](https://doi.org/10.1007/s11081-026-10122-4)
  further limits novelty from “adding classes and gradients”; its inspected
  numerical derivative tests target routing/distribution rather than speed advice.

These establish substantial overlap, not exact equivalence with the proposed
study. In this bounded inspected set, no demonstrated matched-actuator result
settles when omitted lane information changes externally useful advice gradients.
That is an **unresolved candidate gap**, not proof of worldwide absence or priority.

## 3. How to justify additional components

The requirement is not “more detailed traffic looks realistic.” It is “this
information changes the control decision in the specified operating domain.”

1. Establish a strong reduced baseline, including its calibrated mean speed
   response and needed temporal history. Match advice actions, demand, population,
   objective/accounting, horizon and optimization budget. Do not compare a richer
   model against a deliberately memoryless or poorly calibrated straw baseline.
2. Seek physically reachable cases matching the baseline's retained information
   but differing in an omitted variable, initially ending/continuing-lane occupancy.
   If an independent richer reference robustly changes the ranking of the same
   advice perturbations, that representation cannot resolve the distinction.
   This establishes domain-specific information insufficiency, not a universally
   unique lane-state representation.
3. Compare valid smaller/larger representations and conservative component
   ablations. Attribute any control gain separately from calibration, grid,
   action flexibility and optimizer differences. Keep receiving/storage and
   conservation valid: removing a constraint is not a fair simpler model.
4. Check differentiated sensitivities against numerical perturbations internally,
   then test advice direction/ranking and downstream outcomes independently.
   Forward improvement alone is not gradient usefulness; successful autodiff
   alone is neither correctness at event boundaries nor usefulness.

Storage and constrained transfer make a lane-merge candidate physically coherent;
this does not prove that they must be represented as separate extra states.
Speed history may already belong to the strong baseline. Response-group joint
information is conditional on an additional observed failure. Intra-lane order
is deferred unless it explains a residual control-relevant distinction that
simpler continuous information cannot capture.

Continuous aggregate equations also do not automatically certify native
differentiability: flux switches, zero-density divisions and capacity modes need
audit. No smoothing, sampled choices or hybrid sensitivity machinery is approved
by the existence of those hazards.

## 4. Intended contributions — conditional, not already achieved

1. **An information-sufficiency/failure map:** identify where a strong aggregate
   model is adequate and where omitted information changes advice decisions.
2. **Gradient-aware representation selection:** establish which extra information
   improves external action rankings/outcomes, rather than selecting resolution
   solely by forward fit.
3. **A compact deterministic realization and validation contract:** if needed,
   demonstrate that the selected information supports reliable differentiated
   control without moving random probability mass or unnecessary microscopic
   complexity. Existing components may be adapted; invention is not required.

Simply combining known lane dynamics with autodiff is engineering support, not
the proposed scientific contribution. If strong aggregate dynamics suffice, a
substantive bounded sufficiency result may be worthwhile; adding complexity to
manufacture a positive result is not.

## 5. Consequence for the pending gate

Route B remains provisional but becomes explicitly **go/no-go evidence
development**, not a promise of a novel simulator. Its first priority would be
one lane-occupancy omitted-information contrast under the common contract,
plus a closest-predecessor check of that precise claim. Fixed response groups
and intra-lane refinement remain conditional/outside its initial priority.

Before later construction, findings must justify both (a) a genuine
control-gradient information gap and (b) the smallest adequate deterministic
representation. If existing work already answers the precise question, or a
strong aggregate baseline resolves the contrast, revise/narrow or defer the
candidate rather than merely porting it to autodiff.

The gate still asks whether to pursue this bounded hypothesis and its cost.
It does not ask the user to certify missing empirical necessity. No route was
approved by the amendment; no model, calibration or experiment was executed.

Traceability: [new source study](../../extraction/n2_source_studies/feedback23_amendment_predecessors.md),
[claims](../../extraction/n2_claims.csv), [live gate](s02_20_n2_findings_and_gate.md).
