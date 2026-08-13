The xFusionCorp Industries ML platform team has deployed a fraud-detection model as a Docker image. However, the current runtime image includes all packages required for the training phase and the training source itself, resulting in an unnecessarily large image. Your objective is to refactor the single-stage Dockerfile located at /root/code/ml-serve/ into a multi-stage build. This should comprise a builder stage that trains the model and generates model.pkl, followed by a runtime stage that installs only the dependencies necessary for serving and copies the trained model from the builder stage.

1. The Docker daemon is already running. docker version can be run in a VS Code terminal to confirm.

2. The project layout under /root/code/ml-serve/:
    +  ```train_model.py``` – Fits a 10-tree RandomForest on the shared 10-row synthetic fraud set and writes /app/model.pkl via joblib.dump(...). Correct and must remain intact.
    +  ```serve.py``` – Flask app loading the model and exposing POST /predict + GET /health on port 8080. Correct and must remain intact.
    +  ```Dockerfile``` – A single-stage build that installs scikit-learn, pandas, numpy, joblib, and flask, runs the trainer at build time to bake the model in, and serves. The reader rewrites this file.

3. The end state must include:
    +  The Dockerfile carries at least two FROM instructions; the first is given a name (e.g. AS builder) so a later stage can reference it.
    +  The builder stage produces /app/model.pkl (the trained model).
    +  The runtime stage contains /app/model.pkl (copied out of the builder stage) and serve.py.
    +  The runtime stage's pip install line installs only the four packages serve.py needs: flask, joblib, numpy, scikit-learn.
    +  ```docker images ml-serve:v1``` lists the built image; docker run --rm -p 8090:8080 ml-serve:v1 exposes /health returning {"status": "ok"} on port 8090.

> Multi-stage builds let you ship runtime images that carry only what the serving app needs — training dependencies and source files stay in the builder stage and are discarded. docker build -t ml-serve:v1 . can be re-run as each change lands; Docker re-uses cached layers when only runtime-stage lines change.

#### Dockerfile

```
FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir scikit-learn pandas numpy joblib flask

COPY train_model.py /app/train_model.py
COPY serve.py /app/serve.py

RUN python3 /app/train_model.py

EXPOSE 8080
CMD ["python3", "/app/serve.py"]
```
#### train_model.py

```
"""Fit a RandomForest on the shared 10-row synthetic fraud set and
persist the trained estimator to `/app/model.pkl` for the runtime
stage to load at container start-up.
"""
import io

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

DATA = """amount,hour,num_tx_past_day,is_fraud
25.50,8,1,0
1250.00,22,4,1
45.00,12,2,0
890.00,2,3,0
3200.00,23,5,1
12.99,9,1,0
567.00,17,2,0
2100.00,1,4,1
33.50,13,2,0
78.00,10,1,0"""

df = pd.read_csv(io.StringIO(DATA))
X = df.drop("is_fraud", axis=1).values
y = df["is_fraud"].values

model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X, y)

joblib.dump(model, "/app/model.pkl")
print("Model saved to /app/model.pkl")
```

###
