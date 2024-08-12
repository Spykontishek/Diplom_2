import pytest
import allure
import requests
import json
from constants import Constants
from conftest import reg
from helpers.helpers import Helpers


class TestAutorizationUser():
    accessToken = None
    @allure.title('Негативная проверка авторизации юзера с неправильным майлом или паролем')
    @allure.description('Запрос должен вернуть ошибку и правильный код ответа')
    @pytest.mark.parametrize("wrong_value", ["email", "password"])
    @pytest.mark.usefixtures('reg')
    def test_authorization_user_with_wrong_password_or_email_error(self, reg, wrong_value):
        self.accessToken = reg
        payload = {
        "email": Constants.EMAIL if wrong_value != "email" else None,
        "password": Constants.PASSWORD if wrong_value != "password" else None
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(Constants.URL+Constants.AUTH_PATH, data=payload_string, headers=headers)
        assert '"message":"email or password are incorrect"' in response.text
        assert response.status_code == 401

    def teardown_method(self):
        helper = Helpers()
        helper.delete_user(self.accessToken)