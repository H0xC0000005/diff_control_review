# Freeway bottleneck review — presentation and work note

Date: 2026-09-18. User feedback: `temp_content/feedback/feedback.md`, PowerPoint
request4. Communication artifact only; review remains stopped at S06's current
decision gate. No next review, scenario change or experiment is approved here.

## Deliverables

- [Six-slide presentation](freeway_bottleneck_review_20260918.pptx).
- [Layout preview](freeway_bottleneck_review_20260918_preview.png).
- [Reproducible generator](generate_freeway_review_deck_20260918.py).

The user explicitly waived the usual title/contents boilerplate. Exactly six
substantive slides combine the scientific chain into a colleague-facing story,
not one procedural progress slide per sprint. White backgrounds, Calibri,
32pt titles and18pt main/diagram text; main-text lines by slide are8/7/8/6/8/8.
Slide4's illustrative quantitative plot labels are excluded under the user's
plot-text exception. Diagrams are editable native shapes grouped as single
objects; no bitmap diagram, formula asset, animation or extra slide is needed.
Gate IDs, phase labels, access history and approval decisions are in notes only,
not visible presentation content. Source pointers/qualifications are in the
PowerPoint speaker notes and the source map below.

## Explicit working line — user-requested connective revision

The deck now follows a dependency chain, not a collection of sprint summaries:

1. **Task before resolution.** Define the control decision and strongest baseline
   before deciding what additional traffic state deserves to exist.
2. **Concrete task before comparison.** Common speed advice at a narrowing,
   desired-speed response and complete waiting costs establish a fair comparison.
   This makes the next question what aggregate response/history already explains.
3. **Strong alternatives before necessity claims.** Literature supplies credible
   aggregate alternatives and lane mechanisms, but richer-control gains can be
   confounded by changed actions/objectives. Therefore isolate the information
   difference while keeping retained history, advice choices and objective matched.
4. **Information loss must entail decision loss.** Matching totals is insufficient;
   distinguish unavailable information from poor use of available information.
   Require no common acceptable advice within the tested menu, rather than merely
   different optimal rankings. This calls for an actual hidden-state/advice witness.
5. **The analytical obstruction explains the reference bridge.** Conditional free
   flow can hide lane state, but the fixed-service subcase admits common fastest
   advice. Thus inspect native merge interactions for hidden-state-dependent
   benefits that outweigh slowing delay—not an invented merge penalty.
6. **Mechanisms still require a reachable joint witness.** Reference mechanisms
   do not establish matched-history decision value, and candidate preparation has
   reachability problems. The next review question is whether a reachable contrast
   can preserve the full history contract. Only positive decision-value evidence
   motivates testing the smallest conservative added state and, separately, its
   gradient correctness and independently useful control directions.

The lower diagram on slide1 names this working line; explicit “Next” bridges
on slides2–6 identify why each finding requires the subsequent question. Slide5
also makes the analytical-to-reference hand-off explicit. Speaker notes retain
the conditional assumptions and distinguish illustrative, analytical and
source-supported evidence. This revision changes communication only: no joint
witness, minimum-state result, scientific gate closure or experiment approval
is asserted. Lack of a witness is not a theorem of aggregate sufficiency.

## Semantic/source map

