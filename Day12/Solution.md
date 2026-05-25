1.  DVC Config file changes -

```
['remote "s3"']
    url = s3://dvc-storage
    endpointurl = http://localhost:8333
    access_key_id = weedadmin
    secret_access_key = weedadmin123

[core]
    remote = s3
```
2.  Push the config changes
```
root@controlplane ~/code ✖ cd fraud-detection/

root@controlplane fraud-detection on  main [!] ✖ dvc push
Collecting                                   |1.00 [00:00,  790entry/s]
Pushing
1 file pushed                                                          
                                                                       
root@controlplane fraud-detection on  main [!] ➜
```

3. Verify by cliking Seaweed FS Filter

<img width="1864" height="412" alt="image" src="https://github.com/user-attachments/assets/56654648-2889-45aa-8492-6f3f26895852" />
