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
    * Write the Pipeline
    * Deploy model
    * Use and Test model

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
mlflow.create_experiment("semicon-sensor-clf","s3://mlflow-semicon-clf/")

```
(or use a local file)
### 3)
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