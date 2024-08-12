import pytest
import allure
import requests
import json
from constants import Constants

class TestCreateOrder:

    @allure.title('Негативная проверка создания заказа С неверным хешем ингредиента')
    @allure.description('Запрос должен вернуть ошибку и правильный код ответа')
    def test_create_order_with_invalid_hash_of_ingredient_error(self):
        payload = {
        "ingredients": ["%%%"]
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(Constants.URL+Constants.CREATE_ORDER_PATH, data=payload_string, headers=headers)
        assert response.status_code == 500