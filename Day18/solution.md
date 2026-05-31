
1.  Tag the Baseline State on mainFirst, ensure you are on the main branch and create a Git tag to mark the $v1.0$ baseline.Bash# Ensure you are on the main branch
```
git checkout main
git tag -a v1.0 -m "Baseline dataset and pipeline v1.0"
```
2.  Create and Switch to the New BranchCreate your new feature branch where the upgraded dataset will live.Bashgit checkout -b v2-improved
3.  Replace and Re-track the Dataset with DVCTo overwrite the tracked transactions.csv with the contents of transactions_v2.csv without deleting the source v2 file, use the standard cp command. Then, let DVC know the file has changed.Bash# Overwrite the original dataset file with the v2 contents
```
cp data/raw/transactions_v2.csv data/raw/transactions.csv
dvc add data/raw/transactions.csv
```
4.  Reproduce the Pipeline and Commit ChangesRun the DVC pipeline to update all downstream dependencies and metrics based on the new data, then commit both the Git and DVC tracking files.Bash# Reproduce the pipeline stages affected by the data change
```dvc repro
git add data/raw/transactions.csv.dvc dvc.lock
git commit -m "Upgrade dataset to v2 and re-run pipeline"
```
5.  Switch Back to main and Restore v1 DataSwitch back to your main branch. Because Git only tracks the pointer files (.dvc), you must use DVC to sync the actual workspace data back to the $v1.0$ version.Bash# Switch back to the main branch
```
git checkout main
dvc checkout
```

_VerificationOn main: The data/raw/transactions.csv file now contains the original baseline data matching the hash in the v1.0 tag.DVC Extension UI_
