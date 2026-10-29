# Executable protocol plan: selective-discreteness traffic-simulation literature review

**Protocol status:** R8 approved; R9 complete and review closed on 2026-09-07  
**Protocol version:** 0.2, incorporating user decisions of 2026-09-07  
**Draft date:** 2026-09-07  
**Default workspace:** `/home/zpz/repos/diff_minimal_meso/misc/selective_discreteness_literature_review/`  
**Review type:** Proportionate systematic mapping review with focused synthesis  
**Reporting basis:** transparent search, screening, and synthesis records informed by PRISMA/PRISMA-S principles; no claim of an exhaustive formal systematic review  

## 1. Purpose and decision supported

This review will determine whether the proposed differentiable selective-discreteness traffic-simulation stack addresses a defensible literature gap and which models constitute fair scientific baselines or ablations.

It is not intended to prove novelty solely by failure to find an identical paper. It will create a reproducible map of neighboring methods, identify the closest prior work, distinguish inherited/adapted/potentially new elements, and define the comparisons required before making a publication claim.

The review supports four decisions:

1. whether the project has a sufficiently distinct and useful research question;
2. which model components are inherited, adapted, or potentially novel;
3. which internal ablations and external baselines are scientifically necessary and technically feasible;
4. whether the current fixed-time signal-control and cross-fidelity gradient task can distinguish the proposed contribution from existing methods.

The review does not approve or amend simulator methodology. Any consequence for project scope must enter the repository's normal milestone decision process separately. Question B—selection and formulation of the downstream optimization/traffic task—is explicitly outside this review and will receive a separate discussion sprint.

## 2. Review questions

### Primary mapping questions

- **RQ1 — model design space:** Which traffic-simulation methods combine any of continuous aggregate flow, discrete vehicles, route/commodity identity, exact or approximate queue order, lane-level state, finite storage, spillback, signal-stage structure, and local multiresolution refinement?
- **RQ2 — differentiation:** Which methods provide exact/algorithmic derivatives, analytic sensitivities, adjoints, implicit derivatives, smoothed or surrogate gradients, stochastic estimators, or only black-box optimization?
- **RQ3 — control task:** Which methods are used for fixed-time traffic-signal optimization or closely related traffic-control/inverse problems, with what decision variables, objectives, constraints, and validation targets?
- **RQ4 — validation:** Which studies distinguish forward fidelity, derivative correctness, optimization performance, and cross-fidelity or real-world transfer?
- **RQ5 — nearest predecessors:** Does any retrieved method combine continuous vehicle-equivalent mass, persistent exact semantic route/order metadata, a bounded lane-local downstream interaction state, finite accessibility/storage effects, and gradients evaluated for downstream signal decisions?

### Focused synthesis questions

- **RQ6 — incremental information:** What information is lost by homogeneous link models, turn-level queue models, lane-group models, partial-FIFO node models, and integer-vehicle mesoscopic LTM, respectively?
- **RQ7 — minimum credible stack:** Which proposed selective-discreteness components are necessary to distinguish scenarios or gradients that the strongest aggregate/lane-aware baseline cannot distinguish?
- **RQ8 — baseline contract:** Which comparator set provides a fair attribution of any benefit to exact semantic order rather than merely to additional movement/lane queue state?
- **RQ9 — novelty confidence:** After database search and citation snowballing, which contribution statements are supported, unsupported, or still uncertain?

## 3. Operational definitions

The review will classify papers from their implemented state and update rules, not from authors' use of “macroscopic,” “mesoscopic,” “microscopic,” or “hybrid.”

