# Copy-ready initialization prompt for the next agent

Use the following as the first instruction in a fresh session.

---

You are opening a new, semantically independent literature/task-formulation
review for a possible differentiable freeway bottleneck-control research task.
This is not a continuation of project development and must not inherit the
current urban simulator as a fixed modeling constraint.

Your first responsibility is to read the following files completely, in order:

1. `/home/zpz/repos/diff_minimal_meso/AGENTS.md`
2. `/home/zpz/repos/diff_minimal_meso/misc/differentiable_freeway_bottleneck_task_pre_review/README.md`
3. `/home/zpz/repos/diff_minimal_meso/misc/differentiable_freeway_bottleneck_task_pre_review/pre_review_closure_and_handoff.md`
4. `/home/zpz/repos/diff_minimal_meso/misc/differentiable_freeway_bottleneck_task_pre_review/freeway_mesoscopic_meaning_quick_scan.md`
5. `/home/zpz/repos/diff_minimal_meso/misc/differentiable_freeway_bottleneck_task_pre_review/feedback22_email_trace_response.md`
6. `/home/zpz/repos/diff_minimal_meso/temp_content/feedback/email_trace_20260916.md`

Use the closed ramp-metering package only as reusable evidence, not as the scope
or conclusion of this new review. Before repeating any source query, inspect:

- `/home/zpz/repos/diff_minimal_meso/misc/selective_discreteness_ramp_metering_review/reporting/closure_record.md`
- `/home/zpz/repos/diff_minimal_meso/misc/selective_discreteness_ramp_metering_review/synthesis/feedback20_evidence_debate.md`
- `/home/zpz/repos/diff_minimal_meso/misc/selective_discreteness_ramp_metering_review/archive/manifest.csv`
- `/home/zpz/repos/diff_minimal_meso/misc/selective_discreteness_ramp_metering_review/archive/metadata/feedback20_sources.md`

The user has approved N1: a bounded, task-first framing sprint followed by a user
gate. The operational anchor is a temporary or permanent freeway lane-capacity
reduction. F1 speed harmonization/advisory control and F2 coordinated ramp
metering are the primary initial candidates. F4 post-reopening recovery is a
scenario dimension. F3 joint control and F5 cooperative lane-change/merge
control are expansion or boundary candidates, not preselected tasks.

Treat the following as fixed review principles:

- Ask what traffic resolution is necessary; do not assume mesoscopic value.
- Macro, mesoscopic, hybrid, microscopic, or negative/infeasible conclusions are
  all admissible.
- Describe model candidates by retained information and behavior, not by the
  word “mesoscopic” alone.
- Task validity and the minimum model come before compatibility with the current
  project.
- The urban and freeway branches share only the resolution question and evidence
  logic; they need not share a simulator, code base, mesoscopic definition, or
  paper.
- Use strong task-specific lower-resolution and controller/optimizer baselines.
- Separate derivative correctness from gradient usefulness in a richer
  independent evaluator.
- Do not modify project files, Milestone 2 files, source, tests, configs, or any
  closed review package.

Create a new sibling package at:

`/home/zpz/repos/diff_minimal_meso/misc/differentiable_freeway_bottleneck_task_review/`

Do not place the new review inside the closed pre-review or ramp-metering
packages. Start by drafting a concise executable `review_protocol_plan.md` in
the new package. The plan must specify:

1. the bounded N1 objective and non-goals;
2. research questions derived from CQ1--CQ7 in the handoff;
3. candidate-task comparison criteria;
4. search sources and query families, including recent arXiv work where
   appropriate;
5. inclusion/exclusion rules and evidence-strength labels;
6. how existing archived evidence will be reused without overstating its scope;
7. planned screening, extraction, synthesis, and source-archive files;
8. the first user gate and the exact material the user will review;
9. stop conditions for macro sufficiency, excessive entanglement, infeasible
   gradient validation, insufficient novelty, or unacceptable evidence cost;
10. how a new literature-supported candidate may enter without unbounded scope
    growth; and
11. the one-batch institutional-access procedure if paywalled decision-critical
    papers are found.

The first user gate should present a compact task matrix, minimum source map,
explicit exclusion list, and recommendation to select one candidate, refine N1,
or halt the freeway branch. Do not begin simulator development, formal task
implementation, project synchronization, or a full post-N1 review.

After writing the executable plan, stop and report it for user approval. Do not
advance beyond that gate unless the user explicitly authorizes execution.

---
