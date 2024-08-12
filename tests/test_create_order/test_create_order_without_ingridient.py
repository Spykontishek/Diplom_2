import pytest
import allure
import requests
import json
from constants import Constants

class TestCreateOrder:

    @allure.title('Негативная проверка создания заказа без указания ингредиента')
    @allure.description('Запрос должен вернуть ошибку и правильный код ответа')
    def test_create_order_without_ingredient_error(self):
        payload = {
        "ingredients": []
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(Constants.URL+Constants.CREATE_ORDER_PATH, data=payload_string, headers=headers)
        assert '"message":"Ingredient ids must be provided"' in response.text
        assert response.status_code == 400