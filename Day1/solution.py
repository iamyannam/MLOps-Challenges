root@controlplane ~/code ➜  pwd
/root/code

root@controlplane ~/code ➜  python3 -m venv
usage: venv [-h] [--system-site-packages] [--symlinks | --copies]
            [--clear] [--upgrade] [--without-pip] [--prompt PROMPT]
            [--upgrade-deps]
            ENV_DIR [ENV_DIR ...]
venv: error: the following arguments are required: ENV_DIR

root@controlplane ~/code ➜  python3 -m venv /root/code/ml-env

root@controlplane ~/code ➜  source ml-env/bin/activate

root@controlplane ~/code via 🐍 v3.12.3 (ml-env) ➜  pip install numpy pandas scikit-learn matplotlib
Collecting numpy
  Downloading numpy-2.4.4-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (6.6 kB)
Collecting pandas
  Downloading pandas-3.0.3-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (79 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 79.5/79.5 kB 3.8 MB/s eta 0:00:00
Collecting scikit-learn
  Downloading scikit_learn-1.8.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (11 kB)
Collecting matplotlib
  Downloading matplotlib-3.10.9-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (52 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 52.8/52.8 kB 7.5 MB/s eta 0:00:00
Collecting python-dateutil>=2.8.2 (from pandas)
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting scipy>=1.10.0 (from scikit-learn)
  Downloading scipy-1.17.1-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (62 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.1/62.1 kB 8.1 MB/s eta 0:00:00
Collecting joblib>=1.3.0 (from scikit-learn)
  Downloading joblib-1.5.3-py3-none-any.whl.metadata (5.5 kB)
Collecting threadpoolctl>=3.2.0 (from scikit-learn)
  Downloading threadpoolctl-3.6.0-py3-none-any.whl.metadata (13 kB)
Collecting contourpy>=1.0.1 (from matplotlib)
  Downloading contourpy-1.3.3-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (5.5 kB)
Collecting cycler>=0.10 (from matplotlib)
  Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
Collecting fonttools>=4.22.0 (from matplotlib)
  Downloading fonttools-4.62.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (117 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 117.5/117.5 kB 6.4 MB/s eta 0:00:00
Collecting kiwisolver>=1.3.1 (from matplotlib)
  Downloading kiwisolver-1.5.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (5.1 kB)
Collecting packaging>=20.0 (from matplotlib)
  Downloading packaging-26.2-py3-none-any.whl.metadata (3.5 kB)
Collecting pillow>=8 (from matplotlib)
  Downloading pillow-12.2.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (8.8 kB)
Collecting pyparsing>=3 (from matplotlib)
  Downloading pyparsing-3.3.2-py3-none-any.whl.metadata (5.8 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas)
  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Downloading numpy-2.4.4-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (16.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.6/16.6 MB 48.4 MB/s eta 0:00:00
Downloading pandas-3.0.3-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (10.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.9/10.9 MB 72.8 MB/s eta 0:00:00
Downloading scikit_learn-1.8.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (8.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.9/8.9 MB 107.7 MB/s eta 0:00:00
Downloading matplotlib-3.10.9-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (8.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.8/8.8 MB 101.9 MB/s eta 0:00:00
Downloading contourpy-1.3.3-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (362 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 362.6/362.6 kB 77.7 MB/s eta 0:00:00
Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
Downloading fonttools-4.62.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (5.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.0/5.0 MB 101.2 MB/s eta 0:00:00
Downloading joblib-1.5.3-py3-none-any.whl (309 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 309.1/309.1 kB 130.9 MB/s eta 0:00:00
Downloading kiwisolver-1.5.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (1.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.5/1.5 MB 73.8 MB/s eta 0:00:00
Downloading packaging-26.2-py3-none-any.whl (100 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100.2/100.2 kB 77.0 MB/s eta 0:00:00
Downloading pillow-12.2.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (7.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.1/7.1 MB 96.8 MB/s eta 0:00:00
Downloading pyparsing-3.3.2-py3-none-any.whl (122 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 122.8/122.8 kB 99.8 MB/s eta 0:00:00
Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 229.9/229.9 kB 155.2 MB/s eta 0:00:00
Downloading scipy-1.17.1-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (35.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 35.2/35.2 MB 86.8 MB/s eta 0:00:00
Downloading threadpoolctl-3.6.0-py3-none-any.whl (18 kB)
Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: threadpoolctl, six, pyparsing, pillow, packaging, numpy, kiwisolver, joblib, fonttools, cycler, scipy, python-dateutil, contourpy, scikit-learn, pandas, matplotlib
Successfully installed contourpy-1.3.3 cycler-0.12.1 fonttools-4.62.1 joblib-1.5.3 kiwisolver-1.5.0 matplotlib-3.10.9 numpy-2.4.4 packaging-26.2 pandas-3.0.3 pillow-12.2.0 pyparsing-3.3.2 python-dateutil-2.9.0.post0 scikit-learn-1.8.0 scipy-1.17.1 six-1.17.0 threadpoolctl-3.6.0

root@controlplane ~/code via 🐍 v3.12.3 (ml-env) ➜  pip list
Package         Version
--------------- -----------
contourpy       1.3.3
cycler          0.12.1
fonttools       4.62.1
joblib          1.5.3
kiwisolver      1.5.0
matplotlib      3.10.9
numpy           2.4.4
packaging       26.2
pandas          3.0.3
pillow          12.2.0
pip             24.0
pyparsing       3.3.2
python-dateutil 2.9.0.post0
scikit-learn    1.8.0
scipy           1.17.1
six             1.17.0
threadpoolctl   3.6.0

root@controlplane ~/code via 🐍 v3.12.3 (ml-env) ➜  pip freeze > requirements.txt

root@controlplane ~/code via 🐍 v3.12.3 (ml-env) ➜  cat requirements.txt 
contourpy==1.3.3
cycler==0.12.1
fonttools==4.62.1
joblib==1.5.3
kiwisolver==1.5.0
matplotlib==3.10.9
numpy==2.4.4
packaging==26.2
pandas==3.0.3
pillow==12.2.0
pyparsing==3.3.2
python-dateutil==2.9.0.post0
scikit-learn==1.8.0
scipy==1.17.1
six==1.17.0
threadpoolctl==3.6.0

root@controlplane ~/code via 🐍 v3.12.3 (ml-env) ➜  
