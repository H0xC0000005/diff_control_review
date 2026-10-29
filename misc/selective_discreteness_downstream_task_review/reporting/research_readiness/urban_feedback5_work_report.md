# Feedback 5: comparison limits, one-step sensitivity and scientific credit

26 October 2026. Current topic: the conclusion of **“Comparison, sensitivity and scientific credit: agreement on principles.”** The response records those principles as agreed, with concrete observation/model/time-accounting questions still open. No implementation phase or component checkpoint is applied.

[Read the response](urban_feedback5_response.md)

[Mathematical companion, PDF](urban_feedback5_information_and_sensitivity.pdf)

[Retained mathematical source](urban_feedback5_information_and_sensitivity.tex)

## Conclusions and their qualifications

UR-G4 gains **Candidate C**, the user's common maximum aggregate information boundary after removing the packet-order distinction. Native rivals may use subsets. Earlier A/B become supporting comparison/witness strategies. Resolution, admitted histories, actual matched records and error margins remain to specify. Failure of a chosen subset-using model is not an information-limit theorem. State-conditioned one-step prediction and autonomous TST prediction have different information protocols; repeated observation assistance must be reported.

UR-G5 now leads with the agreed one-step discharge/next-state response and its composition into complete TST. The response distinguishes current service, a prior-step perturbation and a persistent fixed-allocation change. It corrects the interpretation of the previous state-sequence wording as packet-path gradients, and explains the possible zero direct current TST charge under the inherited left-interval convention. A queue need not imply weak marginal discharge; the binding physical constraint matters. Absolute cycle length is not introduced. The earlier common-horizon recommendation remains conditional; neither horizon nor completion-based treatment is selected by this feedback.

UR-C7-Q1's adjacent causal/source explanation plus a complete source map is explicitly accepted. Exact credit still needs selected laws. Q1–Q4 and the commitment default/deferred retargeting choice remain untouched. The stable inventory has 15 question IDs and now 34 candidate entries. The principle checkpoint can close on these meanings without claiming that the full methodology or detailed comparison is complete.

## Evidence checked and assumptions

The feedback file, current descriptive proposal/decisions/topic guide, question inventory, completeness map and discussion log were inspected. Relevant accepted task/objective contracts, the macro objective code and existing differentiation meaning were checked. No simulator API, traffic-law replacement or numerical experiment is proposed or run.

The mathematical note distinguishes full traffic state from continuous derivative variables, makes the observation projection/history conditional, proves the two-situation prediction-error bound by the triangle inequality, and derives current/previous-step/state-sequence sensitivities from the inherited transition contract. It includes a movement-exclusive neutral service illustration, rather than inventing the unresolved shared-lane/bay law. Matching observations only at one nominal action does not justify supplying unobserved observation sensitivities. No physically realized matched pair, universal macro impossibility, empirical fidelity or useful gradient is claimed.

Two already-reviewed literature anchors were checked against primary sources to correct the broad macro-blockage expectation:

- **T0008:** [author-hosted journal copy](https://attap.umd.edu/wp-content/uploads/2022/05/TRC522.pdf), printed pp. 130–131, abstract/introduction. This bounded check supports existing aggregate lane-group blockage capability; it does not qualify the complete law or a gradient. The publisher page returned HTTP 403; the public author-hosted copy was accessible.
- **T0014:** [official arXiv v3 record](https://arxiv.org/abs/1601.01054v3), abstract; version revised 2 September 2017, with the journal reference recorded there. This checks the aggregate partial-FIFO capability claim, without adopting its entire algorithm or proving this task's response equivalence.

No other search result is used as technical authority. The response links the primary sources near the bounded correction. Matching B3 alone is distinguished from richer-reference validation, and correct internal derivatives from useful control directions.

## Files changed

New files are the response, mathematical `.tex`/PDF pair, this work report and the [document verification result](urban_feedback5_validation.json).

Updated live records:

- [Current principle discussion](../../temp_content/research_readiness/comparison_sensitivity_and_credit_proposal.md): Candidate C, local-first explanation, accepted credit and concrete unresolved options.
- [Question inventory](../../extraction/research_readiness/urban_open_question_register.md): stable IDs, the new G4 candidate, refined G5/C5 and C7 status, and corresponding evidence descriptions.
- [Decisions](../../temp_content/research_readiness/review_decisions.md), [topic guide](../../temp_content/research_readiness/review_plan.md) and [discussion log](../../temp_content/research_readiness/review_dialogue.md): agreed principles, checkpoint name, qualifications and remaining questions.
- [Completeness/topic map](../../extraction/research_readiness/urban_review_completion_and_work_map.md): strengthened comparison/sensitivity explanations under the accepted principles; related-question links and report budget retained.
- [Overview](urban_readiness_overview.md) and [gap explanation](urban_vsl_standard_gap_explainer.md): present status and the updated connection to the specification standard.
- [Earlier comparison/sensitivity evidence notes](../../extraction/research_readiness/urban_categories345_evidence_notes.md): a front notice identifies the superseding feedback-5 interpretation while retaining the older technical record.
- The feedback inbox receives only the allowed `(answered)` suffix on the feedback-5 heading. No user wording is edited.

Root instructions/context/roadmap, approved implementation plans, M2 contracts, code/tests/configs, scientific results, VSL artifacts and historical phase-named review records are preserved. No earlier validation snapshot is overwritten.

## Build commands and verification

Before edits, `/tmp/urban_feedback5_before_20261026.json` recorded 768 existing file hashes and relevant original text. Documentation edits use `apply_patch`; the feedback token is a byte-level replacement of its heading. Inspection uses `rg`, `sed`, `nl`, read-only git commands and Python standard-library checks. The primary-source check uses the web tool as described above.

The local toolchain is pdfTeX 1.40.25, TeX Live 2023/Debian. Two successful passes of the final source build the PDF:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_feedback5_latex_20261026 misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_feedback5_information_and_sensitivity.tex
```

Run that command twice, then copy the PDF from the build directory beside the retained source. Aux/log files stay in `/tmp/urban_feedback5_latex_20261026`. An initial optional-font request failed because `lmodern.sty` is absent; the source now uses installed standard Computer Modern fonts. A long line was rewritten. The final LaTeX log has no warnings or overfull/underfull boxes. No package was installed and no mathematics was omitted.

The four-page PDF is checked with the existing `pypdf` environment at `/home/zpz/miniconda3/envs/differential_sim/bin/python`. A raster preview was attempted, but `pdftoppm` and other probed local renderers are unavailable. Verification therefore covers compilation, page/text extraction and document structure; visual raster inspection is not claimed.

The preservation/link/inventory audit is retained at `/tmp/urban_feedback5_document_check_20261026.py`:

```bash
python3 /tmp/urban_feedback5_document_check_20261026.py
git status --short
```

Document verification passed: 141 local links/cited lines, 15 stable question IDs and 34 candidates, with all 33 earlier candidate explanations retained. The feedback differs only by its allowed heading token. Of 768 snapshotted files, 758 are byte-identical; ten are the declared live-document/feedback edits, with five new artifacts. Scientific relationships, unrelated questions, settled traffic principles, historical records, root/implementation authorities and the report budget are preserved. No outside change was detected. The four-page PDF matches the clean LaTeX build and has extractable text on every page, checked with pypdf 6.15.0. No traffic simulation, finite-difference/autograd experiment, optimization, SUMO run or scientific acceptance test is executed. Document verification is not evidence of forward or gradient fidelity.

## Remaining scientific questions

The comparison needs its precise aggregation/resolution/history and native model choices, actual matching/sufficiency evidence and margins. The traffic model still needs the coupled allocation/access/service law and its regular local response. The time account needs a concrete horizon/endpoint treatment, with nonclearance and event boundaries handled honestly. Exact source credit and richer-evaluator usefulness remain evidence work. These questions stay within their scientific topics; this response does not start the next model study or authorize implementation/experiments.