- **Continuous traffic mass:** flow/occupancy/count state admits fractional vehicle-equivalent quantities without rounding transfers to individual vehicles.
- **Individual vehicle state:** each vehicle is a persistent simulation entity with at least identity and an individual transition/event/trajectory state.
- **Semantic route/order metadata:** categorical route, route-position, movement, or FIFO-order information persists separately from continuous traffic quantity.
- **Exact order:** the model can distinguish two states that have identical aggregate movement totals but different queue sequences and applies a defined FIFO/order-dependent update.
- **Aggregate composition:** movement/commodity proportions or totals are stored without exact within-queue sequence.
- **Lane-local state:** traffic quantity, queue, service, or accessibility is represented separately by physical lane or lane group.
- **Finite local storage:** lane, pocket, cell, or local queue capacity can constrain inflow and causally propagate blockage/spillback.
- **Differentiable simulator:** the study computes derivatives through simulator dynamics with respect to inputs or controls. Merely using a differentiable surrogate outside a nondifferentiable simulator will be coded separately.
- **Exact/pathwise derivative:** derivative of the implemented fixed execution/active-set map, apart from explicitly reported nonsmooth points; this does not imply unbiasedness for stochastic or discontinuous expectations.
- **Surrogate derivative:** backward computation differs from the hard forward model through smoothing, STE, relaxation, learned proxy, or another approximation.
- **Gradient usefulness:** a gradient direction or gradient-driven decision improves an external, held-out, richer, or real system objective—not only the simulator's own objective.
- **Cross-fidelity validation:** controls or perturbations generated by one model are evaluated under a richer independently specified simulator/model or field evidence.

Definitions may be clarified after pilot screening, but changes must be versioned before full screening and must not be tailored to include or exclude a particular desired result.

## 4. Eligibility criteria

### Include

A record is eligible when it satisfies all applicable conditions:

1. peer-reviewed journal/conference paper, doctoral thesis with substantive method, authoritative technical report, or identifiable preprint with enough methodological detail to classify;
2. road-traffic flow, dynamic network loading, intersection/node modeling, traffic simulation, or traffic-signal optimization is a central subject;
3. contains at least one relevant method dimension: LWR/CTM/LTM/link queue, queue transmission, route/commodity tracking, lane/lane-group queueing, FIFO/partial FIFO, finite storage/spillback, mesoscopic/hybrid resolution, differentiable simulation, traffic-model sensitivities, or simulation-based signal optimization;
4. English full text or an English version sufficient for extraction is obtainable;
5. publication date through the final database search date, with no lower date bound for foundational models.

### Exclude

- traffic prediction or control using only observational machine learning with no traffic-simulation/model dynamics relevant to the RQs;
- generic autonomous-driving trajectory prediction without network traffic propagation, signal-control relevance, or simulator differentiation methodology;
- pure route-choice/assignment theory with no dynamic loading or relevant derivative method, unless needed to interpret a directly included simulator;
- traffic-signal studies that report only controller performance and provide no relevant simulation/modeling contribution, except as task-definition references;
- car-following/lane-changing papers with no connection to the targeted simulator-design trade-off, except a small set used to define what the project deliberately omits;
- editorials, slides, nontechnical web pages, patents, and unverifiable citations;
- duplicate reports of the same method, unless a later version adds material evidence. The most complete version will be primary and related reports cross-linked.

### Borderline rules

- Commercial/software documentation may be retained as contextual evidence but not treated as peer-reviewed methodological proof.
- Preprints are eligible but coded separately from peer-reviewed work; publication status will be rechecked at synthesis time.
- A paper need not be differentiable to qualify as a forward-model or task baseline.
- A paper described as mesoscopic is not automatically included; it must expose relevant state/update or signal-task details.

## 5. Information sources

### Primary discovery sources

- arXiv, searched directly as a first-class source for recent differentiable-simulation and traffic-model work;
- TRID and TRB publisher/index pages accessible without institutional database exports;
- ScienceDirect, SpringerLink, Taylor & Francis, Wiley, PMLR, and other publisher records;
- ProQuest or institutional thesis repositories when theses contain foundational models;
- OpenAlex, Crossref, Semantic Scholar, and Google Scholar for discovery and citation tracing;
- reference lists and forward-citation indexes of included anchor works;
- software repositories only for implementation availability and reproducibility evidence.

Scopus, Web of Science, IEEE Xplore, and ACM Digital Library may be consulted when accessible, but bulk institutional exports are not required and the user will not be asked to execute database-scale query/export work. When an important paper cannot be lawfully read through open sources, Codex may give the user a short per-paper retrieval request suitable for OpenAthens browser access.

Every material search will record platform, query or concept combination, date, and papers retained from it. Exact hit-count accounting is optional when a search interface does not expose stable or exportable results.

## 6. Search architecture

A single mega-query would produce excessive irrelevant control/RL and generic transport records. The review will use four complementary search families. The Boolean strings below are reusable concept templates, not a requirement that the user run institutional database queries.

### Search family S1 — traffic propagation plus identity/order/lane structure

Concept blocks:

