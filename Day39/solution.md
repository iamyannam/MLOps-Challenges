### PyTorch 
> PyTorch is an open-source deep learning framework developed primarily by Meta's AI Research lab. At its core, it is a Python-based library that provides two main features: an n-dimensional array structure (called a Tensor) that can run calculations lightning-fast on accelerators like GPUs, and an automatic differentiation system used to train deep neural networks."

#### Key Concepts to Mention:
**Tensors:** They act just like NumPy arrays, but with the superpower of being able to run on GPUs/TPUs to speed up math.
**Autograd:** PyTorch automatically calculates the calculus gradients (derivatives) required to update neural network weights during training.

#### train_pytorch.py
```
"""Feedforward fraud-detection trainer.

Trains a tiny two-layer network on the synthetic transactions CSV,
logs the run to MLflow with `params.device` + `metrics.final_loss`,
and saves the trained weights to `models/fraud_model.pt`.

Every non-device concern is correctly wired — data loading, model
definition, optimizer setup, loss function, MLflow experiment. The
current wiring assumes a CUDA GPU is always present. Adjust the
device handling so the script runs on whichever accelerator the
host actually exposes and the logged device parameter reflects
the same value.
"""
import os

import mlflow
import numpy as np
import pandas as pd
import torch
import torch.nn as nn

TRACKING_URI = "http://localhost:5000"
EXPERIMENT = "gpu-training"
TRAIN_CSV = "/root/code/fraud-detection/data/train.csv"
MODEL_PATH = "/root/code/fraud-detection/models/fraud_model.pt"

FEATURES = ["amount", "hour", "num_tx_past_day"]
TARGET = "is_fraud"
EPOCHS = 30
LR = 0.01
SEED = 42


class FraudNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(len(FEATURES), 8)
        self.fc2 = nn.Linear(8, 2)

    def forward(self, x):
        return self.fc2(torch.relu(self.fc1(x)))


def main():
    torch.manual_seed(SEED)
    np.random.seed(SEED)

    mlflow.set_tracking_uri(TRACKING_URI)
    mlflow.set_experiment(EXPERIMENT)

    df = pd.read_csv(TRAIN_CSV)
    X = df[FEATURES].values.astype(np.float32)
    y = df[TARGET].values.astype(np.int64)

    X_t = torch.from_numpy(X)
    y_t = torch.from_numpy(y)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = FraudNet()
    model = model.to(device)

    optimizer = torch.optim.SGD(model.parameters(), lr=LR)
    loss_fn = nn.CrossEntropyLoss()

    with mlflow.start_run(run_name="fraud-mlp"):
        mlflow.log_param("device", str(device))

        xb = X_t.to(device)
        yb = y_t.to(device)

        final_loss = None
        for epoch in range(EPOCHS):
            logits = model(xb)
            loss = loss_fn(logits, yb)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            final_loss = float(loss.item())
            print(f"epoch {epoch:02d}  loss={final_loss:.4f}")

        mlflow.log_metric("final_loss", final_loss)

        os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
        torch.save(model.state_dict(), MODEL_PATH)
        print(f"Model saved to {MODEL_PATH}")


if __name__ == "__main__":
    main()
```
<img width="1858" height="948" alt="image" src="https://github.com/user-attachments/assets/f406ec46-4738-4def-9536-827b3f2916a1" />






