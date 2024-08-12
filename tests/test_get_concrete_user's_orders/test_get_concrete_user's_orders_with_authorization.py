import pytest
import allure
import requests
from constants import Constants
from conftest import reg
from helpers.helpers import Helpers


class TestGetUsersOrders():
    accessToken = None
    @allure.title('Позитивная проверка получения всех заказов юзера под авторизованным аккаунтом')
    @allure.description('Запрос должен вернуть правильный код и тело ответа')
    @pytest.mark.usefixtures('reg')
    def test_get_users_orders_with_authorization_success(self, reg):
        self.accessToken = reg
        headers = {
            'Authorization': self.accessToken
        }
        response = requests.get(Constants.URL+Constants.GET_ORDERS_PATH, headers = headers)
        r = response.json()
        assert r['success'] == True
        assert response.status_code == 200

    def teardown_method(self):
        helper = Helpers()
        helper.delete_user(self.accessToken)