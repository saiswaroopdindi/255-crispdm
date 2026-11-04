# Predicting Sensory Wine Quality: A SEMMA Walkthrough


## The dataset and question

The UCI red Vinho Verde subset has 1,599 records, eleven laboratory measurements, and an ordinal sensory score. I tested whether a random forest could predict the recorded score, while treating the score as a human judgment rather than objective quality.

## A split that groups repeated predictor signatures

There are 1,359 distinct predictor signatures; 460 records belong to repeated-signature groups. Identical vectors stay together in a stratified grouped split: 1,119 training rows, 160 validation rows, and 320 test rows. The median baseline and random forest are compared on validation data; the forest is then refit on train plus validation and assessed once on the untouched test partition.

## Aggregate score hides the tail

The validation MAE was 0.669 for the median baseline and 0.485 for the random forest. On the test set, the selected forest scored MAE 0.494, RMSE 0.642, and R² 0.370. It meets a proposed aggregate MAE threshold of 0.65.

That is not the whole story. Rounded predictions fell only between scores 4 and 7. Of 16 extreme test cases (scores 3–4 or 8–10), the model identified none, so the proposed tail-recall gate of 0.80 failed. Test MAE was 1.40 for records rated ≤4 (12 examples) and 1.61 for records rated ≥8 (4 examples), versus 0.36 for score-5 records. This is not validated for triage or decision support.

## What SEMMA surfaced

The workflow separates sampling, exploration, modification, modeling, and assessment. Grouping duplicate measurement vectors avoids an overly optimistic split, and validation-only model selection protects the final test. The major lesson is that an aggregate metric can pass while a specific and important failure criterion fails.

## Limits and reproduction

This is one regional red-wine subset. The ordinal rating reflects a sensory panel, and the sparsely represented score tails remain uncertain. Any future work needs broader samples and a utility measure defined with the panel. Reproduce with [`semma_wine_quality.ipynb`](./semma_wine_quality.ipynb), which downloads the [UCI dataset](https://archive.ics.uci.edu/dataset/186/wine%2Bquality), licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
