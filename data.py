class Url:
    BASE_URL = 'http://qa-scooter.praktikum-services.ru'
    CREATE_COURIER_URL = '/api/v1/courier'
    LOGIN_COURIER_URL = '/api/v1/courier/login'
    ORDER_URL = '/api/v1/orders'


class DataForCourier:
    LOGIN_COURIER_BODY = {
    "login": "courierking111212",
    "password": "123456"
    }