#### Fixed MLFlow reader access on Policy

<img width="1911" height="945" alt="image" src="https://github.com/user-attachments/assets/6b30f949-f9eb-406c-8dd9-3855f18412dd" />

#### Created Approle

<img width="1915" height="980" alt="image" src="https://github.com/user-attachments/assets/3a307a77-3137-407b-8ff9-1882f66995e1" />

#### Configured policy details into approle to enable MLFlow

CLI Command  - ```vault write auth/approle/role/mlflow \     token_policies="mlflow-reader" \     token_ttl=1h \     token_max_ttl=3h```

<img width="1906" height="980" alt="image" src="https://github.com/user-attachments/assets/e23d5db5-d4af-4e23-9511-82a6c43c7c8d" />

#### MLFlow UI - 

<img width="1901" height="944" alt="image" src="https://github.com/user-attachments/assets/c94f6d3a-2219-494d-b01a-d149edf057f8" />



