**********************************************
Corrected Makefile -
# fraud-detection Makefile
.PHONY: setup data train test clean all

setup:
	python3 -m venv mlops-venv
	./mlops-venv/bin/pip install -r requirements.txt

data:
	python src/data/process_data.py

train:
	python src/models/train.py

test:
	pytest tests/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache
	rm -rf models/*

all: setup data train test
**********************************************
root@controlplane ~/code ✖ cd fraud-detection/

root@controlplane ~/code/fraud-detection via 🐍 v3.12.3 ✖ make all
python3 -m venv mlops-venv
./mlops-venv/bin/pip install -r requirements.txt
Collecting scikit-learn (from -r requirements.txt (line 1))
  Downloading scikit_learn-1.8.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (11 kB)
Collecting pandas (from -r requirements.txt (line 2))
  Downloading pandas-3.0.3-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (79 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 79.5/79.5 kB 6.6 MB/s eta 0:00:00
Collecting numpy (from -r requirements.txt (line 3))
  Downloading numpy-2.4.5-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (6.6 kB)
Collecting mlflow (from -r requirements.txt (line 4))
  Downloading mlflow-3.12.0-py3-none-any.whl.metadata (49 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 49.2/49.2 kB 26.1 MB/s eta 0:00:00
Collecting scipy>=1.10.0 (from scikit-learn->-r requirements.txt (line 1))
  Downloading scipy-1.17.1-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (62 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.1/62.1 kB 57.6 MB/s eta 0:00:00
Collecting joblib>=1.3.0 (from scikit-learn->-r requirements.txt (line 1))
  Downloading joblib-1.5.3-py3-none-any.whl.metadata (5.5 kB)
Collecting threadpoolctl>=3.2.0 (from scikit-learn->-r requirements.txt (line 1))
  Downloading threadpoolctl-3.6.0-py3-none-any.whl.metadata (13 kB)
Collecting python-dateutil>=2.8.2 (from pandas->-r requirements.txt (line 2))
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting mlflow-skinny==3.12.0 (from mlflow->-r requirements.txt (line 4))
  Downloading mlflow_skinny-3.12.0-py3-none-any.whl.metadata (50 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 50.0/50.0 kB 17.6 MB/s eta 0:00:00
Collecting mlflow-tracing==3.12.0 (from mlflow->-r requirements.txt (line 4))
  Downloading mlflow_tracing-3.12.0-py3-none-any.whl.metadata (19 kB)
Collecting Flask-CORS<7 (from mlflow->-r requirements.txt (line 4))
  Downloading flask_cors-6.0.2-py3-none-any.whl.metadata (5.3 kB)
Collecting Flask<4 (from mlflow->-r requirements.txt (line 4))
  Downloading flask-3.1.3-py3-none-any.whl.metadata (3.2 kB)
Collecting aiohttp<4 (from mlflow->-r requirements.txt (line 4))
  Downloading aiohttp-3.13.5-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (8.1 kB)
Collecting alembic!=1.10.0,<2 (from mlflow->-r requirements.txt (line 4))
  Downloading alembic-1.18.4-py3-none-any.whl.metadata (7.2 kB)
Collecting cryptography<47,>=43.0.0 (from mlflow->-r requirements.txt (line 4))
  Downloading cryptography-46.0.7-cp311-abi3-manylinux_2_34_x86_64.whl.metadata (5.7 kB)
Collecting docker<8,>=4.0.0 (from mlflow->-r requirements.txt (line 4))
  Downloading docker-7.1.0-py3-none-any.whl.metadata (3.8 kB)
Collecting graphene<4 (from mlflow->-r requirements.txt (line 4))
  Downloading graphene-3.4.3-py2.py3-none-any.whl.metadata (6.9 kB)
Collecting gunicorn<26 (from mlflow->-r requirements.txt (line 4))
  Downloading gunicorn-25.3.0-py3-none-any.whl.metadata (5.5 kB)
Collecting huey<3,>=2.5.4 (from mlflow->-r requirements.txt (line 4))
  Downloading huey-2.6.0-py3-none-any.whl.metadata (4.3 kB)
Collecting matplotlib<4 (from mlflow->-r requirements.txt (line 4))
  Downloading matplotlib-3.10.9-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (52 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 52.8/52.8 kB 12.8 MB/s eta 0:00:00
Collecting pandas (from -r requirements.txt (line 2))
  Downloading pandas-2.3.3-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (91 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 91.2/91.2 kB 17.3 MB/s eta 0:00:00
Collecting pyarrow<24,>=4.0.0 (from mlflow->-r requirements.txt (line 4))
  Downloading pyarrow-23.0.1-cp312-cp312-manylinux_2_28_x86_64.whl.metadata (3.1 kB)
Collecting skops<1 (from mlflow->-r requirements.txt (line 4))
  Downloading skops-0.14.0-py3-none-any.whl.metadata (4.4 kB)
Collecting sqlalchemy<3,>=1.4.0 (from mlflow->-r requirements.txt (line 4))
  Downloading sqlalchemy-2.0.49-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (9.5 kB)
Collecting cachetools<8,>=5.0.0 (from mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading cachetools-7.1.2-py3-none-any.whl.metadata (5.5 kB)
Collecting click<9,>=7.0 (from mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading click-8.4.0-py3-none-any.whl.metadata (2.6 kB)
Collecting cloudpickle<4 (from mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading cloudpickle-3.1.2-py3-none-any.whl.metadata (7.1 kB)
Collecting databricks-sdk<1,>=0.20.0 (from mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading databricks_sdk-0.108.0-py3-none-any.whl.metadata (43 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 43.6/43.6 kB 44.0 MB/s eta 0:00:00
Collecting fastapi<1 (from mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading fastapi-0.136.1-py3-none-any.whl.metadata (28 kB)
Collecting gitpython<4,>=3.1.9 (from mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading gitpython-3.1.50-py3-none-any.whl.metadata (14 kB)
Collecting importlib_metadata!=4.7.0,<10,>=3.7.0 (from mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading importlib_metadata-9.0.0-py3-none-any.whl.metadata (4.5 kB)
Collecting opentelemetry-api<3,>=1.9.0 (from mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading opentelemetry_api-1.41.1-py3-none-any.whl.metadata (1.5 kB)
Collecting opentelemetry-proto<3,>=1.9.0 (from mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading opentelemetry_proto-1.41.1-py3-none-any.whl.metadata (2.4 kB)
Collecting opentelemetry-sdk<3,>=1.9.0 (from mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading opentelemetry_sdk-1.41.1-py3-none-any.whl.metadata (1.7 kB)
Collecting packaging<27 (from mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading packaging-26.2-py3-none-any.whl.metadata (3.5 kB)
Collecting protobuf<8,>=3.12.0 (from mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading protobuf-7.34.1-cp310-abi3-manylinux2014_x86_64.whl.metadata (595 bytes)
Collecting pydantic<3,>=2.0.0 (from mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading pydantic-2.13.4-py3-none-any.whl.metadata (109 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 109.4/109.4 kB 23.2 MB/s eta 0:00:00
Collecting python-dotenv<2,>=0.19.0 (from mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading python_dotenv-1.2.2-py3-none-any.whl.metadata (27 kB)
Collecting pyyaml<7,>=5.1 (from mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
Collecting requests<3,>=2.17.3 (from mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
Collecting sqlparse<1,>=0.4.0 (from mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading sqlparse-0.5.5-py3-none-any.whl.metadata (4.7 kB)
Collecting starlette<1 (from mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading starlette-0.52.1-py3-none-any.whl.metadata (6.3 kB)
Collecting typing-extensions<5,>=4.0.0 (from mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Collecting uvicorn<1 (from mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading uvicorn-0.47.0-py3-none-any.whl.metadata (6.7 kB)
Collecting pytz>=2020.1 (from pandas->-r requirements.txt (line 2))
  Downloading pytz-2026.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting tzdata>=2022.7 (from pandas->-r requirements.txt (line 2))
  Downloading tzdata-2026.2-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting aiohappyeyeballs>=2.5.0 (from aiohttp<4->mlflow->-r requirements.txt (line 4))
  Downloading aiohappyeyeballs-2.6.1-py3-none-any.whl.metadata (5.9 kB)
Collecting aiosignal>=1.4.0 (from aiohttp<4->mlflow->-r requirements.txt (line 4))
  Downloading aiosignal-1.4.0-py3-none-any.whl.metadata (3.7 kB)
Collecting attrs>=17.3.0 (from aiohttp<4->mlflow->-r requirements.txt (line 4))
  Downloading attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
Collecting frozenlist>=1.1.1 (from aiohttp<4->mlflow->-r requirements.txt (line 4))
  Downloading frozenlist-1.8.0-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (20 kB)
Collecting multidict<7.0,>=4.5 (from aiohttp<4->mlflow->-r requirements.txt (line 4))
  Downloading multidict-6.7.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (5.3 kB)
Collecting propcache>=0.2.0 (from aiohttp<4->mlflow->-r requirements.txt (line 4))
  Downloading propcache-0.5.2-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (16 kB)
Collecting yarl<2.0,>=1.17.0 (from aiohttp<4->mlflow->-r requirements.txt (line 4))
  Downloading yarl-1.23.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (79 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 79.6/79.6 kB 31.0 MB/s eta 0:00:00
Collecting Mako (from alembic!=1.10.0,<2->mlflow->-r requirements.txt (line 4))
  Downloading mako-1.3.12-py3-none-any.whl.metadata (2.9 kB)
Collecting cffi>=2.0.0 (from cryptography<47,>=43.0.0->mlflow->-r requirements.txt (line 4))
  Downloading cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.6 kB)
Collecting urllib3>=1.26.0 (from docker<8,>=4.0.0->mlflow->-r requirements.txt (line 4))
  Downloading urllib3-2.7.0-py3-none-any.whl.metadata (6.9 kB)
Collecting blinker>=1.9.0 (from Flask<4->mlflow->-r requirements.txt (line 4))
  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting itsdangerous>=2.2.0 (from Flask<4->mlflow->-r requirements.txt (line 4))
  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting jinja2>=3.1.2 (from Flask<4->mlflow->-r requirements.txt (line 4))
  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting markupsafe>=2.1.1 (from Flask<4->mlflow->-r requirements.txt (line 4))
  Downloading markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
Collecting werkzeug>=3.1.0 (from Flask<4->mlflow->-r requirements.txt (line 4))
  Downloading werkzeug-3.1.8-py3-none-any.whl.metadata (4.0 kB)
Collecting graphql-core<3.3,>=3.1 (from graphene<4->mlflow->-r requirements.txt (line 4))
  Downloading graphql_core-3.2.8-py3-none-any.whl.metadata (11 kB)
Collecting graphql-relay<3.3,>=3.1 (from graphene<4->mlflow->-r requirements.txt (line 4))
  Downloading graphql_relay-3.2.0-py3-none-any.whl.metadata (12 kB)
Collecting contourpy>=1.0.1 (from matplotlib<4->mlflow->-r requirements.txt (line 4))
  Downloading contourpy-1.3.3-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (5.5 kB)
Collecting cycler>=0.10 (from matplotlib<4->mlflow->-r requirements.txt (line 4))
  Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
Collecting fonttools>=4.22.0 (from matplotlib<4->mlflow->-r requirements.txt (line 4))
  Downloading fonttools-4.63.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (118 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 118.7/118.7 kB 30.8 MB/s eta 0:00:00
Collecting kiwisolver>=1.3.1 (from matplotlib<4->mlflow->-r requirements.txt (line 4))
  Downloading kiwisolver-1.5.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (5.1 kB)
Collecting pillow>=8 (from matplotlib<4->mlflow->-r requirements.txt (line 4))
  Downloading pillow-12.2.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (8.8 kB)
Collecting pyparsing>=3 (from matplotlib<4->mlflow->-r requirements.txt (line 4))
  Downloading pyparsing-3.3.2-py3-none-any.whl.metadata (5.8 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas->-r requirements.txt (line 2))
  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting prettytable>=3.9 (from skops<1->mlflow->-r requirements.txt (line 4))
  Downloading prettytable-3.17.0-py3-none-any.whl.metadata (34 kB)
Collecting greenlet>=1 (from sqlalchemy<3,>=1.4.0->mlflow->-r requirements.txt (line 4))
  Downloading greenlet-3.5.0-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (3.7 kB)
Collecting pycparser (from cffi>=2.0.0->cryptography<47,>=43.0.0->mlflow->-r requirements.txt (line 4))
  Downloading pycparser-3.0-py3-none-any.whl.metadata (8.2 kB)
Collecting google-auth~=2.0 (from databricks-sdk<1,>=0.20.0->mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading google_auth-2.53.0-py3-none-any.whl.metadata (5.5 kB)
Collecting protobuf<8,>=3.12.0 (from mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading protobuf-6.33.6-cp39-abi3-manylinux2014_x86_64.whl.metadata (593 bytes)
Collecting typing-inspection>=0.4.2 (from fastapi<1->mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
Collecting annotated-doc>=0.0.2 (from fastapi<1->mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading annotated_doc-0.0.4-py3-none-any.whl.metadata (6.6 kB)
Collecting gitdb<5,>=4.0.1 (from gitpython<4,>=3.1.9->mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading gitdb-4.0.12-py3-none-any.whl.metadata (1.2 kB)
Collecting zipp>=3.20 (from importlib_metadata!=4.7.0,<10,>=3.7.0->mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading zipp-3.23.1-py3-none-any.whl.metadata (3.6 kB)
Collecting importlib_metadata!=4.7.0,<10,>=3.7.0 (from mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading importlib_metadata-8.7.1-py3-none-any.whl.metadata (4.7 kB)
Collecting opentelemetry-semantic-conventions==0.62b1 (from opentelemetry-sdk<3,>=1.9.0->mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading opentelemetry_semantic_conventions-0.62b1-py3-none-any.whl.metadata (2.5 kB)
Collecting wcwidth (from prettytable>=3.9->skops<1->mlflow->-r requirements.txt (line 4))
  Downloading wcwidth-0.7.0-py3-none-any.whl.metadata (36 kB)
Collecting annotated-types>=0.6.0 (from pydantic<3,>=2.0.0->mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-core==2.46.4 (from pydantic<3,>=2.0.0->mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading pydantic_core-2.46.4-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.6 kB)
Collecting charset_normalizer<4,>=2 (from requests<3,>=2.17.3->mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading charset_normalizer-3.4.7-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (40 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 40.9/40.9 kB 42.3 MB/s eta 0:00:00
Collecting idna<4,>=2.5 (from requests<3,>=2.17.3->mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading idna-3.15-py3-none-any.whl.metadata (7.7 kB)
Collecting certifi>=2023.5.7 (from requests<3,>=2.17.3->mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading certifi-2026.4.22-py3-none-any.whl.metadata (2.5 kB)
Collecting anyio<5,>=3.6.2 (from starlette<1->mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading anyio-4.13.0-py3-none-any.whl.metadata (4.5 kB)
Collecting h11>=0.8 (from uvicorn<1->mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython<4,>=3.1.9->mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading smmap-5.0.3-py3-none-any.whl.metadata (4.6 kB)
Collecting pyasn1-modules>=0.2.1 (from google-auth~=2.0->databricks-sdk<1,>=0.20.0->mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading pyasn1_modules-0.4.2-py3-none-any.whl.metadata (3.5 kB)
Collecting pyasn1<0.7.0,>=0.6.1 (from pyasn1-modules>=0.2.1->google-auth~=2.0->databricks-sdk<1,>=0.20.0->mlflow-skinny==3.12.0->mlflow->-r requirements.txt (line 4))
  Downloading pyasn1-0.6.3-py3-none-any.whl.metadata (8.4 kB)
Downloading scikit_learn-1.8.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (8.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.9/8.9 MB 38.0 MB/s eta 0:00:00
Downloading numpy-2.4.5-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (16.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.6/16.6 MB 100.1 MB/s eta 0:00:00
Downloading mlflow-3.12.0-py3-none-any.whl (10.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.6/10.6 MB 106.3 MB/s eta 0:00:00
Downloading mlflow_skinny-3.12.0-py3-none-any.whl (3.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 109.7 MB/s eta 0:00:00
Downloading mlflow_tracing-3.12.0-py3-none-any.whl (1.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 110.7 MB/s eta 0:00:00
Downloading pandas-2.3.3-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (12.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.4/12.4 MB 102.4 MB/s eta 0:00:00
Downloading aiohttp-3.13.5-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 110.4 MB/s eta 0:00:00
Downloading alembic-1.18.4-py3-none-any.whl (263 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 263.9/263.9 kB 124.2 MB/s eta 0:00:00
Downloading cryptography-46.0.7-cp311-abi3-manylinux_2_34_x86_64.whl (4.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.5/4.5 MB 99.2 MB/s eta 0:00:00
Downloading docker-7.1.0-py3-none-any.whl (147 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 147.8/147.8 kB 72.6 MB/s eta 0:00:00
Downloading flask-3.1.3-py3-none-any.whl (103 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 103.4/103.4 kB 103.2 MB/s eta 0:00:00
Downloading flask_cors-6.0.2-py3-none-any.whl (13 kB)
Downloading graphene-3.4.3-py2.py3-none-any.whl (114 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 114.9/114.9 kB 116.7 MB/s eta 0:00:00
Downloading gunicorn-25.3.0-py3-none-any.whl (208 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 208.4/208.4 kB 47.2 MB/s eta 0:00:00
Downloading huey-2.6.0-py3-none-any.whl (76 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 77.0/77.0 kB 80.9 MB/s eta 0:00:00
Downloading joblib-1.5.3-py3-none-any.whl (309 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 309.1/309.1 kB 105.5 MB/s eta 0:00:00
Downloading matplotlib-3.10.9-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (8.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.8/8.8 MB 100.3 MB/s eta 0:00:00
Downloading pyarrow-23.0.1-cp312-cp312-manylinux_2_28_x86_64.whl (47.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 47.6/47.6 MB 79.2 MB/s eta 0:00:00
Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 229.9/229.9 kB 159.9 MB/s eta 0:00:00
Downloading pytz-2026.2-py2.py3-none-any.whl (510 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 510.1/510.1 kB 127.7 MB/s eta 0:00:00
Downloading scipy-1.17.1-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (35.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 35.2/35.2 MB 86.1 MB/s eta 0:00:00
Downloading skops-0.14.0-py3-none-any.whl (132 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 132.2/132.2 kB 121.7 MB/s eta 0:00:00
Downloading sqlalchemy-2.0.49-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (3.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.4/3.4 MB 97.1 MB/s eta 0:00:00
Downloading threadpoolctl-3.6.0-py3-none-any.whl (18 kB)
Downloading tzdata-2026.2-py2.py3-none-any.whl (349 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 349.3/349.3 kB 141.8 MB/s eta 0:00:00
Downloading aiohappyeyeballs-2.6.1-py3-none-any.whl (15 kB)
Downloading aiosignal-1.4.0-py3-none-any.whl (7.5 kB)
Downloading attrs-26.1.0-py3-none-any.whl (67 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 67.5/67.5 kB 24.0 MB/s eta 0:00:00
Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
Downloading cachetools-7.1.2-py3-none-any.whl (16 kB)
Downloading cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (219 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 219.6/219.6 kB 150.3 MB/s eta 0:00:00
Downloading click-8.4.0-py3-none-any.whl (116 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 116.1/116.1 kB 108.0 MB/s eta 0:00:00
Downloading cloudpickle-3.1.2-py3-none-any.whl (22 kB)
Downloading contourpy-1.3.3-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (362 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 362.6/362.6 kB 124.6 MB/s eta 0:00:00
Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
Downloading databricks_sdk-0.108.0-py3-none-any.whl (887 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 887.6/887.6 kB 123.3 MB/s eta 0:00:00
Downloading fastapi-0.136.1-py3-none-any.whl (117 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 117.7/117.7 kB 87.8 MB/s eta 0:00:00
Downloading fonttools-4.63.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (5.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.0/5.0 MB 106.4 MB/s eta 0:00:00
Downloading frozenlist-1.8.0-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (242 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 242.4/242.4 kB 169.3 MB/s eta 0:00:00
Downloading gitpython-3.1.50-py3-none-any.whl (212 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 212.5/212.5 kB 19.0 MB/s eta 0:00:00
Downloading graphql_core-3.2.8-py3-none-any.whl (207 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 207.3/207.3 kB 107.5 MB/s eta 0:00:00
Downloading graphql_relay-3.2.0-py3-none-any.whl (16 kB)
Downloading greenlet-3.5.0-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (611 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 611.4/611.4 kB 119.0 MB/s eta 0:00:00
Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 134.9/134.9 kB 101.3 MB/s eta 0:00:00
Downloading kiwisolver-1.5.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (1.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.5/1.5 MB 104.0 MB/s eta 0:00:00
Downloading markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
Downloading multidict-6.7.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (256 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 256.3/256.3 kB 66.1 MB/s eta 0:00:00
Downloading opentelemetry_api-1.41.1-py3-none-any.whl (69 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 69.0/69.0 kB 73.6 MB/s eta 0:00:00
Downloading importlib_metadata-8.7.1-py3-none-any.whl (27 kB)
Downloading opentelemetry_proto-1.41.1-py3-none-any.whl (72 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 72.1/72.1 kB 76.9 MB/s eta 0:00:00
Downloading opentelemetry_sdk-1.41.1-py3-none-any.whl (180 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 180.2/180.2 kB 85.9 MB/s eta 0:00:00
Downloading opentelemetry_semantic_conventions-0.62b1-py3-none-any.whl (231 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 231.6/231.6 kB 85.5 MB/s eta 0:00:00
Downloading packaging-26.2-py3-none-any.whl (100 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100.2/100.2 kB 98.2 MB/s eta 0:00:00
Downloading pillow-12.2.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (7.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.1/7.1 MB 100.2 MB/s eta 0:00:00
Downloading prettytable-3.17.0-py3-none-any.whl (34 kB)
Downloading propcache-0.5.2-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (61 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.6/61.6 kB 64.8 MB/s eta 0:00:00
Downloading protobuf-6.33.6-cp39-abi3-manylinux2014_x86_64.whl (323 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 323.4/323.4 kB 89.9 MB/s eta 0:00:00
Downloading pydantic-2.13.4-py3-none-any.whl (472 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 472.3/472.3 kB 133.3 MB/s eta 0:00:00
Downloading pydantic_core-2.46.4-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 112.5 MB/s eta 0:00:00
Downloading pyparsing-3.3.2-py3-none-any.whl (122 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 122.8/122.8 kB 106.7 MB/s eta 0:00:00
Downloading python_dotenv-1.2.2-py3-none-any.whl (22 kB)
Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (807 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 807.9/807.9 kB 115.9 MB/s eta 0:00:00
Downloading requests-2.34.2-py3-none-any.whl (73 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 73.1/73.1 kB 68.3 MB/s eta 0:00:00
Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Downloading sqlparse-0.5.5-py3-none-any.whl (46 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 46.1/46.1 kB 30.4 MB/s eta 0:00:00
Downloading starlette-0.52.1-py3-none-any.whl (74 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 74.3/74.3 kB 56.3 MB/s eta 0:00:00
Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 44.6/44.6 kB 41.3 MB/s eta 0:00:00
Downloading urllib3-2.7.0-py3-none-any.whl (131 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 131.1/131.1 kB 117.5 MB/s eta 0:00:00
Downloading uvicorn-0.47.0-py3-none-any.whl (71 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 71.3/71.3 kB 69.9 MB/s eta 0:00:00
Downloading werkzeug-3.1.8-py3-none-any.whl (226 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 226.5/226.5 kB 86.4 MB/s eta 0:00:00
Downloading yarl-1.23.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (100 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100.1/100.1 kB 74.0 MB/s eta 0:00:00
Downloading mako-1.3.12-py3-none-any.whl (78 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 78.5/78.5 kB 75.9 MB/s eta 0:00:00
Downloading annotated_doc-0.0.4-py3-none-any.whl (5.3 kB)
Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
Downloading anyio-4.13.0-py3-none-any.whl (114 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 114.4/114.4 kB 81.1 MB/s eta 0:00:00
Downloading certifi-2026.4.22-py3-none-any.whl (135 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 135.7/135.7 kB 110.0 MB/s eta 0:00:00
Downloading charset_normalizer-3.4.7-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (216 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 216.6/216.6 kB 101.2 MB/s eta 0:00:00
Downloading gitdb-4.0.12-py3-none-any.whl (62 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.8/62.8 kB 64.9 MB/s eta 0:00:00
Downloading google_auth-2.53.0-py3-none-any.whl (246 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 246.1/246.1 kB 168.3 MB/s eta 0:00:00
Downloading h11-0.16.0-py3-none-any.whl (37 kB)
Downloading idna-3.15-py3-none-any.whl (72 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 72.3/72.3 kB 67.3 MB/s eta 0:00:00
Downloading typing_inspection-0.4.2-py3-none-any.whl (14 kB)
Downloading zipp-3.23.1-py3-none-any.whl (10 kB)
Downloading pycparser-3.0-py3-none-any.whl (48 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 48.2/48.2 kB 54.0 MB/s eta 0:00:00
Downloading wcwidth-0.7.0-py3-none-any.whl (110 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 110.8/110.8 kB 105.4 MB/s eta 0:00:00
Downloading pyasn1_modules-0.4.2-py3-none-any.whl (181 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 181.3/181.3 kB 156.6 MB/s eta 0:00:00
Downloading smmap-5.0.3-py3-none-any.whl (24 kB)
Downloading pyasn1-0.6.3-py3-none-any.whl (83 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 84.0/84.0 kB 76.4 MB/s eta 0:00:00
Installing collected packages: pytz, huey, zipp, wcwidth, urllib3, tzdata, typing-extensions, threadpoolctl, sqlparse, smmap, six, pyyaml, python-dotenv, pyparsing, pycparser, pyasn1, pyarrow, protobuf, propcache, pillow, packaging, numpy, multidict, markupsafe, kiwisolver, joblib, itsdangerous, idna, h11, greenlet, graphql-core, frozenlist, fonttools, cycler, cloudpickle, click, charset_normalizer, certifi, cachetools, blinker, attrs, annotated-types, annotated-doc, aiohappyeyeballs, yarl, werkzeug, uvicorn, typing-inspection, sqlalchemy, scipy, requests, python-dateutil, pydantic-core, pyasn1-modules, prettytable, opentelemetry-proto, Mako, jinja2, importlib_metadata, gunicorn, graphql-relay, gitdb, contourpy, cffi, anyio, aiosignal, starlette, scikit-learn, pydantic, pandas, opentelemetry-api, matplotlib, graphene, gitpython, Flask, docker, cryptography, alembic, aiohttp, skops, opentelemetry-semantic-conventions, google-auth, Flask-CORS, fastapi, opentelemetry-sdk, databricks-sdk, mlflow-tracing, mlflow-skinny, mlflow
Successfully installed Flask-3.1.3 Flask-CORS-6.0.2 Mako-1.3.12 aiohappyeyeballs-2.6.1 aiohttp-3.13.5 aiosignal-1.4.0 alembic-1.18.4 annotated-doc-0.0.4 annotated-types-0.7.0 anyio-4.13.0 attrs-26.1.0 blinker-1.9.0 cachetools-7.1.2 certifi-2026.4.22 cffi-2.0.0 charset_normalizer-3.4.7 click-8.4.0 cloudpickle-3.1.2 contourpy-1.3.3 cryptography-46.0.7 cycler-0.12.1 databricks-sdk-0.108.0 docker-7.1.0 fastapi-0.136.1 fonttools-4.63.0 frozenlist-1.8.0 gitdb-4.0.12 gitpython-3.1.50 google-auth-2.53.0 graphene-3.4.3 graphql-core-3.2.8 graphql-relay-3.2.0 greenlet-3.5.0 gunicorn-25.3.0 h11-0.16.0 huey-2.6.0 idna-3.15 importlib_metadata-8.7.1 itsdangerous-2.2.0 jinja2-3.1.6 joblib-1.5.3 kiwisolver-1.5.0 markupsafe-3.0.3 matplotlib-3.10.9 mlflow-3.12.0 mlflow-skinny-3.12.0 mlflow-tracing-3.12.0 multidict-6.7.1 numpy-2.4.5 opentelemetry-api-1.41.1 opentelemetry-proto-1.41.1 opentelemetry-sdk-1.41.1 opentelemetry-semantic-conventions-0.62b1 packaging-26.2 pandas-2.3.3 pillow-12.2.0 prettytable-3.17.0 propcache-0.5.2 protobuf-6.33.6 pyarrow-23.0.1 pyasn1-0.6.3 pyasn1-modules-0.4.2 pycparser-3.0 pydantic-2.13.4 pydantic-core-2.46.4 pyparsing-3.3.2 python-dateutil-2.9.0.post0 python-dotenv-1.2.2 pytz-2026.2 pyyaml-6.0.3 requests-2.34.2 scikit-learn-1.8.0 scipy-1.17.1 six-1.17.0 skops-0.14.0 smmap-5.0.3 sqlalchemy-2.0.49 sqlparse-0.5.5 starlette-0.52.1 threadpoolctl-3.6.0 typing-extensions-4.15.0 typing-inspection-0.4.2 tzdata-2026.2 urllib3-2.7.0 uvicorn-0.47.0 wcwidth-0.7.0 werkzeug-3.1.8 yarl-1.23.0 zipp-3.23.1
python src/data/process_data.py
python src/models/train.py
pytest tests/
========================= test session starts =========================
platform linux -- Python 3.12.3, pytest-9.0.3, pluggy-1.6.0
rootdir: /root/code/fraud-detection
plugins: hydra-core-1.3.2, typeguard-4.5.1, Faker-40.15.0, testinfra-10.2.2, anyio-4.13.0
collected 1 item                                                      

tests/test_smoke.py .                                           [100%]

========================== 1 passed in 0.05s ==========================

root@controlplane ~/code/fraud-detection via 🐍 v3.12.3 ➜  
