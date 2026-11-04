# Video walkthrough script — KDD / Wholesale Customer Spending Profiles

Target length: 6–8 minutes. This is a local recording script; the video has not been recorded or uploaded.

1. **0:00–0:40 | Question and boundary.** Explain that this is an exploratory search for repeatable patterns in annual spend across six categories. Channel and Region are withheld from clustering and used only after fitting. No account decision or customer treatment is approved.
2. **0:40–1:30 | Dataset and checks.** Show the UCI source, 440 rows, six spend features, Channel/Region metadata, hash/license record, and checks for missing, invalid, negative, duplicated, or nonfinite values. Note there are no customer IDs or transaction dates.
3. **1:30–2:25 | Transformations.** Walk through raw standardized spend, log-standardized spend, log-robust spend, and standardized category shares. Say explicitly that category shares are a simple proportion-based heuristic, not a formal log-ratio method.
4. **2:25–3:25 | Candidate clusters.** Show k=2…7 silhouette and minimum-cluster-size results for each representation. Explain why the raw-spend k=2 maximum (0.614) is provisional rather than an automatic approval.
5. **3:25–4:35 | Cohesion and profiles.** Compare the raw 36/404 split and per-cluster silhouette; show the 36-record group’s weak mean silhouette (0.020) and 52.8% negative membership. Contrast the more balanced category-share split. Show original-unit/category-share and Channel/Region profiles for each representation.
6. **4:35–5:35 | Stability.** Explain that the 100 subsamples use shared row indices and fixed K-means initialization across representations. Separate the resampling results from the 25-seed sensitivity check using the saved 20-start configuration. Clarify that ARI is computed on sampled rows; projected cluster sizes use labels predicted for all rows.
7. **5:35–6:35 | Decision and use.** State that the raw small cluster is weakly cohesive and strongly associated with Channel; log partitions are stable but also track Channel. No profile has been linked to an account decision or tested for utility. The artifact is explicitly unapproved.
8. **6:35–7:15 | Artifacts and next step.** Show the notebook, report, assignment CSV, and unapproved snapshot. Propose account-owner interviews and a decision-specific utility study before any customer experiment.

On-screen checklist: show the executed notebook outputs and source citation; explain that annual aggregates cannot establish time trends, prices, customer context, causality, or generalization; do not present clusters as stable customer types.
