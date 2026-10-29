## this file stores the user questions or feedback of the refinement branch of vsl opened on 12 oct 2026.
codex is allowed to modify this file with only one method: once codex answers a question, codex should append the "(answered)" token after that question. if a tab contains multiple questions not clearly separated and it is better to annotate the tab as answered, you can annotate after the tab (e.g. ### 1) instead.

## feedbacks

### 1 (answered)
I just looked at the methods outline, and I find that the opening plan has much more details so I just had a glipmse at it. I want to first explicitly audit that the starting point is correct. also, for the closed ramp metering review, I think one issue that the review goes too deep towards detailed modeling is because I am a bit loss in the series of proposal of procedural next step plans, and there are insufficient audit and thinking about the philosophy and the soundness of local review goals. so I would like to check with my understanding and ask questions based on my understanding to align your review workflows with my logic.
so after I (briefly) read the two materials, I would like to explicitly audit the starting point first. I would first make these explicit to ensure that we have a good starting point:
1. briefly recap the formulated vsl task framework, at component level. I understand the pipeline so you may spend less effort in explaining it but you should briefly do that anyway, and focus more on completeness of involved components and workflow.
2. how the current framework is backed by the literature according to the records: how the components are borrowed or adopted by the existing literature, and why the formulated framework is not well-covered by the well-established models in vsl.
3. what components or flows in the formulated vsl task pipeline should be revised, no matter the reasons are (and not limited to) because the component itself is only framework level and needs refinement, the component is methodologically limiting, but probably need to adhere to a concrete implmentation from the literature, there are new components to be added supported by the literature with methodological or implentation consideration, and so on.
the goal of this step is first ensure that the starting core model is explicitly and well defined, and the next step plan is a reasonable continuation from the core model.
since I only briefly read the material, if I make any principle misunderstanding, point it out.


### 2 (answered)
I only read the starting point audit, but I think that's enough information to raise some questions.
the audit for feedback 1 is clear, and I have some further checks about how should we claim the contribution, or in this refinement of vsl task, what priority in terms of defensible claim should we take.
here is a map that I think workable and suited for the elementary task:
can be claimed (ranked by descending priority):
the usefulness of gradient itself. if the gradient can gives the correct optimization direction while the peer model (aggregation based, and ignores some information considered by the gradient): has performance gap compared to gradient instructed; has worse training process (unstable, noisy, chance for local optima, etc.), need decent or deliberate engineering patch to cover the situation where gradient can naturally give the correct information, or there is no such peer model at all.
the task novelty. little or no work has been tried to apply simulator gradient on this specific vsl task setting, but since we are going elementary, this can be hard to claim.
should not be claimed:
the task is by itself novel
there is no previous gradient based optimization on this (zeroth order gradient is still gradient)
the modeling stack itself is novel
and so on
I would like to make this preference and priority explicit. is this mindset of priority by itself sound, and align with the overall review goal and the intended purpose of the review scope? is this a workable preference for the current vsl refinement?

### 3 (answered) 
it seems that the current review yields a partial result in establishing the lane changing and merging dynamics. there are some fetched models of such that can be used, but they have limitations.
but I concern about the proposed candidate more. changing and evolving the s13 framework model is inevitable and that should be the final purpose of the whole vsl refinement review. yet, your proposal proposes the options as 0-1: either not to change at all or change with some seemingly random and rather procedural descriptions. 
so let's do this in another way. I agree to revise the components, but the old and new ones (and the distinction between the two if necessary, especially for methodological or assumption change) should be marked explicitly (just like a git delta which is a very good practice). so now, explicitly identify, according to the review results at this time, what components in the original framework no longer can serve the review findings, whether they should be changed (other component change may resolve the problem that this component is directly responsible, so a component that has direct responsibility of mishandling may not necessarily be changed). I want to do this explictly and play this cautiously so let's discuss the existing model first, and the proposed changes should be at next step.
also, if I have methodological misunderstanding or any of my claim is unsound, point it out.

### 4 (answered)
the two choices seems like two logical routes, but the descriptions are too procedural, and it is hard for me to capture the big picture, the core idea or the philosophy, and the main changes/addons.
and this happened quite some times before so I want to make this preference explicit and global. when you propose plan options, you should focus on core idea, philosophy, explicitly noted summaries, and major changes in methodology/modeling. this is to ensure the maximum human readability, such that a human can capture these relatively easily and quickly, and understand what each option is doing at a logical and methodological level, rather than diving into the modeling details or so. moreover, I think a straight comparison should help much to quickly and frankly position the options against each other. procedural descriptions like now are ok but only when they helps to serve the previous major parts. you should document this preference and follow it in later proposals. 
and after the documentation, rework the option proposals to adhere to these guidelines.

### 5 (answered)
ok, that somehow helps, but I still cannot pretty get the key differences. so let's do this the other way round. I have a rough mental model regarding this gate as follows:
imagine that there is a "meter" (of course there is no real meter there) which represents the affected effective total service capability shared by A and E as a capability over a point (or a line laterally). then, when traffic on A passes that line in free flow manner, there is no effect on the meter reading (as the default is in terms of free flow capacity). but when E tries to merge onto A and then pass that line, the meter reading will decrease because of E's slow traffic, limiting the shared service. this is also true if there are queues on A that is considerably slow compared to a free flow condition. how the meter reading changes is dependent on the traffic amount discharged, the speed, whether it is from A or E, and the discharge amount function. but anyway that is a singleton effective service accountance and actual discharges only affect the singleton reading (aggregates there), without adding multiple constraints there.
is this mental model a sound design for the gate? which option does it align more? if you think that any part of this model is better than any part of the options, you may revise the options and recommend the new ones. also tell me any additional thing you think necessary to discuss or clarify regarding this mental model.

### 6 (answered)
your concern seems invalid to me. I think in the modeling stack, the queueing caused by temporary merging blocakge or insufficient service capability can already introduces the slowing, so I don't get the point why you explicitly requests a slowing condition for the freeflow. but on the other hand, this is indeed a question that worth considering somehow. I see two options are both somehow reasonable. here are my ideas about them:
a vehicle that travels to the end of the dropped lane, as in reality (e.g. when accident happens on a lane and blocks it), it is forced to merge as established; very likely, it cannot find a gap just adjacent to it (otherwise it can perform the merge before), and accelerating is not an option because it is to the end. hence, naturally, it is very likely that this vehicle has to slow down to find a trailing gap to merge. so forced merge can introduce the slow down is a natural behavior in my mind.
on the other hand, the option D (congestion) is a more natural behavior because the queue can pile up due to various reasons, and it naturally causes the slowing.
so I think the source of slowing is not the problem here, but the major problem is: what kind of slowing behavior, or behavior that can affect the aggregated effective service gate, should we model?
currently both options look fine as by some quick thinking I think they can be modeled macroscopically and also update the downstream meter in aggregated way. also, they are not exclusive so I think picking any one of them while discarding the other totally is not appropriate under my thinking.
so what do you think here? what agreement can we establish? what are your recommended plan based on such agreements, or what you still need to confirm before making a confident and methodologically sound plan?


### 7 (answered)
both of the options are sound model choices, but I doubt whether they model sound traffic behaviors.
I think in this way, starting from the natural behavior of freeway traffic:
I think the sharing of insufficient discharge capability is dependent on how different A and E are. as two extreme cases: when there is a piling queue on E and the traffic on A is free flow, for traffic on E to merge into A, it demands more effective gap to merge, because the speed difference is significant (and after that merge from E impose a somehow slowing effect on A traffic). so there will be less chance for traffic on E to suceed merging, and it takes more effective service capability on the lane A. on the other hand, when both A and E have piling queues, they do not differ much in terms of traffic state (speed) and it is reasonable to assume that they share similar downstream shares, though E has a slight disadvantage due to merge movement and thus takes slightly more effective service, but not much.
the cases between these two extremes, for me, are logical to be blended from these two extremes. and if this is the case, this system can still be modeled in macro way.
so simply taking any of your recommendation is an acceptable modeling choice, but with my thinking, I think both of them are somehow weak in modeling sound traffic behavior. 
what do you think about this?


### 8 (answered)
since the current stack is functionally complete, I want to first do a recap and clarification on the established modeling stack. the purpose of this recap is to put all of the adaptions, improvements, and modifications together into a unified modeling frame. the points that I concern most to fulfill this purpose are:
1. briefly, what is the framework (backbone) of the s13 model (at a framework level), in terms of the components and the component chain
2. from the original s13 model till now, what components are modified, and what components are added; what core question does each included component solve
3. for each component in 2, what is the new formulation; brief mathematic explanation is good. for points 1-3, a pdf is preferred over markdown.
4. a separate report documenting the full mathematical work for the improvements. this should be a pdf as usual.
please do this reporting, and you can include any other points outside the listed 4 points where you think important to elaborate or clarify.

### 9 (answered)
since the step 4 is a closing step without new planned methodological review components, I think it is the point where I would like to also discuss my ideas and requirements to do the project work.
I presented the formulated task setting and stack to two colleagues last week: Philipp is an expert in differentiable simulation but not an expert in traffic simulation, while Wang is an expert in traffic simulation but not an expert in differentiable simulation. 
I focused on:
1. presenting the core review questions/hypothesis, which are introduced many time before so they both understand well and agree;
2. presenting the model stack, in the form of what components are changed from the s13 old stack: pre-merge, merging point representation, merging dynamics, and downstream constraints
3. for eacn component, present the core formulae largely consistent to the previous summary report, and explain what the formulae mean procedurally (the quick dialogue previously is the process where I try to understand the core formulae thoroughly)
both my colleagues understand my elaborations and agree that the task is sound and workable, but they suggest that I should later formulate the task into a formal and compact form, just as those papers where they did a good salesmanship with limited methodology presentation space to achieve human readability and preciseness to define the backbone. they specifically stated that while he can understand my logical explanations, when he looks at the equations they cannot distinguish which parts are our inventions, which are adaptations, and which are borrowed ones. I agree that the clear separation of this is sound, especially because it draws the boundary between my work and the literature in terms of model stack. so I suggested to first present a report about formulated VSL task first to them trying to answer their concerns. the major goal is to document the precise but complete methodology, and to let them fully aware of the logic of problem setting, task definition, modeling components, as well as key equations.
so it seems that there are something misaligned in my presentation style, as I have a strong engineering background and relatively (~1yr) new to pure research. so I would like to first discuss what are the good structures and rules to write a report in this manner. first, here is my mental map of my current idea to write the report:
1. the core review questions, but keep very simple because it is emphasize pretty some times
2. task definition/problem description (short): what is the concrete problem that the vsl review and refinement tries to work on? the case should be concrete and specific, all categorial or abstraction concepts should be defined concretely as possible unless the abstraction is explicitly required by the model stack or task formulation; and what are the criteria that the formulated methodology should fulfill to answer the core questions. clearly state which functional component within the backbone is which work, e.g. adapted/borrowed/invented/inspired etc.
3. model structure. first introduce the overall formed model stack (short), and then introduce the 4 revised components. for each component, I think a paper-like methodology like description should be good, which focuses on human readability and the preciseness to present the methodology backbone. equations can be included if necessary especially in cases such as precisely define the core dynamics or targets etc. use illustrative plots only when text and equations cannot plainly convey the idea with high readability.
4. how the formed modeling stack aims to answer the review questions
5. the complete gradient path, but with only critical gradient steps shown
so with my idea shown, I would like to discuss how this report should be written first:
1. is my idea by itself a sound report structure? can it fit my reporting goal as stated?
2. what amendments, improvements, discards, etc. can be done based on my idea with good justification?
3. what are your proposals of the structure regarding my experience and intention of this report?
4. how consistent is my and your proposal compared to the previous step4 proposal? any major inconsistent points if we fuse the plans into one unified?

### 10 (answered) 
some last notice for the report:
1. the report should be a latex rendered pdf, preferably no more than 2.5 pages; and you should at least use font size 10 for the main text
2. for the notation, reuse the existing defined ones if possible, or well-admitted ones in simulation or traffic; formulate the fomulae so that the reader may spend less time checking back and forth together 
3. only present what we have now as the report serves to convey the whole modeling methodology and stack so functionality is the priority; no need to talk about the limitations that I will mention briefly when I send the report within the email
and open up writing the report with these additional rules.

### 11 amendment requests for the report
you'd better mark each item answered instead of the overall tab since this should go some back and forth rounds
the page limit now relaxes to 3.5 pages (excluding reference) but you should still add contents cautiously, only claiming space that is necessary. the relaxation is to free you from revisiting other contents to claim some space so that you can focus on improving the new content only. but if the additional page is not enough you still need to do house cleaning.
1. section 1 (research question) collapses the questions too much into a single paragraph. I prefer to still express the three core questions in bullet form.  (answered)
2. section 2 (task and global assumptions) has similar readability issue as item 1 because the reader has to do the work by himself to slice the points which requires nontrivial work for the global assumptions. introduce the assumptions as introduction (if any) + bullet point form. the core idea is to do the assumption segregation and granularity for the reader. also for the task definition part, I prefer to explicitly mark the task as a concrete task (a specific case, not a class or abstraction). (answered)
3. I would like to see a brief logical chain in the task definition section that: "what are the literature supported criteria that such kind of a task should fulfill to be deemed good?" -> "how peer works do not suffice such criteria under the current task setting?" -> "what are the core criteria that this project tries to achieve?" a brief chain is enough but I think it should be present. (answered)
4. for the key behavior definition equations, I think it should be better to put the literature source directly after or before the equation, since this is the important point that my colleagues concern about. (answered)
5. I think the introduction part of the traffic model section is too short and boring. I think it should be better to convey a mental map to the reader first: there are pre-choke merging attempts, forced merging at the choke on E, and discharged slow traffic from the choke can still affect upstream traffic. the current version is too procedural and it can confuse my two colleagues even if Wang who has abundant traffic simulation knowledge. also, the mental model should serve as a brief guidance for the reader to have a brief impression about how each component works. (answered)
6. in the section "Forced merging and service sharing", there are quite some variables so I think explicitly saying that "solve for g" is good here. and what is g{}? previously I think you said that this is a pluggable function, but we should assign a concrete form for it. what should be it? (answered)
7. I think the sentence "Entry rates vanish outside that interval; negative-time counts are zero" is procedural in the section "Finite terminal and the merging point" so I prefer to remove it, or you have justifications that this is essential here? you should also check this for other sections. I think the beginning of the section should not be this kind of procedural or boundary details. (answered)
8. I think u_j should be a speed, but you use (in my eyes) weird terms "free marks" and "queue marks". it this literature backed term or we better use the very conventional term "speed"? (answered)
9. the sentence "At an actual zero hit, retest free admission; equality retains feasible free continuation. Use right-hand arrivals at jumps and retain recovery history across transitions." is confusing even to me. what are the core ideas here? I suspect that this is either terminology issue or you should present that at the level of logical core idea but not procedural context. (answered)
for these points, first highlight the changes in red for ease of trace. later I will explicitly tell to move back to normal color.
10. also, section 3.4 begins with a procedural content without introducing the core idea or behavior or begin the equation chain. you should keep in mind that the key purpose of this report is to facilitate high human readability even for my two expert colleagues. I think begin with procedural content is even confusing for me and you should not adopt this strategy unless you have good justifications. also, it is a bit confusing what V means if not have the exact knowledge. I think logical explanation is needed here that "V is the downstream accel speed assuming downstream is always free" or so. also, for D, the "remaining lost service" of what? that should be explicit. this is somehow implicit hanging notation that should be avoided. also check other places where you introduce notation to explicitly define them as logical closure. (answered)


### 11 (answered)
I think in this case I can dismiss the remaining step 4 items as a whole. my justifications are:
1. the VSL task is now treated as a parallel task from urban task. whether they can be aligned should be dependent on the detailed implementation and experiment results.
2. that should be not a new goal unless my colleageus provide new points that are not considered in the previous review.
3. the execution proposal should be the responsibility of implementation agent, not within this review progress.
so in this case can step 4 closed with the current progress? what are the remaining stuff to resolve?

### 12 
besides the VSL review effort, the existing urban task should also yield a report like the VSL one. but since your responsibility is the VSL improvement review, I want to check these:
1. are you aware of the previous urban review progress that attempts to establish a formal task definition? if so, are the existing document enough to identify that what are the current progress of that review? if not, then item 2 is dismissed. (answered)
2. according to the progressive standards established in the VSL improvement review, is it comparable to the VSL standard? if not, what are the major gaps that should be further worked? (answered)
3. as you have the sole responsibility of VSl improvement review, I would like to check about the agent hygeine. should I start a new agent while you produce a handoff to revise the urban review and produce a report with similar standards, or it is better to continue further in the same agent? what are the reasons? (answered)


### 13 (answered)

Here is a fresh email response from Philipp regarding the report:
Hi Peizhu,

Thanks for the summary. I think Wang Yu's points 1 and 2 are key.

Generally, what I'm a bit uneasy about is that there is a lot of complexity here. What you put together is impressive, but just communicating this model to a reader in a paper would easily take several pages, and this is before even touching on the actual contribution.

The other aspect is that as a computer scientist with some minor previous overlaps with traffic engineering, this model is honestly impenetrable to me (e.g., I would decline a review request because I wouldn't be able to do it competently within a reasonable timeframe). The common approach from a CS perspective is to take a common existing model (often in a highly idealized form) and then find or apply the CS method that is our contribution. Here, it seems that the model a combination of ideas from most of the referenced papers, around 6 out of the 7 references if I'm counting correctly. That's an incredible amount of complexity, and just justifying, analyzing, and validating such a model seems like a huge endeavor to me (Wang Yu: please correct me if I'm wrong).

I'm wondering whether there isn't a way to stay much much closer to an existing model and go from there. Maybe it's partly due to my own limited working memory or limited domain expertise, but I feel that having this amount of upfront complexity is in direct conflict to our ultimate goal, which is knowledge generation. I feel currently, we'd end up with a result where the reader will have many questions about the modeling details and wonder how general the findings (on the CS side!) are. I'd feel much less worried if we could boil it down to something like "We're using the VSL task, model, and scenario from [reference 1], adding [model component X] from [reference 2]."

Again, handling this kind of complexity is a great skill, but we need to reduce it to a level where readers (including CS people) trust what we're doing and can mostly still follow along. Question to both of you: Do you see a simplification that avoids this "eclectic" combination of model components that still gives us the essence we need to answer the RQs? If needed, we might want to have a dedicated meeting to try and distill something like this.

Best,
Philipp

I think his major concern as a computer science background researcher is that I may dive into the traffic engineering side too much (as I work in his group in the computer science college). though there is indeed possibility that we don't find an easy way to address the review questions (because that needs expertise, experience, etc.), but I think we can somehow answer this concern by collecting the evidences we found. to fully respond to the concern we need to prove that our formulation is the best middleground that combines some works we can find and the peer works cannot address the review questions so this is pretty difficult. instead, we may respond to him that we have found these closest peer works (...) but they have a collectively these core types of gaps from the review questions, etc. 
but I think his concern is real. at least we haven't explicitly tried to align the model stack to an established single peer work and do minimum adaptions from there. 
are my ideas sound, points the core logic of my colleague's concern, and aligns with the concern? how can we respond to his concern? based on the current collected evidences, can you briefly revise them to figure out a brief direction of response (not the exact response)?

### 14 (answered)
I think I need to check something as my mental model is inconsistent with your report. I think the existing VSL formulation should be treated as a final anchoring point but not a hard constraint. I think the major purpose of the review should be these:
1. find a (or a few) peer works that can serve as the backbone to answer the same research questions
2. audit for each candidate whether can itself or adapting very few other works' components can form a complete modeling stack
3. the existing VSL formulation is a guidance but not constraint; the formed candidate stack need not to be functionally identical to the existing stack, or rather this is only a preference: the approach that resembles the existing stack more is preferred.
so from your elaboration I don't see a good reason not to try to settle down the flow allocation first. 
is this map consistent to your review goal in mind? do you treat the VSL stack as a functional constraint or like my style? does your review results at this gate still valid under my purpose map?

### 15 
I would like to give extra half page as budget (so now 3 pages) but you should try to use as less space as possible, while not spoiling existing content as well.
some further feedbacks:
I think listing the core assumptions as an individual section in the model definition should make the modeling construction more explicitly. I think currently they are mixed in the component definition and that is not very explicit and clear.
what do you mean by "Subraveti adopts Han for capacity drop [3]; we follow that inherited formulation (B) [4] with nominal/VSL caps (B) [5] to give D and R."? I think D and R are hanging symbols as they first appear here. also, there's no downstream explaination for them. Q(x) is semantically brief and clear but what are D and R, intuitively? 
the core question as the bolded title of each component is essential, but I think they should not be there. the core question should be within the section, explaining the core question to resolve and the core functionality of the component, intended. I prefer to use component names as the bolded title because that makes the overall report structure explicit.
what is I in subraveti? what is the definition and intuition of this variable?
the part "Missing downstream E cells are omitted and weights renormalized; A/B lookahead extends with zero outlet density. Empty origins make no requests." looks too procedural to me (like robot language). I can get the rough idea what are you trying to say, but I think some of them are boundary conditions where our choice is natural and logical (thus not belong to the backbone definition), and the wording is too descriptive rather than semantic and logical. remove parts not helpful and rephrase.
what do you mean by "At one boundary, temporarily omit i" in section 3.4? this looks like yet another boundary condition for me... cannot catch its use of defining the backbone.
what is b_xy and P_xy in equation 4? there is no logical intuition about that. I think also equation 4 and 5 look not so intuitive, the form is fine but I think explicitly elaborating the logic and intuition behind (what does it define and what does it do around that, logically?) should definitely help for my colleagues.
what do you mean by "Residual donor traffic gets one straight fallback yℓ (A)"? do you mean that the traffic not served by downstream is queued at the discharging cell?
for the part "E’s use leaves less service for the other requests, whose retained stock can restrict later receiving." do you mean that E's merge into A can make other lanes (here it should be A) less service capable and easier to queue? the current expression is a bit unintuitive to me.
in section 3.5, again, what does h mean? what are the intuitive and logical explanation for the two TST target terms?
what do you mean by "A compact observer adds the final-A density, sufficient on the existing two-state diagnostic."? I cannot catch the point here at all.
the part "Separately, compare gradients with bounded scalar search using the same information, and retain maximum advice as a reference. These definitions isolate what information is needed from how the advice is optimized." looks like arbitrary config to me. how is it related to the target gradient? the core idea behind these is pretty hidden for me.

### 16
for the established new stack, in terms of the key differences (or key similarities) from the old task-first stack, can I understand as follows:
1. use a per-lane preference, and difference of normalized preference as merging scale, instead of merging attempts dependent on travel distance
2. use a coarse CTM instead of lane-aware LTM model
3. in the old model, traffic cannot go from A to B or B to A or A to E. the current lane preference setting does not explicitly forbid these
4. both uses triangular FD for cell/lane flow capacity
5. service fraction differs from the old model at the forced merge. the priority is determined by the lane preference where at the end E can have a high I and thus has good merging share. though, E still imposes a time loss defined in the TST formula
6. the effect from discharged traffic in the old model is removed in the new one
is this set sound? is there any critical misunderstanding? what else should we add into this set to form a complete big picture regarding this aspect?


### 17 
for your claims and proposals, I agree with them all. 
the current repository's agent files (e.g. AGENTS.md, PLANS.md, PROJECT_CONTEXT.md) was for the urban task implementation. I would like to keep the structures and customs already established there during implementation.
also, I want to promote all of reviews under ./misc to /home/zpz/repos/diff_control_review as a standalone git repository and push that online.
I agree that vsl should start in a brand new repository. I make the position as /home/zpz/repos/diff_freeway_vsl. first prepare the handoff material and vsl project init material. it should be mostly migration from the current review. the material should also state the findings and responsibility boundaries of the review and state where should the implementation begin continuing from this boundary. initialize that repository as git repository and push online.