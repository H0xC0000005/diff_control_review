# Remaining standalone Step 3 review: work and validation

Date: 2026-10-19. **Q1–Q3 and final consistency audit delivered at VSL-S3-G1;
formal Step 3 user closure pending.**

## Main outcome

The selected complete law retains the exact aggregate-history ambiguity and
initial-E sufficient encoding. New analysis gives an exact nonzero
common-action interval and a positive-mechanism information/action existence
range through a uniform service/queue/TST comparison. These are bounded
analytical results, not numerical performance or physical admission.

The regular full-objective sensitivity reference includes preparation,
moving eligibility, implicit service, queue-event times and the renewal
account's moving source/mark and old-weight cutoff terms. The standalone
protocol distinguishes derivative correctness, information value, finite
action usefulness and optimizer advantage; nonregular forward cases remain.
The audit finds no new methodological choice. Stop at the final user gate.

[Plain findings and closure gate](vsl_step3_standalone_findings_and_closure_gate.md)

[Standalone verification protocol](../../synthesis/research_readiness/vsl_step3_standalone_verification_protocol.md)

[Seven-page analytical/sensitivity report](../../synthesis/research_readiness/vsl_step3_standalone_information_and_gradient.pdf)

## Files changed

Created eleven artifacts, relative to the review-package root:

- `reporting/research_readiness/vsl_step3_standalone_findings_and_closure_gate.md`
- `reporting/research_readiness/vsl_step3_standalone_consistency_audit.md`
- `reporting/research_readiness/vsl_step3_standalone_review_work_report.md`
- `reporting/research_readiness/vsl_step3_standalone_review_validation.json`
- `reporting/research_readiness/vsl_step3_standalone_symbolic_checks.py`
- `reporting/research_readiness/vsl_step3_standalone_symbolic_results.json`
- `reporting/research_readiness/vsl_step3_standalone_mathematics_build.log`
- `synthesis/research_readiness/vsl_step3_standalone_information_and_gradient.tex`
- `synthesis/research_readiness/vsl_step3_standalone_information_and_gradient.pdf`
- `synthesis/research_readiness/vsl_step3_standalone_verification_protocol.md`
- `extraction/research_readiness/vsl_step3_standalone_sources_and_derivations.md`

Updated eleven existing Markdown records:

- `README.md`
- `vsl_successor_00_opening_plan.md`
- `reporting/research_readiness/vsl_r1_modeling_problem_inventory.md`
- `reporting/research_readiness/vsl_review_progress.md`
- `reporting/research_readiness/vsl_step3_comparison_review_plan.md`
- `reporting/research_readiness/vsl_feedback6_joined_behavior_agreement_and_plan.md`
- `reporting/research_readiness/vsl_cp_qualification_review_plan.md`
- `reporting/research_readiness/vsl_successor_opening_dialogue.md`
- `synthesis/research_readiness/vsl_step3_first_verification_protocol_draft.md`
- `synthesis/research_readiness/vsl_feedback1_core_model_candidates.md`
- `synthesis/research_readiness/vsl_successor_methods_outline.md`

The updated entry points lead with the current completed-review status and
link the new findings/protocol/PDF. Progress distinguishes review completion
from final user closure. The old protocol is labeled historical; its
predecessor and optional SUMO passages are not current coupled-law results.
The dialogue archives the authorization, findings, limits and stopping gate.
Old source/equation/proof/PDF/build/evidence artifacts are not rewritten.

The new Python file performs symbolic algebra/static rational verification
only. It is not simulator code, does not integrate time or traffic states,
and invokes no AD, ODE solver, numerical gradient or optimization routine.

## Assumptions, reasoning limits and scientific status

All selected model, information and objective assumptions are unchanged.
The user-approved standalone evidence scope governs. SUMO is optional;
the closed ramp and urban lines are not reopened.

The new positive action proof uses a deletion reference only to bound the
selected law, restoring positive mismatch and finite positive recovery.
It proves finite-step utility and common-action regret, not direct transfer
of S13, opposite infinitesimal slopes, global smoothness or minimum
attainment. Its free-A range differs from the earlier complete A-delay/
active-renewal family. A joint strong-delay/action/physical witness and a
source-supported operating range remain unestablished. No case is selected
as a main evaluation setting by this existence proof.

