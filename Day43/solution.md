### Features

##### Offline Store (transactions.parquet): This is where our massive historical logs live. It is used to train ML models because it can handle bulk queries efficiently.

##### Online Store (online_store.db): Real-time web or mobile apps can't wait for a heavy Parquet file to scan. Instead, data is loaded into a fast-access database (like SQLite or Redis) so model can fetch a user's profile instantly.

##### Materialization: This is the process of copying data from the slow Offline Store into the fast Online Store.


> To check online_store.db ---> use sqlite3 data/onlinse_store.db ---> .tables

> if sqlite3 command not found, install it via package manager ---> apt-get install sqlite3 -y

<img width="1047" height="871" alt="image" src="https://github.com/user-attachments/assets/6434844d-39de-4dbb-a54b-9e685485817f" />

<img width="1902" height="793" alt="image" src="https://github.com/user-attachments/assets/7604cf9b-25a3-4c57-8f96-5e0ab5ab4312" />