- propagation: `traffic simulation`, `dynamic network loading`, `link transmission model`, `cell transmission model`, `link queue`, `queue transmission`;
- structured state: `multi-commodity`, `route identity`, `vehicle tracking`, `platoon`, `packet`, `cohort`, `FIFO`, `partial FIFO`, `queue order`;
- local physical structure: `lane`, `lane group`, `turn pocket`, `finite storage`, `spillback`, `blockage`, `intersection`.

Boolean template:

```text
TITLE-ABS-KEY(
  ("traffic simulation" OR "dynamic network loading" OR "link transmission model"
   OR "cell transmission model" OR "link queue model" OR "queue transmission")
  AND
  ("multi-commodity" OR "route identity" OR "vehicle tracking" OR platoon*
   OR packet* OR cohort* OR FIFO OR "partial FIFO" OR "queue order")
  AND
  (lane* OR "lane group*" OR "turn pocket*" OR storage OR spillback
   OR blockage OR intersection*)
)
```

Alternative field-tag syntax, usable if Web of Science is accessible:

```text
TS=(("traffic simulation" OR "dynamic network loading" OR "link transmission model"
     OR "cell transmission model" OR "link queue model" OR "queue transmission")
    AND
    ("multi-commodity" OR "route identity" OR "vehicle tracking" OR platoon*
     OR packet* OR cohort* OR FIFO OR "partial FIFO" OR "queue order")
    AND
    (lane* OR "lane group*" OR "turn pocket*" OR storage OR spillback
     OR blockage OR intersection*))
```

### Search family S2 — differentiable traffic simulation and sensitivity

Concept blocks:

- traffic model/simulation;
- differentiation: differentiable, automatic differentiation, adjoint, analytic gradient, sensitivity, perturbation analysis, surrogate gradient, straight-through, smoothing;
- task: signal, network loading, control, optimization, calibration, OD estimation, toll.

Boolean template:

```text
TITLE-ABS-KEY(
  (traffic W/3 (simulat* OR model* OR "network loading"))
  AND
  (differentiab* OR "automatic differentiation" OR autodiff OR adjoint*
   OR "analytic* gradient*" OR "algorithmic differentiation"
   OR "sensitivity analysis" OR "perturbation analysis"
   OR "surrogate gradient*" OR "straight-through" OR smoothing)
  AND
  (signal* OR control OR optim* OR calibrat* OR "OD estimation" OR toll*)
)
```

### Search family S3 — mesoscopic/hybrid signal tasks

```text
TITLE-ABS-KEY(
  (mesoscopic OR "multi-resolution" OR multiresolution OR hybrid)
  AND (traffic W/3 (simulat* OR model*))
  AND (signal* OR intersection* OR junction*)
  AND (optim* OR control OR evaluat* OR calibrat*)
)
```

### Search family S4 — lane queues, storage, and signal optimization

```text
TITLE-ABS-KEY(
  (traffic AND (signal* OR intersection* OR junction*))
  AND (lane* OR "lane group*" OR "turn pocket*" OR "movement queue*"
       OR "turn-level queue*" OR "shared lane*")
  AND (spillback OR blockage OR overflow OR "finite storage" OR FIFO)
  AND (model* OR simulat* OR optim*)
)
```

Search syntax will be translated rather than copied blindly. Web and TRID searches will use smaller paired concepts. arXiv searches will cover both traffic-specific phrases and broader differentiable-simulation terms combined with traffic, transportation, signal, network loading, queue, or mobility terms. Search strings will be piloted against the sentinel papers below.

### Dedicated arXiv procedure

- Search arXiv directly for each search family, not only through general web results.
- Record arXiv identifier, subject category, first-submission date, latest version date, and version screened.
- Check whether a journal or conference version exists and link all versions as one study family.
- Use the most complete version for extraction, while retaining the earliest public date for priority analysis.
- Treat public preprints as sufficient to challenge a first/novelty claim, but keep peer-review status separate from methodological relevance and evidence strength.
- Repeat the arXiv search once immediately before closing the review.

## 7. Sentinel-paper recall test

Before freezing queries, the combined search must retrieve, directly or through one documented snowball step, the following known works:

