## this file stores the user questions or feedback of an additional audit to answer the collegues' concerns about baseline models for this project and how the meso components that substitutes the original macro model stack is backed by the literature.
codex is allowed to modify this file with only one method: once codex answers a question, codex should append the "(answered)" token after that question. if a tab contains multiple questions not clearly separated and it is better to annotate the tab as answered, you can annotate after the tab (e.g. ### 1) instead.

## dialogues

### 1 (answered)
recently I had a meeting with my colleagues, and they argue about the foundation from the literature of this work, what literature works can serve as the baseline of this work, and what downstream tasks are good.
they argued that from my presentation my work looks like a model-first project (develop the model first, then find the gap and do the comparisons), which is not sound in their mind. they argued that it should be better to identify the gap first, define the task I want to solve or perform, find the baseline models, then do the model development. though it is likely because I didn't present the literature foundation explicitly and systematically, I think they point to a real problem that the current project's literature relationship and so on are not explicitly defined and discussed, so that it indeed somehow looks like a model-first project.
previously when forming this project, I had reviewed some literature, and the meso components minimally introduced was once introduced because of the gap identified (only introduce the meso component with the gap, so each meso component should explicitly bridge a gap). but yet I don't remember that this project has any clear definitions for my colleagues' concerns. hence, I would like to make an audit to answer my colleagues' concerns. I would like to separate two questions:
A, what are the gaps this project tries to solve, how the model stack is backed by the literature (borrowed from literature, or modified/inspired by the literature), and what can be the baselines to compare with the project model stack
B, what should be the optimization or traffic task as experiments of this project, how the task is backed by the literature (optimization, traffic engineering, traffic sim, etc.), and how to formulate the task for this project
two questions are inter-dependent, but not too much. let's start with question A first because that's the direct concern from the colleague.
I would like you to do a literature review and audit of the project to answer the following questions to answer question A:
1, what literature works can this project choose as comparisons or ablation baselines?
2, how the three meso components related to literature; is each one modified from the literature method?
3, what literature work has similar modeling stack or constraints, or solves similar tasks that can be used in the ablation or comparison of this project?
4, what literature gap this project tries to bridge by introducing a minimal stack of meso components, and how the stack solves the literature gap?
5, how each literature gap is proved by the current literature so that it is not solved by the current works? I would like you to answer this question in bullet-point comparison, for example:
macro diff-sim is well developed because macro is native to differentiation
meso non-diff sim is also well developed and there are very many variants with different resolutions and modeling sets
but meso diff-sim is hard because:
some works model the individual vehicles and some dynamic components, but they have to use gradient estimation (STE, gumbel) which causes much bias or low-resolution
some other works model the exact gradient, but they have to greatly simplify modeling capability (e.g. assume full FIFO and single-lane link)
so the gap is...
of course, this is just a sketch of illustrative example, you should elaborate with scientific reasoning and well-documented literature, as well as clearly defined items so that the gap is clearly defined.

the literature review (paper list) of this project is at /home/zpz/repos/diff_minimal_meso/temp_content/feedback/sup_files/other/paper_archive_2.yaml. papers mentioned in this archive should have higher priority to be presented.
answer the dialogue at a file in a place that you think is appropriate.

### 2 (feedback for initial full review plan) (answered)
I think the plan is a sound review methodology, but I haven't tried to conduct review like this, so I don't have further improvement ideas and let's see what will happen after this plan. 
for the question you mentioned in the review protocol plan (corresponding to the original order of the questions):
1. I prefer the former (with focused synthesis), and I think finding a full coverage for this field is an overkill. the differentiable traffic simulation by itself is a small field now and do not need such a full coverage review to establish.
2. I'm not sure for this question that whether you can access the institutional database. I only have used OpenAthens access provided by my institution (go to the target website, and click the browser plugin to view the material with institution privilege), and haven't tried to use the access in a database, or login to intra database of research.
so it is acceptable to prompt me to use institutional access to retrieve some paper, but as it will be performed per-paper, you should not put database query-like load to me. letting me to retrieve the important papers that can only be accessed with institutional privilege is acceptable.
3. I am the only human reviewer. and the review is not too formal as it is raised by my personal request. and also, I am a phD student, so I am also learning how to do the systematic literature review. your proposal seems like an overkill and it includes much more completeness and coverage than I thought, but I think it is a good time to learn something here so I approve your procedure. you should adopt single-human-plus-AI workflow.
4. they should be included (as discussed) and as you said treating arxiv as alternative and important information source for more recent works.
5. do not review question B. that deserves a brand new discussion sprint. only review within the scope of question A, which is also the major concern of my colleagues.
6. I don't care about the guaranteed and executable reproducible artifact. I even don't care about the reproucibility as long as the review result is well documented and saved. having the review as methodologically reproducible is fine, but you should not spend time in crafting any artifact solely for reproducibility.

### 3 (feedback after phase R4) (answered)

I want to give a little bit feedback here.
when I formulate the project plan, my concern is mainly in differentiality, but not introducing new mesoscopic component. some of the reasoning:
because micro side stack is hostile to differentiability, so begin with a mature macro stack which should be well established by the literature.
meso requires introducing individual identity, which is related to discrete or random process, so need to exclude them somehow, or find a continuous representation of that, but not approximating discrete model into continuous ones while introducing additional structural bias or variance.
and because of I care about differentiating meso while retaining the meso modeling capability (or in other words not simplifying modeling assumptions to trade differentiability), I care about introducing a minimal set of meso components to achieve this. the components from the literature are more welcomed but there's little importable components so the project must do some adaptions or inventions. the important point is that the components are not the novelty with first priority.
if the simulator is well constructed, it should be able to give useful gradient for multiple in-simulator optimization tasks. this by itself should be a valid contribution. downstream tasks are the ultimate goal but it is beyond the in-sim optimization so it is not drafted in details (thus leaving question 2). so the intended novelty is mainly "we can differentiate a true meso simulator, while not trading model capability or gradient fidelity to achieve differentiability, (and it is useful in downstream tasks!)

I think mostly this is consistent with the current review progress, but I would like to discuss whether:
this set of project goal on introduced novelty is well defined, and
does it contradicts with the current review findings.


### 4 (post R5 feedback) (answered)
for the predecessor set, it is promising and most of the papers are in my veiwed archive. actually, since the project spans several exact branch of simulation and traffic engineering, I expect that there should be many works where each work may focus on diverse and different aspects.
for the borderline inclusions, it seems that all works are contextural relevant but there is at least a major gap in methodology. I usually won't consider these in a literature review but since this is the first time I draft this kind of review plan, I would like to relax my constraints. I see no absolute reason to exclude any of the borderline paper given the project context, so I also agree with the group.


### 5 (post R6 feedback) (answered)
the codebook is just convention. I don't feel any discomfort with it since it complies with the community practices well.
for the set of coding of nearest and non-nearest, I go through the descriptions as a double-check, and I spot no methological issues, and the annotations are reasonable so I approve them.
for the minimum comparison ladder, it seems that it is about both how literature supports baselines used in the experiments, ablations, how to interpret the results, and the potential competition risks that may reduce or void novelty. I think 1-4 are valid concerns or experiment settings to verify and distinguish with peer works, but I think 5 is too contextural and it is not a task that can be alone as a standalone valid experiment. it is a valid ablation to compare with hybrid, but I would like to keep this as a second choice since ablation is the matter after defining the project task definition, novelty, and desired tasks to achieve. so I would like to stash ladder point 5.


### 6 (post R8 feedback) (answered)

you list a few requests to approve specific topic, but I didn't follow this order and read the document from the start all the way to the end, because it is quite condensed with semantics and key conclusions. the conclusions are highly semantic and relies on many assumptions and definitions formed before, which are fine here so I agree with your brief arguments. but keep in mind that after the closure of R9, I would like to pack the review into a report for colleagues, as well as further auditing the current project status and plan. so you need to document the review into a closure so that the basic assumptions are well-known in the field or reasonable, and all other deductions and observations can be derived from these assumptions and reviewed works.
so I approve the R8 material, and proceed to R9. remember that you need to document the review into a closure as requested.

### 7 (report for colleagues) (answered)

I would like to include at least the following in the report:
0. question A scope only. this applies to all other items. also treat this report as a literature review and novelty/contribution review, so if any claim needs support from the literature work, do it in the literature review style. also notice that my colleagues are not domain experts in this specific field (though with abundant knowledge in traffic and simulation) so you need to at least introduce the work somehow when they appear first time, or at appropriate place.
1. what literature works can be adopted as comparison baseline, and in which aspects can they support this project as a baseline comparison (especially those that can be adopted in the experiment; how they can be useful in the experiments and what they can bring?); also elaborate for each work, what is the distinctive gap compared to the project
2. overall, what is the gap in the scope of question A that this project aims to bridge (and the corresponding hypothesis to test); what are the most defensible yet distinctive contribution and novelty this project can (safely) claim, and for each point proposed prove with literature works, especially those nearest neighbours, that why the proposed point is not covered by the current works
3. for each of the design of milestone 1-3 (3 meso components), what are the direct anscestors or inspirations of the component or some elements of the component; why these relationships can be established (e.g. structural, functional, modeling constraint similarity, etc.), what relationship can be derived from these works to the whole component (e.g. composition, adaption, or composite relationship where you need to clearly specify)
4. justify with literature evidence why the proposed 3 meso components are a reasonable minimal set to introduce individual routing behavior and queue order, and thus mesoscopic behavior

you may search for additional works (e.g. works on vehicle packages that not directly related to the project) to support the claims or provide basic context, in order to ensure that the claims are covered by literature evidence relatively completely.

here are some practices that I think are good:
keep the reasoning process flat, not nested; if the process is natively nested, prefer explaining the steps with full semantics instead of using symbols everywhere (e.g. assumption symbols), in this way the colleagues can save time in jumping back and forth to query symbols.
at the same time, also adopt the style of essay in terms of emphasizing the conclusions. it would be very helpful to make an explicit backbone of key conclusions and deductions so that my colleagues can always go for proof and process if they find it necessary, while they can learn about the key results without knowing the details if they would like to, without getting loss in the process. also, inside the conclusions or summaries, you may still include related works, but do this in a pure sematic way and keep what the related works do brief.
use ieee citation format. 
write the report in latex code. in this way, you can also work on good formatting of the report, and you can also render formulae if needed. also render the code into a pdf when you finish.


### 8 (chitchat of report modification)
this section is incremental with modification questions, clarifications, and discussions

1. in the gap identification table, item 2 and 3's distinctive gap descriptions are OK, but I am thinking to mark them in more impressive way. I think the core differences here are: whether the movement ordering in the queue can affect simulation result, and thus affecting FIFO and blockage pattern (FIFO, blockage etc. are dependent to the queue modeling or not) for item 2, and for item 3, one of the key difference (and also captured in the current gap description) is whether the computed lane occupation or queue state can be physically achieved by the traffic (the solution achievability is dependent to the queue ordering or not). are these reasonable abstractions for the two items? do we have better way to state them or integrating them into the current gap items? are they good parts to include in the gap table or as independent elaborations, or they are just repetitions of the current content? (answered)
2. the content of section 2.1 is fine, but I think it would be cleaner if you can change the line for the distinctive gap for each item. (answered)
3. in the section 6, the process is procedually correct. beyond this I would like to add another part: my existing read archive (where I have already did some review before). mention how the archive contributes to the review (e.g. how many papers considered are from the archive etc.). also, I think the limitations of this section are mostly scope-specific and procedual, and not related to scientific method formulation. so I would like to remove the limitation elaboration in this section. (answered)
4. remove the subitems between title and abstract (e.g. subtitles, description, and date). (answered)
5. write a separate highly condensed version of the report. this aims for the professor since he is very busy. the highly condensed version (report abstract) should not have reference at last and only contains no more than 2 pages. it should focus on the most important conclusions & elaborations and the utter most important evidences. it should serve the purpose that the reader should know the overall conclusions of the concerned questions (and you may merge some questions if necessary to condense the content) and the result of the review. generate this report abstract separately from the full report. (answered)
6. the overall flow of the review abstract is now quite satisfying, but one point: in the "The literature establishes all surrounding design p oints, but not their target intersection" part, it should correspond to the baseline model study. however, as my colleagues' concerns are explicitly about baseline models, I don't see any baseline elaboration in the review abstract. you should treat the baseline concept as an important anchor point in the review abstract. or at least, you should explicitly state how the reviewed models relates to the baseline model concept. (answered)

### 9 (start of question B)
"B, what should be the optimization or traffic task as experiments of this project, how the task is backed by the literature (optimization, traffic engineering, traffic sim, etc.), and how to formulate the task for this project
"
I would like to have another review on the question B. but first, question B is not for colleague review; it is only for me to formulate the downstream task in more clear & concise way, mainly in scientific sense. I previously thought that it is too early to define clearly the downstream task, but after the baseline  review I find it promising to define the tasks aim to verify the project or pending the project to be solved. but first, I want to discuss about the file hierarchy that fits the question B discussion.
currently, the question A is closed and fixed. and because question B is not a fundamentally overlapping question compared with question A, so it may be a good practice to create a separate folder. but I think we need to achieve an agreement on how to organize the possible product of problem B discussion first. now propose the most suitable method you can think of for problem B discussion, and also provide some alternative, and answer this in the interactive console pending my approval.


### 10 intermediate discussion about colleague's potential concern about question B (answered)
before the plan drafting, I would like to add an intermediate move, discussing a response of my colleague. I think his idea aligns with question B scope very much and he especially points out an explicit and important point.
here is one of my colleague's response, quote:
"
The plan is now clearer to me, mostly via the hierarchy of baseline models in the table. I assume that the first three models in the table will offer differentiability, the fourth won't. Maybe Wang Yu can judge whether the list (together with the referenced works from the text for each baseline) is concrete enough to anchor the experiments for a critical traffic engineer-type reviewer.

One thing to be explicit about early on is what f and x in df/dx will be supported. What's needed will depend on the tasks, so Wang Yu's input will help here too.
"
Wang Yu is a traffic engineer who published quite some papers in urban simulation, but the team I work with has a major focus on traffic simulation with computer science methods (so Wang is also changing his focus somehow).
it seems that he naturally concerns abou the differentiation formulation in the question B. I think as my colleague says the differentiation formula and the gradient path are dependent on the task definition, but I think it may be good to first use some crafted or toy examples to illustrate that how can this be made explicit. 
also, if you find anything that may be important to elaborate so that it can either expand the current definition within the scope or help me to better understand the work of problem B review and possible project plan amendment, you can propose and elaborate the topic.


### 11 prior discussion of the necessity and purpose of this review (answered)
I feel that since this review is not a mere justification review and it is more like methodologically completing the plan, so the establishment would largely affect what will be amended and improved in the project. hence, I want to spend some more time in some prior questions before diving into the actual review execution.
I want to first discuss about the following two questions before expanding them into a review plan:
1. justify the necessecity of a downstream task review. why this review is necessary to form the downstream task first? is this review better than continuing with the current project development mode, that is implementing the model first and then choose the task based on the model? do we have reasonable statements that it is better to review and define downstream tasks methodologically rather than the current project mode?
2. how it should affect the current project plan and milestone plan, both methodologically and engineeringly. e.g. should the downstream task be the primary guidance and affect model selection and design, as an equal pillar, or simply a reference point? of course you should elaborate more than this example.
3. the purpose of the review. (this is a continuation of the previous two questions.) this should be a part of the review plan, but I want to make explicit and correct as this is the utter core. what outcomes should we expect for this review to better define or improve the plan? how should the purpose of the review defined so that it serves the designated effects for the plan?
when answering these questions, you may assume that it is acceptable to redo milestone 2 and discard the current progress if m2 contradicts with the new project scope and method. in the extreme case where sufficient reason can be justify to prove that milestone 1 contradicts with the formed new project scope, milestone 1 can also be discarded, but only do so when utterly necessary with cautious justifications.

### 12 feedback for open planning questions of the review plan (answered)
I read through the plan to the end and agree that it is an acceptable plan. I did not spot any aparrently false logic yet there will be further colleague discussion and my personal improvement ideas after, but first let's close the current plan approval since it is in principle acceptable.
first, the development of the project is halted before the review (no concurrent progress) so request 1 is voided and should be dismissed.
for request 2, the review should be guided by the project scope and should not be exhaustive on the sim-op literature.
for request 3, the search scope is fine. it should be easier to keep the review fit if a sector is missing and added upon requested than searching fields that are proven unuseful or simply for coverage.
for request 4, the gates are fine and necessary. I don't have any comments on them.
for request 5, the green split is indeed a preferred one but I would like to talk about this in more details in my further improvement ideas, not now.
for request 6, you should only work within the review package. do not change any existing project documents unless explicitly requested by me.
report whether this set of decision is acceptable. if there is any conflict or critical mistake, point them out. otherwise, close the current plan and wait for further discussions about colleague feedback and improvement.

### 13 another intermediate move to discuss colleagues' ideas (answered)
I receive a trace of emails from my colleague after some time, and it includes some new ideas. the trace is available at /home/zpz/repos/diff_minimal_meso/temp_content/feedback/email_trace_20260909_downstream_topic.md.
though there are only pieces of new idea, I think we can still form something from their ideas. in my email, I try to summarize what I can do. since this is an open trace, I don't have a template for discussion, but I have these questions:
1. what are the key distinctive ideas that we can extract from this trace? how they can contribute to the current review and task definition?
2. in my response, I try to summarize what are the promising next steps of the topic review and project review. does my summary captures the major agreements and propose a sound next step?
3. anything that you think valueble to extract from the email trace that not in my email? elaborate them.

### 14 my further ideas about good practices or preferences (answered)
overall I agree with the arguments you proposed regarding the email trace, while I think my feedbacks are too specific and they can be dismissed at this point.
I have some further ideas or preferences about the plan, you may admit or refute each of the item if you find good reasons:
1. alongside the task definition, I think it is also important to figure out the baseline task formulation. because as my colleagues concerned baseline model is an important anchor to design the experiment, hence I think the baseline selection and task definition should be also specified along the proposed task formulation.
2. in the email trace, colleagues also recommended the signal green phase split task. meanwhile, my previous experience in traffic simulation is also mainly in tsc, so I prefer to prioritize tsc tasks. this is also somehow a big target since tsc is overall difficult in the mean of traffic engineering and if the diffsim is proven effective in optimizing tsc tasks then the value can be well established.
3. as a preference, for the proposed tasks, while they must comply with the current literature capabilities, I would prefer more semantic and traffic engineering sound, and simple tasks.
4. I think the task proposal part of the review can be further decomposed into two parts. part one focuses on finding a narrow set and more concrete task formulation around green split optimization (which includes the task variants, e.g. with/without lane blockage, and what's the geometry of the intersection; also, what is intended to be verified for each variant). part one not only serves as an example of task selection and formulation, but also a concrete and near-executable plan of the first task. part two should propose further tasks away from the green split or closely related tasks, while it can be more conceptual and propose methodological level algorithms and task definitions first.

### 15 post T3 feedback (answered)
for the paper inclusion decisions:
t0004: reject; micro differentiability must be achieved by approximation if it must be integrated with model stack, which contradicts with the project goal.
t0019: per-intersection tsc method reference only; network level control part outside scope.
t0020: reject unless it has distinctive novel meso formulation compatible with the project; actuated is outside scope of this review.
t0026: probably it yield too little marginal value. it is likely that introducing this kind of methodology complexity won't affect the experiment design much and does not deserve the sacrificed simplicity. downgrade to borderline; if the tradeoff is bad, reject it later.
t0033: if the paper is tightly coupled to gridlock but not analysis on spillback process in a single or simple intersection layout, reject it later.
t0038: reject. it seems irrelevant to the project method and I expect much efforts to adopt their evaluation, and also since they serve a different purpose I wonder is there indeed anything the project can learn from it.
I think papers not mentioned are OK. if you think further description of the paper may alter my decision, you may defer the decision for that paper and elaborate further.
for the taxonoy, it looks like a set with good coverage on the task/functionality choice and correct emphasis on the fixed-time green split. I agree with that.
I don't have any comment on the codebook. anyway, if I have individual questions, I will just ask you instead of querying the codebook so just go on.

### 16 post T6 chitchat (answered)
I think /home/zpz/repos/diff_minimal_meso/misc/selective_discreteness_downstream_task_review/synthesis/experiment_formulation_formal.tex has a good definition about the task formulation (general parts among the variants), and a sound basic derivative framework, but I think there are two points that can be further sharpened and explained.
first, I agree with V0 to V4 as valid variants. I think V5 should be cut from previous set as V0-V4 has a clear scientific design to validate the corresponding factor, and V5 mainly serves as integration test and initial network test. V5 can always be required when necessary after V0-V4 are completed.
under this aggrement, I think the formal experiment formulation should be sharpened:
1. for each variant, how the gradient should be propagated through the new factor introduced in each variant? I think it is necessary to define them formally so that the gradient propagation is well defined for V0-V4.
2. the derivative general formula is sound, but I also concern about the gradient path after the individual components' gradient propagation is defined. I would like you to define the gradient propagation from f to x and clearly define f and x, which should also be my colleague's concern (what's f, x, df/dx, and how it should be computed?)

### 17 post T7 feedback (answered)
since the part 1 is ready to be closed, close part 1.
then, I want to make a goal change for part 2. last week I discussed with my colleagues, and Wang Yu propose me to first look at ramp control on freeway as a parallel second task (instead of a further task). his reasons are:
1. freeway is widely studied and ramp metering is a relatively simple control task in traffic engineering
2. ramp metering is well established and can find examples real life examples that can be imported as simulations, especially in america
3. the literature has long ago proven that controllers such as PID can already perform pretty well for ramp metering tasks
4. the mathematical formulation of ramp control is simpler than TSC, and probably has shorter gradient paths
5. ramp metering on the freeway also have multi-lane, blockage, and spillback behavior, though different from TSC
then, I doubted with the following major reasons:
1. my experience was mainly in TSC, and I only have textbook knowledge about ramp control
2. I think ramp control needs to model lane changes because of merging and evading of ramp traffic, that are outside the current simulator scope
3. it is also highly likely that the speed should be explicitly modeled, which is also outside the current scope
hence, I want to change part 2 into a feasibility study to answer the following questions:
1. is ramp metering a suitable second parallel task to validate the simulation hypothesis, while concerning the scope and component closure of the simulator? what are the logical justifications for the yes or no answer?
2. what are the literature works that can support the justifications?
3. if the task is indeed suitable, what is probably the good task formulation for ramp control for the project?
first, discuss whether the part 2 change is clearly defined. what are the remaining critical plan choices to make before changing the part 2 scope?

### 18 decisions for remaining design choices before part 2 (answered)
for Q1, I think strict compatibility is the bottom line, unless there is another explicit review on the common compatibility of the TSC task and the ramp task. but up to my knowledge, it is difficult as seen in the literature to make the two compatible within one simulator in the backbone unless it is a general simulator. I think the m4(node solver) is the place that needs changes, because ramp control and TSC needs different node solver dynamics. but besides that, I don't see any beforehand necessity to allow modification.
for Q2, I agree with candidate A: it must have diagnostic value or can provide empirical proof for hypothesis validation, otherwise why bother including it? the purpose of the project is not to pass the benchmark. anyway there is no benchmark for similar meso diffsim task definition.
for Q3, the review should be minimal because the feasibility and necessity study is the priority. but if we find that to verify the hypothesis (e.g. to introduce spillback, blockage, etc.)  it is necessary to increase the complexity, it is acceptable to do so with reasonable justifications.

### 19 decision after part 2 phase RM3
I agree that A should be a reference case: it is elementary, and it can show almost no value (that I can think about) to demonstrate the necessity of meso behavior and components (e.g. the ledger plays no effect on the single ramp). it should be a correctness check only unless you can justify any distinct value it can have compared to existing and closed cases.
I think it is not yet the time to close part 2. at least we need to find a convincing enough set of evidences to prove that part 2 is not feasible. I think candidate B is a good point to start, so let's proceed with this first and collect key evidences that supports or against ramp control. 
moreover, I think a key aspect to concern is that what distinct value or hypothesis verification method can the ramp control brings that are different from the current closed tasks? if ramp control itself cannot inject new validation aspects or hypothesis, I think it is a good reason that against this task. but this should belong to a later review phase, or it should be resolved now?

amendment:
I am thinking⠁about the following problem: does one meter case really bring value to the project? literature also sometimes use multi on- and off-ramp cases in the freeway study. in multi ramp cases, the ledger has some value which is quite instinct because it affects lane occupation and weaving. so I want to further discuss the following two questions:
1. what are the proven or possible value that the single ramp case can bring? can it verify the fidelity and unique meso behavior of the current project scope? and to the end, would lane changing modeling be an unavoidable component if the single ramp case is designed to fulfill the project purpose?
2. is the multi ramp case better than the single ramp case? elaborate with literature evidence, and you should also consider the current project scope and closed methodology. 

### 20 feedback after B1 audit
I think according to the diverge verdict, B1-P provides only limited distinct value, and it cannot be treated as an orthogonal standalone task from TSC with distinct value. I think the current evidence is towards the against side, that we must make a significant amount of specific design, modeling compromise, and change of existing milestone to find a narrow way out. hence, for the next step, instead of formulating the B1-P, I want to collect the current fetched evidence (and because I don't have literature knowledge about ramp metering), and do a debate about the evidences first. I have the following concerns, while because I don't have literature knowledge, you should add in important points that you think are important:
1. what are the literature works for mesoscopic simulation of ramp metering? what are the major mesoscopic behavior that such works tried to introduce, and how they are distinct and important from macroscopic counterparts?
2. what are the literature works for differentiable ramp metering? what are the major contributions of differentiability in this context?
3. from my previous review, I see that all differentiable simulation works are evaluated on urban networks. is there any major reason to justify a differentiable work on the freeway control, or the reason is too weak e.g. macro sim and controllers can already provide very good results?
4. for the current set of evidences, remember that the primary target is to construct a parallel second task, which should at least provide some distinct and orthogonal hypothesis verification value for the project. but the current evidence seems not supporting this position. collect the evidences, and justify the reasonable gap between the formulated B1-P and the desired position. is B1-P an acceptable parallel second task with such value? if not, what is the gap? 
besides these questions, you should add essential explanations, elaborations, and additional important point to complement the set and catch my possible misunderstanding and neglegance of important points here.

### 21 feedback after further audit on feasibility
I agree that the original purpose should be refuted, and the reasons I think are sufficient to defer or simply halt D1, and hang the remaining formulations about other research questions.
so, for the next step, I want to do a last sprint to collect what we have already reviewed and discussed, and write a brief report to my colleagues regarding the reviewed feasibility. because it was my colleague that suggested ramp control as a second task, I would like to present the against reasons and the gap clearly. but before the report, I want try to close the current situation via the following questions:
1. list the most important and distinct for and against reasons, at most five for each. each reason should by itself enough to support for or against the decision, if no other important reasons are present. this is the ideal case, if you find it difficult to guarantee such importance, you should first guarantee distinctiveness.
2. is the following report structure reasonable to fulfill my purpose: 
overall conclusion first, including the overall againast position, the closest acceptable position of the task, and the gap of taking the position
the review result of mesoscopic ramp control, differentiable ramp control, and similar works compared to the existing project architecture
key reasons that renders the task as a parallel second task unacceptable
the closest acceptable position if we really want to adopt the ramp control, and that can only serves as a correctness validation role while the cost to adapt methodology and engineering concern is somehow decent 
short conclusion: hence ramp metering is not suitable as a second task
and the short reference list (ieee, and citations should be used through the report whenever literature evidence is needed)
3. what else should we do apart from these two to properly close the review and report to the colleagues?

### 22 discussion about email trace (answered)
the email trace about the report discussion is available at /home/zpz/repos/diff_minimal_meso/temp_content/feedback/email_trace_20260916.md. 
I think via the discussion, the colleagues propose an indeed useful direction apart from our previous "treating the current modeling as the primary anchor" approach. it is reasonable that a similar yet relatively independent task formulation can be found in the freeway side while sharing the similar high-level thinking compared to the current project formulation. hence, I think it may be necessary to start another literature review regarding an individual task formulation on the freeway side. the formulation can disregard the current project formulation and progress, but it should have the same high-level idea, and it should also answer the same set of fundamental research questions about distinct novelty, necessity of meso behavior, and gradient effectiveness. 
but first let's discuss about the email trace. do I capture the overall ideas of my colleagues and propose a reasonable next step? what are the candidates for the next step after this email trace? what can probably be good candidates for the freeway side task formulation (at a very high level)? and anything that we haven't discussed but you think is important to clarify my understanding and teach me the essential literature knowledge?

### 23 discussion after N2 gate
the n2 findings and gate provides a report mainly on found literature evidences and general gap, but I think these questions are still unanswered in the report:
1. what can be good candate as B2 task definition, that the methodlogy is backed by the literature while attempting to address a potential gap?
2. on the basis of question 1, or should be answered before question 1, what should be the minimal information required to simulate some distinctive behavior compared to macroscopic, while keeping that natively differentiable?
I think these questions are important, but I am not sure whether they belong to this phase's responsibility to answer. what should be the key questions to decide at this gate?

amendment: the proposed task is quite sound, and I agree that it is reasonable that the speed control should be dependent on lane occupation, even intra-lane dynamics. but I also think that this is quite a straightforward traffic task, and as you elaborated, it should be established already by some works. also, since the model is more like macroscopic, it is reasonable that it is natively differentiable. since we focus on the differentiability side, I wonder whether the claimed topic is already somehow covered by the literature. moreover, how to justify that the introduced set of components are necessary for the control? what are the intended contributions for this topic proposal?
do a brief review to answer these questions.

### 24
I want to report to my colleagues briefly, so I want a short handout to describe the current progress. I think the review recap from s01 to s06 is a good place to start, just make sure that the modified version is colleague facing, and the readability and semantics should be enhanced because they have little knowledge about the review procedure. also, the handout should be a rendered pdf with at most 2 pages.
besides the handout, you should also provide a small list of bullet points, at most 5, as the most important points in the email body. 

amendment: the overall flow is good, but I want to do some modifications. 
remove the preparation flaw section, and rename the recommended next step as the next step plan; also revise the section to present it more oriented as a next step plan presentation. also do a final check that the handout does not have any hanging symbols and statements that cannot be understand without prior knowledge about the review.

### 25 (answered)
I think the revised ordering is fine and I would like to make this as the next step plan. I want to do these at this point:
1. close the current review with conditional findings (candidate A). document this properly and a later agent should recover the review findings, conclusions, and reviewed material from the documentation.
2. draft a colleague report containing these:
the task formulation of the current review chain (from s01 or earlier preparation stage);
the core review questions, and how they are answered (as a short and major conclusion);
the core gap that why the review questions are not completely answered, what are the gaps (list as bullet point + short elaboration), and why these gaps cannot be further addressed (e.g. negative review findings, or no supportive material, etc.);
what is the formulated task that is proven by the literature, under the current modeling assumptions;
notice that the report should be colleague facing: no symbols and statements that cannot be understood without knowing the project context, and focus on presenting the key conclusions as well as making the report more human-readable and highly semantic.
there is no page limit but since this report serves as colleague report purpose and the item 1 already asks for a complete documentation, you should only present the key methodological findings, but not procedural statements, partial conclusions, etc.
3. log the next step plan at appropriate place.

### 26 (answered)
ok, the question definition is clear here. but I think two options are both not satisfying: option A is good methodologically, but it does not face the representation mismatch directly but instead trying to adapt. option B tolerates the error here and I don't think this error is something that should exist because such error invalidates some methodological modeling assumptions. 
I think here the core problem is this: the representation of the moving constraint is conflicting with the CTM modeling now. the moving constraint naturally requires continuous longitudinal representation because a constraint should be able to move continuously to model the impact. discretize that into ctm cells invalidate this. on the other hand, the intra-cell averaging method of ctm is naturally not compatible to keep a distinct position of the constraint, and the cell boundaries and the moving constraint is naturally unaligned in terms of longitudinal position. instead finding an adaption like option A, I think solving this on a more root level is prefered. 
one mental model that may solve the issue as well as keeping the existing task formulation is as such: throw away the CTM on the ramp. model ramp macroscopically. then, constraints can propagate from the meter into the merge lane, where the longitudinal and driving dynamics can be preserved, as well as how much traffic mass each constraint is leading, and how constraints interact with each other. then if a constraint is admitted to merge into the main lane, use another account model to instantiate the blockage effect caused by slow merging traffic. the leaking traffic issue in this gate would vahish under this modeling because the merging movement is purely continuous. also, since the main lanes are still modeled by CTM, the heterogeneous traffic pattern and admittance of merging are still retained.
the core idea is this: for me it seems that the core conflict is representation mismatch between CTM and moving constraints. since we have closed results on the CTM branch, probably the best way to solve this mismatch is to discard the CTM somehow in the conflicted part. 
but this is just a mental model without any rigorous proof. so I want to first discuss about my thought:
1. is it logically sound and probably a solution to the current question? is the modeling representation mismatch real and a real cause for the current problem?
2. can CTM be totoally or somehow discarded here? what are the reasons that we must retain CTM to support other modeling components or it is feasible to discard it?
3. for the "adaption" method you proposed, how can we justify that it bridges the question with sound methodological explanation, or it is better to attack the root cause (if it is acceptable to adjust established stack somehow without touching the backbone of the stack)? or do we need further justification to find more evidence and see whether the adaption or the representation change works better?

### 27 (answered)
I go with the slides to present the progress to the colleagues, yet we arrive at the conclusion that I may go too far along this line.
for the last week, we tried to find a suitable task formulation for the ramp metering setting while faithfully and conservatively answering the three review questions. but after discussing with my colleagues I think we neglected some additional conditions and thus falls into a review pitfall.
the three review questions are the commonground between I and the colleagues. however, they suggested that another purpose of the review is to find a secondary task for elementary verification of the review question's philosophy. also, the second task should not have a too distinct formulation as the first urban task, otherwise they are too separated in the task pipeline so that it will be more difficult to put them together within one work. also, it becomes much harder for me to have a first easy handle to verify the idea.
so because we have already gone so far trying to construct the ramp metering task, I think we can conclude that the current review already yields a negative result based on the new discussion. I think it is because of two major reasons:
1. the ramp metering task is a rather simple control task, because the controller is very strong (the ramp traffic is totally dependent on the meter policy) and also the ramp policy only changes the ramp traffic where it can be relatively easily controlled by receiving the actual merge condition (e.g. PID control can fit this well enough already)
2. the ramp metering task is too well studied and formulated, and also because of 1 there are plenty of works trying to make the macro information more fine-grained, as well as using truely micro information such as stochastic lane changes, evading, and micro merging which is very hard to be utilized under the review questions.
so I proposed to close the current ramp metering line as negative, and go back to formulate the previous two established tasks, the urban and vsl tasks. we have agreed that the vsl task makes sense (especially by a traffic engineering expert) as an elementary verification task and the established framework makes control sense. it can also generate enough variations by configuring the road geometry, control and interaction zone, and driver behavior such as merging model and compliance. but they are more like drafts (especially vsl task, where the urban task is also formulated methodologically but at a conceptual level) so I further proposed to go back and first refine the vsl task to arrive at a paper-like methodology framework, refine the urban case (from the previous review and task formulation work) if necessary to the same level, discuss with respective experts again, and begin first with the vsl task which should be more elementary and can act as a verification of my idea (while in the previous review the task formulation should be backed by the literature, and should be uncovered by the literature if correctly formed).
so the provisional next steps is to formulate the vsl task into paper-ready level. I see three major requirements to comply with:
1. the formulated method pipeline should be able to serve as the methodology section of a paper (so that I mean paper-ready)
2. the task should be kept elementary and be able to be implemented as the first task to verify the hypothesis
3. the formed pipeline itself (and its modules) should be well backed by the literature, and it should have some distinct control problem where the gradient should be able to solve but not well-solved by the literature existing models. existing work that tries to solve may not matter as long as it is not an established question by a branch of vsl.
the above contents are descriptive stuff about the meeting and my ideas after that. so it is a major change to the current review scheme, where we focused on trying to find a complete modeling stack on ramp metering. so I would like you to answer the following questions:
1. any comments about the process and my idea?
2. is there any major flaw with the discussion conclusion and my provisional next steps? if so, how to fix or improve that?
3. what should be done to properly close this line of review and prepare for the next step plan?
4. should I handle the next step task to another agent (since you are in fully in charge of reviewing and the context is cluttered with several review progresses)? how can you justify your suggestion? to keep agent hygeine, what you suggest to do next?

## user idea cache
this section is only for the user to cache some temp ideas here, and they are highly volatile and changes often; it should not be considered in any of the dialogues.
