import math
import types


class Order:
    """
    Class create order

    Attributes:
        morning_discount: float
        price: int
        strategy: function
    """

    morning_discount = 0.25

    def __init__(self, price, strategy=None):
        """
        Sets all required attributes for the object
        Parameters:
            price: int
            strategy: function
        """
        self.price = price
        if strategy:
            self.final_price = types.MethodType(strategy, self)

    def final_price(self):
        """
        Function applies discount to the amount
        :return: int, the final amount
        """
        return math.floor(self.price - self.price * self.morning_discount)


def morning_discount(self):
    """
    Function applies 50% discount to the amount
    :return: int, the final amount
    """
    return math.floor(self.price - self.price * 0.5)


def elder_discount(self):
    """
    Function applies 90% discount to the amount
    :return: int, the final amount
    """
    return math.floor(self.price - self.price * 0.9)
