
test:
	pytest tests/

quality_checks:
	isort .
	black --skip-string-normalization .

build: quality_checks test integration_test
	docker compose -f docker-compose.yml up --build	

integration_test:
	bash build_test_shut.sh

setup:
	pipenv install --dev
	pre-commit install