- Yperman — *The Link Transmission Model for Dynamic Network Loading*;
- Tampère et al. — generic first-order node models;
- Wright et al. — high-dimensional node models/partial FIFO;
- Yahyamozdarani and Tampère — COS node model;
- Han et al. — continuum approximation of on/off signals;
- Raadsen et al. — extended macroscopic node model for multilane traffic;
- de Souza et al. — mesoscopic LTM able to track individual vehicles;
- Wei et al. — turn-level queue transmission;
- Liu and Chang — lane-group spillback and blockage signal optimization;
- Zhou and Taylor — DTALite;
- Balasha and Toledo — MESCOP;
- Andelfinger — differentiable agent-based simulation;
- Son et al. — differentiable hybrid traffic simulation;
- Seo — differentiable LTM with dynamic route choice.

Failure to retrieve several sentinel papers triggers query revision before the main discovery search. Sentinel inclusion does not determine the final review conclusion.

## 8. Workspace and file contract

Planned package layout:

```text
selective_discreteness_literature_review/
  review_protocol_plan.md
  protocol_versions/
  search/
    search_log.csv
    search_queries.md
    source_records/
  records/
    master_records.csv
    related_reports.csv
  screening/
    title_abstract_screening.csv
    full_text_screening.csv
    exclusion_codes.md
  full_text/
    manifest.csv
  extraction/
    evidence_matrix.csv
    baseline_feasibility.csv
  snowballing/
    backward_candidates.csv
    forward_candidates.csv
    snowball_log.csv
  synthesis/
    model_taxonomy.md
    baseline_map.md
    novelty_gap_report.md
    evidence_tables/
  reporting/
    prisma_counts.csv
    review_report.md
    limitations.md
  README.md
```

This is a target layout, not a requirement to manufacture empty artifacts. Create only files that preserve useful review evidence. Source records are retained when exportable. Full-text PDFs must not be redistributed when licensing prohibits it; `full_text/manifest.csv` will record lawful local paths, DOI/URL, and access status.

## 9. Import and deduplication procedure

1. Codex records candidate papers discovered through accessible searches and citation trails in `master_records.csv`.
2. When a platform provides a useful export, preserve it under `search/source_records/`; do not create exports solely to satisfy the protocol.
3. Normalize DOI, arXiv ID, title, year, author names, venue, abstract, and source links while retaining identifiers needed to revisit the record.
4. Deduplicate in descending confidence:
   - exact normalized DOI;
   - exact database identifier crosswalk;
   - normalized exact title plus year;
   - high title similarity plus first author/year, followed by manual confirmation.
5. Link preprint, conference, journal, thesis, and software reports of the same method in `related_reports.csv`; do not automatically discard a report that contains unique method or validation evidence.
6. Ask the user to retrieve only individual high-value inaccessible papers after open and author-hosted alternatives have been exhausted.

No useful source record will be overwritten merely to simplify the corpus.

## 10. Screening procedure

### Stage 0 — calibration pilot

- Sample 20–30 diverse candidate records across search families.
- Codex screens the pilot and presents borderline examples and proposed decisions to the user as the sole human reviewer.
- Compare disagreements and clarify ambiguous definitions.
- Version the protocol if criteria change, then rescreen the pilot.

### Stage 1 — title/abstract screening

Each record receives:

- `include`, `exclude`, or `uncertain`;
- one primary exclusion code if excluded;
- reviewer, date, and short note for uncertain/borderline cases.

Conservative rule: uncertainty advances to full-text screening.

### Stage 2 — full-text screening

- Obtain lawful full text for every included/uncertain record.
- Apply eligibility criteria to the full method and experiment, not only the abstract.
- Assign one explicit primary exclusion reason to each excluded full text.
- Borderline model-class papers are adjudicated against the operational definitions.
- Maintain counts needed for a PRISMA-style flow diagram.

### Single-human-plus-AI oversight

Codex performs discovery, first-pass screening, and extraction. The user is the sole human reviewer and checks:

- the 20–30-record pilot's borderline and representative decisions;
- every exclusion at full-text stage;
- every record classified as a nearest predecessor;
- all disputed novelty statements.

Routine clearly irrelevant title/abstract exclusions do not require individual human review unless the user requests a sample. AI assistance and the single-human review design will be disclosed in the final report.

## 11. Exclusion-code draft

