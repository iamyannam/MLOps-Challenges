#### data_quality.yml

```
name: Data Quality

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

jobs:
  data-quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Great Expectations
        run: |
          pip install --break-system-packages \
            great_expectations pandas numpy

      # TODO: add the data-quality GATE step here. Run the drift_check
      #       checkpoint with:  python3 -m src.gx_run
      #   `src/gx_run.py` exits non-zero when the checkpoint fails, so as
      #   an ordinary step its failure fails the job and BLOCKS the merge —
      #   that is the gate. Do NOT add `continue-on-error:` to the step and
      #   do NOT append `|| true` / `; true` to the command: either one lets
      #   a failing checkpoint pass, so bad data would merge anyway.

      - name: Run Data Qulaity Data Check
        run: python3 -m src.gx_run
```

#### Merge the changes

```
git add .
git commit -m "Check Qulaity GATE"
git push origin enforce-data-quality-gate
```

##### Check Gitea UI and see Action for quality gate check passed or not

<img width="1851" height="762" alt="image" src="https://github.com/user-attachments/assets/31103111-ea54-4634-9601-82434b930da0" />
