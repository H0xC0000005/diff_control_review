# Feedback 7: current agreements and one unresolved point

**Historical response, superseded where amended.** The user subsequently withdraws the frozen queue decision and selects sequential packets with progressive per-packet balancing. The original response below is preserved.

[Read the separate amendment response](urban_feedback7_amendment_response.md)

26 October 2026. This response concerns the current batch only. No next batch, model-building pass or experiment is opened.

## Brief agreements

- **Queue observation:** use the established queue at timestep start. Earlier assignments in that timestep do not progressively update what later allocations observe. Merely having a target does not make approaching traffic part of the established queue. Actual storage/receiving is still consumed when entry occurs.
- **Homogeneous partial entry:** your confirmation settles the example. The 0.2 remains physically on the common feeder. If targets were already 0.4/0.6 and admissions are 0.3/0.5, pending targets remain 0.1/0.1. I withdraw the extra partial-admission question: the example did not demonstrate a further decision you need to make. Conservation and residual bookkeeping are construction obligations; a genuine conflict would need a concrete counterexample.
- **Receiving shares:** use the relevant green to weight inbound legs, then share equally among eligible lanes within a leg. Respect feasible demand, average service and physical order; reuse shares that cannot be used. Give the leg its weight once, so additional lanes do not multiply its total priority. These are simultaneous quantities, without phase precedence.
- **Earlier choices stand:** internal bay geometry, joint homogeneous splitting without artificial target order, elapsed-rate service, fixed commitments and original/realized-lane order.

For example, green weights in a 3:2 ratio give two legs 0.6/0.4 of one receiving unit if their feasible demands permit it. Two eligible lanes on the first leg receive 0.3 each. If a lane cannot use its share, reuse the surplus within the leg; if the leg cannot use its grant, redistribute to other eligible legs by their green weights. Zero-green movements still have zero effective service.

## One unresolved point in this batch

**Does the frozen observation still feed one joint balancing calculation, or is the full lane cost fixed independently of the incoming assignment?**

With initial bay/other queues 0.2/0 and one incoming unit, equal geometry and nonbinding room:

- Frozen background plus joint balancing gives intended additions 0.4/0.6.
- Fully frozen unequal costs, under deterministic least-cost choice, direct the unit toward the initially empty lane.

The first removes sequential observation updates but retains simultaneous load balancing. The second also removes that load feedback and changes the earlier equilibrium example. Feedback 7 clearly fixes observation timing; I have not silently selected between these two cost meanings. This is the only unresolved interpretation from the three questions you answered.

[Separate short explanation of this same unresolved point](../../temp_content/research_readiness/queue_snapshot_choice.md)

No additional packet-order or partial-admission question is pending. The original broad directions remain agreed; explicit batch closure has not been recorded.

## Supporting record

The receiving principle is the user's selected rule with feasible caps and reuse. Green remains in effective service; it is not multiplied into an already allocated discharge again. For a common exit, use the green of the movement from each leg into that exit, rather than an unspecified sum of phases. Combining the rule with the full mixed-lane model has not been opened by this response.

The [restricted M0 signal branch](../../../../context_snapshots/diff_minimal_meso/docs/milestones/milestone_0_ltm_baseline.md#L426) deliberately prohibits reuse of unused green-weighted receiving quotas. The current urban choice is a declared different coupling; the approved plan/code remain unchanged. The earlier progressive queue-cost formula is now marked historical in the supporting companion; no replacement cost is approved yet.

This pass reads feedback 7 and the current review records and M0 source contract. It creates this response and the short current-point note, synchronizes live records and marks only the feedback-7 heading answered. Feedback 6, root files, code/tests/configs, approved plans and previous validation artifacts remain untouched. No new literature search, mathematical model construction, simulator run, installation or next batch is undertaken. Document checks and the existing companion's status-update build are recorded below when complete.

The existing companion was built twice using pdfTeX 1.40.25 / TeX Live 2023, then copied beside its retained `.tex` source. Build command:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_feedback7_latex_20261026 misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_coupled_lane_model_candidates.tex
```

Scoped Python/pypdf checks passed: 150 local links; 15 question IDs, 34 high-level candidate definitions and eleven named directions retained; completeness tables and displayed equations unchanged. The 101-file snapshot has thirteen intended existing edits and 88 unchanged files, plus two new Markdown artifacts. The six-page PDF matches its build, has text on every page and has no LaTeX warnings/box issues. No raster-inspection claim is made. The result is `/tmp/urban_feedback7_check_20261026.json`. Read-only `git status --short` still lists only pre-existing tracked edits to `AGENTS.md`, `PLANS.md` and `memo.txt`. No simulator or empirical-gradient test is performed.
