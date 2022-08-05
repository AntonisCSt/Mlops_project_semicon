## Semiconductor quality prediction and pipeline
#### A MLops Zoom camp project

Task 1)
Add experiment tracking and set-up registery server (local) artifacts in s3 with MLflow
    * Experiment tracking (DONE)
    * Model registery ()

Task 2)
Convert notebook into a pipeline

Task 3)
Create tests,linting and pre-commit hooks

Task 5)
Add orchestration with Prefect

Task 4)
Connect with cloud. Upload model to the cloud.

Task 6)
To be continued




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