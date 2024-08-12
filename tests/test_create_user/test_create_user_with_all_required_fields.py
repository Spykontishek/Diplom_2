import pytest
import requests
import allure
import json
from constants import Constants
from helpers.helpers import Helpers
from faker import Faker


faker = Faker()

class TestCreateUser():
    accessToken = None
    @allure.title('Позитивная проверка создания юзера с заполнением всех обязательных полей')
    @allure.description('Запрос должен вернуть правильный код и тело ответа')
    def test_creating_сourier_with_all_required_fields_success(self):
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
        self.accessToken = r['accessToken']
        assert r['success'] == True
        assert response.status_code == 200


    def teardown_method(self):
        helper = Helpers()
        helper.delete_user(self.accessToken)
