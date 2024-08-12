import pytest
import allure
import requests
import json
from constants import Constants
from conftest import reg
from helpers.helpers import Helpers


class TestChangeUserData():
    accessToken = None
    @allure.title('Позитивная проверка изменения данных юзера под авторизованным аккаунтом')
    @allure.description('Запрос должен вернуть правильный код и тело ответа')
    @pytest.mark.usefixtures('reg')
    def tests_change_user_data_with_authorization_success(self, reg):
        self.accessToken = reg
        payload = {
        "email": Constants.EMAIL,
        "password": Constants.PASSWORD,
        "name": "Usernam"
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': self.accessToken
        }
        response = requests.patch(Constants.URL+Constants.CHANGE_PATH, data=payload_string, headers=headers)
        r = response.json()
        assert r['success'] == True
        assert response.status_code == 200

    def teardown_method(self):
        helper = Helpers()
        helper.delete_user(self.accessToken)