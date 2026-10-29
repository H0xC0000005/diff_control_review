# S13.80 — M2 contract dialogue and decisions

Date: 2026-09-30. Status: G1–G7 closed; M2C-A accepted 2026-10-01.

## User approval

The user judged G1–G5 and G7 to be definition/guardrail/boundary clearance and
approved the complete recommended Candidate A set. The user separately confirmed
G6-A as the methodologically sound aggregate-model behavior under hidden
information and instructed execution of S13 if the open questions were closed.

The closed global contracts are:

- **G1-A:** neutral demand-proportional finite receiving;
- **G2-A:** common VSL enters through the shared longitudinal speed/sending path;
- **G3-A:** exact constructive spatial handoff;
- **G4-A:** an open source-bounded parameter regime;
- **G5-A:** a bounded one-parameter action family including the fastest endpoint;
- **G6-A:** exact observer identity plus a strong aggregate countermodel; and
- **G7-A:** conceptual gradient contract only after decision relevance.

## Contract interpretation used in execution

The common action is represented equivalently by speed or preparation-zone
traversal time. Slower advice increases residence time in a fixed spatial zone.
On the selected active branch, remaining ending-lane mass decays continuously by
paired lateral transfer. Traffic still requiring a lane change at the choke
consumes additional receiving work under the neutral proportional allocation.

The exact pair enters the preparation zone at the decision boundary with the
same aggregate spatial history and total cohort mass but different ending-lane
fractions. Physics and geometry are common after that boundary; no hidden-state
switch changes the model.

## Guardrails retained

- The transfer-rate branch and homogeneous batch service are explicit analytical
  adaptations, not source claims.
- The parameter result must hold on an open inequality-defined regime, not one
  chosen numerical example.
- Fastest advice remains an endpoint of the full continuous action interval.
- Aggregate observers receive identical predecision histories and must use the
  same decision rule at that point.
- Gradient relevance is claimed only inside the conditional analytical model and
  after the useful-action split is established.
- No empirical, calibration, implementation or field-validity claim is added.

## Post-execution semantic and evidence clarification

The user asked how the exponential transfer branch is supported and why one
extreme speed is not a universally best policy. The clarification is:

- the reviewed literature directly supports lane-wise continuous conservation,
  paired mandatory lateral transfer, density/geometry-dependent transfer
  incentives, finite target receiving and extra gap work for lateral entrants;
- it does not directly report or calibrate S13's memoryless constant-rate
  exponential transfer under common VSL. That law is the declared analytical
  specialization obtained when a fixed active branch removes a constant
  fraction of remaining ending-lane mass per unit time;
- common-VSL lane-drop and field sources support the possibility that a shared
  speed changes lane preparation, but report mixed response and do not join that
  response to the same finite-receiving equations or information comparison;
- complete clearance at the slowest advice is not an optimality criterion. The
  S13 objective charges preparation travel time and complete choke-clearance
  time. Slowing has an immediate travel-time cost while its merge-work benefit
  diminishes as ending-lane mass is exhausted; and
- no universal endpoint policy follows. Nonbinding receiving or little residual
  merge demand favors the fastest action, a material merge penalty can favor an
  interior slower action, and only a stronger parameter condition would make the
  slowest endpoint optimal for a particular state.

This clarification does not change G1--G7 or the conditional certificate.
Further literature review or empirical/cross-fidelity evidence is required only
to strengthen the claim from source-bounded methodological possibility to a
traffic-valid transfer law or an operational VSL recommendation. The current
source search supports no literature-wide absence claim.

## Study-sufficiency concern and audit

The user accepted the elementary mechanism role but asked whether S13 and its
extensions can support a study rather than a one-off favorable construction. The
resulting [study-sufficiency audit](s13_35_study_sufficiency_and_extension_audit.md)
finds that S13 is a complete conditional certificate and viable study kernel,
but not a complete representation-necessity or external gradient-usefulness
study.

The decisive limitation is compression: after the decision boundary, the S13
equations need only total cohort mass and remaining mandatory-merge mass. Full
per-lane state is therefore not established as necessary. A defensible
theoretical extension must compare the strong aggregate observer, an
aggregate-plus-merge-pressure statistic, grouped lane state and fuller lane
state; it must also delete causal links and classify a small preregistered family
of transfer/service laws. An applied usefulness claim additionally requires an
independent richer evaluator and implementation derivative evidence.

This audit does not alter the executed certificate or close M2C-R1. It clarifies
that accepting M2C-A would accept the analytical kernel. A broader theoretical
or empirical study would require a separately approved plan.

## Certificate acceptance and future-work boundary

The user accepted M2C-R1 Candidate A and directed that broader extensions remain
future work. S13 therefore closes with M2C-A. The agreed prospective route to a
research-ready task is staged rather than appended to S13: model-family and
minimum-information review; traffic-domain/reference-evaluator admission;
matched gradient-usefulness protocol review; and integrated research-plan
freeze. No stage is opened by this discussion.

## Post-closure explanation of the mean-time objective — 2026-10-02

The user asked for the slide's hanging symbols to be defined, confirmation of
mean versus total system time, and derivation of the objective and speed
derivative. Read Sections 3–6 of the accepted model contract and the certificate
gradient section. No new scientific choice is needed: the proportional
homogeneous fluid-batch assumption already fixes the population-time integral.

The [explanation PDF](../../synthesis/s13/s13_mean_time_and_speed_derivative_explained.pdf)
and [editable source](../../synthesis/s13/s13_mean_time_and_speed_derivative_explained.tex)
give a complete symbol/unit table, paired transfer, receiving-work accounting,
class-specific proportional exit rates, the rectangular-plus-triangular
remaining-population integral, a transparent arithmetic illustration, and the
three-step chain-rule derivative with sign interpretation. They explicitly
distinguish work from vehicle mass, mean discharge time from last-departure
time, and the assumed linear batch from a generic freeway queue. The
illustration is not a simulation or calibrated parameter result.

Corrected slide 8 of the [weekly deck](../../../slides/weekly_freeway_control_review_20261002.pptx)
to display remaining mass as a function of traversal time, define the receiving
work multiplier precisely and name the batch assumption behind the one-half
factor. Expanded its speaker notes and linked the explanation source. Slide 13
now explicitly labels ramp J as total time; fixed-mass normalization would
scale its objective and derivative equally. Generator, notes, vector assets,
previews and validation JSON remain in `misc/slides/`.

Verified the existing latexmk/pdflatex toolchain. Build commands:

    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/s13_objective_explanation_latex misc/differentiable_freeway_bottleneck_task_review/synthesis/s13/s13_mean_time_and_speed_derivative_explained.tex
    /home/zpz/miniconda3/envs/differential_sim/bin/python misc/slides/generate_weekly_freeway_control_review_20261002.py

Copied the built PDF beside its TeX source. LaTeX compilation passes with no
overfull/underfull boxes or warnings in the final log; pypdf confirms three
complete readable pages. Revised deck passes its existing font, line-count,
source-path, text-fit, package/XML/SVG and bounds checks. Slide 8 has six body
lines plus two equation lines, within the declared eight-line limit; its
full-size layout preview was inspected. No native Office/PDF visual renderer
is installed, and previews retain their documented font substitution. No
production change, dependency installation, traffic simulation or numerical
gradient validation took place. S13 remains closed; later VSL work stays
deferred. This explanatory task does not select the ramp observer or advance
its pending gate.
