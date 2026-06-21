**cross_validate.py**

```
"""Cross-validation evaluator for the fraud-detection model.

Runs k-fold cross-validation, logs every fold as a nested MLflow run
under a single parent, and writes an aggregate report at
`reports/cv_results.json`.

Every non-end-state concern is correctly wired — fold iteration,
metric computation, parent + child MLflow runs, artefact logging.
Adjust the CV splitter and the aggregate dict so the report
matches the schema the release checklist requires.
"""
import os
import json
import numpy as np
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold, StratifiedKFold
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score

TRAIN_CSV = "/root/code/fraud-detection/data/train.csv"
REPORTS_DIR = "/root/code/fraud-detection/reports"
CV_RESULTS_JSON = os.path.join(REPORTS_DIR, "cv_results.json")
N_SPLITS = 5
EXPERIMENT_NAME = "fraud-detection-cv"


def main():
    df = pd.read_csv(TRAIN_CSV)
    X = df.drop(columns=["is_fraud"])
    y = df["is_fraud"]

    cv = StratifiedKFold(n_splits=N_SPLITS, shuffle=True, random_state=42) #

    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.set_experiment(EXPERIMENT_NAME)

    fold_results = []

    with mlflow.start_run(run_name="cv-parent"):
        mlflow.log_param("n_splits", N_SPLITS)
        mlflow.log_param("cv_type", type(cv).__name__)

        for fold_idx, (train_idx, test_idx) in enumerate(cv.split(X, y), start=1):
            X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
            y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

            model = RandomForestClassifier(
                n_estimators=100, max_depth=5, random_state=42
            )
            model.fit(X_train, y_train)
            preds = model.predict(X_test)
            proba = model.predict_proba(X_test)[:, 1]

            fold = {
                "fold": fold_idx,
                "accuracy": round(accuracy_score(y_test, preds), 6),
                "f1": round(f1_score(y_test, preds), 6),
                "roc_auc": round(roc_auc_score(y_test, proba), 6),
            }
            fold_results.append(fold)

            with mlflow.start_run(run_name=f"fold-{fold_idx}", nested=True):
                mlflow.log_param("fold", fold_idx)
                mlflow.log_metric("accuracy", fold["accuracy"])
                mlflow.log_metric("f1", fold["f1"])
                mlflow.log_metric("roc_auc", fold["roc_auc"])

        acc_vals = [r["accuracy"] for r in fold_results]
        f1_vals = [r["f1"] for r in fold_results]
        auc_vals = [r["roc_auc"] for r in fold_results]

        aggregate = {
            "mean_accuracy": round(float(np.mean(acc_vals)), 6),
            "std_accuracy": round(float(np.std(acc_vals)), 6),
            "mean_f1": round(float(np.mean(f1_vals)), 6),
            "std_f1": round(float(np.std(f1_vals)), 6),
            "mean_roc_auc": round(float(np.mean(auc_vals)), 6),
            "std_roc_auc": round(float(np.std(auc_vals)), 6),
            "folds": fold_results,
        }

        mlflow.log_metric("mean_accuracy", aggregate["mean_accuracy"])
        mlflow.log_metric("std_accuracy", aggregate["std_accuracy"])       
        mlflow.log_metric("mean_f1", aggregate["mean_f1"])
        mlflow.log_metric("std_f1", aggregate["std_f1"])       
        mlflow.log_metric("mean_roc_auc", aggregate["mean_roc_auc"])
        mlflow.log_metric("std_roc_auc", aggregate["std_roc_auc"])

        os.makedirs(REPORTS_DIR, exist_ok=True)
        with open(CV_RESULTS_JSON, "w") as f:
            json.dump(aggregate, f, indent=2, sort_keys=False)
        mlflow.log_artifact(CV_RESULTS_JSON)

    print(f"aggregate: {aggregate}")
    print(f"report: {CV_RESULTS_JSON}")


if __name__ == "__main__":
    main()
```


<img width="1885" height="955" alt="image" src="https://github.com/user-attachments/assets/03f0c506-19a4-420a-9f5a-0c8ebf2c7f14" />


**MLFlow UI**

<img width="1862" height="968" alt="image" src="https://github.com/user-attachments/assets/414ca534-023b-4aa3-9da3-d7a297184725" />
