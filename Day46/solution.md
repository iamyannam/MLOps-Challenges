### The Problem
An AI model learns from data. If you feed it corrupted, messy, or missing data, the AI will break, crash, or make terrible decisions. Right now, if bad data gets in, the team doesn't find out until three hours later when the system crashes in production. That wastes time and money.

### The Solution: A "Data Contract"
The team is setting up an automated checkpoint upstream (before the data ever reaches the AI). They are creating a strict Data Contract—a set of rules that the incoming data must follow to be allowed through.
#### Rules : We are using a tool called Great Expectations to write four specific rules for the data

---

#### author_expectations.py

```
# ------------------------------------------------------------------
    # Encode the platform's data contract as four expectations.
    # ------------------------------------------------------------------

    # TODO 1: Schema -- exactly these columns must exist in the batch.
    suite.add_expectation(
        ge.ExpectTableColumnsToMatchSet(
            column_set=["amount", "hour", "num_tx_past_day", "is_fraud"]
        )
    )

    # TODO 2: `amount` is a transaction amount and is never negative.
    suite.add_expectation(
        ge.ExpectColumnValuesToBeBetween(
            column="amount", 
            min_value=0
        )
    )

    # TODO 3: `hour` is the hour-of-day the transaction occurred (0-23).
    suite.add_expectation(
        ge.ExpectColumnValuesToBeBetween(
            column="hour", 
            min_value=0, 
            max_value=23
        )
    )

    # TODO 4: `is_fraud` is a binary label (0 or 1).
    suite.add_expectation(
        ge.ExpectColumnValuesToBeInSet(
            column="is_fraud", 
            value_set=[0, 1]
        )
    )
```

---

Once, the execution comppletes verify the following

<img width="1761" height="900" alt="image" src="https://github.com/user-attachments/assets/0ea29717-896e-4755-8616-7c7cff2ebf7f" />

<img width="1892" height="737" alt="image" src="https://github.com/user-attachments/assets/a82f65d2-a8cf-463e-81ba-aab0b21056ee" />

#### fraud_schema.json

```
{
  "expectations": [
    {
      "id": "8def8ea8-6e76-419a-bf41-95f9982b43df",
      "kwargs": {
        "column_set": [
          "amount",
          "hour",
          "num_tx_past_day",
          "is_fraud"
        ]
      },
      "meta": {},
      "severity": "critical",
      "type": "expect_table_columns_to_match_set"
    },
    {
      "id": "39c281d9-a4f0-428b-83a8-2dc330bc9121",
      "kwargs": {
        "column": "amount",
        "min_value": 0.0
      },
      "meta": {},
      "severity": "critical",
      "type": "expect_column_values_to_be_between"
    },
    {
      "id": "8685daab-9d57-4a58-be2e-5e180bc0272e",
      "kwargs": {
        "column": "hour",
        "max_value": 23.0,
        "min_value": 0.0
      },
      "meta": {},
      "severity": "critical",
      "type": "expect_column_values_to_be_between"
    },
    {
      "id": "cdd40ad4-befd-4d4f-8cbc-8e8def58ed90",
      "kwargs": {
        "column": "is_fraud",
        "value_set": [
          0,
          1
        ]
      },
      "meta": {},
      "severity": "critical",
      "type": "expect_column_values_to_be_in_set"
    }
  ],
  "id": "b4111bb2-8594-463c-bb5c-c2a77875f0e2",
  "meta": {
    "great_expectations_version": "1.18.2"
  },
  "name": "fraud_schema",
  "notes": null
}
```

