import allure
import pytest

import courier_methods
import data


class TestCreateCourier:
    @allure.title("Тест успешного создания курьера")
    def test_successful_courier_create_returns_ok(self):
        response, login, password, first_name = courier_methods.CourierMethods.register_new_courier_and_return_login_password()
        assert response.status_code == 201 and (response.json()['ok'] == True)

    @allure.title("Тест создания двух одинаковых курьеров")
    def test_create_two_same_couriers_returns_error(self):
        with allure.step("Регистрация курьера и получение данных (логин/пароль/имя) для регистрации"):
            response, login, password, first_name = courier_methods.CourierMethods.register_new_courier_and_return_login_password()
        courier_body = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        with allure.step("Повторная регистрация с полученными данными"):
            response = courier_methods.CourierMethods.create_courier(courier_body)
        assert response.status_code == 409 and (response.json()['message'] == 'Этот логин уже используется')

    @allure.title("Тест создания курьера без одного из обязательных полей")
    @pytest.mark.parametrize('login,password,firstName',
    [
        ['courierking11112','12345678',''],
        ['courierking11112','','King'],
        ['','12345678','King']
    ]
    )
    def test_create_courier_without_required_field_returns_error(self,login,password,firstName):
        courier_body = {
            "login": login,
            "password": password,
            "firstName": firstName
        }
        response = courier_methods.CourierMethods.create_courier(courier_body)
        assert response.status_code == 400 and (response.json()['message'] == 'Недостаточно данных для создания учетной записи')

class TestLoginCourier:
    @allure.title("Тест успешной авторизации курьера")
    def test_successful_courier_login_returns_id(self):
        response = courier_methods.CourierMethods.login_courier(data.DataForCourier.LOGIN_COURIER_BODY)
        assert response.status_code == 200 and ('id' in response.text)

    @allure.title("Тест авторизации курьера с неверными логином/паролем")
    @pytest.mark.parametrize('login,password',
    [
        ['courierking111212', '12345'], #неверный пароль
        ['courierking1117', '123456'] #неверный логин
    ]
    )
    def test_login_courier_with_invalid_credentials_returns_error(self,login,password):
        courier_body = {
            "login": login,
            "password": password
        }
        response = courier_methods.CourierMethods.login_courier(courier_body)
        assert response.status_code == 404 and (response.json()['message'] == 'Учетная запись не найдена')

    @allure.title("Тест авторизации курьера без одного из обязательных полей")
    @pytest.mark.parametrize('login,password',
    [
        ['courierking6467', ''],
        ['', '12345678']
    ]
    )
    def test_login_courier_without_required_field_returns_error(self, login, password):
        courier_body = {
        "login": login,
        "password": password
        }
        response = courier_methods.CourierMethods.login_courier(courier_body)
        assert response.status_code == 400 and (response.json()['message'] == 'Недостаточно данных для входа')

    @allure.title("Тест авторизации курьера под несуществующим пользователем")
    def test_login_not_exist_courier_returns_error(self):
        courier_body = {
            "login": 'wdwqfjnewonvw123454',
            "password": 'password'
        }
        response = courier_methods.CourierMethods.login_courier(courier_body)
        assert response.status_code == 404 and (response.json()['message'] == 'Учетная запись не найдена')