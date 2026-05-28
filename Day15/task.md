The xFusionCorp Industries ML team manages model hyperparameters through params.yaml so experiments can vary without code changes. The fraud-detection project's train stage already wires params.yaml for n_estimators, but dvc repro currently fails. Correct the parameter wiring and demonstrate that DVC re-runs the train stage when the parameter changes.


1.  A project exists at /root/code/fraud-detection/ with a three-stage DVC pipeline (process_data, split_data, train) and a params.yaml already in place. Do not modify the Python files.

2.  The train stage in dvc.yaml references the n_estimators parameter. Every name listed under params: must resolve to a key in params.yaml.

3.  Review params.yaml, correct whatever prevents dvc repro from completing, and run the full pipeline.

4.  Demonstrate that DVC tracks parameter changes by updating n_estimators to a different value (for example 200). Run dvc repro again—only the train stage should re-execute, the new value must be recorded in dvc.lock, and models/model.pkl must be regenerated.

_The DVC extension's PARAMS section under the DVC view will surface the values from params.yaml directly in the editor._

**dvc.yaml file**
```
stages:
  process_data:
    cmd: python src/data/process_data.py
    deps:
      - data/raw/transactions.csv
      - src/data/process_data.py
    outs:
      - data/processed/clean_transactions.csv

  split_data:
    cmd: python src/data/split_data.py
    deps:
      - data/processed/clean_transactions.csv
      - src/data/split_data.py
    outs:
      - data/processed/train.csv
      - data/processed/test.csv

  train:
    cmd: python src/models/train.py
    deps:
      - data/processed/train.csv
      - src/models/train.py
    params:
      - n_estimators
    outs:
      - models/model.pkl
```

**params.yaml file**
```n_estimator: 100```
