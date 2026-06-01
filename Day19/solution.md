1. Correct dvc.yaml file by using the commands and dvc repro
```
stages:
  ingest:
    cmd: python scripts/ingest.py
    deps:
      - scripts/ingest.py
      - data/raw/data.csv

  validate:
    cmd: python scripts/validate.py
    deps:
      - data/raw/data.csv
      - scripts/validate.py
    outs:
      - reports/validation.json:
          cache: false

  preprocess:
    cmd: python scripts/preprocess.py
    deps:
      - data/raw/data.csv
      - scripts/preprocess.py
    outs:
      - data/processed/clean.csv

  train:
    cmd: python scripts/train.py
    deps:
      - data/processed/clean.csv
      - scripts/train.py
    params:
      - n_estimators
      - max_depth
      - test_size
      - random_seed
    outs:
      - models/model.pkl
      - data/processed/test_split.csv
    metrics:
      - metrics.json:
          cache: false

  evaluate:
    cmd: python scripts/evaluate.py
    deps:
      - models/model.pkl
      - data/processed/test_split.csv
      - scripts/evaluate.py
    outs:
      - reports/evaluation.json:
          cache: false
```
2.  End to end instructions from the r=terminal
```

root@controlplane ~/code ✖ cd ml-pipeline/

root@controlplane ml-pipeline on  main ➜  cp scripts-staging/train.py scripts/

root@controlplane ml-pipeline on  main [?] ➜  cp scripts-staging/evaluate.py scripts/

root@controlplane ml-pipeline on  main [?] ➜  dvc repro
Running stage 'ingest':                                                
> python scripts/ingest.py
Data ingested successfully: 20 rows, 5 columns
Generating lock file 'dvc.lock'                                        
Updating lock file 'dvc.lock'

Running stage 'validate':                                              
> python scripts/validate.py
Validation: 20 rows, valid=True
Updating lock file 'dvc.lock'                                          

Running stage 'preprocess':                                            
> python scripts/preprocess.py
Preprocessed: 20 clean rows
Updating lock file 'dvc.lock'                                          

Running stage 'train':                                                 
> python scripts/train.py
Trained: {'accuracy': 1.0, 'f1_score': 1.0}
Updating lock file 'dvc.lock'                                          

Running stage 'evaluate':                                              
> python scripts/evaluate.py
Evaluation: {'accuracy': 1.0, 'f1_score': 1.0, 'precision': 1.0, 'recall': 1.0, 'test_samples': 4}
Updating lock file 'dvc.lock'                                          

To track the changes with git, run:

        git add dvc.lock

To enable auto staging, run:

        dvc config core.autostage true
Use `dvc push` to send your updates to remote storage.

root@controlplane ml-pipeline on  main [!?] ➜  dvc push
Collecting                                  |3.00 [00:00, 1.10kentry/s]
Pushing
3 files pushed                                                         
                                                                       
root@controlplane ml-pipeline on  main [!?] ➜  git add .              

root@controlplane ml-pipeline on  main [+] ➜  git commit -m "End to End changes"
[main 01f7d4f] End to End changes
 7 files changed, 228 insertions(+), 1 deletion(-)
 create mode 100644 dvc.lock
 create mode 100644 metrics.json
 create mode 100644 reports/evaluation.json
 create mode 100644 reports/validation.json
 create mode 100644 scripts/evaluate.py
 create mode 100644 scripts/train.py

root@controlplane ml-pipeline on  main ➜  git tag v1.0

root@controlplane ml-pipeline on  main ➜  git tag -l
v1.0

root@controlplane ml-pipeline on  main ➜  
```

3.  Check the output in SeaweedFS filter
    <img width="1754" height="489" alt="image" src="https://github.com/user-attachments/assets/c3f5e404-ea76-4608-bb73-103918771a7b" />
