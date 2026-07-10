#### Step 1: Log in to HashiCorp Vault
    Select the Token authentication method, paste the copied root token, and log in.
#### Step 2: Enable the KV v2 Secrets Engine
##### Option1 - Using Vault UI
1.  Once logged in, click on Enable new engine on the Secrets overview page.

2.  Select KV from the list of secrets engines and click Next.

3.  In the Path field, enter secret (if it isn't already defaulted).

4.  Expand Method Options or look for the version setting and ensure Version 2 is selected.

5.  Click Enable Engine

##### Option2 - Using CLI
```
export VAULT_TOKEN=$(cat /root/code/vault-token)
export VAULT_ADDR="http://127.0.0.1:8200"

vault secrets enable -path=secret kv-v2
```
#### Step 3: Create the MLflow Secret
##### Option A: Via the Vault UI
1.  Click into the newly created secret/ engine.Click Create secret.

2.  In the Path for this secret field, type mlflow.

3.  In the Secret data table, add the following key-value pair:
    Key: admin_password
    Value: [Enter any non-empty secure password of your choice]
##### Option B: Via CLI
```
vault kv put secret/mlflow admin_password="YourSecurePasswordHere"
```
#### Step 4: Verify Service Startup
Check MLFlow UI
```
curl -I http://localhost:5000/
```

<img width="1831" height="956" alt="image" src="https://github.com/user-attachments/assets/244652d6-6ccb-4b29-b00e-41e48c714e77" />

