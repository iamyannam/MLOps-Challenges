Find the model which has highest f1_score from MLFlow UI

<img width="1900" height="553" alt="image" src="https://github.com/user-attachments/assets/5160c8db-6a5b-4bc8-9290-ebe597fdb31c" />

Register the model 'fraud-detector-v2' as and add alias 'champion'

<img width="1878" height="530" alt="image" src="https://github.com/user-attachments/assets/3ede6e3e-e403-4fa1-ae1b-f279c203dd2d" />

run in shell ```export MLFLOW_TRACKING_URI=http://localhost:5000```

```
nohup mlflow models serve \
  -m "models:/fraud-detector-v2@champion" \
  --host 0.0.0.0 \
  --port 5001 \
  --env-manager=local \
  >/tmp/fraud-detector-v2-serve.log 2>&1 &
```

Verify the server is listening - ```curl -i http://localhost:5001/health```

run monitor.sh to see if it healthy 

create monitor.sh  from the given template and make it executable and run

<img width="1044" height="781" alt="image" src="https://github.com/user-attachments/assets/b2eafef7-576b-41cb-852b-48bf8f80e698" />


