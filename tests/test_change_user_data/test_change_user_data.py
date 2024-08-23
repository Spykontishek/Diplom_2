import pytest
import allure
import requests
import json
from constants import Constants
from conftest import reg
from data import Data



class TestChangeUserData():
    token = None
    @allure.title('Позитивная проверка изменения данных юзера под авторизованным аккаунтом')
    @allure.description('Запрос должен вернуть правильный код и тело ответа')
    def tests_change_user_data_with_authorization_success(self, reg):
        token = reg
        payload = {
        "email": Constants.EMAIL,
        "password": Constants.PASSWORD,
        "name": "Usernam"
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': token
        }
        response = requests.patch(Data.URL+Data.CHANGE_PATH, data=payload_string, headers=headers)
        r = response.json()
        assert r['success'] == True
        assert response.status_code == 200




    @allure.title('Негативная проверка изменения данных юзера под неавторизованным аккаунтом')
    @allure.description('Запрос должен вернуть ошибку и правильный код твета')
    def tests_change_user_data_without_authorization_error(self, reg):
        payload = {
        "email": Constants.EMAIL,
        "password": Constants.PASSWORD,
        "name": "Usernam"
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.patch(Data.URL+Data.CHANGE_PATH, data=payload_string, headers=headers)
        assert Data.AUTH_ERROR_MASSAGE in response.text
        assert response.status_code == 401

