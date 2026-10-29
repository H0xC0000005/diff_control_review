## this file stores the user questions or feedback of the refinement branch of urban based on the existing review opened on 20 oct 2026.
codex is allowed to modify this file with only one method: once codex answers a question, codex should append the "(answered)" token after that question. if a tab contains multiple questions not clearly separated and it is better to annotate the tab as answered, you can annotate after the tab (e.g. ### 1) instead.

## feedback

### 1
I think these categories definitely help, but I would like to check some further concerns:
1. it looks like most of the categories are independent (3,4,5; 1,2 looks dependent on each other somehow but not entangled), so I wonder whether can we resolve the questions class by class (i.e. modular closure first) instead of pipeline-like procedure centric method. this would be a better logical way in my mind because I don't need to frequently switch context. (answered)
2. the categories definitely help, but I still find it somehow difficult to follow the concrete questions bit by bit, and many stuff included are boundary definitions, behavioral distinction, etc., which are more procedural centric (which is difficult for a human to catch if without the prior knowledge about the procedure that is the case here). so I wonder can we resolve the questions in this way: formulate the logical categories and their core questions for each first, then discuss these at a logical and behavioral (and principle) level; then, figure out the concrete answer to detailed questions while treating these discussions and agreements as guidelines. it this a feasible way to resolve the questions? (answered)

### 2 (answered)
ok, that is clearer, yet I think the unmodified questions are kind of confusing here. they are written quite procedurally. I think it is largely because of the section structure you are instructed in the agent file that you must have e.g. core gap, problem statement, model chain function, etc. these work well in engineering context because they form a set of watertight definition about the problem, but it works the opposite here. by looking at them (especially you write them procedurally and descriptively rather than explainatory and semantically) I feel loss to capture both why this problem is logically important and what is the core problem and its scope that I need to decide. now dismiss this structure for this report and all later reports. instead, the first priority is the ease of human readability and ease of logical understanding; precise definition is good but no longer essential. if elaborative text is not enough, use examples. keep the problem description short but logically straightforward and concise. you should still list candidates, but at a conceptural level about how it works and how it addresses the question rather than descriptive of procedures like now.
please rework the current plan according to these principles. also, these principles apply for all later question statements and candidates.


### 3 discussion for categories 1 and 2 (answered)
if I have any critical misunderstanding that has the risk of misinterpreting a backbone component, point it out and correct it before accepting my decision based on false understanding.
for question 1: I agree with your recommendation (candidate B). logically only allowing initialization by feeding the queue into an empty scenario is an established simulation practice, and I think only the formal experiment result sould tell whether should we perform candidate A upgrade. candidate B is sufficient for dev and early validation.

for question 2: I think candidate B is needed here. here are some justifications: 1. this is the natural behavior where in reality drivers tend to pick the most free lane according to his own perception. 2. if the lane allocation is fixed, it is easy to generate unrealistic/highly synthesized data which I worry (without concrete evidence) that the credibility can get hurted. moreover, by removing lane redistribution and keep it fixed, at an isolated intersection studied first, only the blockage geometry affects the blockage events. this makes the changes of service dynamics fixed, and only changes gradient at threshold points which is bad. with redistribution, the blockage can be continuously dependent on the control policy which is good for gradient. 3. the lane redistribution itself is a de-fragmentation method of packets. and I think the lane redistribution itself should be within the previous review if I'm not wrong, and the assumption that the driver entering the waiting zone should distribute across the lanes so that lanes have near equal preference (an equilibria) should be somehow discussed and established in the previous review. update your recommendation and provide justifications for or against my ideas.

for question 3: yes, I agree that using the rate is natural here. moreover, I think using the rate as the lane capacity is both aligned with common literature approach as well as the established review before. but of course, the rate is dependent on the signal phase, where I am not sure do we need another discussion. to model that concretely.

for question 4: I think local mixing is methodologically sound but it is neither an essential component nor implementationally feasible. intuitively, it can create local flattening or even discrete process in the gradient. even these can be properly handled, it still creates much cross gradient paths that can add gradient complexity with no proven advantage. keeping the exact order should be the correct approach in the link. moreover, jointly with question 2, a lane allocation at the near-intersection zone will dissolve the order into actual lane occupation, purely deterministically. this should be better in terms of gradient path formulation while not making any proven methodological tradeoff.


### 4 answer for further question of feedback 3 response (answered)
question A: I think average service suffice at this stage. a phase structure needs much explicit differentiation tuning since within each phase changing the split yields zero gradient. effective average service is better because it is continuously correlated to the green split.

question B: first thing first, this scenario should only happen if the corresponding serviced lane has zero capacity or the remaining capacity is below a small threshold where upstream packs won't attempt to go downstream at all. otherwise, if the first pack is larger than the remaining space, the first pack can always sliced to enter the grid zone. if the upstream pack is indeed queued, it should be still first resolved by the lane allocation solver and append the corresponding traffic to each of the lane's upstream queue. or simpler, don't go through the allocation solver, just append to the desired lane (because it is far upstream).

besides these, are the four questions in the current gate still unresolved (which ones)? 

### 5 answer to fair comparison part (answered)
What can the simpler models legitimately know?
I think head-on comparison of models is model-dependent and tightly couples with model selection. hence I would like to think about this in terms of limits. 
the rival model should be macroscopic state based, and it should have as much as observed state as the experiment model as possible, while isolating the introduced meso distinction (here the pack ordering). hence the maximum state allowed should be defined as defined states with mesoscopic information aggregated. e.g. the rival model can see the left bay mass and adjacent through lane mass as well as queue speed, upstream speed, etc. of course, a rival model very likely cannot utilize the exact full set, a subset of available information is completely ok. if the rival model can reconstruct the blockage, order, etc. behavior or accurately estimate the effect indistinguishable from the experiment model (within a margin) then the hypothesis is already weak. but by expectation I don't think this is the case at least the literature hasn't shown yet that a macro model can tackle this.
also I think this limit is stronger than your candidates so I hope this can solve the question.

Does the sensitivity count the consequences after control ends?
I think our understanding deviates here. seems you use a -> per-pack or per-mass trajectory gradient respect to TST of the trajectory -> consider multiple or all trajectories and aggregate gradient. I don't think trajectory is the right stuff because it is not natural logic. the natural questions should be: if I distribute more cycle split on this leg, how much traffic can the left turning serve more? it can be zero (blockage) or little (queued or jammed) or much. the core control question should be "if I turn the control knob this way, how can I change the current state and the control target at this step if I did so last time?". so trajectory cannot answer this question.
the ladder structure is sound though. so I think in my mind the gradient steps should be:
1. first answer the question at one timestep, not through a time series. evaluate the derivateive of control variable regarding to TST or other quantities such as queue length and effective discharge. the question to answer is "at this step if I make the cycle longer in this leg, how much can the concerned quantity change and in which direction?"
2. generalize step 1 into a time series and TST wrt. cycle split should be the main gradient concern as this is the core control problem.
I am not sure whether this can solve the question so you can make further elaboration about the remaining parts, or you can close with explaination why this resolves the question.

How should the report make its scientific origin clear?
I think it is more like a presentation issue for the reporting, but it is good to have it here. I agree that both candidates are good in respective contexts so I agree with the recommendation now. anyway the vsl report is good as a guidance example here.

### 6 answer to storage and service part (answered)
Where does a turner reach the bay opening?
the first example of blockage is the exact behavior that should be produced. bay and lane interaction geometry should be modeled in the grid zone because it is near-intersection geometry. I don't think the mouth option is a sound modeling choice. so keep the internal option.
also, the behavior of one-to-may lane mapping should be: if any of the downstream lanes spill back through the mouth, then all of the many lanes that tries to enter are blocked upstream to the mouth. of course this affects lane allocation once queue spills back over the mouth but that is another question. and beyond this, I don't see any additional behavior that the mouth should add to model it completely. correct or improve my idea if wrong or incomplete.

What does “the less congested lane” mean?
in reality, the drivers very largely determine the lane occupation based on the queue (including approaching vehicles) because the perception field is limited. I think using the queue itself (we don't have the necessity to model moving traffic) should be the right step. using service-aware queued work is a valid choice but it is not effective and natural here, because naturally that information should be unavailable to the driver (even the driver can look at the queue the driver needs additional thinking and experience so it is still generally unavailable...)

What order does a split create in a common feeder?
they are both not quite the picture in my mind. I don't think we must introduce an additional rule to determine the lane service order if a pack is distributed along different lanes. the lane equilibrium itself may suffice. continuing from your example:
suppose the assignment is because the bay has already 0.2 units while the left-through lane is empty. if the capacity of both lanes are 1.0, a piece of cake. the allocation is fully realized. if the capacity of both lanes are 0.5 instead, the two lanes can still be filled because the pack is homogeneous. then, 0.2 units are spilled back on the shared lane.
notice that the allocation within a packet can be computed one-shot without introducing the service ordering. hope this answers your concern. if not raise the remaining gap or point me out if I'm wrong.

How does a mixed lane use average service?
yes, s.elapsed seems like a more natural chocice, because it concerns how fast the lane can serve the traffic but not just determining the discharge directly based on budget, skipping the intermediate constraints.

Can another reachable head use unspent downstream room?
I think yes. because we care cycle-aggregated behavior, but not intra-cycle behavior, since we don't introduce phase structure and use effective discharge first, different discharges should semantically mean "average over cycle". so there should not be any explicit order saying who should be served first, else that is dependent on the phase structure. so go with R.reuse.

### 7 answer to teh separate questions from 6 (answered)
Which traffic does a driver count when comparing queues?
let's keep this simple first. the driver only concerns the established queue at the start of the current timestep. this has much simplicity while not sacrificing too much modeling genuity. progressively treating members before the driver as queue is more reasonable but that introduces chained dependency.

How does a homogeneous block enter partly while keeping its commitments?
your interpretation of the example is correct.
I don't get the meaning of this question, as well as necessity. what ambiguity can arise from this example? why we need this extra stuff while I think the example itself is quite self-explainatory? even the core idea is unclear to me.

How do competing lanes share limited downstream room?
intuitively, if multiple lanes discharge towards the same downstream link, their share should be proportional to the green split if they belong to different inbound legs. if they are within the same leg just equally distribute.

amendment:
ok... the issue that the incomining packs will only select the static lane based on the starting snapshot is true. how about in this way:
the stored content in each lane should be movement order, while the packs are instantiated downstream with FIFO ordering. so the later packs should take a look on how early packs piles up the queue. I withdraw the previous decision.
instead, the lane allocator just does this greedily: since the route is not important in the mass grid, but the current movement is important, so the lane allocator just receives the packs in order, and for each pack distribute the pack according to the lane equilibrium? in the first version, distribution can be perfect, i.e. perfect equality of the same movement group lanes, but that will be equal to merging the identical lanes into x-times capacity single lane. later the distribution can be imperfect e.g. the pack has a desired lane and distribution preference; in this case there may be no way to calculate this jointly. but currently I agree that it is very like your interpretation that the packs can be distributed in batch, but not quite "jointly" because e.g. the heterogeneous packs order in a shared lane may be natural and straight forward to construct with sequential but troublesome for a joint allocation solver.
the distribution based on lane queue equality should be differentiable though there's quite some min operations. 

### 8 (answered)
Which queue-based explanation should be the principal B1?
it looks like this is more like an intra-model question. I think as long as the model's input is within the avaialble macro information constraint, it doesn't matter how the model explains the blockage or the pack ordering. I think if this is the case, the soundness of the selected rival model should be a more prioritized concern, followed by the alignment to the task and easiness to import/implement.
so both options seem methodologically fine to me at this point, though I'm not sure how would they work in the implementation. the question itself, under my justification, seems invalid at this point.
currently A seems more sound because it is queue-based. movement conflict is not a part of the current scope.

Which lane/storage explanation should be the principal B2?
also, this looks like a problem within the model selection. again, the two options seems both within the agreed information constraint, and (from your elaboration) the selection of model class does not make a methodological choice because it is covered by the constraint.
currently, it seems that A is indeed more sound. B seems like adding another layer of intermediate dependency.

though, the concrete selection of rival model is dependent on the exact state representation and even implementation, but at the current methodological level, I think this should be suffice. also point me out if I make any principle mistake.

### 9 (answered)
I think the question itself is again valid under its setting, but to me it is not sound because I have a different assumption.
you assume that the lane allocation should be counted before knowing the actual discharge capability. but I think the allocation should be counted based on the known actual discharge capability.
if discharge capability is known before the allocation, and the allocation is counted based on the actual discharge capability, the problem no longer exists. I think your raised question arises because of the inconsistency between computed allocation and the actual discharge capability as they don't dependent on each other. I think computing the allocation based on the actual discharge capability can introduce the consistency at the root level.
of course the actual discharge may change during the allocation process because the physically realized blockage or something, but that does not affect the logical dependency under my assumption.
answer this question only. do not continue to the next step.

### 10 answer to first report draft questions (answered)
1. Which lanes may a left turner use?
I think this is totally dependent on the scenario selection. both are sound engineering choices in some real life instances. but for a scenario to start with, I think candidate B is a better choice because it introduces a heterogeneous ordering on the shared lane.

2. Where should a new lane choice become binding?
I think this should be discussed already before. the general idea is that the first traffic commited onto the lanes already should be counted by later traffic. looks like the candidate B is the choice but I wonder how different this question is compared to the previous raised one regarding whether later traffic should consider early traffic committed at the same step.

3. Does the unadmitted remainder receive a binding lane target now?
no, it should not. it should be kept at the ending of the link and serviced first next time, while only blocking further packs of the same movement. e.g. when a left pack is blocked and cannot enter, the allocator should look at further through packs if still has through service capability.

4. If old multi-lane targets are binding, how should scarce entry be shared?
it looks like yet another allocation question to discuss to me. you don't understand why it is a new question from the previous ones clear enough and I cannot understand the question itself and necessity to raise it. explain it more clealy and logically.

5. Does downstream receiving act as an average rate or a consumable timestep allowance?
ok, seems like this is a more fine-grained version of the previous question. I think A is mathematically simpler because in candidate B, the remaining parts of the shared discharge is dependent on the discharge capability of early discharge so it is a sequential dependency, while A only slices the time and there is no sequential dependency of different discharge states. retain A.

answer the questions only and mark which ones are resolved and which ones are still open. 


### 11 pdf revision
pending points:
user proposed 3-lane case
explicitly state the meaning of lambda in equation 4. I don't think it is present in the current version. I think it should be explicit that this is the lane solver dynamics. also the purpose is to solve lambda. V's logical meaning should be better to be explicit.
plus the wordings in console discussion

other improvement suggestions based on semantics and personal views:
there are still some wordings such as "These admission/scan rules are defined here from the agreed traffic policy." from section 3.2, that targets me. recall that the purpose of this report is to inform the colleagues so they should not be present in the final version.
some of the wordings are too compact e.g. "pre-truncating candidates to the earliest S mass would recreate cross-movement blocking..." that are very hard for my colleagues to unpack as this kind of compactness are larely procedural. remember that ease of understanding, clarity of logic, and readability are top priority over compactness.
some of the wordings are meaningful but not direct or weird to human. e.g. "Retained cohorts keep their original eligibility...". we researchers don't pretty use fluffy words, and we tend to use standard terms and plain language as much as possible. using plain language should also help to promote readability and ease of understanding.
the equations are clear and concise after the discussion with you, yet I think many of them are not intuitive to the reader. it should be good to introduce the core idea logically in plain language rather than using descriptive and objective language to introduce procedural stuff. I think currently the core ideas are absent from all of the shown equations.
I only finished reading section 3.2 but I think implementing these first should boost my reading much so let's do this batch first

because this structure is borrowed from vsl, it should help presentation much since I and my colleagues are satisfied by that; but since we are working in a different problem setting where the method stack lies in different literature position (and the task setting varies quite much), I wonder do we have any other structural options that should help the presentation. propose some of them but not implement them yet.

### 12 yet another batch pdf revision
for section 3.2, I think the logic is clear; yet the literature dependency is not clear. I think I have viewed some papers about "lane equilibrium" though I cannot remember the names exactly... we should mention the dependency. also check other components: if the core idea or the key idea of that component is dependent (borrowed/adapted/instantiated) from a literature idea, state it. if an equation also has such dependency, also state it, like what you do to denote LTM dynamics in section 3.1.
around equation 6 and 7, eta_ij is used but not defined, and unexplained. not sure is there any other similar notation problem. I think we need some notation cleaning here.
equation 8's description is too procedural as discussed, making the reader hard to follow the logic. also, the connection (as you asserted in the console) to the previous part of this section is not defined, making this part more disjoint. fix this. either use elaborative full example defined or logical and intuitive elaboration, and don't contain boundary conditions such as "This is an internal calculation of the timestep total; it neither introduces an active signal phase clock nor replaces the linearly interpolated propagation histories." because this means nothing in conveying the methodology to the colleagues.
I think two pieces are still missing from the report: the CTM based near-intersection mass grid; and the link-wise and per-lane ledger (and how it propagates the gradient relatively friendly). these were present in the previous review and task plans. I think they are key components of the stack. if they are indeed necessary to form a complete report, include them, or justify why they are not quite needed here.
equation 10 should be more explicit as discussed. moreover, the part "No entry segment exists when inflow is zero. Internal section crossings retain route position; the junction crossing advances it. Exact-compatible adjacent records may merge while preserving route, order and timing. A movement grid summarizes mass along that order without replacing the exact head record." is a bit "encrypted" as a reader with no prior project knowledge (and even me) cannot quite catch the core idea. I think introducing why this traffic availability is needed (e.g. sequential and time-aware discharge between timestep needs this, of course more than that) is much more valuable. substitute that into more logical and elaborative content that can explain the core idea and component clearly.
for equation 11 (TST definition), since I think it is a very core equation in the control question, it deserves a replication of variable meaning and core logic of terms. currently they are absent.
V0-V4 comes from the old review, good to have them but I think should state the purpose clearly: the ladder is a progressive ablation series; currently the purpose is not stated so I worry that the reader may misunderstand the purpose
the paragraph "Compare B0 aggregate, B1 structured movement queues, B2 responsive lane/storage aggregates and B3 selective ordered state under the same population, geometry, action and time account. These roles describe models, not a universal hierarchy of information. A macro model may read the original fine time series through its own converter or estimator. Its retained variables, memory, observation schedule and calibration must be declared. Successful aggregate inference is a valid explanation; an estimator retaining the full ordered ledger uses mesoscopic state. Equal current counts do not imply equal information in all histories. Distinguish a one-step test conditioned on observations, prediction with later observations, and forecasting without them; state which data remain fixed under a proposed service change." is fully procedural. don't do this, this even confuses me and breaks the flow of the writing. state the brief core idea logically or otherwise remove this.
the readers can be easily confused by notation B1/B2... they are internal notations. also don't use these. briefly expand inline if necessary. but currently the paragraph "The working B1 source is the link queue model [3]; the working B2 direction combines lane-exit allocation [4] with a sourced finite-storage/access adaptation, for which [5] is a candidate. Each complete baseline must be checked for physical soundness and task fit. Citation alone does not establish a valid bay-entry composition." is a citation check, good to have, but the purpose is unclear. I don't see a relationship defined to the ablation ladder or the chosen model stack, so it is like hanging.
for V4, the term "held-out" is too abstract and not concretely defined. held-out on what?
for the sensitivity (section 5), using the over-dot is completely valid, but personally I prefer to use delta(x)/delta(y) or dx/dy form which is more self-explainatory
also, it is important to introduce that how the gradient can penetrate each module, but currently a overall line that shows the logical or highly analytical gradient path is missing. so the readers have to build up the pieces on their own, imposing significant understanding difficulty.

I haven't finished reading yet but let's do this batch first. highlight the changes in moderately saturated and bright red.

### 13 yet another batch of pdf revision
first, remove all the red from previous steps.

M_xy and n_l should be explicitly and briefly explained in equation 11.
the equation 14 above refers to w_lcr to eq.11 but it's not there. also it should be explained.

the explainatory idea of equation 15, as well as 16; the key notation is defined previous but not referenced or recalled respectively

record a dialogue entry: you said "
I prefer your option 1, with a small refinement:
1. Lead with the mass-balance statement: dV/dα=∑_{ℓ} dx_{ℓ}/dα. Its traffic meaning is that changes in total admitted mass must equal the combined changes in individual lane admissions.
2. Immediately below, give the categorical expansion of each lane’s admission gradient. This directly explains the terms being summed.
3. Put the solved filling-level gradient in a separate equation, introduced by: “Substituting these lane responses into the mass balance and solving for the common filling-level sensitivity gives…”" for the eq.15 presentation issue discussion. I agree to improve via my proposed option 1.
eq.16 has a similar problem so this improvement logic should also apply to eq.16.
eq.17 describes a different formula but the presentation issue is similar.

though I clear through the gradient section and can understand each of the gradient component, and we have a clear gradient overall path, and I can get the rough mapping between each discussed point and the big map, but I think it should be even better to emphasize what role does each part of the discussed gradient formula has in that big map. in this way the reader can from time to time refresh the relevant position and construct the gradient path with a clear framework in the mind. currently I think the framework sense is not strong enough when the user sees tons of bricks and motar. a reader should be able to look at the framework by sequential reading from time to time.

differentiation equations should reference which equations it differentiate; otherwise it is quite possible to introduce misunderstanding when the reader tries to pick its source

state explicitly and clearly eq.17 only considers the head clearance path of eq.8, and also the brief intuitive idea 

substutute the detailed example with task elaboration; also it should state why this is related as a relevant case of some differentiation formula or fit some role in the gradient path


