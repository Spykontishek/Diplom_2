import pytest
import requests
import allure
import json
from constants import Constants


class TestCreateUser():
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    @allure.title('Негативная проверка создания юзера с 1 отсутствующим обязательным полем')
    @allure.description('Запрос должен вернуть ошибку и правильный код ответа')
    def test_creating_user_with_missing_required_fields_error(self, missing_field):
        payload = {
            "email": Constants.EMAIL if missing_field != "email" else None,
            "password": Constants.PASSWORD if missing_field != "password" else None,
            "name": Constants.NAME if missing_field != "name" else None
        }
        payload_string = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(Constants.URL+Constants.REG_PATH, data=payload_string, headers=headers)
        assert '"message":"Email, password and name are required fields"' in response.text
        assert response.status_code == 403