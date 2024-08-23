import pytest
import requests
import allure
import json
from constants import Constants
from helpers.helpers import Helpers
from conftest import reg
from faker import Faker


faker = Faker()

class TestCreateUser():
    token = None
    @allure.title('Позитивная проверка создания юзера с заполнением всех обязательных полей')
    @allure.description('Запрос должен вернуть правильный код и тело ответа')
    def test_creating_user_with_all_required_fields_success(self):
        password = faker.password()[:8]
        name = faker.first_name()[:8]
        payload = {
        "email": Constants.EMAIL,
        "password": password,
        "name": name
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(Constants.URL+Constants.REG_PATH, data=payload_string, headers=headers)
        r = response.json()
        self.token = r['accessToken']
        assert r['success'] == True
        assert response.status_code == 200

    def teardown_method(self):
        helper = Helpers()
        helper.delete_user(self.token)


    @allure.title('Негативная проверка создания юзера, который уже существует')
    @allure.description('Запрос должен вернуть ошибку и правильный код ответа')
    def test_сreate_2_identical_users_error(self, reg):
        payload = {
            "email": Constants.EMAIL,
            "password": Constants.PASSWORD,
            "name": Constants.NAME
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(Constants.URL + Constants.REG_PATH, data=payload_string, headers=headers)
        assert '"message":"User already exists"' in response.text
        assert response.status_code == 403


    @pytest.mark.parametrize("test_email, test_password, test_name",
                             [
                                 ("", Constants.PASSWORD, Constants.NAME),
                                 (Constants.EMAIL, "", Constants.NAME),
                                 (Constants.EMAIL, Constants.PASSWORD, "")
                             ])
    @allure.title('Негативная проверка создания юзера с 1 отсутствующим обязательным полем')
    @allure.description('Запрос должен вернуть ошибку и правильный код ответа')
    def test_creating_user_with_missing_required_fields_error(self, test_email, test_password, test_name):
        payload = {
            "email": test_email,
            "password": test_password,
            "name": test_name
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(Constants.URL+Constants.REG_PATH, data=payload_string, headers=headers)
        assert '"message":"Email, password and name are required fields"' in response.text
        assert response.status_code == 403



