# Predicting Sensory Wine Quality from Laboratory Measures — SEMMA project report

## Executive summary

This SEMMA project predicts the recorded red-wine sensory score from 11 physicochemical measurements. A repeated-signature-aware split and validation-selected random forest achieve test MAE **0.494**, RMSE **0.642**, and R² **0.370**. Aggregate MAE is below the proposed 0.65 threshold, but tail recall is **0.0** on 16 extreme-score rows, so the proposed tail-capture gate fails. The model is not validated for triage or decision support.

## Data and provenance

The UCI red Vinho Verde subset has 1,599 rows and 12 columns (11 laboratory measures plus quality). There are no missing values; scores range from 3 to 8. The notebook groups identical predictor signatures before splitting: 1,359 unique signatures, 460 rows in repeated groups, and no repeated signature has conflicting labels. UCI: [dataset page](https://archive.ics.uci.edu/dataset/186/wine%2Bquality), [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/), DOI 10.24432/C56S3T. Kaggle listing: https://www.kaggle.com/competitions/uci-wine-quality-dataset.

Executed retrieval time: **2026-10-27 03:30:09 UTC**; archive SHA-256 `3ed56667f4b828242bd732d7d1dd7f2861e54432239d7fa63877014cbb0304d4`; red CSV SHA-256 `4a402cf041b025d4566d954c3b9ba8635a3a8a01e039005d97d6a710278cf05e`.

## SEMMA execution and split design

SEMMA phases are Sample, Explore, Modify, Model, and Assess. A stratified grouped 10-fold assignment reserves folds 0–6 for training, fold 7 for validation, and folds 8–9 for test, keeping identical measurement vectors together. This yields 1,119 training rows (951 groups), 160 validation rows (136 groups), and 320 test rows (272 groups), with no group overlap. The random forest is selected only on validation MAE, then refit on train plus validation. Test is assessed once. No scaling is needed for this tree model.

| Result | Value |
|---|---:|
| Median baseline validation MAE | 0.669 |
| Random forest validation MAE | 0.485 |
| Random forest test MAE / RMSE / R² | 0.494 / 0.642 / 0.370 |
| Aggregate MAE gate (≤0.65) | Pass |
| Extreme-score row recall (scores 3–4 or 8–10) | 0.0 of 16; tail gate (≥0.80) fails |

By observed score band, test MAE is 1.40 for ≤4 (n=12), 0.36 for score 5 (n=136), 0.45 for score 6 (n=128), 0.70 for score 7 (n=40), and 1.61 for ≥8 (n=4). Rounded predictions fall only between 4 and 7, explaining the zero extreme-score recall. These sparse tails are not reliably characterized by aggregate MAE.

## Use limits and ethics

This model is a coursework experiment, not a validated human-review triage tool. The target is an ordinal panel judgment treated approximately as numeric; it is not an objective measure of quality. The dataset is one red-wine subset from one region and context. Prospective evaluation, more representative samples, and explicit panel-defined utility would be required before any decision-support use.

## Critique and revision evidence

The independent GPT-5.6 review challenged random row splitting because repeated predictor vectors could cross partitions, ordinal-score interpretation, and tail performance claims. Revisions group repeated signatures, select by validation only, report signed errors and score bands, add an explicit tail-capture gate, and remove unsupported claims that human review makes use safe. GPT-5.6 review pass 2 confirmed split integrity and numerical consistency, corrected “mean” to “median,” and led to pinned setup versions and source hash checks. Pass 3 found residual triage/handoff claims in notebook scaffold text and removed them; limitations and the local artifact status now match the failed tail-capture result. GPT-5.6 pass 3 also removed residual triage wording and template placeholders; the saved artifact was rebuilt with `research_only_not_approved` status. A final persona-style GPT-5.6 review found no remaining material defects.

## Reproducibility

The Colab-ready notebook was executed locally with Python 3.14.5, pandas 3.1.0, NumPy 2.5.4, and scikit-learn 1.9.1. Notebook outputs and local model/sample-score artifacts are included. Source data are retrieved from UCI at run time.
