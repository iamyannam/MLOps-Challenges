#### production.yaml

```
name: Production release

on:
  pull_request:
    branches: [main]

env:
  VAULT_ADDR: http://localhost:8200
  MLFLOW_TRACKING_URI: http://localhost:5000

jobs:
  fetch-secret:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Read MLflow password from Vault
        run: |
          TOKEN=$(cat /root/code/vault-token)
          PASSWORD=$(curl -s -H "X-Vault-Token: $TOKEN" "$VAULT_ADDR/v1/secret/data/mlflow" | jq -r '.data.data.mlflow_password // empty')

          if [ -z "$PASSWORD" ]; then
            echo "::error::Failed to retrieve mlflow_password from Vault at secret/data/mlflow"
            exit 1
          fi

          echo "::notice::Successfully fetched mlflow_password (length: ${#PASSWORD})"

  data-quality:
    runs-on: ubuntu-latest
    needs: fetch-secret
    steps:
      - uses: actions/checkout@v4
      - name: Install Great Expectations
        run: pip install --break-system-packages great_expectations pandas numpy
      - name: Run schema checkpoint
        run: python3 -m src.gx_run --checkpoint schema_check

  register-model:
    runs-on: ubuntu-latest
    needs: data-quality
    steps:
      - uses: actions/checkout@v4
      - name: Install deps
        run: pip install --break-system-packages mlflow numpy scikit-learn pandas
      - name: Register model
        env:
          VAULT_KEY_USED: mlflow_password
        run: python3 -m src.register
      - name: Assert a version exists in the registry
        run: |
          python3 -c "
          import mlflow
          mlflow.set_tracking_uri('$MLFLOW_TRACKING_URI')
          client = mlflow.tracking.MlflowClient()
          rm = client.get_registered_model('fraud-detector')
          assert rm.latest_versions, 'fraud-detector has no versions'
          print('Registered model versions:', [v.version for v in rm.latest_versions])
          "
```

#### Stage Secret in Vault (Port 8200)
Access Vault and create secret secret/mlflow.
et key mlflow_password to any non-empty value (e.g., supersecret2026).

#### Execute below commands for code push

```
cd /root/code/fraud-detector
git checkout production-release
git add .gitea/workflows/production.yml
git commit -m "feat: implement vault secret fetch in workflow"
git push origin production-release
```

#### Gitea PR Execution (Port 3000)
+  Log in to Gitea (gitea-admin / gitea2026).
+  Create a PR from production-release $\rightarrow$ main.
+  Verify all 3 jobs (fetch-secret $\rightarrow$ data-quality $\rightarrow$ register-model) complete successfully.
+  Merge the Pull Request.

#### Promote Model in MLflow (Port 5000)
+  Go to MLflow UI $\rightarrow$ Models $\rightarrow$ fraud-detector.
+  Select the registered version created by the workflow.
+  Add the production alias to point to this version.
