As see in the error in Datadocs, the amount values are in negative from inputs and in the script the minimum amount value expected is 0, 
Change the amount expectation's min_value from 0 to -5000 (or remove it entirely):

#### fix_drift.py

```
    suite.add_expectation(
        ge.ExpectColumnValuesToBeBetween(column="amount", min_value=-5000)
    )
```

<img width="1764" height="948" alt="image" src="https://github.com/user-attachments/assets/89bf62a8-7ac2-44cd-8ef7-babe235e5d88" />

<img width="1914" height="846" alt="image" src="https://github.com/user-attachments/assets/f05a0878-edde-4eab-90fc-cb21ba6c81b7" />

<img width="1871" height="913" alt="image" src="https://github.com/user-attachments/assets/243adf4d-8191-4062-8c20-8d20e5d8361d" />


