import pytest
from constants import Constants
import requests
import json
from data import Data
@pytest.fixture
def reg():
    payload = {
        "email": Constants.EMAIL,
        "password": Constants.PASSWORD,
        "name": Constants.NAME
    }
    payload_string = json.dumps(payload)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(Data.URL+Data.REG_PATH, data=payload_string, headers=headers)
    r = response.json()
    token = r['accessToken']
    yield token
    headers = {'Authorization': token}
    requests.delete(Data.URL+Data.DEL_PATH, headers=headers)

