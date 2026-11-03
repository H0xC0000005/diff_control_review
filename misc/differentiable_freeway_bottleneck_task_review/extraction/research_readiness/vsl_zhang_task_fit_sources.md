# Zhang task fit: primary readings and evidence limits

2026-11-02. Supports the executed bounded task-fit review and its
[terminal/scope choice](../../reporting/research_readiness/vsl_zhang_task_fit_findings_and_choice.md).
This list records papers actually inspected; it does not add controller
dependencies or archive paper PDFs.

## [1] Zhang et al. — common speed-setting design and candidate aggregate predictor

C. Zhang, E. Chung, N. R. Sabar, A. Bhaskar, and Y. Ma, “Optimisation of
variable speed limits at the freeway lane drop bottleneck,”
*Transportmetrica A: Transport Science*, vol. 19, no. 2, Art. no. 2033878,
2023, doi: [10.1080/23249935.2022.2033878](https://doi.org/10.1080/23249935.2022.2033878).

[Institutional 44-page primary manuscript](https://ira.lib.polyu.edu.hk/bitstream/10397/92568/1/Zhang_Optimization_Speed_Freeway.pdf)

[Institutional metadata](https://research.polyu.edu.hk/en/publications/optimisation-of-variable-speed-limits-at-the-freeway-lane-drop-bo/)

**Reading.** Recheck Section 2 and equations (1)–(6), PDF pp. 7–9;
Section 3.2's parameter representation and evaluation, p. 12;
Section 4.3, equation (12) and Figure 14's accompanying description,
pp. 19–21; Table 6, p. 35; captions for Figures 14–18.
The source's segment settings, throughput task, discrete/boundary
constraints and native CTM branch are distinguished from our adaptations.

**Access.** Web PDF text was readable. Screenshot calls returned no
inspectable images or a cache-miss error, so no new rendered-page
inspection is claimed. An approved curl download to /tmp succeeded after
the sandbox's DNS failure; no PDF renderer was available in the inspected
environment, and none was installed. The source figure interpretation
relies on accompanying primary text, not a claimed visual/code audit.

Temporary copy:

- /tmp/vsl_zhang_task_fit_20261102/zhang_primary.pdf
- 1,585,773 bytes.
- SHA256: cddd8a35c633e811096647ba3d0ad3db0682e41c279379c83669d45bfc2179f7

No new copy is placed in the review paper archive. The reference list is
the durable paper-access record; the temporary copy is not a repository
dependency.

## [2] Hadiuzzaman and Qiu — inherited FD law traced for A's terminal state

M. Hadiuzzaman and T. Z. Qiu, “Cell transmission model based variable
speed limit control for freeways,” *Can. J. Civ. Eng.*, vol. 40, no. 1,
pp. 46–56, 2013, doi:
[10.1139/cjce-2012-0101](https://doi.org/10.1139/cjce-2012-0101).

[Author-uploaded primary full text](https://www.researchgate.net/publication/263387345_Cell_transmission_model_based_variable_speed_limit_control_for_freeways)

**Why read.** [1] explicitly cites this work for its demand/supply diagrams.
Follow that existing lineage only to check the bottleneck's state/location,
not to add its MPC controller, select a new rival or revive ramp control.

**Actual scope.** The author-uploaded article identifies Hadiuzzaman as
uploader. Inspect Section 4.1's upstream discharge/bottleneck distinction,
Section 4.2's finite-cell description and equations (1)–(5), including
the prose immediately around the bottleneck demand/supply and jam-density
assumption. Selected Section 6 text identifies the distinct source cells;
no calibration, experimental performance or complete controller audit is
claimed. The DOI landing-page open was inaccessible via the web tool.

**Use and limit.** Clarifies that the law has a density-bearing bottleneck
region separate from the upstream discharge region. It does not establish
an exact free-exit point counterpart for our fixed task. No source results
or percentages transfer, and no paper code or experiment was run.

## Local analytical evidence reused

- [Complete selected member](../../synthesis/research_readiness/vsl_joined_candidate_contract_and_qualification.tex),
  Sections 1–2, 5–7: positive constant advice, initialized cohort/free
  completion line, X/Z states, full objective and complete derivative.
- [Analytical regularity addendum](../../synthesis/research_readiness/vsl_methodology_review_analytical_addendum.tex),
  Section 3: regular advice intervals and the qualified derivative.
- [Common-controller correction](../../reporting/research_readiness/vsl_shared_controller_correction.md):
  identical control map versus different parameter tuning.

The common B specification and mass-preserving projection are our task
adaptations/analytical reasoning. The unresolved A mapping is a source-fit
finding, not a proof that no compatible aggregate model can exist.
Delle Monache is excluded from the active proposal and is not reintroduced
by this pass.

