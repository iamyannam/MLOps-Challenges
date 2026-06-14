**MLProject**

```
name: trainer

entry_points:
  train:
    parameters:
      n_estimators:
        type: int
        default: 100
      max_depth:
        type: int
        default: 5
      test_size:
        type: float
        default: 0.2
      random_seed:
        type: int
        default: 42
    command: >
      python3 train.py
      --n_estimators {n_estimators}
      --max_depth {max_depth}
      --test_size {test_size}
      --random_seed {random_seed}
```

> Run the commands mlflow run .
```
mlflow run . -e train -P n_estimators=200 -P max_depth=10 --env-manager=local
```
<img width="1757" height="864" alt="image" src="https://github.com/user-attachments/assets/1a6bd3b2-dd83-4e0b-a6c8-31fb8ec1cd7f" />

```
mlflow run . -e train --env-manager=local.
```
<img width="1820" height="976" alt="image" src="https://github.com/user-attachments/assets/f504c93b-d59f-4119-8afd-6031c3a7c6d7" />

<img width="1919" height="687" alt="image" src="https://github.com/user-attachments/assets/b250e83b-ba67-4ed6-ac47-060556b377f7" />
