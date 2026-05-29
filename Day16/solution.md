Configure dvc.yaml file as below
```
stages:
  process_data:
    cmd: python src/data/process_data.py
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

  train:
    cmd: python src/models/train.py
    deps:
      - data/processed/train.csv
      - src/models/train.py
    outs:
      - models/model.pkl
    metrics:
      - metrics.json:
          cache: false

```
run ```dvc repro``` && ```dvc metrics show```

<img width="1015" height="724" alt="image" src="https://github.com/user-attachments/assets/eefb76e8-03af-4025-a8ef-c75dafcef076" />
