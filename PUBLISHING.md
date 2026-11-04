# Publishing and submission handoff

The local portfolio site is `docs/index.html`. A GitHub repository and Pages site have not been created because this machine has no authenticated GitHub session (`gh auth status` reports not logged in) and no remote is configured.

## GitHub repository and Pages

1. Create a GitHub repository for this folder. Choose public if the course expects a public URL; inspect the dataset licenses before adding data files. This project intentionally does not include raw datasets.
2. Push the project to the repository's `main` branch.
3. In repository settings, enable GitHub Pages with the `main` branch and `/docs` folder as the publishing source.
4. Open the Pages URL, test all three report/notebook links, and use that URL for the course submission.

The Pages site is a static landing page. GitHub renders repository Markdown and notebooks when opened in the repository; the Pages URL itself is not a full Markdown renderer.

## Before submitting

- The notebooks have already been run locally end to end. Re-run in Colab and compare the outputs before publication.
- Reports and article drafts contain verified local run results; edit them into your own voice before publishing.
- Review the documented GPT-5.6 critique/revision notes before submission.
- Record the three walkthrough videos, verify captions and attribution, and upload them to YouTube if required.
- Publish the three edited articles on Medium if required.
- Confirm that the published website loads in a private browser window, then submit its URL in the course portal before the stated deadline.

The user requested a local-only handoff. No repository, site, article, video, or course submission has been published.

The portfolio copies each project report, article draft, and executed notebook into `docs/` so the links work when GitHub Pages publishes from that folder. After editing a source report or notebook, run `python3 scripts/sync_site_assets.py` to refresh the local Pages copies.
