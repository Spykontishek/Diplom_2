import pytest
import allure
import requests
import json
from constants import Constants
from conftest import reg
from helpers.helpers import Helpers

class TestCreateUser():
    accessToken = None
    @allure.title('Негативная проверка создания юзера, который уже существует')
    @allure.description('Запрос должен вернуть ошибку и правильный код ответа')
    @pytest.mark.usefixtures('reg')
    def test_сreate_2_identical_couriers_error(self, reg):
        self.accessToken = reg
        payload = {
            "email": Constants.EMAIL,
            "password": Constants.PASSWORD,
            "name": Constants.NAME
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(Constants.URL + Constants.REG_PATH, data=payload_string, headers=headers)
        assert '"message":"User already exists"' in response.text
        assert response.status_code == 403

    def teardown_method(self):
        helper = Helpers()
        helper.delete_user(self.accessToken)

