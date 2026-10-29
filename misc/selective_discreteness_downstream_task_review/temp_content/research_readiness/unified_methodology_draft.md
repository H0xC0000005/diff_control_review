# Urban methodology: revised report for colleagues

**Current topic, 28 October: clean colleague-facing reports completed for review.** All red tints are removed. The final edit removes implementation/review-history scaffolding while retaining the traffic explanations, provenance, gradient roadmap, examples, assumptions and evidence limits. All 23/35 equations and their numbering are unchanged. The clean reports have 9/11 pages. Earlier PDF and LaTeX versions remain intact.

[Clean methodology report — start here](../../reporting/research_readiness/urban_compact_methods_report_clean.pdf)

[Clean mathematical companion](../../reporting/research_readiness/urban_methodology_specification_clean.pdf)

[Main LaTeX source](../../reporting/research_readiness/urban_compact_methods_report_clean.tex)

[Companion LaTeX source](../../reporting/research_readiness/urban_methodology_specification_clean.tex)

[Formula provenance](../../extraction/research_readiness/urban_formula_provenance.md)

[Previous highlighted report with the citation correction](../../reporting/research_readiness/urban_compact_methods_report_formula_provenance_citation_fix.pdf)

[Previous highlighted companion](../../reporting/research_readiness/urban_methodology_specification_formula_provenance.pdf)

## What changed

Only actual admissions create receiving-lane membership. The remainder stays with its owner without a future-lane vector. Later packets see earlier admitted load; unserved traffic keeps priority within its movement, while other movements are inspected.

Physical access is explicit. U feeds parallel F1 and F2. F1 branches to left-only B and through-only T1; F2 continues to shared through/right T2. Through traffic chooses at admission to F1/F2 using current feeder loads and feasible entry. Once resident, traffic cannot switch feeders. A residual in F1 blocks its followers while independent F2 traffic may continue. The bay opening remains inside the zone, with disjoint physical storage and unchanged travel, route and admission principles.

The eligible candidate list uses ready mass A, with S as a total sending budget. A universal first-S prefix would incorrectly suppress independently accessible later traffic. Physical lanes still serve prefixes through their access predicate. This is an explicit urban adaptation of M1 extraction, not a claim about current code.

The sensitivity account now follows actual additions, residual sending/receiving, retained unassigned mass, head times and boundary reconstruction. Frozen waiting-vector and old-target derivatives are removed. Current-head receiving sharing and the selected constant average receiving convention remain.

## What is complete and what remains

The agreed traffic rules, physical ownership, complete TST, conditional sensitivities and fairness/reference protocol are consolidated. Hand-definition checks and feasibility/uniqueness reasoning support their internal coherence. The earlier policy question set was closed. The current revision makes formula provenance explicit within the agreed explanatory structure; the alternative document structures remain proposals.

Native B1/B2 implementation qualification, numerical calibration and all forward/gradient/usefulness experiments remain later work as previously agreed. The report does not treat these as executed evidence or claim that a native adapter has already been qualified. The next user-facing action is review of the consolidated report, not implementation.

[Current equation/source map and coverage](../../extraction/research_readiness/urban_methodology_specification_sources.md)

[Work and verification record](../../reporting/research_readiness/urban_methodology_draft_work_report.md)

[Superseded report and question appendix — archive](../../archive/research_readiness/urban_methodology_before_feedback10_application_20261027/README.md)

[Agreed decisions](review_decisions.md)

[Discussion record](review_dialogue.md)

The much earlier evolving draft and its source map also remain historical support; their conditional waiting-target formulas are not current model rules.

[Earlier evolving mathematical draft](../../reporting/research_readiness/urban_unified_methodology_draft.pdf)

[Earlier source map](../../extraction/research_readiness/urban_unified_methodology_sources.md)

[Feedback 11: changes and remaining scope](../../reporting/research_readiness/urban_feedback11_response.md)

[Geometry realization](approach_geometry_review.md)

[Feedback 12: second improvement batch](../../reporting/research_readiness/urban_feedback12_response.md)

[Feedback 13: current presentation revision](../../reporting/research_readiness/urban_feedback13_response.md)
