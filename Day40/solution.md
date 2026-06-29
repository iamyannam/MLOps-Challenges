### Makefile

```
.PHONY: train-pipeline clean

# xFusionCorp Industries — Fraud Detection Training Pipeline.
# Usage: make train-pipeline

train-pipeline:
	python3 src/validate_data.py
	python3 src/tune.py
	python3 src/select_model.py	
	python3 src/register.py
	python3 src/report.py

clean:
	rm -rf models/ reports/
```

### select_model.py

```
"""Stage 3 — Model selection.

Reads every run in the `fraud-detection-tuning` experiment, picks
the best candidate by the training metric, validates it against the
release threshold, and persists the selection to
`reports/selection.json` for the register stage.
"""
import json
import os
import sys

import mlflow

TRACKING_URI = "http://localhost:5000"
EXPERIMENT = "fraud-detection-tuning"
REPORTS_DIR = "/root/code/fraud-detection/reports"
SELECTION_JSON = os.path.join(REPORTS_DIR, "selection.json")

RELEASE_THRESHOLD = 0.4


def main():
    mlflow.set_tracking_uri(TRACKING_URI)
    client = mlflow.MlflowClient()
    exp = client.get_experiment_by_name(EXPERIMENT)
    if exp is None:
        sys.exit(f"[select] experiment {EXPERIMENT!r} not found.")

    runs = mlflow.search_runs(
        experiment_ids=[exp.experiment_id],
        order_by=["metrics.f1_score DESC"],
        max_results=200,
    )
    if runs.empty:
        sys.exit(
            f"[select] no runs in experiment {EXPERIMENT!r} — the tune "
            "stage has not produced any candidates yet."
        )

    best = runs.iloc[0]
    score = float(best["metrics.f1_score"])
    if score < RELEASE_THRESHOLD:
        sys.exit(
            f"[select] best candidate ({score:.4f}) is below the "
            f"release threshold ({RELEASE_THRESHOLD})."
        )

    selection = {
        "run_id": best["run_id"],
        "model_type": best.get("tags.model_type", ""),
        "f1_score": score,
    }
    os.makedirs(REPORTS_DIR, exist_ok=True)
    with open(SELECTION_JSON, "w") as f:
        json.dump(selection, f, indent=2)
    print(f"[select] {selection}")


if __name__ == "__main__":
    main()
```

### register.py

```
"""Stage 4 — Register the selected model.

Reads the selection written by the previous stage, registers the
selected run's model as `fraud-detector` in the MLflow Model
Registry, and assigns the release-lane alias so the serving layer
can fetch the right version by name.
"""
import json
import os
import sys

import mlflow
from mlflow.tracking import MlflowClient

TRACKING_URI = "http://localhost:5000"
REPORTS_DIR = "/root/code/fraud-detection/reports"
SELECTION_JSON = os.path.join(REPORTS_DIR, "selection.json")

REGISTERED_MODEL_NAME = "fraud-detector"
RELEASE_ALIAS = "staging"


def main():
    if not os.path.exists(SELECTION_JSON):
        sys.exit(
            f"[register] {SELECTION_JSON} missing — the select stage "
            "has not produced a selection yet."
        )
    with open(SELECTION_JSON) as f:
        selection = json.load(f)

    mlflow.set_tracking_uri(TRACKING_URI)
    client = MlflowClient()

    model_uri = f"runs:/{selection['run_id']}/model"
    version = mlflow.register_model(model_uri, REGISTERED_MODEL_NAME)

    client.set_registered_model_alias(
        REGISTERED_MODEL_NAME, RELEASE_ALIAS, version.version,
    )
    print(
        f"[register] {REGISTERED_MODEL_NAME} v{version.version} "
        f"aliased as {RELEASE_ALIAS!r}"
    )


if __name__ == "__main__":
    main()
```


<img width="1327" height="825" alt="image" src="https://github.com/user-attachments/assets/8d8700d3-a9d3-4a70-8c7e-4d242993c7cf" />
