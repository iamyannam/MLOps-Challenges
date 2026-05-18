I have done chnages in the toml file as below.
<img width="1863" height="884" alt="image" src="https://github.com/user-attachments/assets/77fb8a66-e956-4a60-9728-77c306accd95" />

After this I got an error saying
root@controlplane ~/code ➜  cd fraud-detection/

root@controlplane ~/code/fraud-detection via 🐍 v3.12.3 ➜  ruff check src/
I001 [*] Import block is un-sorted or un-formatted
 --> src/data/process_data.py:1:1
  |
1 | / import os
2 | | import pandas as pd
  | |___________________^
  |
help: Organize imports

F401 [*] `os` imported but unused
 --> src/data/process_data.py:1:8
  |
1 | import os
  |        ^^
2 | import pandas as pd
  |
help: Remove unused import: `os`

Found 2 errors.
[*] 2 fixable with the `--fix` option.

root@controlplane ~/code/fraud-detection via 🐍 v3.12.3 ✖ ruff check src/
All checks passed!

root@controlplane ~/code/fraud-detection via 🐍 v3.12.3 ➜  black --check src/
All done! ✨ 🍰 ✨
5 files would be left unchanged.
<img width="1029" height="827" alt="image" src="https://github.com/user-attachments/assets/77827fd7-d524-4b33-a0da-e55d2b765e4c" />



root@controlplane ~/code/fraud-detection via 🐍 v3.12.3 ➜  
