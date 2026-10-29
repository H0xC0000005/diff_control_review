# Possible structures for the urban methods report

28 October 2026. **Proposal only.** Feedback 11 asks for alternatives to the VSL-derived structure without applying one yet. The current PDF keeps its five-part order: research questions; task and assumptions; traffic model; information/decision tests; complete sensitivity. This batch improves the explanations within that structure.

The urban report has a different explanatory burden from the VSL example. It combines propagation, lane assignment, physical access, head service and receiving constraints. Its central claim also depends on what strong aggregate models can already infer. A helpful structure must explain that causal chain and distinguish inherited ingredients from the particular composition being tested. A catalogue of operators or a chronology of our discussions would not do that.

Use the same example to compare the alternatives: a full left bay leaves a turner obstructing the inside feeder, while the parallel through/right lane can still move. Increasing left service may relieve that obstruction; changing through service may have a different effect. The question is which state description can predict the resulting complete-time response.

## A. Start with the traffic mechanism

Open with the geometry and this blockage example. Use it to pose the information, decision and gradient questions. Then define the traffic and control assumptions, explain how propagation, allocation and service reproduce the example, derive the local and accumulated response, and finish with the comparisons needed to test the claim.

The reader first understands the phenomenon, then sees why each state variable and equation is necessary. Each model subsection answers a concrete question: who has arrived, who can reach a lane, who discharges and what remains. Source credit sits beside the relevant mechanism, with the full attribution record in the companion.

This is my provisional recommendation for the main report. It best addresses the present difficulty of understanding the purpose of an equation before its details. Its main risk is letting one example appear to establish the whole result. The introduction must therefore state that alternative lanes and aggregate inference can weaken or remove the expected advantage; the later tests decide that question.

Suggested reader flow: **traffic example and research questions → task and assumptions → causal model → local-to-complete sensitivity → fair comparisons and evidence limits.**

## B. Separate the model from the study design

Open with the research problem, task and testable hypotheses. Present a self-contained model section covering geometry, state, propagation, allocation, service and objective. Follow it with the sensitivity derivation, then a separate study-design section specifying scenario families, baselines, observations, reference simulation and evaluation measures.

This makes the contribution easier to assess as a paper: the reader can distinguish the proposed traffic model from the experiment used to evaluate it. It also provides a natural home for the literature position of each ingredient and for a concise account of what is newly composed. It would become especially useful when numerical experiments are available.

The risk is that the reader meets a substantial model before fully seeing which comparison each detail enables. The opening example and short causal introductions would still be essential. At the current methods-only stage, the study-design section must not read as executed evidence.

Suggested reader flow: **problem, task and hypotheses → complete model and objective → sensitivity → comparison and validation design → scope of claims.**

## C. Organize around the three scientific claims

Introduce the physical task, then use three main parts: what order information changes, whether it changes a control decision, and whether its gradient predicts useful improvement. Each part contains its traffic example, the required model ingredients, the strongest relevant aggregate explanation and the evidence needed to distinguish them. A shared model specification prevents incompatible definitions across parts.

This gives a reader interested in the scientific contribution a direct route from each claim to its support. The full-bay example would first motivate accessible-state information, then a service perturbation, then its predicted and reference-evaluated consequence.

The risk is repetition and fragmented model learning: the same allocation/service law serves all three claims. Equal present counts also cannot be presented as a universal impossibility result for history-aware macro models. This structure would work better for a later results-led paper than for a first complete explanation of the method stack.

Suggested reader flow: **common task/model overview → information claim → decision claim → gradient-usefulness claim → combined limitations**, with the full equations in one shared specification.

## What is selected now

None of these structural alternatives is adopted by feedback 11. Option A is the provisional recommendation; B suits a conventional full methods-and-experiments paper, and C suits a mature results narrative. The existing VSL order remains a viable baseline after clearer writing. Choosing an alternative would change the exposition, not the closed initialization, allocation, service, information-boundary or objective principles.

[Revised report and reading guide](unified_methodology_draft.md)

## A specific simplification raised during equation-8 reading

The reader needs the traffic rule before the internal clock: a head block consumes part of the timestep's service time, then an already resident next block can use what remains at its own rate. This determines the final transferred amounts even when the global simulation saves states only at timestep boundaries. The main text can explain that rule and a short numerical example, with the explicit sigma/delta calculation retained in the companion. This is a proposed local exposition change, compatible with any of the three structures above; it does not select a new service law, add intermediate-time outputs or reopen event-resolved propagation histories. It is not yet applied to the PDF.

**Feedback-12 application:** the current report retains the original five-part order and uses a fully defined service example plus causal explanation before the sigma/delta formula. The option to move that formula to the companion is not selected; the broader alternatives A–C remain proposals.
