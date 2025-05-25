import allure
import pytest

import order_methods


class TestCreateOrder:
    @allure.title("Тест успешного создания заказа")
    @pytest.mark.parametrize(
    'firstName,lastName,address,metroStation,phone,rentTime,deliveryDate,comment,color',
    [
        ['Александр','Пушкин','Царское Село',45,'89999999123',4,'2025-05-29','Эксперт по дуэлям',['GREY']],
        ['Зубенко','Михаил','Москва',21,'89991111111',2,'2025-06-12','Мафиозник',['BLACK']],
        ['Илон','Маск','Стар-Бейс',211,'89876543210',7,'2025-06-22','электро-самокат на ракетной тяге',['BLACK','GREY']],
        ['Кама','Пуля','Сочи',54,'89991112222',1,'2025-07-29','Таааа, шааа',['']]
    ]
    )
    def test_create_order_returns_track(self, firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color):
        order_body = {
            "firstName": firstName,
            "lastName": lastName,
            "address": address,
            "metroStation": metroStation,
            "phone": phone,
            "rentTime": rentTime,
            "deliveryDate": deliveryDate,
            "comment": comment,
            "color": color
        }
        response = order_methods.OrderMethods.create_order(order_body)
        assert response.status_code == 201 and ('track' in response.text)


class TestGetListOfOrders:
    @allure.title("Тест успешного получения списка заказов")
    def test_get_orders_list_returns_orders(self):
        response = order_methods.OrderMethods.get_orders_list()
        assert response.status_code == 200 and (type(response.json()['orders']) ==list)