```
cd /root/code/fraud-detection

# Stop Git tracking the dataset but keep the file on disk
git rm --cached data/raw/transactions.csv

# Track the dataset with DVC
dvc add data/raw/transactions.csv

# Stage the DVC pointer file and updated gitignore
git add data/raw/transactions.csv.dvc data/raw/.gitignore

# Record the commit
git commit -m "Track transactions dataset with DVC"
```

```
root@controlplane ~/code ✖ cd fraud-detection/

root@controlplane fraud-detection on  main ➜  ls -ltr
total 8
drwxr-xr-x 3 root root 4096 May 23 04:13 data
-rw-r--r-- 1 root root   18 May 23 04:13 README.md

root@controlplane fraud-detection on  main ➜  git rm --cached data/raw/transactions.csv
rm 'data/raw/transactions.csv'

root@controlplane fraud-detection on  main [✘?] ➜  dvc add data/raw/transactions.csv
100% Adding...|███████████████████████████████|1/1 [00:00, 53.73file/s]
                                                                       
To track the changes with git, run:

        git add data/raw/.gitignore data/raw/transactions.csv.dvc

To enable auto staging, run:

        dvc config core.autostage true

root@controlplane fraud-detection on  main [✘?] ➜  git add data/raw/.gitignore data/raw/transactions.csv.dvc

root@controlplane fraud-detection on  main [✘+] ➜  git commit -m "Track transactions dataset with DVC"
[main 9fbfdfe] Track transactions dataset with DVC
 3 files changed, 6 insertions(+), 11 deletions(-)
 create mode 100644 data/raw/.gitignore
 delete mode 100644 data/raw/transactions.csv
 create mode 100644 data/raw/transactions.csv.dvc

root@controlplane fraud-detection on  main ➜
```
<img width="1057" height="836" alt="image" src="https://github.com/user-attachments/assets/7d074d83-28cf-4639-b2c6-8eae558b129b" />
