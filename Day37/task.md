The xFusionCorp Industries ML platform team runs fraud-detection training as a four-stage pipeline—preprocess, featurize, train, evaluate—orchestrated by a single script that logs the end-to-end run to MLflow. A pre-staged pipeline is already in place, but the stage-chain invariant is broken: the pipeline currently produces a feature matrix that does not reflect the upstream drop-and-clean work. Your task is to correct the stage wiring so every stage reads from its immediate predecessor and one MLflow run captures the full pipeline.

1.  The MLflow tracking server is already running on port 5000. The MLflow UI button at the top of the lab can be opened to confirm—the dashboard loads with an empty training-pipeline experiment.
2.  The project layout under /root/code/fraud-detection/:
    +  ```data/raw/train.csv``` – The same 200-row synthetic binary-classification dataset the rest of the Training section uses (imbalanced roughly 70 / 30).
    +  ```configs/pipeline_config.yaml``` – Declares the data paths, model hyperparameters, output paths, and MLflow settings every stage consumes. Correct and must remain intact.
    +  ```src/preprocess.py, src/featurize.py, src/train.py, src/evaluate.py``` – The four pipeline stages. preprocess.py drops negligible-amount rows (amount < 50) and duplicates before writing the processed CSV. The four stages are wired through the config's data: paths.
    +  ```run_pipeline.py``` – The orchestrator that executes the four stages in order and logs one MLflow run with the config-driven parameters and the final evaluation metrics. Correct and requires no edits.

3.  Identify the stage whose input path breaks the chain, correct the wiring in the VS Code editor, save, and run python3 run_pipeline.py once from the project root.
4.  The end state must include:
    +  The row count of data/features/features.csv equals the row count of data/processed/train_clean.csv and is strictly less than the 200-row raw CSV.
    +  models/model.pkl and reports/evaluation.json are written and the report carries accuracy, f1, and roc_auc as numeric values.
    +  Exactly one MLflow run exists in the training-pipeline experiment, carrying params.model_type, params.n_estimators, params.max_depth, and the three evaluation metrics.

## preprocess.py
```
"""Stage 1 — Preprocess.

Reads raw transactions from `data/raw/train.csv`, drops the rows that
a production pipeline would reject (negligible-amount transactions
below $50 and any duplicates), and writes the cleaned dataset to
`data/processed/train_clean.csv`.

The row-count contract is load-bearing for the rest of the pipeline:
  raw_rows - dropped_rows = processed_rows  (≈192 rows, not 200).
If a later stage reads the raw file instead of this stage's output,
the row count in `data/features/features.csv` will not match and
the pipeline invariant is broken.
"""
import os

import pandas as pd
import yaml

os.chdir("/root/code/fraud-detection")

with open("configs/pipeline_config.yaml") as f:
    config = yaml.safe_load(f)

raw_path = config["data"]["raw_path"]
processed_path = config["data"]["processed_path"]

df = pd.read_csv(raw_path)
before = len(df)

df = df[df["amount"] >= 50].copy()
df = df.drop_duplicates().reset_index(drop=True)

os.makedirs(os.path.dirname(processed_path), exist_ok=True)
df.to_csv(processed_path, index=False)

print(
    f"[preprocess] raw_rows={before} -> processed_rows={len(df)}  "
    f"({before - len(df)} dropped)"
)
```

## featurize.py
```
"""Stage 2 — Featurize.

Reads the upstream stage's output, engineers one derived column
(`amount_log = log1p(amount)`), and writes the feature matrix to
`data/features/features.csv` for the training stage to consume.

Every concern other than the input wiring is correctly in place —
feature engineering, column preservation, on-disk layout. Adjust
the input source so the stage-chain invariant holds: the row count
out of this stage must match the row count the preprocess stage
produced.
"""
import os

import numpy as np
import pandas as pd
import yaml

os.chdir("/root/code/fraud-detection")

with open("configs/pipeline_config.yaml") as f:
    config = yaml.safe_load(f)

input_path = config["data"]["raw_path"]
features_path = config["data"]["features_path"]

df = pd.read_csv(input_path)
df["amount_log"] = np.log1p(df["amount"])

os.makedirs(os.path.dirname(features_path), exist_ok=True)
df.to_csv(features_path, index=False)

print(
    f"[featurize] input={input_path}  rows={len(df)}  "
    f"columns={len(df.columns)}"
)
```

