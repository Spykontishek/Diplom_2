import pytest
import allure
import requests
import json
from conftest import reg
from data import Data

class TestCreateOrder:
    @allure.title('Позитивная проверка создания заказа под авторизованным аккаунтом')
    @allure.description('Запрос должен вернуть правильный код и тело ответа')
    def test_create_order_with_authorization_success(self, reg):
        token = reg
        payload = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d"]
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': token
        }
        response = requests.post(Data.URL+Data.CREATE_ORDER_PATH, data=payload_string, headers=headers)
        assert 'owner' in response.text
        assert response.status_code == 200


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
        response = requests.post(Data.URL + Data.CREATE_ORDER_PATH, data=payload_string, headers=headers)
        r = response.json()
        assert r['success'] == True
        assert response.status_code == 200

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
        response = requests.post(Data.URL + Data.CREATE_ORDER_PATH, data=payload_string, headers=headers)
        assert response.status_code == 500

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
        response = requests.post(Data.URL + Data.CREATE_ORDER_PATH, data=payload_string, headers=headers)
        assert 'owner' not in response.text
        assert response.status_code == 200


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
        response = requests.post(Data.URL+Data.CREATE_ORDER_PATH, data=payload_string, headers=headers)
        assert Data.EMPTY_ID_OF_INGREDIENT_MASSAGE in response.text
        assert response.status_code == 400