The regular derivative construction has explicit chart, transversality and
cutoff conditions. Degenerate cases remain in the task. No generalized
gradient, smoothing or altered causal rule is silently selected. Full lane
state, discrete order and AD superiority are not established necessities.

Step 3's remaining review work is complete; formal user closure is pending.
Numerical AD/difference/solver evidence, optimizer performance and applied
MP6 are unexecuted. Step 4, construction and experiments remain unopened.

## Commands and source inspection

Repository/current-record inspection used `git status --short`, `rg -n`,
`sed -n`, read-only Python file inspection and the earlier accepted context,
plan, feedback and source records. No applicable implementation pass is
opened. A fresh Python `pathlib`/`hashlib`/`json` snapshot protected 399
existing files before edits; pre-edit Markdown was also saved for exact
change inspection:

- `/tmp/vsl_step3_standalone_review_before.json`
- `/tmp/vsl_step3_standalone_review_before_text.json`

Primary web search/open/find viewed Kong et al.'s event-sensitivity
definition/derivation and rechecked Delle Monache et al.'s VSL gradient
precedent. The reference list records versions, sections and reading limits.
No new traffic law, empirical parameter or native reference was adopted.

[Viewed papers and derivation/source map](../../extraction/research_readiness/vsl_step3_standalone_sources_and_derivations.md)

Exact algebra command:

```bash
/home/zpz/miniconda3/envs/differential_sim/bin/python misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_step3_standalone_symbolic_checks.py
```

Used Python 3.11.9 and existing SymPy 1.14.0. The 29 identities cover the
service comparison/error bound, old complete-objective expansion, profile
area/partials, service-root derivatives, arrival Leibniz/clock chain,
event/cutoff terms and complete travel-time accounting. Seventeen exact
static checks cover the reused family's observation/loading, preparation,
ordinary load, receiving/storage and new negative interval.

One initial check could not simplify equivalent partial-derivative
substitutions in the moving-arrival chain. Rewrote the checker using
independent argument symbols and explicit `Subs(...).doit()`; the direct
chain derivative then agrees exactly. The mathematical formula did not
change. All final identities and static checks pass. These checks do not
machine-certify the queue comparison proof or establish numerical gradients.

Verified `/usr/bin/pdflatex` before building. Build command:

```bash
python3 /tmp/vsl_step3_standalone_build.py
```

It runs the following three times, using the recorded temporary build
directory, then copies only the new PDF/log to the package:

```bash
/usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/vsl_step3_standalone_latex_1s5sn5xi /home/zpz/repos/diff_minimal_meso/misc/differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_step3_standalone_information_and_gradient.tex
```

The retained source builds a seven-page PDF, 216952 bytes. The final log has
no warnings or over/underfull boxes. Existing pypdf 6.15.0 checked extracted
page text, mathematical cross-references, font types and PDF link targets.
Only Type 1 fonts are present. This is text/layout-log/font/link inspection,
not raster visual inspection. No package was installed.

Document synchronization used `apply_patch` and:

```bash
python3 /tmp/vsl_step3_standalone_review_sync.py
```

Final document/preservation command:

```bash
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_step3_standalone_review_checks.py
git status --short
```

The exact existing-file/new-file allowlists, all other protected hashes,
local Markdown links/headings, TeX references, PDF links/destinations,
current status/claim limits and prior root edits are checked. Counts and
final results are in the machine-readable record. Root Git status remains
the pre-existing `AGENTS.md`, `PLANS.md` and `memo.txt` edits; the review
package is Git-ignored. User feedback is unchanged.

[Exact algebra results](vsl_step3_standalone_symbolic_results.json)

[Final document/PDF/preservation validation](vsl_step3_standalone_review_validation.json)

## Next allowed action

User review accepts or corrects the completed Step 3 contract at VSL-S3-G1.
Do not open Step 4 or execute the task automatically. A later approved
execution proposal must select outcome-blind parameter cases, independent
reference implementations, precision/solver/step/error settings, numerical
acceptance criteria and fair resource budgets before runs.
