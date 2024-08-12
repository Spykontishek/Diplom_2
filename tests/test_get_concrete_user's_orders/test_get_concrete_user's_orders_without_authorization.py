import pytest
import allure
import requests
from constants import Constants


class TestGetUsersOrders():
    accessToken = None
    @allure.title('Позитивная проверка получения всех заказов юзера под авторизованным аккаунтом')
    @allure.description('Запрос должен вернуть ошибку и правильный код ответа')
    @pytest.mark.usefixtures('reg')
    def test_get_users_orders_without_authorization_error(self):
        response = requests.get(Constants.URL+Constants.GET_ORDERS_PATH)
        assert '"message":"You should be authorised"' in response.text
        assert response.status_code == 401