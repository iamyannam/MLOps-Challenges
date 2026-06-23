## tune.py
```
import os
import yaml
import numpy as np
import pandas as pd
import optuna
import mlflow
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score

TRAIN_CSV = "/root/code/fraud-detection/data/train.csv"
CONFIGS_DIR = "/root/code/fraud-detection/configs"
BEST_PARAMS_YAML = os.path.join(CONFIGS_DIR, "best_params.yaml")
EXPERIMENT_NAME = "hyperopt-tuning"
N_TRIALS = 20
N_SPLITS = 3

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment(EXPERIMENT_NAME)


def objective(trial, X, y):
    n_estimators = trial.suggest_int("n_estimators", 50, 500)
    max_depth = trial.suggest_int("max_depth", 3, 20)

    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=42,
    )

    cv = StratifiedKFold(
        n_splits=N_SPLITS,
        shuffle=True,
        random_state=42,
    )

    scores = cross_val_score(model, X, y, cv=cv, scoring="f1")
    score = float(np.mean(scores))

    # Log each trial as an independent MLflow run
    with mlflow.start_run():
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_metric("f1_score", score)

    return score


def main():
    df = pd.read_csv(TRAIN_CSV)
    X = df.drop(columns=["is_fraud"])
    y = df["is_fraud"]

    study = optuna.create_study(
        direction="maximize",
        study_name=EXPERIMENT_NAME,
    )

    study.optimize(
        lambda trial: objective(trial, X, y),
        n_trials=N_TRIALS,
    )

    os.makedirs(CONFIGS_DIR, exist_ok=True)

    with open(BEST_PARAMS_YAML, "w") as f:
        yaml.safe_dump(
            study.best_params,
            f,
            sort_keys=True,
        )

    print(f"best params: {study.best_params}")
    print(f"best f1: {study.best_value:.6f}")
    print(f"wrote {BEST_PARAMS_YAML}")


if __name__ == "__main__":
    main()
```
## run tune.py

<img width="1020" height="808" alt="image" src="https://github.com/user-attachments/assets/8312a1d5-446e-45c3-8f37-585d7fa7ba28" />


