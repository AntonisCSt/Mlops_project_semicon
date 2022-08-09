# In this script we use the transformed input data and the model to make predicictions.

import os
import pickle
from fastapi import FastAPI
from loguru import logger
import mlflow

RUN_ID = os.getenv('RUN_ID','18bfcb19c9c8499cbe630f3323649351')

logged_model = f's3://mlflow-semicon-clf/{RUN_ID}/artifacts/artifacts/'
# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

def prepare_features():
    features = 1
    return features


def predict(features):
    preds = 1
    return preds


app = FastAPI()

@app.post("/predict")
async def predict(row:dict):
    features = prepare_features()
    pred = predict(features)
    return {'prediction': 1, 'model_version': RUN_ID }

if __name__ == "__main__":
    # Use this for debugging perpuses

    logger.debug("Running in developement mode. Do not run like this in production")
    import uvicorn
    uvicorn.run(app, host="localhost",port=8001,log_level="debug")