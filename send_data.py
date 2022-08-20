import json
import uuid
from datetime import datetime
from time import sleep

from pyarrow import csv
import requests

table = csv.read_csv(".\evidently_service\datasets\sample_test_data.csv")
data = table.to_pylist()


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)


with open("target.csv", 'w') as f_target:
    for row in data:
        #print(max(0,int(row['Pass/Fail'])))
        row['id'] = str(uuid.uuid4())
        duration = row['Pass/Fail']
        data=json.dumps(row, cls=DateTimeEncoder)
        #duration = str(duration)
        f_target.write(f"{row['id']},{duration}\n")
        resp = requests.post("http://127.0.0.1:9696/predict",
                             headers={"Content-Type": "application/json"},
                             data=json.dumps(row, cls=DateTimeEncoder)).json()
        sleep(1)
        break