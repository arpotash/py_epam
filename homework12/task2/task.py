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
