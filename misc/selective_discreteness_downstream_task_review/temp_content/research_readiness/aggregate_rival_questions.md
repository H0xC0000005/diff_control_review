# Aggregate comparison models: selection within the agreed information boundary

**Policy discussion closed by the user, 26 October 2026.** The options remain a record for later concrete model selection. A/A are working preferences; exact equations are not approved by closure.

[Recommended next work: unified methodology draft](methodology_draft_next_work.md)

26 October 2026, updated after feedback 8. **The methodology-level discussion is settled:** both families are eligible under the agreed information boundary; later concrete selection prioritizes model/adaptation soundness, task alignment and then import/implementation ease. The user's working preferences are A for B1 and A for B2, not approval of unspecified equations. The options below remain a candidate record for later model definition, rather than mandatory new principle-level choices. No next batch, implementation or experiment is opened.

[Separate feedback 8 response and corrections](../../reporting/research_readiness/urban_feedback8_response.md)

A turn bay can have room while traffic on the common feeder prevents a turner from reaching it. The proposed model retains ordered packets to explain that obstruction. Before claiming that order is needed, we need strong aggregate rivals that can explain queue buildup, lane use and physical blockage in their own ways.

The agreed sequential packet allocator, lane order and average service are not reopened. B0 remains the homogeneous reference and B3 the ordered model. The choice among admissible B1/B2 explanations can wait for their concrete states and equations. Information eligibility does not itself establish soundness, equivalent predictions or task compatibility.

## B1 candidates for later concrete selection

Consider left and through demand sharing an approach. Left service becomes restrictive and its queue grows. Does the rival explain the resulting loss of through flow through evolving turn queues, or through a geometric rule describing how much one movement restricts another?

**A — Evolve separate turn queues.** Wei and colleagues' turn-level queue-transmission model is the concrete starting point. Its green-fraction input and fixed-speed branch are relevant here. Its common/turn-link geometry and actual service law still need compatibility review. The traffic idea is to explain changing obstruction through evolving movement-specific queues, rather than infer it solely from one link total. [Primary model, §§2.1–2.3](https://arxiv.org/html/2310.12249v2).

**B — Describe partial obstruction between movements.** Specify, from the lane geometry, how much of through flow is affected when the left destination is constrained. Wright and colleagues' partial-FIFO model provides this explanation through restriction intervals. “Partial FIFO” means an obstructed movement need not stop all unrelated lanes. This directly represents cross-movement obstruction without storing packet rank, but the restriction geometry must be specified independently of the test outcomes. It is a node rule coupled to a propagation model, not by itself a complete queue-evolution model. [Primary model, §3.2](https://arxiv.org/html/1601.01054v3).

In the shared example, A explains the growth of directional queues; B explains the spatial extent of a restriction. They can overlap in behavior, but they are distinct principal formulations. We should not combine whichever features happen to produce the strongest result and call the mixture a published model.

**Working preference: A, subject to concrete soundness and task fit.** B remains eligible: partial FIFO describes physical queue obstruction, not a new model of conflicting signal movements. Queue-based structure alone does not establish A's superiority. Published existence or a simulation result does not supply a validated derivative for the adapted task.

## B2 candidates for later concrete selection

Now give the rival the same physical bay length, lane permissions and storage. It must distinguish a full bay from a vacant but inaccessible bay. This is a stronger challenge: perhaps aggregate lane states and physical queue interactions are sufficient even without an ordered packet ledger.

**A — Combine endogenous lane allocation with one declared physical-storage/access law.** Use Gong, Bliemer and Raadsen's multilane equilibrium node as the allocation anchor, with a specifically identified lane-storage/blockage source. Its native allocation concerns sending flow at link exit, not traffic entering a finite bay. The composition therefore needs an explicit bridge between those operations; the word “equilibrium” does not make it identical to the newly agreed B3 allocator. This is a modeling direction whose joined equations are not yet qualified. [Allocation source, §§4–5](https://doi.org/10.1016/j.trb.2025.103208).

**B — Start from a coherent published lane-group physical-queue model.** Liu and Chang's formulation explicitly represents lane-group queues and blockage of entry into a target group, including unavailable storage and obstruction by another queue. It offers a concrete alternative starting point for the bay example. Its native movement-to-group mapping and binary signal status differ from assumptions that must be checked here; it cannot simply be labeled the same responsive allocation and average-service model. [Author-hosted paper, §2.4 and Table 1](https://attap.umd.edu/wp-content/uploads/2022/05/TRC522.pdf).

A prioritizes endogenous lane allocation and makes its composition visible. B prioritizes a published account of physical queue interaction and makes its necessary adaptations visible. Neither is currently a fully specified B2 for this task. B can replace the principal B2 only if it satisfies the accepted lane/storage and responsive-allocation role; otherwise it is a useful supporting comparison, not permission to weaken that role. Gao's directional-queue model remains supporting context rather than an assumed ready shared-lane bay model.

**Working preference: A, with a specifically justified physical-storage/access source still to assess.** This adopts no combined equations. B is not excluded for having intermediate dependencies: A also joins mechanisms, and actual representation determines their complexity. If A cannot be joined faithfully, another compatible realization remains eligible without repeating a generic family-choice vote. A real change to the accepted B2 role would still need an explicit scientific decision.

## What is already fixed for this comparison?

Both rivals may access the original fine-grained series through their own declared conversion into macro state, including legitimate state estimation and observation updates. Native models may use subsets. Successful aggregate inference counts against needing an explicit ordered ledger. No common preprocessing filter or autonomous-only restriction is introduced.

Likewise, equal current queue totals do not prove that a history-aware macro rival cannot distinguish two cases. For example, left-before-through and through-before-left can give different realized shared-lane service; whether a rival predicts that difference depends on its full retained record, not just one snapshot. Preparation must respect the agreed loading-from-empty construction. These are reminders of agreed fairness, not extra questions in this set.

The physical task, effective-service action, complete TST and accepted evidence obligations remain common. Source-faithful native laws may differ, but their adaptations and resulting capability differences must be visible. A win over one selected rival is not a proof that all macro models lack the relevant information. R1/R2 remain forward references rather than gradient baselines; their detailed realization and the sensitivity derivation are outside this question set.

**No further principle-level reply is needed for these two family choices.** The selection policy and A/A working preferences are recorded. Exact representations, equations and adaptations remain later model-definition work; they are not approved merely by satisfying the information boundary. Only a concrete scientific conflict needs to return for a decision. No next batch or construction task is opened.

[Supporting source checks and limits](../../extraction/research_readiness/urban_aggregate_rival_source_notes.md)

[Decisions and closure of the preceding batch](review_decisions.md)
