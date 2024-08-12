import pytest
import allure
import requests
import json
from constants import Constants
from helpers.helpers import Helpers
from conftest import reg

class TestCreateOrder:
    accessToken = None
    @allure.title('Позитивная проверка создания заказа под авторизованным аккаунтом')
    @allure.description('Запрос должен вернуть правильный код и тело ответа')
    @pytest.mark.usefixtures('reg')
    def test_create_order_with_authorization_success(self, reg):
        self.accessToken = reg
        payload = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d"]
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': self.accessToken
        }
        response = requests.post(Constants.URL+Constants.CREATE_ORDER_PATH, data=payload_string, headers=headers)
        assert 'owner' in response.text
        assert response.status_code == 200

    def teardown_method(self):
        helper = Helpers()
        helper.delete_user(self.accessToken)