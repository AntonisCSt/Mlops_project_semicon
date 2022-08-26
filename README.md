## Semiconductor quality prediction and pipeline
#### A MLops Zoomcamp project

## About the project
Manufacturing process feature selection and categorization. The project focuses on MLops best practices.

The projects contains semicoductor sensor data and classifies the end product as Pass or Fail. There are ~580 sensor features that are used. Can we make a classification model that uses the best featuers to make Pass/Fail prediction?

## About the data

* Data Set Characteristics: Multivariate
* Number of Instances: 1567
* Area: Computer
* Attribute Characteristics: Real
* Number of Attributes: 591
* Date Donated: 2008-11-19
* Associated Tasks: Classification, Causal-Discovery
* Missing Values? Yes


## MLops project solution and architecture



## Tasks and dates
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
Add orchestration with Prefect 
* Added Prefect flow in train.py (DONE) (12/08/22)
* Full deploy prefect

Task 4)
Add Monitoring
* Add Monitoring service (DONE) (19/08/22)
* Connect mlflow to monitoring image (DONE) (23/08/22)

Task 4)
AWS model deploy also connect kinesis and lambda function
* Predict using kinesis streams

Task 5)
Best practices --> Create tests,linting and pre-commit hooks
* Add tests:
    Prefect tasks (DONE) (15/08/22)
    Integration tests (DONE) (20/08/22)
* Add pre-commit hooks (Done) (20/08/22)
* Add linting (DONE) (20/08/22)
* Add Makefile (DONE) (22/08/22)
* Add CI/CD (DONE) (22/08/22)

Taks 6)
Final touches
* Make Readme.md nicer
* Write project description
* Write Instructions
* Test Instructions

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


#### 4) Testing flow and other functions

run: pytest

#### 5) Run app and monitoring service

docker compose -f docker-compose.yml up --build
python .\send_data.py


#### 6) Running Makefile

If you are on windows and want to run a Makefile go to: https://chocolatey.org/install and follow the instructions

run this in gitbash:

make build

It will run needed tests and then build image and run the container

after this you can run:

python send_data.py

python ./prefect_monitoring/prefect_monitoring.py

This will create an html file with the report



### How can you contribure:
Currently this project focuses on MLops. It is weak on the actual ML-pipeline.

1) A good idea is to apply L1 regularization in a feature selection step.

2) Try other classification models and grid search.


### Usefull commands:

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

linting and black:

pylint --recursive=y train.py, predict.py, ./prefect_monitoring/prefect_monitoring.py, ./prediction_service/app.py

black --skip-string-normalization  --diff train.py, predict.py, ./prefect_monitoring/prefect_monitoring.py

black --skip-string-normalization train.py, predict.py, ./prefect_monitoring/prefect_monitoring.py, ./prediction_service/app.py


git:

pre-commit


prefect:

prefect orion start

aws ecs:
docker compose --project-name semicontest -f docker-compose.yml up --build