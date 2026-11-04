# Discovering Wholesale Customer Segments — KDD project report

## Executive summary

This KDD exercise searches for exploratory profiles in six annual spending features. Raw-spend standardization with k-means gives its highest silhouette at k=2 (**0.614**), with clusters of 36 and 404 customers. But the smaller cluster has mean silhouette only 0.020 and 52.8% of its members have negative silhouette. It is not a cohesive segment. Repeated 80% subsampling selects k=2 in 100/100 raw-spend runs with a fixed initialization seed. The raw-spend small cluster has variable membership under subsampling; the saved 20-start configuration has ARI 0.899 median and 0.801 minimum across 25 seeds. No customer taxonomy or operational treatment is approved.

## Data and provenance

UCI Wholesale Customers contains 440 rows, six spending values, Channel, and Region. The clustering uses only the six nonnegative spend features; Channel and Region are held out for descriptive profiling. There are no missing values, invalid category codes, negative/nonfinite spends, duplicate full rows, or duplicate spend vectors. UCI: [dataset page](https://archive.ics.uci.edu/dataset/292/wholesale%2Bcustomers), [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/), DOI 10.24432/C5030X. Kaggle listing: https://www.kaggle.com/binovi/wholesale-customers-data-set.

Executed retrieval time: **2026-10-27 03:30:25 UTC**; archive SHA-256 `647e6a61683ed23f48c7b04e1e2be78835eca8758b32267603fc42a1479dbfb8`; CSV SHA-256 `c3d018c643565b85cee733c4a2ac76dd76e080e857cb23f0ccfcc2e15a6c17ef`.

## KDD process and results

The notebook documents selection, preprocessing, transformation, data mining, interpretation, and use. Candidate k=2…7 is evaluated under four representations. The best silhouette is raw-spend standardization (k=2, 0.614); log-standardized, log-robust, and standardized category-share alternatives score 0.290, 0.253, and 0.377 at k=2. This comparison demonstrates that the result depends on representation. At k=3 raw-standardized silhouette is 0.548 but one cluster has only two records.

In original units, the 36-record cluster has median total spend 68,707; median Milk 16,691.5, Grocery 26,136.5, and Detergents_Paper 12,614.5. Its mean silhouette is 0.0196, median −0.0156, and 52.8% negative. The 404-record cluster has median total spend 25,832.5 and mean silhouette 0.667. The small cluster is 91.7% Channel 2, compared with 27.0% in the larger group; Region 3 shares are 63.9% and 72.5%. These associations suggest the raw-spend partition largely tracks the held-out Channel distinction, but do not explain or validate it.

Across 100 shared 80% row subsamples, every representation used the same sample indices and K-means `n_init=20, random_state=42`; this isolates row-sample variation from initialization. Raw-spend k=2 was selected in 100/100 runs. Agreement with the full-data labels on sampled rows had median ARI 0.776 (range 0.397–1.000) and small-cluster Jaccard median 0.700 (range 0.366–1.000). Projecting subsample models to all rows gave raw-spend small-cluster sizes from 13 to 85. Across the same 100 subsamples, median ARI was 0.776 raw-standardized, 0.977 log-standardized, 0.955 log-robust, and 0.977 category-share-standardized; k=2 was selected 100, 100, 87, and 99 times respectively. Separate seed sensitivity for the saved raw model across 25 seeds gave median ARI 0.899 (range 0.801–1.000). The log-standardized and log-robust partitions each have sizes 252/188. For log-standardized, the 252-member cluster is 3.2% Channel 2 and the 188-member cluster is 71.3% Channel 2; log-robust shows 3.6% and 70.7%. Region 3 shares vary less (69.8% and 74.5%). The standardized category-share heuristic yields a more balanced 196/244 split, mean silhouette 0.377, worst-cluster mean 0.307, and 7.14% negative silhouettes in one cluster; its Channel 2 shares are 60.7% and 9.4%. These are descriptive geometries, not validated business segments; the raw-spend small group is especially weakly cohesive.

## Decision and safeguards

The artifact is saved as an unapproved exploratory snapshot. Do not use it to automatically change service, pricing, or customer treatment. A useful next iteration would define a business decision with account owners, assess different distance/feature choices, test out-of-sample repeatability, and evaluate whether any profile produces measurable utility without unfair treatment.

## Critique and revision evidence

The independent GPT-5.6 review challenged using Channel/Region as spend dimensions, scale dominance, and asserting customer types from a silhouette maximum. Revisions restrict clustering to spend, compare four representations, add per-cluster silhouette diagnostics and 100 resamples plus seed sensitivity, and explicitly reject the weak small cluster as an approved taxonomy. GPT-5.6 review pass 2 caught that seed sensitivity used n_init=1 instead of the saved n_init=20, alternative representations lacked equivalent resampling/profiling, sampled-subset ARI was mislabeled as projected, Channel context was missing, and the limitations text was still an instruction. The notebook now tests the saved configuration, reports shared-row 100-resample k=2 stability for all representations, distinguishes subset ARI from projected cluster size, reports Channel proportions, and replaces the limitations placeholder with dataset and decision limits.

## Reproducibility

The Colab-ready notebook was executed locally with Python 3.14.5, pandas 3.1.0, NumPy 2.5.4, and scikit-learn 1.9.1. It saves an explicitly unapproved local model snapshot and row assignments; source data are fetched from UCI at run time.
