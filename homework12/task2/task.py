import math
import types


class Order:
    morning_discount = 0.25

    def __init__(self, price, strategy=None):
        self.price = price
        if strategy:
            self.final_price = types.MethodType(strategy, self)

    def final_price(self):
        return math.floor(self.price - self.price * self.morning_discount)


def morning_discount(self):
    return math.floor(self.price - self.price * 0.5)


def elder_discount(self):
    return math.floor(self.price - self.price * 0.9)


order_1 = Order(100, morning_discount)
order_2 = Order(100, elder_discount)
assert order_1.final_price() == 50
assert order_2.final_price() == 10