- `E01_NOT_ROAD_TRAFFIC`
- `E02_NO_RELEVANT_DYNAMIC_MODEL`
- `E03_PREDICTION_ONLY`
- `E04_CONTROLLER_ONLY`
- `E05_NO_RELEVANT_METHOD_DETAIL`
- `E06_MICRO_BEHAVIOR_OUTSIDE_SCOPE`
- `E07_ASSIGNMENT_ONLY`
- `E08_NONTECHNICAL_OR_UNVERIFIABLE`
- `E09_NO_ACCESSIBLE_ENGLISH_FULL_TEXT`
- `E10_DUPLICATE_OR_SUPERSEDED_REPORT`
- `E11_OTHER`, requiring a note

Codes will be frozen after pilot screening.

## 12. Evidence-extraction schema

Each included method will be coded for:

### Bibliographic and maturity fields

- citation key, DOI, title, authors, year, venue;
- document type and peer-review status;
- full-text source and access date;
- software/data availability;
- related/superseding reports.

### Model state and physics

- operational fidelity class;
- LWR/CTM/LTM/link-queue/queueing/car-following/other backbone;
- spatial and temporal discretization;
- continuous mass, integer vehicles, packets/cohorts, or mixed representation;
- route/commodity identity and persistence;
- exact order, aggregate composition, probabilistic order, or no order;
- per-link, per-movement, per-lane-group, per-lane, or individual state;
- finite storage, queue length, spillback, and backward-wave treatment;
- lane choice/allocation, lane changing, and realized accessibility;
- FIFO domain and partial-FIFO mechanism;
- signal representation and within-cycle effects;
- stochastic elements and structural decisions.

### Differentiation fields

- differentiated inputs/controls;
- AD framework or analytic method;
- reverse/forward/adjoint/implicit/finite-difference method;
- exact fixed-path, smoothed, STE, reparameterized, likelihood-ratio, or learned surrogate;
- treatment of min/max, events, branches, categorical choices, and randomness;
- finite-difference or analytic derivative validation;
- active-set/nonsmooth diagnostics;
- reported gradient bias, variance, failures, or stability.

### Task and evidence fields

- traffic task and decision variables;
- objective and constraints;
- network/scenario scale;
- calibration and initialization;
- forward reference and comparators;
- optimization baselines and budget matching;
- cross-fidelity or field validation;
- runtime/memory/hardware;
- principal findings and author-stated limitations.

### Audit interpretation fields

- relationship to project Component I, II, or III;
- candidate baseline/ablation role;
- required matching assumptions;
- threat to a proposed novelty claim;
- evidence strength;
- reviewer inference, kept separate from author claims.

A codebook with allowed categorical values will be created before full extraction.

## 13. Quality and relevance assessment

Papers will not be excluded merely for low quality unless they lack enough information to classify. Instead, evidence will be weighted using two separate axes.

### Method credibility

Classify each item as `strong`, `adequate`, or `weak/unclear`, with a short reason:

- equations/state/update rules sufficiently specified;
- conservation, units, and boundary semantics explicit;
- implementation or independent reproduction material available;
- validation against analytic/reference/field/richer model;
- numerical settings and scenarios reproducible;
- limitations and failure regimes reported.

### Review relevance

Classify relevance as `nearest`, `direct`, `contextual`, or `excluded from synthesis`, with a short reason based on:

- similarity of traffic physics;
- similarity of retained semantic/lane/order information;
- similarity of differentiation mechanism;
- similarity of fixed-time signal task;
- feasibility of a matched comparison;
- direct bearing on the novelty claim.

The classifications guide synthesis and baseline selection; no numeric scoring artifact will be created solely for procedural completeness.

## 14. Citation snowballing

### Anchor set

Begin with included versions of Yperman, Tampère, Wright, Han, COS, Raadsen, de Souza, Wei, Liu–Chang, DTALite, MESCOP, Andelfinger, Son, and Seo.

### Backward snowballing

- Screen all references whose titles/contexts indicate relevant state representation, FIFO, lane queues, spillback, multiresolution coupling, differentiation, or signal optimization.
- Record the parent anchor and discovery reason.

### Forward snowballing

- Use Scopus and Web of Science cited-by results, supplemented by Google Scholar/OpenAlex/Semantic Scholar.
- Screen citing papers using the same eligibility criteria.

### Iteration and stop rule

- Perform at least two generations from the anchor set.
- Continue beyond two generations only while a generation yields a new eligible methodological family, a new nearest-predecessor candidate, or a material challenge to the gap statement.
- Stop after a complete generation yields no such additions. Record numerical yield at each generation.

## 15. Synthesis plan

