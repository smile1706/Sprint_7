import requests
import random
import string

from data import Url


class CourierMethods:
    @staticmethod
    def create_courier(body):
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER_URL}', json=body)
        return response


    @staticmethod
    def register_new_courier_and_return_login_password():
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', json=payload)

        if response.status_code == 201:
            return response, login, password, first_name

    @staticmethod
    def login_courier(body):
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER_URL}', json=body)
        return response