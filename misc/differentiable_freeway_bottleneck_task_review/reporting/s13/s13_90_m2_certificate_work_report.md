# S13.90 — M2 analytical-certificate work report

Date: 2026-09-30. Status: **Closed 2026-10-01 with M2C-A accepted.**

## Work completed

- Recorded approval of G1-A through G7-A and treated the global contracts as
  closed inputs.
- Reused the S05 exact-history/obstruction analysis and S12 mechanism/source
  audit before any discovery; no new broad search was required.
- Mapped per-lane conservation, mandatory transfer, finite receiving, gap cost,
  common VSL and the aggregate countermodel into one explicit analytical
  contract.
- Distinguished direct structural adoption, bounded analytical adaptation and
  original S13 deduction.
- Proved conservation, the exact spatial handoff, strict convexity, an open-
  regime different-action result, positive observer-only minimax regret and a
  conditional state-relevant gradient direction.
- Classified aggregate/fixed-service limits and nonsmooth active-set boundaries.
- Produced formula-bearing LaTeX/PDF artifacts and stopped at S13-UG1.

## Files created

- `extraction/s13_m2_source_to_equation_audit.md`
- `synthesis/s13/s13_m2_model_contract.tex`
- `synthesis/s13/s13_m2_model_contract.pdf`
- `synthesis/s13/s13_m2_certificate_analysis.tex`
- `synthesis/s13/s13_m2_certificate_analysis.pdf`
- `reporting/s13/s13_20_m2_certificate_findings_and_gate.md`
- `reporting/s13/s13_80_m2_contract_dialogue.md`
- `reporting/s13/s13_90_m2_certificate_work_report.md`

## Files updated

- `s13_00_m2_analytical_contract_certificate_review.md`
- package sequence, README guides, successor plan and document registry.

## Commands and tools

- Repository/source inspection with `sed`, `rg`, `cat` and `find`.
- SymPy 1.14 symbolic differentiation and substitution checks for the complete
  objective, stationary point and speed derivative.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error` for both formula
  artifacts; the certificate required one documented correction adding the
  missing derivative macro before successful recompilation.
- PDF header/size and LaTeX-log warning checks.
- Package-local Markdown link, CSV, registry, artifact and focused whitespace
  validation; `git diff --check`.

No simulator, SUMO, traffic experiment, calibration, optimization,
implementation, automatic differentiation or environment-changing command was
run.

## Acceptance results

| Planned criterion | Result |
|---|---|
| Source-bounded conservative M2 contract | Passed conditionally; adaptations explicit. |
| Exact strong-history pair | Passed conditionally through the S05 spatial handoff. |
| Hidden state changes endogenous service | Passed. |
| Different useful action over full family | Passed on a nonempty open regime. |
| Strong aggregate observer/countermodel test | Passed at the open-loop decision point. |
| Conditional conceptual gradient path | Passed inside the fixed active regime. |
| Primary verdict | Provisional M2C-A pending user disposition. |

## Assumptions and unresolved risks

The constant positive transfer-rate branch, symmetric continuing-lane reduction,
batch handoff and homogeneous proportional service are conditional analytical
adaptations. Their source compatibility is documented; their empirical validity
is not established. Exact observer equality inherits S05's conditional
preparation rather than a native trajectory. Alternative priority rules,
postdecision feedback and implementation-level nonsmooth derivatives remain
outside the certificate.

## Status at the original execution stop

S13 completed execution through S13-UG1 / M2C-R1 and stopped for user
disposition. No successor review was automatic.

## Post-execution study-sufficiency audit

On 2026-10-01, the user requested an audit of whether the elementary certificate
and its extensions can support a complete study. The resulting
[`S13.35` audit](s13_35_study_sufficiency_and_extension_audit.md) concludes that
S13 is a complete conditional certificate and viable study kernel, but cannot by
itself establish full per-lane representation necessity or external gradient
usefulness.

The audit identifies four minimum theoretical extensions: causal-link deletion,
a small preregistered transfer/service family, a strong aggregate-to-compressed-
state-to-lane-state information ladder, and decision/gradient phase
classification. It separately identifies independent-evaluator and derivative
evidence required for an applied usefulness claim. No extension was executed or
authorized.

Files added or updated for this audit are the S13.35 report, S13 dialogue, this
work report, package/sequence/reporting guides and document registry. Commands
were read-only `sed`, `rg`, `find` and `tail`, followed by documentation patches,
link/registry validation and `git diff --check`. No formula artifact, source
search, simulator, optimization, implementation or environment change was
needed.

## Closure update

On 2026-10-01, the user accepted M2C-R1 Candidate A. S13 is closed with M2C-A.
The [closure record](s13_99_m2_certificate_sprint_closure.md) preserves the
conditional claim boundary and a four-stage prospective review ladder toward a
research-ready task. None of those stages is open.
