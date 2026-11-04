"""Mirror project reports, article drafts, and notebooks into the /docs Pages tree."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = {
    "01_crisp_dm_bike_demand": "crisp_dm_bike_demand.ipynb",
    "02_semma_wine_quality": "semma_wine_quality.ipynb",
    "03_kdd_wholesale_segments": "kdd_wholesale_segments.ipynb",
}
for folder, notebook in PROJECTS.items():
    source = ROOT / folder
    target = ROOT / "docs" / folder
    target.mkdir(parents=True, exist_ok=True)
    for filename in ("REPORT.md", "MEDIUM_DRAFT.md", notebook):
        shutil.copy2(source / filename, target / filename)
