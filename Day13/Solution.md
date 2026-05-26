1.  Fixed the DVC Config file by adding access key and secret access key
    ```
    [core]
      remote = s3

    ['remote "s3"']
      url = s3://dvc-storage
      endpointurl = http://localhost:8333
      access_key_id = weedadmin
      secret_access_key = weedadmin123`
    
    ```

2.  Change directory and run the ```dvc pull``` command
    ```   
    root@controlplane ~/code ✖ cd fraud-detection/

    root@controlplane fraud-detection on  main [!] ➜  dvc pull
    Collecting                                   |1.00 [00:00,  735entry/s]
    Fetching
    Building workspace index                     |2.00 [00:00,  723entry/s]
    Comparing indexes                           |4.00 [00:00, 2.23kentry/s]
    Applying changes                             |1.00 [00:00, 1.26kfile/s]
    A       data/raw/transactions.csv
    1 file fetched and 1 file added

    root@controlplane fraud-detection on  main [!] ➜  
    ```

<img width="1781" height="909" alt="image" src="https://github.com/user-attachments/assets/500af7ff-0cb1-4012-a944-225722935fae" />
