**Make sure to run all the trainer scripts first**

<img width="1047" height="866" alt="image" src="https://github.com/user-attachments/assets/b75d95d7-d39e-4e4a-b196-7efe1bf0b9a4" />

## Fix bakeoff.py script and run it.

`"""Pick the winning candidate from the `bakeoff` MLflow experiment and
persist it at /root/code/fraud-detection/reports/winner.json.

Assumes train_rf.py, train_gb.py, and train_lr.py have each been run
at least once so the experiment contains three candidate runs.

The winner is the run with the highest metrics.f1_score. The saved
report must contain:

    {
      "model_type": "<candidate tag>",
      "run_id":     "<mlflow run id>",
      "f1_score":   <float>
    }
"""
import json
import os

import mlflow

TRACKING_URI = "http://localhost:5000"
EXPERIMENT = "bakeoff"
REPORTS_DIR = "/root/code/fraud-detection/reports"
WINNER_JSON = os.path.join(REPORTS_DIR, "winner.json")


def main():
    mlflow.set_tracking_uri(TRACKING_URI)
    client = mlflow.MlflowClient()
    exp = client.get_experiment_by_name(EXPERIMENT)
    if exp is None:
        raise SystemExit(
            f"Experiment {EXPERIMENT!r} not found. Run the three "
            "trainer scripts first."
        )

    runs = mlflow.search_runs(
        experiment_ids=[exp.experiment_id],
        order_by=["metrics.f1_score DESC"],
        max_results=10,
    )
    if runs.empty:
        raise SystemExit(
            f"No runs found in {EXPERIMENT!r}. Run the three trainer "
            "scripts first."
        )

    winner = runs.iloc[0]

    # FIX 2: Identify the correct tag column for model_type dynamically
    model_type_column = "tags.model_type" if "tags.model_type" in winner else "tags.mlflow.runName"

    report = {
        "model_type": winner.get(model_type_column, "unknown"),
        "run_id": winner["run_id"],
        "f1_score": float(winner["metrics.f1_score"]),
    }

    os.makedirs(REPORTS_DIR, exist_ok=True)
    with open(WINNER_JSON, "w") as f:
        json.dump(report, f, indent=2)

    print(f"Winner written to {WINNER_JSON}: {report}")


if __name__ == "__main__":
    main()``

```


<img width="1766" height="882" alt="image" src="https://github.com/user-attachments/assets/6ce15ced-0bda-4b35-b096-3025399c0ed4" />


<img width="1878" height="971" alt="image" src="https://github.com/user-attachments/assets/008298f8-8039-4ae4-8696-688ded902e17" />
