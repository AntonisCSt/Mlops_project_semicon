LOCAL_TAG:=$(shell date +"%Y-%m-%d-%H-%M")
LOCAL_IMAGE_NAME:=stream-model-duration:${LOCAL_TAG}

test:
	pytest tests/

quality_checks:
	isort train.py, predict.py, ./prefect_monitoring/prefect_monitoring.py, ./prediction_service/app.py
	black --skip-string-normalization train.py, predict.py, ./prefect_monitoring/prefect_monitoring.py, ./prediction_service/app.py
	pylint --recursive=y train.py, predict.py, ./prefect_monitoring/prefect_monitoring.py, ./prediction_service/app.py

build: quality_checks test
	docker build -t ${LOCAL_IMAGE_NAME} .

integration_test: build
	LOCAL_IMAGE_NAME=${LOCAL_IMAGE_NAME} bash integraton-test/run.sh

publish: build integration_test
	LOCAL_IMAGE_NAME=${LOCAL_IMAGE_NAME} bash scripts/publish.sh

setup:
	pipenv install --dev
	pre-commit install