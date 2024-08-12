import pytest
import allure
import requests
import json
from constants import Constants

class TestCreateOrder:

    @allure.title('Позитивная проверка создания заказа под неавторизованным аккаунтом')
    @allure.description('Запрос должен вернуть правильный код и тело ответа')
    def test_create_order_without_authorization_success(self):
        payload = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d"]
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(Constants.URL+Constants.CREATE_ORDER_PATH, data=payload_string, headers=headers)
        assert 'owner' not in response.text
        assert response.status_code == 200
