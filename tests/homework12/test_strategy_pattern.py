from homework12.task2.task import Order, elder_discount, morning_discount


class TestGetDiscountStrategy:
    def test_get_morning_discount(self):
        """
        Testing that method final_price returns 50
        with function(morning_discount) as argument
        """
        order = Order(100, morning_discount)
        assert order.final_price() == 50

    def test_get_elder_discount(self):
        """
        Testing that method final_price returns 10
        with function(elder_discount) as argument
        """
        order = Order(100, elder_discount)
        assert order.final_price() == 10

    def test_get_discount_default(self):
        """
        Testing that method final_price returns 75
        with default discount
        """
        order = Order(100)
        assert order.final_price() == 75
