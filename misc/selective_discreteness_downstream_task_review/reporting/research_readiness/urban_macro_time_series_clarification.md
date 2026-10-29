# A macro model may learn its state from the original fine-grained series

26 October 2026. Clarification following feedback 5. This refines the agreed comparison principle, without reopening the settled sensitivity, source-credit or traffic principles.

**Yes: the rival should be allowed to access the original time series through its declared micro/meso-to-macro method.** I made the earlier distinction too restrictive when it sounded like every legitimate TST comparison required a model to run without further observations. That is not a general requirement of this review.

The important distinction is between the source data and the representation used by the model. Vehicle or packet records can supply lane mass, flow, speed, queue measures or a model-defined aggregate description of blockage. A model can estimate and update those quantities from the time series while remaining macroscopic. Its aggregation/state-estimation method is part of what is being tested. We should not prohibit a successful macro summary merely because the source record contained the finer information.

## What the agreed boundary now means

The shared comparison can provide the original record. Each rival declares how it converts that record into macro variables, what history or memory it retains, and how its macro dynamics use those variables. It can use a subset of the available data. We do not require one preselected projection to erase order before every rival gets to apply its own method.

For example, a rival can read lane-level vehicle observations, construct bay and through-lane masses and speeds, and estimate an aggregate obstruction state. If that state predicts the relevant service response well, this is a valid result against the need to retain the full packet ordering. It should not be dismissed as information leakage simply because its estimate captures an effect caused by order.

The boundary must describe the whole method, including retained memory. A transient computation from fine records into macro variables is allowed. If an implementation also keeps an exact ordered packet ledger for later queries, that is retained mesoscopic state in the method and must be credited as such. Naming only its final output “macro” would not explain how much order it actually preserves. This is a representation/accounting distinction, not a ban on reading the original data.

This also narrows the scope of the earlier information-limit argument. Two cases that look identical under one fixed aggregation need not look identical under another model's legitimate summary of the original series. The bound still applies when a particular model's complete retained macro record is identical. An assertion about every allowed macro method would require establishing that condition across the admitted representation class. We have not done that. Successful reconstruction or estimation remains an admissible outcome that weakens the extra-order hypothesis in that regime.

## What observation updates tell us about the result

There are several legitimate comparison questions:

| What the experiment does | What the result establishes |
|---|---|
| Aggregate the original series and test local service/state responses | Whether the model's macro representation and response law explain the observed traffic situations |
| Update the macro state as new observations arrive, then predict the next response | Whether the combined estimator and macro dynamics work under the stated observation stream |
| Start from common conditions and forecast without later state observations | Whether the model predicts the full evolution without those updates |

The first two are allowed; the third is not a prerequisite for calling a rival legitimate or macroscopic. The earlier paragraph should have used this distinction to explain what a test establishes, rather than impose a blanket input restriction.

There remains a separate control question about when data are available. The full record can be used in retrospective analysis, calibration and validation. For a claim about predicting the effect of a new allocation, state which observations are available at that decision and which later observations are supplied. Future outcomes under the changed allocation cannot be treated as predictions made before those outcomes were observed. Likewise, holding an observed series fixed gives a conditional response; its complete TST interpretation must state how subsequent state changes are treated. This does not make the data non-macro or invalidate the local test. It identifies the predictive task and sensitivity being measured.

## Relation to SUMO and Vissim

Your simulator example is consistent with this distinction. SUMO explicitly provides lane/edge macro measures computed from simulated vehicle activity. Vissim documents both raw vehicle measurement records and results aggregated by time interval. These are direct examples of fine-grained simulation supplying aggregate observations through a defined boundary. [SUMO lane/edge measures](https://sumo.dlr.de/docs/Simulation/Output/Lane-_or_Edge-based_Traffic_Measures.html), [Vissim measurement evaluation](https://cgi.ptvgroup.com/vision-help/VISSIM_2026_EN-DE/en-us/Content/11_Auswertungen/AuswertungQuerschnittsmessungen.htm).

The record now states: **original time-series access and model-defined conversion to macro state are allowed; successful aggregate reconstruction counts; the representation/memory and observation schedule are reported so the claim is clear.** This updates UR-G4 Candidate C. It adds no candidate, removes no native rival and imposes no new principle checkpoint.

[Updated comparison principle](../../temp_content/research_readiness/comparison_sensitivity_and_credit_proposal.md)

[Updated mathematical companion](urban_feedback5_information_and_sensitivity.pdf)

[Work and preservation checks](urban_macro_time_series_work_report.md)
