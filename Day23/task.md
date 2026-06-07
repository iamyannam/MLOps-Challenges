A xFusionCorp Industries data scientist has accumulated ten runs in the fraud-detection MLflow experiment. Your task is to triage those runs via the MLflow UI: mark the single best-performing candidate as the shortlisted model, and flag every clearly under-performing run for removal.


1.  The MLflow tracking server is already running on port 5000, and the fraud-detection experiment has been pre-populated with ten runs. The runs can be viewed via the MLflow UI button → fraud-detection experiment.

2.  Using the MLflow UI, complete the triage below. The end state is what is tested—the path taken through the UI is not.
    +  Shortlist the best candidate. Among all runs where metrics.f1_score > 0.85, the single run with the highest f1_score must carry a run-level tag: key review-status, value shortlisted.
    +  Reject the under-performers. Every run where metrics.f1_score < 0.75 must carry a run-level tag: key review-status, value rejected.

3.  The other runs (those in the 0.75 ≤ f1 ≤ 0.85 band, and the second-best shortlisting candidate) must carry no review-status tag at all.

send_runs.py
```
"""Seed the `fraud-detection` experiment with ten runs carrying
deterministic synthetic metrics.

No model is trained — f1_score and accuracy are hardcoded. The lab
exercises the MLflow UI's triage workflow (search, sort, tag) and
does not depend on real metric values. Synthetic values make the
set of runs deterministic across spawns and keep startup under
the §12.3.A.4 time budget.
"""
import sys
import mlflow
from mlflow import MlflowClient

TRACKING_URI = "http://localhost:5000"
EXPERIMENT_NAME = "fraud-detection"

# The ten pre-seeded runs. Values are chosen so that both the
# `metrics.f1_score > 0.85` filter (runs 5-9) and the
# `metrics.f1_score < 0.75` filter (runs 1 and 10) return non-empty
# result sets, and the top f1_score (0.95) is unambiguous.
RUNS = [
    {"n_estimators":  50, "max_depth":  3, "f1_score": 0.72, "accuracy": 0.70},
    {"n_estimators": 100, "max_depth":  4, "f1_score": 0.78, "accuracy": 0.76},
    {"n_estimators": 150, "max_depth":  5, "f1_score": 0.81, "accuracy": 0.80},
    {"n_estimators": 200, "max_depth":  6, "f1_score": 0.84, "accuracy": 0.83},
    {"n_estimators": 250, "max_depth":  7, "f1_score": 0.86, "accuracy": 0.85},
    {"n_estimators": 300, "max_depth":  8, "f1_score": 0.88, "accuracy": 0.87},
    {"n_estimators": 350, "max_depth":  9, "f1_score": 0.91, "accuracy": 0.89},
    {"n_estimators": 400, "max_depth": 10, "f1_score": 0.93, "accuracy": 0.92},
    {"n_estimators": 500, "max_depth": 12, "f1_score": 0.95, "accuracy": 0.94},
    {"n_estimators":  25, "max_depth":  2, "f1_score": 0.70, "accuracy": 0.68},
]


def main():
    mlflow.set_tracking_uri(TRACKING_URI)
    client = MlflowClient()

    existing = client.get_experiment_by_name(EXPERIMENT_NAME)
    if existing is not None:
        run_count = len(client.search_runs([existing.experiment_id]))
        if run_count >= len(RUNS):
            # Re-spawn safety: runs already present, do not duplicate.
            sys.exit(0)
        experiment_id = existing.experiment_id
    else:
        experiment_id = client.create_experiment(EXPERIMENT_NAME)

    for cfg in RUNS:
        run = client.create_run(experiment_id=experiment_id)
        run_id = run.info.run_id
        client.log_param(run_id, "n_estimators", cfg["n_estimators"])
        client.log_param(run_id, "max_depth", cfg["max_depth"])
        client.log_metric(run_id, "f1_score", cfg["f1_score"])
        client.log_metric(run_id, "accuracy", cfg["accuracy"])
        client.set_terminated(run_id)


if __name__ == "__main__":
    main()
```
