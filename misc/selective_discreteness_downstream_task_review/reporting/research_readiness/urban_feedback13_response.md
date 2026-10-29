# Feedback 13: explaining the model-to-gradient connection

28 October 2026. **This revision batch is complete.** Selected feedback-13 changes are marked in red as short phrases and equation terms; the earlier broad red markup remains removed. The main report remains eight pages; the mathematical companion has ten. The five-part report structure, traffic rules, geometry and comparison agreements remain unchanged.

[Revised main report](urban_compact_methods_report.pdf)

[Mathematical companion](urban_methodology_specification.pdf)

The gradient section now follows one causal story: green changes service rates; rates and head-clearance times determine discharge; remaining mass changes lane loads and later entry; entry times and cumulative histories change future availability; repeated updates determine sink exits and complete TST. Each block explains which part of that story it supplies and where its outputs enter next. The overall state-chain equation remains the common framework rather than a disconnected introduction.

The grid definition explicitly names the overlap mass omega, movement mass M in a lane/bin, and total resident lane mass n, including moving and waiting traffic. Omega is the positive min/max overlap already used by the representation, not an additional traffic state. The derivative now refers to a quantity actually defined in the forward equation. Both representations count one physical mass.

The agreed option 1 is applied to allocation and leg sharing: total derivative balance first, individual categorical responses below it, and the solved filling-level or multiplier gradient in a separate equation with the substitution explained. Definitions of positive uncapped lanes, binding caps, lambda, theta, starting loads and green weights are recalled where used. The text explains why capped-bound responses are subtracted, why starting-load responses are added in allocation, and why weight responses are subtracted in service sharing. A capped receiver can have a changing cap and therefore a nonzero gradient.

Every sensitivity block identifies its forward source. The explicit service-amount sum now appears in the traffic model before its derivative. The head-clearance formula is separated from the total-discharge derivative and expressly covers only the head-clearance branch of the stopping-time minimum. The other stopping conditions are described in the main text and their derivatives are explicit in the companion. The explanation connects earlier head removal to service time available to followers, then to timestep discharge and future state.

The former equation-18 numerical example is replaced by a concrete task explanation: transferring green from through to a left-turn blocker lowers the through rate but can free enough time to increase through discharge. This illustrates why movement order can matter to the control response. The text links that mechanism directly to the rate and duration channels. The calculation remains optional in the companion; the main report does not treat it as proof of complete-TST benefit or superiority over aggregate models.

The last two derivative blocks now explicitly reference the entry-time and TST equations. The TST block explains the intermediate conservation identity—remaining population equals released mass minus sink exits—and states that releases, timestep and common horizon are fixed during differentiation.

## Finding the equations after revision

References in feedback 13 use the previous numbering. Separate displays and causal ordering change some numbers:

| Previous report | Revised report |
|---|---|
| 11: grid | 12: explicitly named overlaps, movement/bin mass and lane total |
| 14: grid derivative | 19 |
| 15: allocation derivatives | 20: total/cases; 21: solved filling-level response |
| 16: leg-sharing derivatives | 15: total/cases; 16: solved multiplier response |
| 17: discharge and head time | 17: discharge response; 18: head-clearance duration response |
| 18: detailed local example | Traffic explanation after 18; optional companion calculation in 15–16 |
| 19: entry-time derivative | 22, explicitly differentiating 11 |
| 20: TST derivative | 23, explicitly rewriting and differentiating 13 |

[Updated equation/source map](../../extraction/research_readiness/urban_methodology_specification_sources.md)

[Discussion record, including the agreed presentation choice](../../temp_content/research_readiness/review_dialogue.md)

Verification covers clean two-pass LaTeX builds, equation references and mapping, unchanged forward-law blocks, grayscale output, page layout and exact first-order balance/branch identities. Detailed commands and evidence are in the work record.

[Work and verification](urban_methodology_draft_work_report.md)

**Current topic: review of the revised report.** This batch adds no unresolved scientific choice and opens no new question batch. Numerical calibration, concrete baseline qualification, implementation and empirical forward/gradient/usefulness tests remain later work.
