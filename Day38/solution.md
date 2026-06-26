## train_parallel.py

```
"""Parallel training bake-off for the fraud-detection model.

Trains the same RandomForestClassifier twice — once on a single
worker, once across every available CPU — so the two configurations
can be compared side-by-side in the MLflow UI. Every run logs the
measured wall time as `metrics.training_time_seconds` and the
`n_jobs` value actually used under `params.n_jobs`.

Every non-end-state concern is correctly wired — data loading, CV
split, MLflow experiment setup, model persistence. Adjust the
`N_JOBS_VALUES` list and the `mlflow.log_param` call so the second
run actually runs in parallel and the logged `n_jobs` parameter
distinguishes the two runs in the UI.
"""
import os
import time

import joblib
import mlflow
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

TRACKING_URI = "http://localhost:5000"
EXPERIMENT = "parallel-training"
TRAIN_CSV = "/root/code/fraud-detection/data/train.csv"
MODEL_PATH = "/root/code/fraud-detection/models/model.pkl"

N_ESTIMATORS = 200
RANDOM_STATE = 42

N_JOBS_VALUES = [1, -1]


def main():
    mlflow.set_tracking_uri(TRACKING_URI)
    mlflow.set_experiment(EXPERIMENT)

    df = pd.read_csv(TRAIN_CSV)
    X = df.drop(columns=["is_fraud"])
    y = df["is_fraud"]

    last_model = None
    for n_jobs in N_JOBS_VALUES:
        run_name = "serial" if n_jobs == 1 else "parallel"
        with mlflow.start_run(run_name=run_name):
            mlflow.log_param("n_jobs", n_jobs)
            mlflow.log_param("n_estimators", N_ESTIMATORS)

            model = RandomForestClassifier(
                n_estimators=N_ESTIMATORS,
                random_state=RANDOM_STATE,
                n_jobs=n_jobs,
            )
            start = time.perf_counter()
            with joblib.parallel_backend("multiprocessing"):
                model.fit(X, y)           
            elapsed = time.perf_counter() - start

            mlflow.log_metric("training_time_seconds", elapsed)
            print(
                f"[{run_name}] n_jobs={n_jobs}  "
                f"training_time_seconds={elapsed:.3f}"
            )
            last_model = model

    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(last_model, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")


if __name__ == "__main__":
    main()
```

<img width="1132" height="827" alt="image" src="https://github.com/user-attachments/assets/17edaf6b-4d6c-4fde-9c8a-31f9d4532733" />

### Understanding the concept

#### Serial vs Parallel Run for a model