| Slide | Presentation point | Review basis |
|---|---|---|
| 1 | Model-first versus task-anchored methodological design; resolution serves useful control gradients. | [Pre-review principles](../differentiable_freeway_bottleneck_task_pre_review/pre_review_closure_and_handoff.md), section3; [recap](../differentiable_freeway_bottleneck_task_review/01_review_recap_through_s06.md), section1. |
| 2 | Common desired-speed advice at a narrowing; strong aggregate baseline and complete waiting accounting. | S01 scope and S02 task clarification; recap section1. |
| 3 | Established aggregate/lane ingredients do not prove richer information is necessary; changed-action/objective comparisons are confounded. | [S02 findings](../differentiable_freeway_bottleneck_task_review/reporting/s02/s02_20_n2_findings_and_gate.md), sections3–5; [novelty clarification](../differentiable_freeway_bottleneck_task_review/reporting/s02/s02_36_feedback23_amendment_novelty_and_component_necessity.md); [S03 findings](../differentiable_freeway_bottleneck_task_review/reporting/s03/s03_20_rb_findings_and_gate.md). |
| 4 | Equal totals versus equal full history; information loss versus model inadequacy; compare all acceptable actions. | [S04 methodology](../differentiable_freeway_bottleneck_task_review/reporting/s04/s04_20_rb_diagnostic_methodology_findings_and_gate.md). The30 vehicle-equivalent15/15 and5/25 examples are explanatory, not measured data or certified preparations. |
| 5 | Conditional hidden-information construction and restricted fixed-service obstruction; useful slowing needs state-dependent interaction effects. | [S05 findings](../differentiable_freeway_bottleneck_task_review/reporting/s05/s05_20_rb_certificate_findings_and_gate.md) and its formal analysis; S06 native mechanism audit. |
| 6 | Mechanism basis remains credible, but joint information/decision evidence and minimum-state/gradient evidence remain open; contrast must be reachable. | [S06 findings](../differentiable_freeway_bottleneck_task_review/reporting/s06/s06_20_reference_bridge_findings_and_gate.md), [source audit](../differentiable_freeway_bottleneck_task_review/extraction/s06_reference_mechanism_source_audit.md). |

Primary anchors named in speaker notes include Frejo2019 (mean response),
Wei2025 (speed history), Seliman2020 (macro/micro reoptimization confounds),
Chen2025 (lane control but no information-only gradient comparison), Erdmann2015
(native lane-change/speed coupling), and Zhang2023 (regulatory lane-drop evidence
outside the moderate-response contract). No new source review or novelty claim.

## Build, checks and limitations

Build command:

```bash
/home/zpz/miniconda3/envs/differential_sim/bin/python misc/slides/generate_freeway_review_deck_20260918.py
```

Installed python-pptx/Pillow were inspected; no dependency installation or
environment modification. Existing deck style was reused selectively, not its
urban scientific content. PASS: saved PPTX reopened; six slides and no boilerplate;
Calibri/32pt/18pt checks;8-line limit (plot exception above); native group bounds;
conservative font-substituted width/height checks; speaker notes; no procedural
IDs in visible text; ZIP integrity. Initial width checks identified overlong
titles/labels, which were shortened without reducing font size or weakening
the checks. Preview color initialization was corrected and build rerun.

The contact sheet was generated by reading the saved PPTX shape/group transforms
and visually inspected. It uses DejaVu Sans substitution and a limited Pillow
renderer: it is a layout proof, **not** independent PowerPoint/LibreOffice
rendering or certification of identical font behavior. LibreOffice/soffice is
unavailable; no renderer was installed. Full Office layout should be checked
when the user opens the PPTX. Calibri is specified in the actual deck.

Commands: rg/sed for feedback/evidence/style inspection; command-v and Python
module/API/font inspection for presentation tools only; apply_patch for source/
notes/feedback edits; Python generator/validation; view_image for preview;
unzip-t for package integrity. No SUMO/provider check, traffic run, gradient
test or production code/config change. Files created are the four deliverables/
supporting files above; feedback request4 is marked answered using its explicitly
permitted annotation only. The living review dialogue records this task.

Connective revision: changed the same generator, PPTX, preview and this note;
appended the interactive amendment to the existing review dialogue. Rebuilt and
reopened the six-slide PPTX; all layout/font/line/source-note checks passed at
8/7/8/6/8/8 main lines. Inspected the regenerated contact sheet and rechecked ZIP
integrity. The first revised build caught an overlong node label; it was shortened
without shrinking the required font or weakening validation. User feedback was
not edited again. No additional artifact pack or review sprint was created.

Assumptions: English deck, consistent with prior colleague presentations; output
under existing misc/slides convention; six slides rather than extra boilerplate;
recap through S06 remains the current scientific boundary. Remaining risk is
Office/font rendering, plus the existing unresolved scientific information-value
claim. Next allowed action is user presentation review or the existing S06 gate
decision; neither a new scientific sprint nor experiment starts automatically.
