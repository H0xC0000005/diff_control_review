# Weekly review deck — source and production note

Date: 2026-09-11

## Artifact

- `weekly_reviews_and_downstream_task_20260911.pptx`
- Reproducible generator: `generate_weekly_review_deck_20260911.py`
- Rendered equation assets: `weekly_reviews_20260911_formulae/`

## Interpreted request

The deck introduces the week's scientific content from the baseline/literature-positioning review through the current downstream-task review. It deliberately emphasizes concepts and contracts rather than progress reporting. The downstream task is described as near-final but not closed.

The deck contains exactly two boilerplate slides and sixteen substantive slides. It uses a white background, Calibri, 32 pt substantive titles, an 18 pt minimum for editable text, basic geometric diagrams, and rendered mathematical notation.

Amendment: the three-component slide now names the literature anchors and distinguishes what they establish: individual/event order as a forward precedent; movement/partial-FIFO restrictions without exact head order; and lane blockage, overflow, physical queues, and allocation. This was incorporated into the existing three-column slide without increasing the slide count.

Second amendment: the baseline-ladder slide now identifies the closest literature-defined model/task precedents, the adoption mode, and the controlled scientific question for B0, B1, B2, B3, and the R1/R2 references. It distinguishes equation transcription, project-owned composition, bounded reference reproduction, and direct SUMO reuse. This was incorporated without increasing the slide count.

Second amendment: each column now distinguishes the literature precedent from the project's evolution of it. Order is adapted into a continuous-mass semantic ledger; restriction concepts are modified and coupled to ledger-conditioned accessibility; and established storage/lane effects are adopted locally and coupled to the aggregate LTM. The slide explicitly locates the potential novelty in the selective composition and matched derivative/usefulness test, not in any ingredient alone.

## Source mapping

- Novelty, gap, claim safety, and contribution: `../selective_discreteness_literature_review/synthesis/novelty_gap_report.md`
- Model families and three-component positioning: `../selective_discreteness_literature_review/synthesis/model_taxonomy.md`
- Baseline ladder: `../selective_discreteness_literature_review/synthesis/baseline_map.md`
- Downstream family and scope: `../selective_discreteness_downstream_task_review/synthesis/task_taxonomy.md`
- Scenario variants: `../selective_discreteness_downstream_task_review/synthesis/primary_green_allocation_suite.md`
- Formal task, derivative contract, and gradient paths: `../selective_discreteness_downstream_task_review/synthesis/experiment_formulation_formal.tex`
- Baseline coverage and fairness: `../selective_discreteness_downstream_task_review/synthesis/baseline_realization_matrix.md`
- Literature adoption and engineering affinity: `../selective_discreteness_downstream_task_review/synthesis/literature_adoption_matrix.md`

## Build and checks

Build command:

```bash
MPLCONFIGDIR=/tmp/dmm_mpl_config XDG_CACHE_HOME=/tmp/dmm_xdg_cache /home/zpz/miniconda3/envs/differential_sim/bin/python misc/slides/generate_weekly_review_deck_20260911.py
```

The generated package was reopened with `python-pptx`, checked for an 18-slide total and an 18 pt editable-text floor, and passed `unzip -t`. LibreOffice is not installed in this environment, so no independent rasterized visual inspection was available; layout was checked structurally from dimensions and text bounds.

## Status boundary

This communication artifact does not close T6, approve implementation, or alter any scientific decision. It reports the current review contract and explicitly retains implementation-coupled calibration and exact operator derivatives as open work.
