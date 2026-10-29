# B1 full-text request — batch 1

Date: 2026-09-14. **Satisfied:** the user supplied the requested final PDF; identity, 22-page readability and SHA-256 verified. Full-text audit completed. No action remains on this historical retrieval request. Current checkpoint: `../synthesis/b1_conclusion_checkpoint.md`.

Please supply the following **one paper**. No credentials, database searches or other documents are requested.

| ID | Paper | Identifier | Suggested filename |
|---|---|---|---|
| RM0016 | Cheng Zhang, Wei Ma, Jing Zhao, Chengyuan Ma, Yuelong Su and Xiaoguang Yang. **Destination-Aware Coordinated Ramp Metering for Preventing Off-Ramp Queue Spillover and Mainstream Congestion.** IEEE Intelligent Transportation Systems Magazine, 2024, 16(1), 40–61; early-access record 2023. | [DOI 10.1109/MITS.2023.3323029](https://doi.org/10.1109/MITS.2023.3323029) | `RM0016_Zhang_et_al_destination_aware_ramp_metering.pdf` |

## Why this paper is needed now

It is a close comparator for B1's core idea: controlling upstream admissions while accounting for destinations and downstream exit-queue spillover. The abstract establishes relevance but does not reveal enough to assess its traffic-state equations, lane/storage assumptions, route-memory resolution or the basis of its control benefits.

Before claiming B1 adds a selective-discreteness test, we must determine whether this existing model already captures the proposed mechanism with coarser state, what it omits, and whether its equations can support a fair single-meter comparison. Studying a coordinated-control paper does **not** authorize multiple optimized meters in our task.

**Abstract summary (paraphrased):** the study combines destination-aware traffic evolution and spillover-prevention constraints within model predictive control, using a modified feasible-direction solution method and a Shanghai freeway case study. This is a source-screening summary, not a verified methodological extraction. [Author-institution record](https://research.polyu.edu.hk/en/publications/destination-aware-coordinated-ramp-metering-for-preventing-off-ra/).

## Drop location

`/home/zpz/repos/diff_minimal_meso/misc/selective_discreteness_ramp_metering_review/archive/user_supplied/`

A publisher PDF or complete accepted manuscript is suitable. Please include supplementary material only if the paper needs it to specify the traffic model. If unavailable, say so; we will discuss the evidence limitation rather than treating the abstract as full evidence.

## Access attempts and resumption

Checked the author-institution publication record, DOI route, title/DOI PDF searches and an author's university publication list. The institutional record supplies metadata/abstract but no full-text link; the DOI fetch failed and searches did not produce a usable open manuscript. The author's university list confirms the final 2024 volume/pages, resolving the older 2023 in-press metadata.

On resumption: verify identity/version and readability, archive a checksum and extraction, inspect the model and comparisons, then continue the B1 pass to a supported conclusion. No further B1 selection approval is needed. Stop for discussion at that conclusion before detailed formulation or any scope expansion.
