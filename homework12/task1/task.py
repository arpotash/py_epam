class SimplifiedEnum(type):
    """
    Metaclass unpacks a collection of class attributes
    and create creates attributes of the same name in the class
    """

    def __new__(cls, name, bases, attrs):
        """
        Method unpacks a collection of class attributes
        and create creates attributes of the same name in the class

        :param cls: class object
        :param name: class name
        :param bases: tuple with parents classes
        :param attrs: attribute dictionary
        :return: class object
        """
        slots_keys = f"_{attrs['__qualname__']}__keys"
        for elem in attrs[slots_keys]:
            attrs[elem] = elem
        return type.__new__(cls, name, bases, attrs)


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")
