1. Change dvc.yaml file as below
   ```
   stages:
    process_data:
      cmd: python src/data/process.py
      deps:
        - data/raw/transactions.csv
        - src/data/process_data.py
      outs:
        - data/processed/clean_transactions.csv

    split_data:
      cmd: python src/data/split_data.py
      deps:
        - data/processed/clean_transactions.csv
        - src/data/split_data.py
      outs:
        - data/processed/train.csv
        - data/processed/test.csv
   ```
2.  Once done Please foloow '''dvc repro''' and '''dvc status''' commands
```
root@controlplane fraud-detection on  main [!] ✖ dvc status
process_data:                                                              
        changed deps:
                modified:           data/raw/transactions.csv
                modified:           src/data/process_data.py
        changed outs:
                deleted:            data/processed/clean_transactions.csv
split_data:
        changed deps:
                deleted:            data/processed/clean_transactions.csv
                modified:           src/data/split_data.py
        changed outs:
                deleted:            data/processed/train.csv
                deleted:            data/processed/test.csv

root@controlplane fraud-detection on  main [!] ➜  dvc repro
Running stage 'process_data':                                              
> python src/data/process_data.py
Processed 15 rows
Generating lock file 'dvc.lock'                                            
Updating lock file 'dvc.lock'

Running stage 'split_data':                                                
> python src/data/split_data.py
Train: 12 rows, Test: 3 rows
Updating lock file 'dvc.lock'                                              

To track the changes with git, run:

        git add data/processed/.gitignore dvc.lock

To enable auto staging, run:

        dvc config core.autostage true
Use `dvc push` to send your updates to remote storage.

root@controlplane fraud-detection on  main [!?] ➜  dvc status
Data and pipelines are up to date.                                         

root@controlplane fraud-detection on  main [!?] ➜  
```

<img width="1046" height="726" alt="image" src="https://github.com/user-attachments/assets/0971d936-59d5-43dc-b14f-7c55a2fb0b60" />
