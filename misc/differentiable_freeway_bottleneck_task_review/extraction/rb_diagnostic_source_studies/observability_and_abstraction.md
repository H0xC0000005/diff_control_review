# Observability and abstraction — methodology source audit

Inspected: 2026-09-17. New sources use MD-S identifiers rather than modifying
closed FB registers. Selected-method E3 is not traffic validation. Web-accessible
copies were inspected; no new PDF was downloaded, pinned or added to the source
manifest. No inaccessible source is necessary to the reported methodological gate.

## MD-S1 — Hermann/Krener 1977

[Author-hosted 13-page copy](https://www.math.ucdavis.edu/~krener/1-25/10.IEEETAC77.pdf),
IEEE TAC22(5),728–740, DOI10.1109/TAC.1977.1101601.
Introduction/primary indexed introductory text inspected; scanned PDF has no
browser line extraction. Defines state, output and control separately and links
realization/reduction to input-output behavior. General smooth-system framework;
not a certified observability-rank calculation for our driving reference.
Attempted university alternate copy failed. No rank theorem transferred to SUMO.

## MD-S2 — Bekiaris-Liberis/Roncoli/Papageorgiou 2017

[Aalto accepted-manuscript copy](https://acris.aalto.fi/ws/portalfiles/portal/28009519/ENG_Bekiaris_Liberis_et_al_Highway_traffic_state_estimation_Transportation_research_part_B.pdf),
48 PDF pages including repository cover; journal TRB106,1–28;
DOI10.1016/j.trb.2017.11.001. Not the shorter Procedia conference version.
II-B/II-E require per-cell lane-aware probe speed/density/lateral-flow quantities
and lane-boundary flows. III-E/F distinguish strong from weak structural
observability under measurement/parameter assumptions. This is not an estimator
using only our lane-blind observations. II-C assumes positive probe density for
ratio expressions and discusses heuristic empty-data handling. Do not adopt its
observer, random-walk noise or empty-data repairs into the deterministic candidate.
Publisher/Crete routes failed; lawful Aalto full text resolved access. No user request.

## MD-S3 — Li/Walsh/Littman 2006

[Author-associated Microsoft Research copy](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/camera-ready-9.pdf),
10 PDF pages, ISAIM2006. Selected3.3–3.4 and table1 inspected.
Distinguishes model-, action-value- and policy-related abstractions; preserving
an optimal action does not in general make an abstract sequential planner valid.
Use this distinction to audit claims, not import finite discounted MDP theorems
into continuous advice or introduce RL/probability-mass transport. Our initial
finite-menu common-action test is narrower than full sequential planning.

## MD-S4 — Abel/Hershkowitz/Littman 2016

[Official PMLR paper](https://proceedings.mlr.press/v48/abel16.pdf),9 PDF pages;
PMLR48,2915–2923. Selected definitions9/12, theorem1 and5.1;5.2 scope inspected.
Approximate state abstractions can bound behavioral loss under model/action-value
similarity assumptions. Those assumptions are not a measured-observation distance
threshold and provide no numerical bound for this traffic task. No stochastic
abstraction dynamics, error constant or algorithm adopted.

## Reuse and review coverage

Reused FB0026 mean-response study; FB0022/27 history/information lineage;
FB0038/39 mechanism/counterevidence; FB0040 matched-actuator, accounting and
gradient hazards; existing contrast/information audit. Original studies/claims
and archive bytes remain unchanged. This is a methods check, not a reopened
latest-VSL novelty search. New theory sources do not settle the direct root claim.

Exact new queries are recorded in
[query log](../../search/rb_diagnostic_methodology_query_log.csv).
Access outcomes/locations are recorded in
[access log](../../search/rb_diagnostic_methodology_access_log.csv).

Reviewer reasoning, not a source-reported traffic result: sampled-channel
equality is distinct from all-observer impossibility; hidden preparation forcing
needs an explicit availability boundary; finite objective closeness does not
certify gradients; a compressed lane statistic needs its own sufficiency test.
