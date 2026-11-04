# Forecasting Hourly Bike Rental Demand: A CRISP-DM Walkthrough


## Business question before model choice

A historical bike-share dataset can answer a forecasting question, but an aggregate hourly total cannot tell a planner which station needs bikes. I framed this as a system-wide demand experiment and treated station redistribution as outside the evidence.

## Data and design

The UCI Bike Sharing archive contains 17,379 observed hourly rows. I compared their daily totals with the companion daily file; all 731 days reconcile exactly, so the 165 omitted hour slots represent zero-count periods and are added before modeling. The resulting timeline has 17,544 hourly slots. I removed `casual` and `registered` because their sum is the target `cnt`. I also excluded weather recorded during the target hour: a day-ahead forecast cannot know observed conditions from that future hour. The model uses calendar fields and a time trend. The development period ends in September 2012, with October–December held out. The 165 omitted hour slots are validated zero-demand periods, including 40 in Q4, so the holdout uses the complete 2,208-hour grid. Monthly rolling-origin folds on January–September are used for model selection. The comparison is a median-by-weekday/hour baseline.

## Results: a failed gate is still a result

On the untouched fourth-quarter holdout, the baseline MAE was 81.10 bikes per hour. Calendar HistGradientBoosting had MAE 97.00, RMSE 148.59, and RMSLE 1.044. Candidate MAE was 19.6% worse, so it missed the proposed 10% improvement gate. It also missed the seasonal guardrail: source season code 1 (264 hours) has candidate MAE 87.1% worse than baseline, while code 4 (1,944 hours) has candidate MAE 6.8% worse. Codes 2 and 3 are absent. The day-block bootstrap interval for candidate-minus-baseline MAE was [3.52, 27.79].

The mean signed error was −72.24 (actual minus prediction), indicating overprediction; the lower and moderate actual-demand quartiles also show overprediction. October looked better than baseline, while November and December did not. The practical conclusion is to reject this candidate and investigate better seasonal baselines and more historical test periods—not to deploy it.

## What CRISP-DM changed

The first attempt's weather inputs were unavailable at the stated forecast origin, and the original random split did not resemble forecasting into the future. Reframing the input contract changed the score and conclusion. The workflow makes the business question, data checks, time-aware validation, holdout decision, and handoff risks visible as separate phases.

## Limitations and next steps

The data are from one bike-share system in 2011–2012 and cover one fourth-quarter holdout. Season codes 2 and 3 are absent from that test; the report uses the source codes without relying on conflicting season labels. Aggregate demand cannot guide station-level redistribution. A next study should define the planning decision and cost, add station-level observations, use weather forecasts archived as available at issue time, and compare multiple seasonal backtests.

## Reproduce it

Open [`crisp_dm_bike_demand.ipynb`](./crisp_dm_bike_demand.ipynb) in Colab. The notebook downloads UCI data when run. Source: [UCI Bike Sharing](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset), licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
