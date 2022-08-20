#This script tests the docker-compose.yml
import requests
import json
import datetime
from pyarrow import csv
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27018')

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)

def test_prediction_service():
    table = csv.read_csv(".\evidently_service\datasets\sample_test_data.csv")
    data = table.to_pylist()
    row = data[0]

    resp = requests.post("http://127.0.0.1:9696/predict",
                                headers={"Content-Type": "application/json"},
                                data=json.dumps(row, cls=DateTimeEncoder)).json()
    assert type(resp['Pass/Fail']) == int

def test_mongo_db():
    db = client.get_database("prediction_service")
    type(db) == pymongo.database.Database



if __name__ == "__main__":
    test_prediction_service()
    test_mongo_db()