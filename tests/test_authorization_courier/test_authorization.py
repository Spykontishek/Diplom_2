import pytest
import allure
import requests
import json
from constants import Constants
from data import Data
from conftest import reg



class TestAutorizationUser():
    @allure.title('Позитивная проверка авторизации юзера под существующим аккаунтом')
    @allure.description('Запрос должен вернуть правильный код и тело ответа')
    def test_authorization_user_with_exiting_account_success(self, reg):
        payload = {
        "email": Constants.EMAIL,
        "password": Constants.PASSWORD
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(Data.URL+Data.AUTH_PATH, data=payload_string, headers=headers)
        r = response.json()
        assert r['success'] == True
        assert response.status_code == 200


    @allure.title('Негативная проверка авторизации юзера с неправильным майлом или паролем')
    @allure.description('Запрос должен вернуть ошибку и правильный код ответа')
    @pytest.mark.parametrize("test_email, test_password", [(Constants.EMAIL, "zzzzzzzz"),("zzzzzzzz", Constants.PASSWORD)])
    def test_authorization_user_with_wrong_password_or_email_error(self, reg, test_email, test_password):
        payload = {
        "email": test_email,
        "password": test_password
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(Data.URL+Data.AUTH_PATH, data=payload_string, headers=headers)
        assert Data.WRONG_EMAIL_OR_PASSWORD_MASSAGE in response.text
        assert response.status_code == 401

