FROM python:3.9.7-slim

RUN pip install -U pip
RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile","Pipfile.lock","./"]

RUN pipenv install --system --deploy
RUN pipenv install uvicorn

COPY ["predict.py","./"]

EXPOSE 8001

ENTRYPOINT [".\predict.py"]