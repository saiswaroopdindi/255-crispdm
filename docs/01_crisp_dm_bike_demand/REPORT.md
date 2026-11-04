# Forecasting Hourly Bike Rental Demand — CRISP-DM project report

## Executive summary

This CRISP-DM project tests whether calendar features improve hourly bike-demand forecasts on a future period. On the untouched October–December 2012 holdout, the calendar-only HistGradientBoosting model scored MAE **97.00 rentals/hour**, worse than the median weekday/hour baseline (**81.10**). The proposed overall improvement gate (at least 10%) and represented-season guardrail both fail. The correct outcome is no-go for operational use; the notebook preserves the failed result and its diagnostic slices.

## Business understanding

The data support a historical aggregate demand-forecasting exercise. A system-wide hourly total does not identify which stations need bikes, so this project does not claim it can make station redistribution decisions. A future operational study would need station-level data, forecast-origin weather inputs, a decision-specific baseline, and planner-defined costs.

## Data and provenance

UCI Bike Sharing hourly source (17,379 observed records; 17,544 slots after the validated zero completion), listed in the Kaggle Bike Sharing Demand competition. The source contains `cnt`, `casual`, and `registered`; the component counts are excluded because they sum to the target. The 17,379 observed `hour.csv` rows have no null fields or duplicate instants, and the target identity holds. The companion `day.csv` daily totals exactly equal the sums of observed hourly counts for all 731 dates. The 165 omitted hourly slots (40 in Q4) are therefore added with zero demand before modeling. The completed series has 17,544 slots, including a complete 2,208-hour Q4 holdout. UCI source: [dataset page](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset), [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/), DOI 10.24432/C5W894. Kaggle listing: https://www.kaggle.com/competitions/bike-sharing-demand.

The executed notebook asserts the recorded source hashes before analysis and records retrieval time **2026-10-27 03:37:40 UTC**, archive SHA-256 `b70182d0d0508e9abbb79306ce5c0cec34869000f8220175ac83d11dbe845401`, `hour.csv` SHA-256 `e03de4ee4ef4dc376ac6e04bf829673c6269e8eba5c60fa121640fa2f829504f`, and `day.csv` SHA-256 `a6bcf826782d3c0fbfdcbeead17cd0884185a0dafe8ff10cd48a874ee7ba18be`. All three hashes are asserted by the notebook.

## Method and evaluation

The development period ends September 30, 2012; the one untouched holdout covers October 1 through December 31, 2012 (2,208 hours, with the 40 omitted hour.csv slots included as validated zeros). Monthly rolling-origin validation from January through September selects the calendar model (validation MAE 60.88 vs baseline 95.42). The day-ahead feature contract uses month, weekday, hour, and a time trend. Observed weather from the target hour is excluded because it would not be available at the forecast origin. The baseline is the training-period median for weekday and hour. Predictions are clamped at zero for both metrics and scoring.

| Holdout model | MAE | RMSE | RMSLE |
|---|---:|---:|---:|
| Median weekday/hour baseline | 81.10 | 122.35 | 0.843 |
| Calendar HistGradientBoosting | 97.00 | 148.59 | 1.044 |

The candidate is **19.6% worse** in MAE overall. Its day-block bootstrap 95% interval for candidate-minus-baseline MAE is **[3.52, 27.79]**, favoring the baseline. The two source season codes represented are 1 (264 hours; MAE 201.87 vs baseline 107.88, 87.1% worse) and 4 (1,944 hours; 82.76 vs 77.46, 6.8% worse); codes 2 and 3 are absent. The candidate has mean signed error −72.24 (actual minus prediction, indicating overprediction). Monthly MAE shows it wins October but loses November and December. Both proposed acceptance gates fail.

## Deployment decision and limitations

The local artifact and sample scores are a reproducibility handoff only, marked `research_backtest_not_operationally_approved`. Do not use this model for staffing or dispatch. The history covers one system in 2011–2012, the holdout spans only one quarter, and the aggregated target cannot resolve station-level actions. Further work should compare stronger seasonal/time-series baselines, run multiple year/season holdouts, and evaluate against a documented planning utility before reconsidering use.

## Critique and revision evidence

The independent GPT-5.6 review identified target-hour weather leakage, a business mismatch between total rentals and station redistribution, a single-origin temporal test, and weak baseline/acceptance evidence. The revisions remove contemporaneous weather, define a calendar-only day-ahead contract, add monthly rolling validation and a Q4 holdout, report a weekday/hour baseline with source-season-code and day-block uncertainty analysis, and keep the failed operational gate explicit. GPT-5.6 review pass 2 additionally caught the missing-hour reporting discrepancy and imprecise season description; both are corrected here and in the notebook. Setup versions are pinned and archive/hour/day hashes are checked. GPT-5.6 pass 3 caught the signed-error direction and season-code ambiguity. A final review caught stale validation values and wording that conflated analytical and business success; these are corrected, and the complete zero-reconciled holdout is stated. A later review established that omitted hourly rows reconcile to zero using day.csv; the complete hourly grid and every metric/artifact were regenerated accordingly. It also prompted explicit separation of analytical screening from unresolved business success and a stronger no-go deployment decision. A final persona-style GPT-5.6 review found no remaining critical discrepancy.

## Reproducibility

The Colab-ready notebook was executed locally with Python 3.14.5, pandas 3.1.0, NumPy 2.5.4, and scikit-learn 1.9.1. Outputs and local scoring artifacts are included; re-run the notebook with network access to fetch the licensed source data.
