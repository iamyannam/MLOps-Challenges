SeeweedFS endpoint is missing in the mlflow flow server start.

**start-mlflow.sh**
```
#!/bin/bash
# Start the MLflow tracking server with the production-style wiring:
# - PostgreSQL backend for run metadata
# - SeaweedFS (S3-compatible) for artefact storage
# - host/CORS flags so the MLflow UI button works through the lab proxy
set -e

export AWS_ACCESS_KEY_ID=weedadmin
export AWS_SECRET_ACCESS_KEY=weedadmin123
export MLFLOW_S3_ENDPOINT_URL=http://localhost:8333

exec mlflow server \
  --backend-store-uri postgresql://mlflow:mlflow123@localhost:5432/mlflow \
  --artifacts-destination s3://mlflow-artifacts \
  --host 0.0.0.0 --port 5000 \
  --allowed-hosts '*' --cors-allowed-origins '*'
```

> A trpical Seeweed deployment has the floowing
```
  master        : 9333
  volume        : 8080
  filer         : 8888
  s3 gateway    : 8333
```

run ```bash /root/code/restart-mlflow.sh```

run ```python3 /root/code/log_test_run.py```

<img width="1896" height="392" alt="image" src="https://github.com/user-attachments/assets/e27c386a-78f9-446e-8af9-f83f05b0e99b" />

<img width="920" height="347" alt="image" src="https://github.com/user-attachments/assets/382b63dd-e377-4aee-b93b-6515d8ec2928" />

