import pytest
from constants import Constants
import requests
import json
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
    response = requests.post(Constants.URL+Constants.REG_PATH, data=payload_string, headers=headers)
    r = response.json()
    token = r['accessToken']
    yield token
    headers = {'Authorization': token}
    requests.delete(Constants.URL+Constants.DEL_PATH, headers=headers)

