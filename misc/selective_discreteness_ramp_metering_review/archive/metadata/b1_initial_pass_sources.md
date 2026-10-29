# B1 initial pass source archive

Date: 2026-09-14. Metadata and paraphrased extraction notes; no new usable full-text file was saved in this pass.

Later access update, same date: user supplied RM0016 final publisher PDF, 22 pages, preserved under `../user_supplied/RM0016_Zhang_et_al_destination_aware_ramp_metering.pdf`. Full audit: `../../extraction/RM0016_full_text_audit.md`; checksum in manifest. Earlier access attempts below remain historical; no retrieval request is pending.

## RM0015

Michael J. Cassidy (2003), _Freeway On-Ramp Metering, Delay Savings, and Diverge Bottleneck_. Transportation Research Record 1856(1), 1–5. DOI https://doi.org/10.3141/1856-01.

Primary metadata/abstract: https://its.berkeley.edu/publications/freeway-ramp-metering-delay-savings-and-diverge-bottleneck and https://journals.sagepub.com/doi/10.3141/1856-01. Publisher shows an access gate. Two indexed CiteSeer manuscript URLs failed to open. Relevant scope: system exit accounting and metering under diverge restrictions. Full journal article not inspected; not needed in addition to the independently inspected report for the present interim argument.

## RM0016 — full text required

Cheng Zhang; Wei Ma; Jing Zhao; Chengyuan Ma; Yuelong Su; Xiaoguang Yang. _Destination-Aware Coordinated Ramp Metering for Preventing Off-Ramp Queue Spillover and Mainstream Congestion_. DOI https://doi.org/10.1109/MITS.2023.3323029.

Author-institution abstract/metadata: https://research.polyu.edu.hk/en/publications/destination-aware-coordinated-ramp-metering-for-preventing-off-ra/ (2023 early-access/in-press, provisional pp.2–24). Author's university bibliography confirms final citation: IEEE Intelligent Transportation Systems Magazine 2024, 16(1), 40–61: https://bs.usst.edu.cn/eng/2022/0907/c13582a281172/page.htm, publication item 17. Use DOI to identify; final PDF version to be verified on receipt.

Abstract-level relevance: destination-aware predictive control incorporating downstream spillover. Exact state, equations, lane/queue closure and comparison adequacy are unknown. No numerical result is adopted. DOI open failed; title/DOI and PDF searches plus author-institution pages yielded no usable open full text. Institutional request: `../../reporting/b1_access_request_batch_1.md`.

## RM0017

Michael J. Cassidy (2002), _Critique of a Freeway On-Ramp Metering Scheme and Broader Related Issues_. UCB-ITS-RR-2002-4, May 2002.

Metadata: https://its.berkeley.edu/publications/critique-freeway-ramp-metering-scheme-and-broader-related-issues-0. Primary PDF: https://escholarship.org/content/qt804724nd/qt804724nd.pdf. Browser-readable, 24 PDF pages. Inspected §3 and beginning of §4, PDF pp.6–9, particularly pp.7–8 on downstream exit composition and differing source destination shares. Related to RM0015, not assumed to be the same version or counted as independent replication. This source supports the conditional aggregate admission argument, not selective-order fidelity.

Download command: `curl -L --fail --max-time 45 https://escholarship.org/content/qt804724nd/qt804724nd.pdf -o misc/selective_discreteness_ramp_metering_review/archive/full_text/RM0017.pdf`. Sandbox attempt failed DNS; retried with approved escalation. Escalated command reported success but produced zero bytes. Verified size using `ls -l`; removed only that newly created empty placeholder using `apply_patch`. No paper content or user data was deleted. Browser inspection and these notes remain available; **no local RM0017 PDF exists**. Future full-text retrieval should validate payload before reporting success.

## Existing sources/project evidence

Reused RM0009 and RM0002 extraction from the archive rather than redownloading. Inspected closed M1 plan §3.4 and §14, source `ledger.py` lines 466–578, `nodes.py` structural capacities and service paths, and M2 Phase-B revision's neutral-domain statement. No behavioral tests or project edits were performed. Source-specific qualifications in earlier records remain in force.
