# Report revision: the formed modeling backbone

**Historical v2 record.** On 2026-10-22 the user requests a source-color and
relationship key. The expanded monochrome PDF/LaTeX below are archived
byte for byte; the original build/verification describe that version and
its original artifact paths. The current pass is recorded in the
[color revision work report](vsl_literature_backbone_review_color_work_report.md).

2026-10-21. **Requested revision delivered; awaiting user reading.**
The analytical review remains complete. This pass improves the presentation
of its selected model; no new methodological choice or scientific run is
opened. Report acceptance and JM1 findings acceptance remain separate.

The user approves removing the former Section 4 and prioritizes explaining
the formed stack: CTM/LTM identity, early and forced merging, and the causal
chain. The budget is now 2.5 main-text pages excluding references. Retain
the literature-first organization, with a shorter comparison and selection
followed by a substantially expanded model section. Use 11 pt main text and
18 mm margins. The final main text occupies about 2.47 text pages; eight
IEEE references follow on page 3. The whole PDF has three pages.

## Files and preservation

- Update the [report PDF, now archived](../../synthesis/research_readiness/vsl_literature_report_versions/v2/vsl_literature_backbone_review_report.pdf)
  and [LaTeX source, now archived](../../synthesis/research_readiness/vsl_literature_report_versions/v2/vsl_literature_backbone_review_report.tex).
- Preserve the [first-draft PDF and source](../../synthesis/research_readiness/vsl_literature_report_versions/v1/README.md)
  byte for byte. Add an archive reading note for its original relative PDF
  link. The first-draft build/verification remain historical evidence.
- Synchronize the package README, selected temporary report structure and
  successor dialogue. Update the old draft work record's links to the archive.
- Add this record, the [final build log](vsl_literature_backbone_review_revision_build.log)
  and [document verification](vsl_literature_backbone_review_revision_validation.json).

## What the reader can now follow

| Report component | Traffic explanation and source/formulation alignment |
|---|---|
| Physical model and state | A lane-resolved CTM-type road with physical density/storage cells and the selected Han extended first-order budgets. No LTM link or separate point queue is appended. The diagram shows stocks → desires/budgets → shared movements → new stocks. |
| Sending/receiving, Eqs. (1)–(2) | Reproduce the selected Q/D/R laws, fixed FD constants and boundary ghosts from sections 1–2 of the [joined contract](../../synthesis/research_readiness/vsl_joined_candidate_contract_and_qualification.pdf). Explain advice-limited sending, state-dependent discharge, downstream space and congestion-wave service. Every receiver has one allowance for all straight/diagonal arrivals. |
| Early desires, Eq. (3) | Retain the Subraveti density/incentive framework, thesis 2:2:1 lookahead and declared endpoint conventions. Explain the 750 m route urgency, possible density-driven attempts farther upstream and cooperation. E traffic becomes ordinary receiving-lane traffic. Full bias branches remain in the unchanged companion. |
| Realization and choke, Eqs. (4)–(6) | Reproduce joint normalized requests, equal-priority capped sharing, one own-lane fallback and old-state conservation. Explain that final E has only the A outlet, so it must merge or wait under the same service rule. Fixed priorities do not fix the realized merge fraction. Shared service and retained density cause the interaction; no speed-mismatch/recovery meter is added. |
| Objective and derivative, Eqs. (7)–(8) | Substitute the already defined V(n)=hᵀn into the existing exact-residual and full-derivative formulas. This is the same objective, not a new terminal approximation. The fixed K* and regular-branch condition stay next to the derivative. |
| Information/control comparison | Keep the same physical model under E+(A+B) versus per-lane observations, the diagnostic one-statistic observer, lawful history inference, maximum advice and equal-information scalar search. These are task definitions, not claims of achieved advantage. |

The source foundation is the already completed
[literature comparison](vsl_published_backbone_findings.md),
[source/interface audit](../../extraction/research_readiness/vsl_methodology_review_source_and_interface_audit.md)
and [assumption record](../../extraction/research_readiness/vsl_joined_candidate_sources_and_assumptions.md).
No new source search or primary-paper reading is claimed in this writing
pass. No mathematical or traffic-model review is reopened. The broad
evidence-limit section is removed from the compact report, while its
[findings](vsl_methodology_review_findings_and_gate.md) and
[analytical qualifications](../../synthesis/research_readiness/vsl_methodology_review_analytical_addendum.pdf)
remain unchanged. No global simplicity, positive action gap, useful gradient
or physical validation is claimed.

## Build, document checks and results

Read the live report, selected structure, joined contract, analytical
addendum and global assumptions with `sed`, `cat` and `rg`. Check repository
status with `git status --short`. Use `apply_patch` for text and Python file
tools to archive the prior PDF/LaTeX. No dependency installation occurs.

Build twice after the final source edit:

```bash
pdflatex -interaction=batchmode -halt-on-error -file-line-error -output-directory /tmp/vsl_literature_report_revision2/latex /home/zpz/repos/diff_minimal_meso/misc/differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_literature_backbone_review_report.tex
```

Copy the final PDF beside the `.tex` and preserve the log. A TeX save-position
marker records where main text ends, before the references. Relative to the
18 mm text frame, two full pages plus the occupied fraction of page 3 are
2.4747 pages, within 2.5. The references are not counted. Check extracted
page contents, equation/reference labels, embedded fonts, main-text size,
PDF/Markdown links and build messages. No raster rendering is claimed;
this environment lacks an available PDF rasterizer. These are document
checks, not numerical traffic validation.

Before-edit snapshot:
`/tmp/vsl_literature_report_revision2/before.json` (574 existing files).
Run the final checks with:

```bash
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_literature_report_revision2/document_checks.py
git status --short
```

Checks pass: three PDF pages, main text within 2.5 pages, eight equations
and eight IEEE references with settled labels, no final warnings or
overflow messages, resolved current links, unchanged first-draft archive
hashes and preserved files outside the six expected reporting/navigation
edits. Ordinary math subscripts use TeX's standard script sizes; the main
prose/table/reference text is 11 pt. The pre-existing tracked modifications
to AGENTS.md, PLANS.md and memo.txt are unchanged. Exact artifact hashes,
counts, tool versions and page extent are recorded in the verification JSON.

## Status and next allowed action

The report now explains the basic modeling chain and contains no standalone
Section 4. The selected physical equations and assumptions remain fixed;
illustrative values are not a frozen experiment configuration. Unexpanded
bias branches/proofs remain available in the linked formulation. The user
may request bounded report revisions or accept it. No simulator code,
traffic experiment, numerical differentiation, optimizer run, dependency,
sub-agent or external communication occurs. The old accepted VSL report,
historical gates, closed ramp line and separate urban work remain untouched.
