#### Create docker file

```
# ML training image for the fraud-detection trainer.
#
# Author each instruction below to the team standard, then build with:
#   docker build -t ml-trainer:v1 .
# from inside /root/code/ml-docker/.

# TODO 1: Base image — use python:3.11-slim. Do not use an alpine
#         base: its musl libc has no manylinux wheel for scikit-learn,
#         so the pip install fails (or falls back to a slow source
#         build that exceeds the lab's memory budget).
FROM python:3.11-slim

# TODO 2: Set the working directory to /app.
WORKDIR /app

# TODO 3: Install the training dependencies with pip (no cache):
#         scikit-learn, pandas, numpy, joblib. All four are imported
#         by train.py — joblib is used at runtime for joblib.dump, so
#         omitting it aborts the container with ModuleNotFoundError.
RUN pip install --no-cache-dir scikit-learn pandas numpy joblib

# TODO 4: Copy train.py into the image at /app/train.py.
COPY train.py /app/train.py

# TODO 5: Set the default command to run the trainer: python3 train.py.
CMD ["python3", "train.py"]
```

#### docker build -t ml-training:v1 .