## train.py
```
"""Stage 3 — Train.

Reads the feature matrix, splits out a stratified held-out test
set (persisted to `data/features/test_set.csv` so the evaluation
stage scores on the same rows), fits a RandomForest per the config,
and writes the pickled model to `models/model.pkl`.
"""
import os

import joblib
import pandas as pd
import yaml
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

os.chdir("/root/code/fraud-detection")

with open("configs/pipeline_config.yaml") as f:
    config = yaml.safe_load(f)

features_path = config["data"]["features_path"]
target = config["data"]["target_column"]
test_size = config["data"]["test_size"]
seed = config["data"]["random_state"]
model_path = config["output"]["model_path"]

df = pd.read_csv(features_path)
X = df.drop(columns=[target])
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=test_size, stratify=y, random_state=seed,
)

test_set_path = "data/features/test_set.csv"
X_test_df = X_test.copy()
X_test_df[target] = y_test
X_test_df.to_csv(test_set_path, index=False)

model = RandomForestClassifier(
    n_estimators=config["model"]["n_estimators"],
    max_depth=config["model"]["max_depth"],
    random_state=config["model"]["random_state"],
)
model.fit(X_train, y_train)

os.makedirs(os.path.dirname(model_path), exist_ok=True)
joblib.dump(model, model_path)

print(f"[train] rows={len(df)}  model_saved={model_path}")
```

## evaluate.py
```
"""Stage 4 — Evaluate.

Loads the model and the held-out test set from the training stage
and writes the evaluation metrics (`accuracy`, `f1`, `roc_auc`) to
`reports/evaluation.json` as a flat numeric dict.
"""
import json
import os

import joblib
import pandas as pd
import yaml
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score

os.chdir("/root/code/fraud-detection")

with open("configs/pipeline_config.yaml") as f:
    config = yaml.safe_load(f)

target = config["data"]["target_column"]
model_path = config["output"]["model_path"]
report_path = config["output"]["report_path"]

model = joblib.load(model_path)
test_df = pd.read_csv("data/features/test_set.csv")
X_test = test_df.drop(columns=[target])
y_test = test_df[target]

preds = model.predict(X_test)
proba = model.predict_proba(X_test)[:, 1]

metrics = {
    "accuracy": round(float(accuracy_score(y_test, preds)), 6),
    "f1": round(float(f1_score(y_test, preds, zero_division=0)), 6),
    "roc_auc": round(float(roc_auc_score(y_test, proba)), 6),
}

os.makedirs(os.path.dirname(report_path), exist_ok=True)
with open(report_path, "w") as f:
    json.dump(metrics, f, indent=2)

print(f"[evaluate] metrics={metrics}  report_saved={report_path}")
```

## run_pipeline.py
```
"""Orchestrator — runs all four pipeline stages in order under a
single MLflow run.

Logs the config-driven model hyperparameters as run parameters
before the stages fire, and the final evaluation metrics (read back
from `reports/evaluation.json`) once the last stage completes. Fails
fast on the first non-zero stage exit.
"""
import json
import os
import subprocess
import sys

import mlflow
import yaml

os.chdir("/root/code/fraud-detection")

with open("configs/pipeline_config.yaml") as f:
    config = yaml.safe_load(f)

mlflow.set_tracking_uri(config["mlflow"]["tracking_uri"])
mlflow.set_experiment(config["mlflow"]["experiment_name"])

STAGES = ["preprocess.py", "featurize.py", "train.py", "evaluate.py"]


def main():
    with mlflow.start_run(run_name="full-pipeline"):
        mlflow.log_param("model_type", config["model"]["type"])
        mlflow.log_param("n_estimators", config["model"]["n_estimators"])
        mlflow.log_param("max_depth", config["model"]["max_depth"])

        for stage in STAGES:
            print(f"[pipeline] running src/{stage} ...")
            result = subprocess.run(
                [sys.executable, f"src/{stage}"],
                capture_output=True, text=True,
            )
            sys.stdout.write(result.stdout)
            if result.returncode != 0:
                sys.stderr.write(result.stderr)
                raise SystemExit(f"[pipeline] stage failed: {stage}")

        report_path = config["output"]["report_path"]
        with open(report_path) as f:
            metrics = json.load(f)
        for key, value in metrics.items():
            mlflow.log_metric(key, value)

        mlflow.log_artifact(config["output"]["model_path"])
        print("[pipeline] completed.")


if __name__ == "__main__":
    main()
```
