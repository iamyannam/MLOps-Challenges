**autolog_experiment.py**
```
"""
MLflow autologging — two TODO blocks activate MLflow's automatic
capture of parameters, metrics, and the trained model for the
`model.fit(...)` call below.

The dataset and the model here are synthetic. A LogisticRegression
fitted on a deterministic four-row XOR-like array stands in for a
real training step so that autologging has a valid sklearn fit()
call to instrument. No real ML workflow takes place; the focus of
the lab is autolog configuration, not model quality.

Both TODO blocks must be completed BEFORE `model.fit(...)` runs —
autolog hooks sklearn at call time, and the active experiment
scopes where the autologged run lands.
"""
import numpy as np
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression

mlflow.set_tracking_uri("http://localhost:5000")


# TODO 1: enable autologging for the sklearn flavour so that the
# subsequent model.fit(...) call records parameters, metrics, and
# the trained model on the active experiment automatically.
mlflow.sklearn.autolog()

# TODO 2: set the active experiment to "autolog-demo" so the
# autologged run lands in that experiment rather than the Default one.
mlflow.set_experiment("autolog-demo")

# Synthetic four-row XOR-like array. Not a real ML dataset — just
# a deterministic toy to give sklearn.fit() something to execute.
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 1, 1])

model = LogisticRegression(C=1.0, max_iter=100, random_state=42)
model.fit(X, y)

print("Autolog run complete — check the MLflow UI")

```

Once run the command ```   python3 /root/code/autolog_experiment.py``` ,check for MLFlow UI experminets

<img width="1871" height="460" alt="image" src="https://github.com/user-attachments/assets/ec3b5515-154a-4a84-9cda-0dc063e2f0b0" />

<img width="1828" height="483" alt="image" src="https://github.com/user-attachments/assets/d787d51c-42dc-4281-83b5-3497df661fa4" />

<img width="1858" height="936" alt="image" src="https://github.com/user-attachments/assets/5695d727-82eb-4860-a80f-e78b1eb25b77" />


