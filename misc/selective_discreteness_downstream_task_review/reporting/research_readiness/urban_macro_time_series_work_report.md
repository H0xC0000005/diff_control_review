# Original-series access: clarification work record

26 October 2026. Current topic: the interpretation of UR-G4's macro information boundary. Agreed clarification: a macro rival may read the original fine-grained series through its declared conversion or state estimator. This refines Candidate C; the principle checkpoint remains settled. No candidate, implementation phase or additional approval checkpoint is added.

[Read the clarification](urban_macro_time_series_clarification.md)

## Changes and their meaning

The earlier statement that an autonomous comparison must evolve without later observations was too restrictive when applied to all legitimate TST comparisons. The records now allow observation-updated macro models and model-defined summaries of the original series. Representation/dynamics and retained memory determine what information the method preserves; source resolution alone does not. Successful aggregate estimation remains a valid result against the need for full order retention. Exact ordered state retained inside a preprocessor must still be disclosed.

The observation schedule identifies what was observed and predicted, and whether a response is conditional on a fixed series. It does not determine macro status or comparison eligibility. A limit under one fixed projection also does not exclude another admissible macro summary. The mathematical companion's observation section and proof scope are corrected; its local/previous-step/TST derivations remain unchanged.

Updated files are the [feedback-5 response](urban_feedback5_response.md), its [mathematical source](urban_feedback5_information_and_sensitivity.tex)/[PDF](urban_feedback5_information_and_sensitivity.pdf), the [active principle discussion](../../temp_content/research_readiness/comparison_sensitivity_and_credit_proposal.md), [question inventory](../../extraction/research_readiness/urban_open_question_register.md), [decisions](../../temp_content/research_readiness/review_decisions.md), [topic guide](../../temp_content/research_readiness/review_plan.md), [completeness map](../../extraction/research_readiness/urban_review_completion_and_work_map.md), [overview](urban_readiness_overview.md), [gap explanation](urban_vsl_standard_gap_explainer.md), and [discussion log](../../temp_content/research_readiness/review_dialogue.md). This clarification, this work record and its [validation result](urban_macro_time_series_validation.json) are new. Older work reports/verification results remain historical and are not overwritten.

All 15 IDs and 34 candidates remain. The G4 C explanation is refined in place; other candidate explanations and scientific relationships remain. Q1–Q4, the sensitivity/source-credit principles and numerical horizon status are preserved. No feedback inbox, root instruction/context/roadmap, approved implementation plan, M2 record, source/test/config or VSL artifact is edited.

## Sources and checks

Bounded primary checks used [SUMO lane/edge output documentation](https://sumo.dlr.de/docs/Simulation/Output/Lane-_or_Edge-based_Traffic_Measures.html) and [PTV Vissim 2026 measurement documentation](https://cgi.ptvgroup.com/vision-help/VISSIM_2026_EN-DE/en-us/Content/11_Auswertungen/AuswertungQuerschnittsmessungen.htm). These confirm support for aggregate simulator measurements and raw/aggregate measurement records. They are not an adoption/version choice or a survey establishing how often a protocol is used. No other search result supports a technical claim.

Inspection uses `rg`, `sed`, `tail`, Python standard-library reads and read-only `git status --short`. Edits use `apply_patch`. The pre-edit snapshot is `/tmp/urban_macro_time_series_before_20261026.json`, covering 773 files. The document audit is `/tmp/urban_macro_time_series_document_check_20261026.py`:

```bash
python3 /tmp/urban_macro_time_series_document_check_20261026.py
git status --short
```

The existing pdfTeX 1.40.25 / TeX Live 2023 toolchain rebuilds the mathematical companion with two passes, retaining auxiliary files separately:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_macro_time_series_latex_20261026 misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_feedback5_information_and_sensitivity.tex
```

After two passes, copy the generated PDF beside its source. Verification checks the build log, PDF page/text extraction with existing pypdf, local links, candidate/relationship continuity and protected files. Raster inspection is not claimed; the preceding task established that the probed local renderers are absent. No package installation, traffic simulation, gradient experiment, optimization or SUMO/Vissim execution is performed.

Document verification passed: 119 local links/cited lines; all 15 IDs and 34 candidate entries retained, with only G4 C's candidate explanation refined. The local/previous-step/TST mathematics and the response's local-sensitivity section are byte-identical to the preceding version. Scientific relationships and the report budget are preserved. Of 773 snapshotted files, 762 are byte-identical and eleven are the declared live-document/math edits; three artifacts are new. Feedback, root/implementation authorities, historical records and VSL artifacts are unchanged, with no outside change detected. The rebuilt PDF has four pages with extracted text throughout and no LaTeX warnings or box overflows.

## Remaining questions

Concrete models still need their conversion/state definitions, retained history, observation timing and response target. A new-allocation prediction must identify which observations were available before its outcome, and a total sensitivity must account for relevant state/input responses. Those definitions can be developed in the concrete comparison; this clarification does not mandate an unobserved rollout or restart the settled principles.
