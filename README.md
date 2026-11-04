# Data Mining Process Assignment: CRISP-DM, SEMMA, and KDD

This repository contains three separate, Colab-ready data mining projects. Each uses a different dataset and includes an executable notebook, detailed report, Medium article draft, and video walkthrough script.

## Projects

| Method | Project | Dataset | Main task |
|---|---|---|---|
| CRISP-DM | [Bike demand](./01_crisp_dm_bike_demand/) | Bike Sharing Demand (Kaggle listing; UCI source) | Future-period regression |
| SEMMA | [Wine quality](./02_semma_wine_quality/) | Wine Quality (Kaggle listing; UCI source) | Ordinal-score regression experiment; tail gate fails |
| KDD | [Wholesale segments](./03_kdd_wholesale_segments/) | Wholesale Customers (Kaggle listing; UCI source) | Exploratory clustering |

## Run

Each notebook has been executed end to end locally and includes saved outputs. The setup cells pin package versions and assert the UCI source hashes. Re-run with network access and a compatible Python runtime; the saved reports describe the verified local runs, holdout results, and limitations.

## Critique and revision practice

Each notebook records independent GPT-5.6 critique and revisions. Review findings, results, and limits are reflected in the reports and notebooks. A reusable critique prompt and review checklist are in [`REVIEW_PROTOCOL.md`](./REVIEW_PROTOCOL.md).

## Website

[`docs/index.html`](./docs/index.html) is a static assignment portfolio suitable for GitHub Pages. It can be published after creating/configuring a GitHub repository and enabling Pages.

## Publication and hand-in status

Articles and video walkthrough scripts are drafts; no videos have been recorded. No authenticated GitHub session or remote repository is configured. The site and drafts are local only. No external publication or course submission has been made. No raw source dataset files are included.

## Method references

- CRISP-DM 1.0, [IBM-hosted reference PDF](https://public.dhe.ibm.com/software/analytics/spss/documentation/modeler/14.2/es/CRISP-DM.pdf)
- SAS, [Data Mining and SEMMA](https://support.sas.com/documentation/cdl/en/emcs/66392/HTML/default/n0pejm83csbja4n1xueveo2uoujy.htm)
- Fayyad, Piatetsky-Shapiro, and Smyth, [The KDD Process for Extracting Useful Knowledge](https://doi.org/10.1145/240455.240464)

The local run used the versions listed in [`requirements-lock.txt`](./requirements-lock.txt). Each notebook pins these versions and checks the downloaded UCI archive and data-file hashes before analysis. Python 3.14.5 was used locally; a different Colab Python runtime may require compatible adjustments.

Google Drive link:  https://drive.google.com/drive/folders/1XY84Lfsxlr5hc01JHO6iEOr42tSQWjFz?usp=sharing

Link to medium articles:
https://medium.com/@saiswaroopdindi1/forecasting-hourly-bike-rental-demand-a-crisp-dm-case-study-95fef1f46558
https://medium.com/@saiswaroopdindi1/predicting-wine-quality-from-laboratory-measures-a-semma-analysis-dd9e5b62e000
https://medium.com/@saiswaroopdindi1/exploring-wholesale-spending-profiles-with-the-kdd-process-ae0f7c6a15de

