The xFusionCorp Industries ML team uses DVC pipelines to keep data processing reproducible. A draft dvc.yaml exists in the fraud-detection project, but dvc repro does not complete the full pipeline. Correct the pipeline definition so it runs cleanly end to end.


1.  A project exists at /root/code/fraud-detection/ with DVC initialised. Python scripts are at src/data/process_data.py and src/data/split_data.py; raw input is at data/raw/transactions.csv. Do not modify the Python files or the input data.

2.  The corrected pipeline must declare two stages with the following behaviour:
    -  process_data – Depends on data/raw/transactions.csv and src/data/process_data.py; produces data/processed/clean_transactions.csv.
    -  split_data – Depends on data/processed/clean_transactions.csv and src/data/split_data.py; produces data/processed/train.csv and data/processed/test.csv.
3.  Review the existing dvc.yaml and correct everything that prevents dvc repro from completing.

4.  After your changes, dvc repro must run end to end and dvc status must report no stale stages.

_Once the pipeline is valid, the DVC extension's PIPELINES section under the DVC view will list both stages and visualise the dependency graph between them._

<img width="1759" height="837" alt="image" src="https://github.com/user-attachments/assets/472cacee-edf1-44ad-a05e-8abf6c4c1e10" />

<img width="995" height="423" alt="image" src="https://github.com/user-attachments/assets/efadefce-7e9f-4da6-8ee5-ebfd44fe09dc" />

split_data.py
```
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/processed/clean_transactions.csv")
train, test = train_test_split(df, test_size=0.2, random_state=42)
train.to_csv("data/processed/train.csv", index=False)
test.to_csv("data/processed/test.csv", index=False)
print(f"Train: {len(train)} rows, Test: {len(test)} rows")
```
<img width="1026" height="657" alt="image" src="https://github.com/user-attachments/assets/f09bb91e-7571-4e4a-9cf7-2994c3971a4c" />