### Systematic map

Produce counts and cross-tabulations by:

- state granularity versus continuous/integer traffic quantity;
- semantic identity/order versus lane/storage resolution;
- forward-model class versus derivative method;
- control task versus validation level;
- exact versus surrogate gradients;
- internal versus cross-fidelity/field validation.

### Model-family comparison

Build an evidence-backed matrix covering at minimum:

1. homogeneous differentiable macro LTM;
2. multi-commodity/route-aware macro DNL;
3. turn-level or movement-queue link models;
4. lane-group/lane-aware macro models;
5. partial-FIFO node models;
6. queue-based/event-based mesoscopic models;
7. individual-tracking mesoscopic LTM;
8. differentiable microscopic/agent-based models;
9. differentiable hybrid/multiresolution models;
10. the proposed selective-discreteness design point.

### Narrative synthesis

For each proposed component, report:

- closest antecedents;
- directly inherited equations/concepts;
- adaptations;
- apparently distinct elements;
- unverified novelty risks;
- minimum baseline needed to attribute value;
- evidence required to justify retaining the component.

### No quantitative meta-analysis by default

Runtime, accuracy, and optimization results are expected to be incomparable across networks, hardware, calibration, objectives, and budgets. They will be normalized or pooled only if a sufficiently homogeneous subset is identified and a defensible effect definition can be frozen before analysis.

## 16. Baseline-selection rule

A method becomes a required external baseline when it meets all three conditions:

1. it is among the closest models on the state/behavior dimension central to the claim;
2. a matched implementation or faithful reproduction is feasible without changing either model's scientific meaning;
3. omitting it would permit an alternative explanation that the project merely added an already established aggregate feature.

If direct reproduction is infeasible, classify it as:

- conceptual comparator;
- equation/reference-case comparator;
- executable external baseline;
- held-out richer evaluator.

The final report must not imply that conceptual comparators were experimentally implemented.

## 17. Novelty-claim decision rules

Classify each claim as:

- **Supported as inherited:** direct established precedent exists.
- **Supported as adaptation:** antecedents exist, but the transformation and consequence are explicit and nontrivial.
- **Potentially novel:** no functionally equivalent method is found after database search and snowballing, with uncertainty stated.
- **Unsupported:** a close equivalent exists or the distinction has not been operationalized.
- **Not assessable:** insufficient full text, ambiguous method, or missing comparison.

No “first” claim will be recommended solely from this review. A first-of-kind statement requires an especially narrow operational definition, a completed search log, and human verification of all nearest predecessors.

## 18. Execution phases and checkpoints

### Phase R0 — protocol review and freeze: complete

Deliverables:

- approved review questions;
- frozen definitions and eligibility rules;
- agreed databases and reviewer roles;
- approved search families and sentinel set.

The user closed the protocol decisions on 2026-09-07. A new substantive ambiguity may reopen only the affected rule.

### Phase R1 — accessible-source search pilot

- Translate and test queries across arXiv, TRID, general scholarly discovery, and primary publisher sources.
- Run sentinel recall and inspect the first 100 results per family for precision.
- Revise queries transparently.

Deliverables: `search_queries.md`, initial `search_log.csv`, pilot diagnosis. Stop only if the pilot requires a material scope change; otherwise continue to R2.

### Phase R2 — discovery search and corpus construction

- Codex searches accessible sources and builds the deduplicated master set.
- Request individual OpenAthens retrievals from the user only for important inaccessible papers.

Deliverables: master records, related-version links, and discovery summary. Continue unless access to a nearest-predecessor candidate is blocked.

### Phase R3 — screening pilot

- Review the calibrated 20–30-record sample.
- Resolve criteria ambiguities and freeze exclusion codes.

Deliverables: pilot decision note and protocol amendment if required. Stop only for unresolved scope/eligibility ambiguity.

### Phase R4 — title/abstract screening

- Screen all deduplicated records.
- User reviews borderline records; clearly irrelevant exclusions remain documented without mandatory individual review.

Deliverables: screened set and exclusion summary. Continue to full-text screening.

### Phase R5 — full-text screening

- Retrieve and screen full texts.
- Record explicit exclusion reasons and access failures.

Deliverables: included corpus and material full-text exclusion reasons. Stop for user review of nearest-predecessor and borderline decisions.

### Phase R6 — extraction and quality assessment

