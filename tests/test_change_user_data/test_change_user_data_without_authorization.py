import pytest
import allure
import requests
import json
from constants import Constants
from conftest import reg
from helpers.helpers import Helpers

class TestChangeUserData():
    accessToken = None
    @allure.title('Негативная проверка изменения данных юзера под неавторизованным аккаунтом')
    @allure.description('Запрос должен вернуть ошибку и правильный код твета')
    def tests_change_user_data_without_authorization_error(self, reg):
        self.accessToken = reg
        payload = {
        "email": Constants.EMAIL,
        "password": Constants.PASSWORD,
        "name": "Usernam"
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.patch(Constants.URL+Constants.CHANGE_PATH, data=payload_string, headers=headers)
        assert '"message":"You should be authorised"' in response.text
        assert response.status_code == 401

    def teardown_method(self):
        helper = Helpers()
        helper.delete_user(self.accessToken)