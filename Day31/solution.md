**train_config.yml**
```
model:
  type: RandomForestClassifier
  n_estimators: 100
  max_depth: 5
  random_state: 42
data:
  train_path: /root/code/fraud-detection/data/train.csv
  target_column: is_fraud
output:
  model_path: /root/code/fraud-detection/models/model.pkl
mlflow:
  tracking_uri: http://localhost:5000
  experiment_name: fraud-detection

```
Check in MLFlow UI for successful run for fraud-detection.

<img width="1834" height="953" alt="image" src="https://github.com/user-attachments/assets/121b8f33-d551-4987-a5b4-bb170fbdf7f9" />



<img width="1053" height="841" alt="image" src="https://github.com/user-attachments/assets/6c702f33-2ac5-4ec1-94b7-f2089c78abd0" />
