```
cd /root/code/fraud-detection

# Run three experiments with different n_estimators values
dvc exp run -S n_estimators=50
dvc exp run -S n_estimators=200
dvc exp run -S n_estimators=500

# Compare metrics and parameters across experiments
dvc exp show
```
The dvc exp show output will include the experiment IDs, n_estimators, and the resulting f1_score from metrics.json.
Once you identify the experiment with the highest f1_score, apply it to the workspace:
```dvc exp apply ```

After applying the experiment, the workspace will contain:

+  the selected n_estimators value in params.yaml
+  the corresponding metrics.json
+  the corresponding models/model.pkl

To make that state the tracked project state, commit the changes:
```
git add .
git commit -m "Promote best DVC experiment"
```

<img width="1020" height="760" alt="image" src="https://github.com/user-attachments/assets/338811e4-fc02-4cd1-99aa-b39fe702d1d6" />
