# Standalone Step 3: viewed papers and derivation provenance

Date: 2026-10-19. This is the reference list for papers viewed in the remaining
standalone Step 3 sprint, with reading limits. No full-paper collection,
new traffic-model adoption or claim of an exhaustive literature search.

## Papers viewed in this sprint

| Reference | Material actually inspected | Support and limit |
|---|---|---|
| Nathan J. Kong, J. Joe Payne, James Zhu and Aaron M. Johnson (2024), **Saltation Matrices: The Essential Tool for Linearizing Hybrid Dynamical Systems**, Proceedings of the IEEE 112(6), 585--608; DOI 10.1109/JPROC.2024.3440211. [Author manuscript, arXiv:2306.06862v3](https://arxiv.org/pdf/2306.06862). | Version/date and publication cover; introduction; Section III-A definition/equations 9--14 and assumptions; Section III-B geometric derivation through the guard/time-shift calculation. PDF pages 1--2 and 5--8, zero-based pages 0--1 and 4--7. Other application sections were not reviewed. | Event-time changes require a sensitivity correction even when physical state is continuous. The regular result assumes differentiable guards and transverse isolated events; simultaneous/grazing cases need separate analysis. This supports the existing event-aware evidence contract, not a new traffic model or a theorem reducing our history state. |
| Maria Laura Delle Monache, Benedetto Piccoli and Francesco Rossi (2016), **Traffic regulation via controlled speed limit**, [arXiv:1603.04785](https://arxiv.org/pdf/1603.04785). | Rechecked title/abstract, Section 3.3 on cost variations/gradient guidance and its immediate comparator context, PDF pages 1 and 12--13. No new numerical result or entire-method requalification. Previously reviewed in the accepted baseline/source archive. | VSL cost variations and numerical gradient control already exist. Its LWR/outflow-tracking objective differs from the present complete-TST lane-drop task; neither its derivative nor its performance result is transplanted. |

No simulator manual was newly reviewed and no native evaluator was opened.
The new hybrid-sensitivity paper supplies a mathematical reference for
already planned moving-event differentiation; it changes no queue rule,
traffic state or intervention.

## Accepted traffic literature reused from the archive

The selected model's conservation, receiving, work, propagation and recovery
lineage is retained through the existing source-to-equation map. No paper
supplies the complete joined H1/T1/W-F/S-E-P/R-E/O-R model.

[Current component/source/decision map](vsl_feedback8_model_stack_source_map.md)

[Physical source and identification audit](vsl_mp6_physical_source_audit.md)

[Accepted baseline screen and paper references](vsl_successor_baselines_and_evidence_gaps.md)

The latter retains Wei--Han--Wang's aggregate history/capacity-drop model,
Jin--Jin's lane-drop VSL model, Hegyi et al.'s METANET control,
Carey et al.'s multi-lane receiving/work model and Nagalur Subraveti et al.'s
continuous lane-changing model. Leclercq et al. motivates point-insertion
recovery through the physical/source audit. Those papers were reused through
their archived extractions, not newly read or newly adopted in this sprint.
Their empirical and task-domain limitations are unchanged. The pre-existing
reference list preserves DOI/version and publication-year distinctions.

## What is reused, and what is newly deduced here?

| Responsibility | Existing input | New work and attribution limit |
|---|---|---|
| Exact aggregate-history collision | Archived H1 loading construction in the 14 October information/sensitivity note. | Rechecked that the terminal amendment cannot affect the upstream, terminal-empty prefix. No new sensor or observation contract. |
| Initial E sufficiency | Initial A/B symmetry, known parameters, empty history and WF-Q1 unique forward law. | Rechecked exact A+E/G objective/defined-gradient equality for the selected complete law. No claim E is a unique encoding or a general freeway sufficient state. |
| Common-action result | Monotone H1 front workload and selected free-mark/queue guards. | Derived a nonzero exact baseline-work interval for the matched pair in which the actual coupled model stays free at all advice. The predecessor's larger small-work classification is not asserted. |
| Information/action possibility | Earlier fixed-work H1/T1 exact objective, preparation derivative and strict action gaps. | New service/queue brackets give a uniform selected-law objective bound with positive mismatch and finite positive recovery. It transfers finite action contrast and nonzero common-action regret, not an infinitesimal gradient sign or calibrated regime. |
| Full-TST sensitivities | Selected H1 arrivals, W-F root, causal queues, O-R mass window and fixed-horizon accounting. | Derived preparation/arrival/root sensitivities and the mass-cutoff/event terms of the history integral. These are own model-specific deductions. Kong et al. supplies only the regular finite-state event-timing principle. |
| Strong competitors and novelty limits | Accepted aggregate/history, compact, continuous lane-aware and scalar-search screens. | Preserved separate information, model-form and optimizer attributions. No complete source baseline is silently adopted or assembled. |

The mathematical comparison constructs an existence range intentionally.
That is not outcome-blind empirical admission or authority to choose the
main evaluation cases after seeing their preferred actions. Later numerical
execution must report its fixed cases, error budgets and negative outcomes.

## Reading and tool record

Used primary arXiv search, PDF open and text find for the two papers above.
Relevant query strings were `site.arxiv.org "Saltation Matrices" "Essential
Tool"` and `site.arxiv.org 1603.04785 speed limits cost variations`.
Checked the published 2024 citation/version for the new sensitivity paper;
no secondary search-result claim is used as evidence. No paper PDF was
downloaded into the review package. Repository inspection used `rg`, `sed`
and the already archived TeX/Markdown records. No package was installed.

[Own derivations, proofs and sensitivity references, PDF](../../synthesis/research_readiness/vsl_step3_standalone_information_and_gradient.pdf)

[Plain findings and gate](../../reporting/research_readiness/vsl_step3_standalone_findings_and_closure_gate.md)
