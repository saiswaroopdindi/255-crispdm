# Discovering Wholesale Customer Profiles: A KDD Walkthrough


## From data mining to a testable question

I used the UCI Wholesale Customers dataset to explore whether annual spending across six product categories forms useful profiles. Channel and Region are held out from clustering and used only to describe the resulting groups. These are not established customer types.

## Representation matters

After standardizing raw spending, k=2 produced the highest silhouette across k=2…7 (0.614), with groups of 36 and 404 customers. But the smaller group's mean silhouette was only 0.020, its median was negative, and 52.8% of members had negative silhouette. Four feature representations also changed the apparent separation: k=2 silhouette was 0.290 with log-standardized values, 0.253 with log-robust scaling, and 0.377 with standardized category shares (a proportion-based heuristic, not a formal log-ratio transform). The maximum raw-scale silhouette alone is not enough to declare success.

The 36-record group's median total annual spend was 68,707, with median Grocery 26,136.5 and Milk 16,691.5. It may look like a high-spend profile in some categories, but cohesion is weak. In 100 shared 80% subsamples, with fixed `n_init=20` and `random_state=42`, raw-spend k=2 was selected every time. On sampled records only, ARI against matching full-data labels had median 0.776 (range 0.397–1.000), and small-cluster Jaccard median was 0.700 (range 0.366–1.000). Separate seed sensitivity for the saved 20-start configuration across 25 seeds had median ARI 0.899 and range 0.801–1.000. Across those same 100 row samples, median ARI is 0.776 for raw spend, 0.977 for log-standardized, 0.955 for log-robust, and 0.977 for standardized category shares; k=2 selection rates are 100%, 100%, 87%, and 99%. Standardized category shares form a more balanced 196/244 split with overall silhouette 0.377, worst-cluster mean 0.307, and 7.14% negative silhouettes in one group. The raw-spend small cluster is 91.7% Channel 2, versus 27.0% in the larger group. The two log partitions each split 252/188; their 252-member groups are only 3–4% Channel 2, while their 188-member groups are about 71% Channel 2. Region 3 shares vary less across these log clusters (about 70–75%). All four representations have original-unit/category-share and Channel/Region profiles in the notebook. These results show representation and Channel context matter; they do not demonstrate which profile, if any, helps an account decision.

## Limits and generalization

The 440 records contain annual category totals without transaction dates, prices, account context, or customer identifiers. They cannot explain how purchasing changes over time or why a customer belongs to a group. The labels are representation-dependent and the log-based partitions also align strongly with Channel. These patterns may not transfer to another distributor or period.

## Decision

The analysis is exploratory and business acceptance is not established; no stakeholder utility or decision test has been performed. The local artifact is labeled unapproved. Before any business experiment, account owners should define a decision, review whether profiles help, and check for harmful differences in customer treatment. Do not automatically change service or pricing based on these labels.

The highly repeatable log partitions also track Channel strongly, so repeatability alone does not show additional customer value.

## Reproduce it

Run [`kdd_wholesale_segments.ipynb`](./kdd_wholesale_segments.ipynb) in Colab. The source is [UCI Wholesale Customers](https://archive.ics.uci.edu/dataset/292/wholesale%2Bcustomers), licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
