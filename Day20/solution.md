1. Create Required DirectoriesMLflow requires the target backend directory to exist before launching, or the startup will fail.
```
mkdir -p /root/code/mlflow-backend/
mkdir -p /root/code/mlflow-artifacts/
```
3. Launch the MLflow Tracking ServerRun the tracking server in the background using nohup so it persists after closing the terminal. The flags ensure it binds to all interfaces,
connects to the SQLite database, stores artifacts in the correct directory, and bypasses proxy restrictions.
```
nohup mlflow server \
  --host 0.0.0.0 \
  --port 5000 \
  --backend-store-uri sqlite:////root/code/mlflow-backend/mlflow.db \
  --default-artifact-root /root/code/mlflow-artifacts/ \
  --cors-allowed-origins '*' \
  --allowed-hosts '*' > /root/code/mlflow.log 2>&1 &
```
3. Verify Server StatusConfirm that the server is active, listening on port 5000, and that the SQLite database file has been successfully initialized.bash# Check if the process is running
``` 
ps aux | grep mlflow
ls -l /root/code/mlflow-backend/mlflow.db
```
4. Click on MLFlow UI button

<img width="1918" height="864" alt="image" src="https://github.com/user-attachments/assets/b523f2a9-2c18-41f7-96b1-cfdb4866c60b" />

<img width="1868" height="931" alt="image" src="https://github.com/user-attachments/assets/f25b725c-ca19-4d31-ad22-2477e81cbf23" />


