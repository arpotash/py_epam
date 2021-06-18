from homework12.task2.task import Order, elder_discount, morning_discount


class TestGetDiscountStrategy:
    def test_get_morning_discount(self):
        order = Order(100, morning_discount)
        assert order.final_price() == 50

    def test_get_elder_discount(self):
        order = Order(100, elder_discount)
        assert order.final_price() == 10

    def test_get_discount_default(self):
        order = Order(100)
        assert order.final_price() == 75
