# Why a vacant turn bay can still be unusable

**Current report, 28 October: clean colleague-facing edition.** Both reports are black, with 9/11 pages. Review-history and implementation-status scaffolding is removed; the traffic reasoning, scientific provenance, gradient framework and all equations are retained. Previous versions are preserved.

[Clean main report](urban_compact_methods_report_clean.pdf)

[Clean companion](urban_methodology_specification_clean.pdf)

A turner needs both bay room and a path to the opening. A through block in an actual shared feeder can obstruct that path. Additional through service may then help left demand later, while additional left service initially achieves little. The urban study tests whether retaining the relevant traffic order improves useful service-allocation sensitivities beyond sound aggregate explanations.

The feedback-11 revision keeps the VSL presentation order while explaining each equation through its traffic meaning. The representative approach now has an inside left/through feeder branching to a left bay and through-only lane, beside an independent through/right lane. The mathematical companion is synchronized.

[Consolidated compact methodology report](urban_compact_methods_report_clean.pdf)

[Detailed mathematical specification](urban_methodology_specification_clean.pdf)

The report now applies the closed agreements. Traffic quantity is continuous; ordered route metadata preserve realized-lane sequence. Fresh allocation uses known sending, receiving and access. Only admitted mass becomes lane-committed; unadmitted mass stays at its owner without a future-lane vector.

The allocator considers packets in recorded order and retains priority within a blocked movement, while inspecting other physically accessible movements. Once traffic occupies a lane, its head can block followers. U admits through traffic to either F1 or F2; F1 branches to B/T1 and F2 continues to T2. A blocked inside lane therefore need not stop the parallel lane, and no resident traffic can jump across. V is the total feasible admitted mass; lambda is the common load level used to balance it across receiving lanes.

The sensitivity now follows actual admissions, residual resources, eligibility and head times through complete population time. Fixed continuation stops new control variation but continues the state response. Source waiting, moving mass and queues are counted once. The current report contains no frozen-waiting or old-target rationing construction.

The accepted V0–V4 task, four effective-service groups, current-ready-head receiving policy and model-owned conversion of original fine observations remain. Strong macro inference is allowed and must count against the necessity of explicit order. The model does not claim universal macro indistinguishability or empirical superiority.

**Current topic, 28 October: clean colleague-facing edition completed for review.** Feasibility reasoning and exact hand-definition checks are supplied. Native B1/B2 implementation qualification, numerical calibration, forward/derivative testing and richer-evaluator usefulness remain later work. The report is not simulator implementation or experimental evidence.

[Current source map and completeness limits](../../extraction/research_readiness/urban_methodology_specification_sources.md)

[Current reading guide](../../temp_content/research_readiness/unified_methodology_draft.md)

[Decisions](../../temp_content/research_readiness/review_decisions.md)

[Work and verification](urban_methodology_draft_work_report.md)

[Superseded candidate and question appendix](../../archive/research_readiness/urban_methodology_before_feedback10_application_20261027/README.md)

[Feedback-11 changes](urban_feedback11_response.md)

[Alternative structures — proposed, not applied](../../temp_content/research_readiness/report_structure_options.md)
