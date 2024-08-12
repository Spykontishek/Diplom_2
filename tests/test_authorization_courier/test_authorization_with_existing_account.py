import pytest
import allure
import requests
import json
from constants import Constants
from conftest import reg
from helpers.helpers import Helpers


class TestAutorizationUser():
    accessToken = None
    @allure.title('Позитивная проверка авторизации юзера под существующим аккаунтом')
    @allure.description('Запрос должен вернуть правильный код и тело ответа')
    @pytest.mark.usefixtures('reg')
    def test_authorization_user_with_exiting_account_success(self, reg):
        self.accessToken = reg
        payload = {
        "email": Constants.EMAIL,
        "password": Constants.PASSWORD
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(Constants.URL+Constants.AUTH_PATH, data=payload_string, headers=headers)
        r = response.json()
        assert r['success'] == True
        assert response.status_code == 200

    def teardown_method(self):
        helper = Helpers()
        helper.delete_user(self.accessToken)