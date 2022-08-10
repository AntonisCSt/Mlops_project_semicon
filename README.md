## Semiconductor quality prediction and pipeline
#### A MLops Zoom camp project

Task 1)
Add experiment tracking and set-up registery server (local) artifacts in s3 with MLflow
    * Experiment tracking (DONE)
    * Model registery (DONE)
    * Connect to S3 (DONE)

Task 2)
Convert notebook into a pipeline
    * Define pipeline (DONE)
    * write individual scirpts of pipeline (DONE)
    * create a scikit learn pipeline to have preprocess and model together (DONE)
    * finish predict (DONE)
    * Use and Test model (DONE)

Task 3)
Create tests,linting and pre-commit hooks

Task 5)
Add orchestration with Prefect

Task 4)
Connect with cloud. Upload model to the cloud.

Task 6)
To be continued



## Instructions

#### 1) Install enviroment
use:
```
$pipenv install
```

#### 2) Create a S3 bucket for mlflow

in train.py and main_notebook.ipynb
```python
mlflow.create_experiment("semicon-sensor-clf","[your S3 bucket]")

```
(or use a local file)

#### 2.1) (Optional) Train model and upload


#### 3) Run prediction locally using FastAPI and uvicorn server (dev)

run: predict.py

go to : http://localhost:8001/docs

press :"try it out"

use example: from test_one_input.txt (it should give output as "0")

#### How can you contribure:
Currently this project focuses on MLops. It is weak on the actual ML-pipeline.

1) A good idea is to apply L1 regularization in a feature selection step.

2) Try other classification models and grid search.


Usefull commands:

pipenv:

$pipenv install
$pipenv install --dev [library]
$pipenv --venv

mlflow: 

mlflow server --backend-store-uri=sqlite:///mlflow.db --default-artifact-root=s3://mlflow-semicon-clf/

use:

mlflow.set_tracking_uri("sqlite:///mlflow.db")
#mlflow.set_experiment("testing-mlflow")
mlflow.create_experiment("semicon-sensor-clf","s3://mlflow-semicon-clf/")
mlflow.set_experiment("semicon-sensor-clf")