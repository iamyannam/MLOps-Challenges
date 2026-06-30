## Feast

Feast is an open-source data infrastructure tool that operationalizes feature management by providing a unified metadata registry and dual-storage architecture (offline lakes for point-in-time historical training, online key-value stores for low-latency inference). It acts as a decoupled abstraction layer that standardizes feature definitions across Python/SQL to eliminate training-serving skew and promote cross-team feature reuse.

> Model needs features like clean, processed data. Feast serves these features through a unified architecture, delivering historical data for model training and low-latency data for real-time inference.


#### To Initialise the Feast Project

```
feast init feature-repo
```

#### To apply Feast

```
cd feature_repo/feature_repo
feast apply
```

#### Launch the Feast UI

```
feast ui &
```

<img width="1020" height="874" alt="image" src="https://github.com/user-attachments/assets/d7694236-2eb1-40b0-9f2d-23460c0d30ea" />

#### Feast UI


<img width="1858" height="951" alt="image" src="https://github.com/user-attachments/assets/0cf2351f-9359-4700-a094-6e5ef8fc7a55" />