- Pilot extraction on 8–10 diverse papers.
- Freeze codebook, then extract all included methods.
- Human verifies nearest predecessors and a sample of other records.

Deliverables: evidence matrix, qualitative credibility/relevance judgments, and baseline-feasibility table. Stop for evidence audit.

### Phase R7 — backward/forward snowballing

- Run iterative citation discovery and screen additions.
- Update extraction for newly included papers.

Deliverables: snowball log, saturation decision, and final corpus summary. Continue unless snowballing exposes a method that may invalidate the project framing.

### Phase R8 — synthesis

- Produce taxonomy, model-family map, component lineage, baseline recommendations, and novelty judgments.
- Explicitly list conclusions changed from the initial targeted audit.

Deliverables: draft review report and evidence tables. Stop for substantive review.

### Phase R9 — closure

- Resolve factual corrections and screening/extraction disputes.
- Freeze material protocol deviations, limitations, search/screening summary, and audit conclusion.
- Identify project decisions that may need separate reopening; do not change project files automatically.

Deliverables: final review package and closure record.

## 19. Reproducibility and change control

- Every material protocol amendment receives a version, date, reason, affected records, and whether rescreening is required.
- Search strings are never silently replaced after results are seen.
- Available source exports remain unchanged; scripts are created only when they save material work or reduce error.
- Random samples use a recorded seed.
- Manual corrections retain a concise note when they affect inclusion, extraction, or conclusions.
- Publisher metadata and DOI records take precedence over informal archive titles or search snippets.
- Author claims and reviewer inferences occupy separate fields.
- Search updates performed later must be labeled as updates rather than merged invisibly into the original search.

## 20. Resource estimate and practical scope control

Workload depends on search yield. Proportionate planning range:

- 150–600 candidate records across accessible discovery sources;
- 80–300 records after deduplication and obvious relevance filtering;
- 30–100 full texts;
- 25–75 included methodological records.

These are planning estimates, not quotas. The objective is credible coverage of the design neighborhood, not exhaustive coverage of all traffic simulation. If yield is much larger, narrow using the approved Question A relevance boundary. If yield is much smaller, broaden queries and citation snowballing before concluding that the field is sparse.

## 21. Risks and mitigations

- **Terminology fragmentation:** “mesoscopic” and “differentiable” are used inconsistently. Mitigation: operational coding from state/update rules.
- **Source overlap:** duplicate and versioned reports. Mitigation: DOI/arXiv/title matching and explicit study-family links.
- **Selection bias toward known papers:** sentinel tests can overfit queries. Mitigation: broad concept searches plus unrelated-result precision checks and snowballing.
- **Recent-paper instability:** 2025–2026 preprints may change or be published. Mitigation: record version/date and recheck at synthesis.
- **Unavailable full text:** institutional access may still omit some records. Mitigation: author repositories, interlibrary routes, and explicit access-failure reporting.
- **AI screening error:** nuanced traffic semantics may be misclassified. Mitigation: calibration, human checking, conservative inclusion, and full-text review of nearest competitors.
- **False novelty by granularity:** a paper may implement equivalent behavior under different terminology/data structures. Mitigation: compare observable state/update capability, not names.
- **Unfair baseline comparison:** different tasks or physics can make performance rankings meaningless. Mitigation: baseline-feasibility contracts and explicit comparator roles.
- **Review scope drift into Question B:** task literature is needed only to classify relevance. Mitigation: record task fields when present, but do not search for or formulate the downstream task in this review; reserve it for the later Question B sprint.

## 22. Closed protocol decisions and next action

The user closed the initial questions on 2026-09-07:

1. use a proportionate systematic mapping review with focused synthesis, not an exhaustive intervention-style systematic review;
2. do not require institutional database exports; use accessible discovery and request only important individual papers through the user's OpenAthens access;
3. use a disclosed single-human-plus-AI workflow;
4. include theses and preprints with separate maturity coding, and treat arXiv as a first-class recent-literature source;
5. limit this review strictly to Question A; Question B receives a separate sprint;
6. preserve enough documentation to support and explain the conclusions, but do not create artifacts solely for reproducibility or preregistration.

The protocol completed without a remaining blocking design question. R8 was approved by the user and R9 closed the review on 2026-09-07. Any colleague-facing report, audit of the project plan, Question B sprint, or pre-submission search refresh is separate follow-on work requiring explicit user instruction.
