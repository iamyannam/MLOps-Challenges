### Feast - 
Feast is a Feature Store. It doesn't actually compute your data; it's the organizer, warehouse manager, and lightning-fast delivery driver 
that sits between your raw data and your AI models.

#### Feature Views
A blueprint or schema definition that tells Feast exactly what your features are, where they live, 
and how they should be mapped for both training and real-time inference.

#### features.py

```
"""Feature definitions for the fraud-detection project.

Declares the `customer` entity, the `transactions` batch source, and
one feature view (`customer_transaction_features`) that exposes the
customer's `amount`, `hour`, and `num_tx_past_day` features to the
feature store.

Every non-end-state concern is correctly wired — imports, source
pointer, feature-view name, entity-to-view binding, TTL. Adjust
the entity `join_keys` so it maps onto the column Feast actually
needs to look up in the source, and adjust the `amount` feature's
declared `dtype` so it matches the type written by the generator.
"""
from datetime import timedelta

from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float32, Int64, String 

transactions_source = FileSource(
    path="data/transactions.parquet",
    timestamp_field="event_timestamp",
)

customer = Entity(
    name="customer",
    join_keys=["customer_id"],  # Maps onto the physical column 'customer_id' in your source
    description="Customer identifier keyed by the transactions source.",
)

customer_transaction_features = FeatureView(
    name="customer_transaction_features",
    entities=[customer],  
    ttl=timedelta(days=365),
    schema=[
        Field(name="amount", dtype=Float32),  
        Field(name="hour", dtype=Int64),
        Field(name="num_tx_past_day", dtype=Int64),
    ],
    source=transactions_source,
    online=True,
)
```

<img width="1874" height="800" alt="image" src="https://github.com/user-attachments/assets/2a55a848-ab9b-469b-bf3f-e7654c4802d4" />


<img width="1899" height="819" alt="image" src="https://github.com/user-attachments/assets/b79bd2db-9da7-4d4e-99f6-4d5eeb03e6d8" />



<img width="1291" height="879" alt="image" src="https://github.com/user-attachments/assets/89e485a8-b293-48ae-9ce1-ed7cfd8e8587" />




