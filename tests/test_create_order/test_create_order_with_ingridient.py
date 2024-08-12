import pytest
import allure
import requests
import json
from constants import Constants

class TestCreateOrder:

    @allure.title('Позитивная проверка создания заказа с указанием ингредиента')
    @allure.description('Запрос должен вернуть правильный код и тело ответа')
    def test_create_order_with_ingredient_success(self):
        payload = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d"]
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(Constants.URL+Constants.CREATE_ORDER_PATH, data=payload_string, headers=headers)
        r = response.json()
        assert r['success'] == True
        assert response.status_code == 200
