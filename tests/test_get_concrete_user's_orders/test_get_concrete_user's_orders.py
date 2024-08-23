import pytest
import allure
import requests
from constants import Constants
from conftest import reg


class TestGetUsersOrders():
    @allure.title('Позитивная проверка получения всех заказов юзера под авторизованным аккаунтом')
    @allure.description('Запрос должен вернуть правильный код и тело ответа')
    def test_get_users_orders_with_authorization_success(self, reg):
        token = reg
        headers = {
            'Authorization': token
        }
        response = requests.get(Constants.URL+Constants.GET_ORDERS_PATH, headers = headers)
        r = response.json()
        assert r['success'] == True
        assert response.status_code == 200


    @allure.title('Позитивная проверка получения всех заказов юзера под авторизованным аккаунтом')
    @allure.description('Запрос должен вернуть ошибку и правильный код ответа')
    def test_get_users_orders_without_authorization_error(self):
        response = requests.get(Constants.URL+Constants.GET_ORDERS_PATH)
        assert '"message":"You should be authorised"' in response.text
        assert response.status_code == 401