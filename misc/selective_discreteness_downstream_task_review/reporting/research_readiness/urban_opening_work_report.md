# Urban opening work report

Date: 2026-10-20. Status: **S0–S1 complete; proposal awaiting user review.**

The accepted experiment asks a useful traffic question: does retained order explain access and service well enough to improve a common service-allocation decision? The opening audit finds that its task and evidence contract are established, while essential coupled traffic laws still need specification. The new package makes those decisions reviewable before drafting a complete-model report.

## Files created

Seven new files, all within this urban review package:

| File | Purpose |
|---|---|
| [Readiness overview](urban_readiness_overview.md) | Traffic-first finding and entry point |
| [Phase A proposal](../../temp_content/research_readiness/phase_A_proposal.md) | Completion rubric, global-first stages, reading/report structure and stop conditions |
| [Phase A dialogue](../../temp_content/research_readiness/phase_A_dialogue.md) | Interpreted instructions, recovered decisions and proposed scope/ownership treatment |
| [Authority/gap audit](../../extraction/research_readiness/urban_authority_and_gap_audit.md) | Source precedence, A/R/N/E classifications, physical interfaces, provenance recovery, 11 gap studies and variant sensitivity coverage |
| [Question register](../../extraction/research_readiness/urban_open_question_register.md) | 6 global and 8 local questions, candidates with pros/cons, dependencies, mixed splits and reopen rules |
| This work report | Changes, assumptions, commands, checks and current boundary |
| [Static verification](urban_opening_validation.json) | Link/inventory/coverage and preservation results; no scientific validation claim |

Package-local temp_content holds editable planning material. No pre-existing urban artifact was rewritten, including historical T6/T7 statuses. The three pre-existing tracked modifications were AGENTS.md, PLANS.md and memo.txt; they remain the user's changes. The current branch is m2_interaction_zone; no branch/checkout was created and this task did not resume M2 implementation. The package and temp_content are ignored under the existing .gitignore, so new artifacts do not appear in ordinary git status; no ignore or staging rule was changed.

## Assumptions and decision status

- The initialization prompt is the active instruction; its scope ends at the standards/records/gap/plan gate.
- T6/T7 acceptance controls older pending and exact-production-order text. V0–V4, effective-service action, complete TST, baseline fairness and staged external evidence are retained. V5/I1 and the ramp line remain excluded/closed.
- M2's closed G1–G6 provide infrastructure within their stated neutral domain; local recommendations are not approvals. No later approved M2 Phase-C/M3 decision was located in the inspected current records.
- P8 reconsideration is authorized. Moving methodological closure into this successor is proposed; no replacement law, within-bin relaxation, waveform or implementation is approved.
- Source roles and reading depth come from the recorded extraction/adoption material and inspected project plans. This opening does not newly verify external source equations, software availability or empirical claims.
- A 4–6 page compact report is a provisional urban budget, not a copied VSL requirement or an approved limit. The present prose/table planning artifacts do not contain a new mathematical derivation.

## Commands and environment

Read-only inspection used pwd, git status --short, git branch --show-current, git check-ignore -v, rg --files, rg -n, cat, sed and wc. Relevant reads covered repository instructions/context/roadmap, the opening prompt/handoff and clarifications, feedback, accepted urban closure/task/baseline/source records, inherited M0/M1/M2 contracts and selected code/tests/configs. No dependency API was invented or changed. No environment manifest matching the inspected non-report project patterns was located; this does not imply the runtime environment is unavailable.

The system pdftotext command was unavailable. The existing differential_sim Python environment supplied pypdf 6.15.0 on Python 3.11.9, which read the existing five-page urban and four-page VSL PDFs without installation. Extracted text was saved only under /tmp/urban_opening_read.pdf.txt and /tmp/vsl_opening_read.pdf.txt. The urban LaTeX source was read fully; the VSL report's source and coverage/assumption records were inspected as presentation examples. No traffic or differentiation package was executed.

The local LaTeX check found latexmk and pdflatex; pdflatex --version reported pdfTeX 1.40.25 / TeX Live 2023 (Debian). No new PDF was built: the authorized output is a prose opening proposal. Later formula-heavy stages must build and retain their own LaTeX source/PDF and inspect the result.

Edits used apply_patch. Python standard-library inspection generated a pre-edit SHA-256 snapshot at /tmp/urban_opening_before_20261020.json, covering 808 existing files across root instructions, code/tests/configs, approved plans, feedback/planning, all 69 original urban files and all 506 files in the VSL/freeway package. This records the starting bytes, including pre-existing user modifications.

The final document check is:

    python3 /tmp/urban_opening_document_checks_20261020.py
    git status --short

Its durable result is urban_opening_validation.json. It checks new-artifact existence, local links, the rubric/question/gap/stage inventories, required question presentation fields, named stop/scope boundaries and preservation of all snapshotted files. Source hashes identify the inspected documentary inputs. It does not evaluate traffic equations, derivatives or physical realism.

## Checks, results and remaining work

Static document checks passed, including local links, all 14 question records, the 10-point rubric, 11 gap records, staged plan and preservation of all 808 original files. The verification JSON contains exact counts and artifact hashes. Ordinary git status retains only its three pre-existing modified paths.

No scientific tests, reference simulations, gradients, optimization, SUMO, installations or detached jobs were run. Numeric tolerances, demand calibration, scenario seeds and execution budgets remain for later approved planning; no new numeric scientific result is claimed.

Unresolved methodology comprises the initial/history domain; average-service/order/resource clock; retained-order policy and physically realized bay access; faithful B1/B2 equations; information/history matching; independent reference and external mapping; complete conditional sensitivity; and equation-level attribution. The proposed S6 whole-model audit must reconcile these before S7 report drafting. Actual forward/derivative/usefulness evidence remains separate future work.

Urban Part I stays closed. This successor stops at its requested opening gate. The next allowed action is user review of the proposed standard, inventory and bounded sequence, followed by S2 global-contract discussion only if opened. No later report-writing or model-refinement stage has begun.
