class SimplifiedEnum(type):
    def __new__(cls, name, bases, attrs):
        slots_keys = f"_{attrs['__qualname__']}__keys"
        for elem in attrs[slots_keys]:
            attrs[elem] = elem
        return type.__new__(cls, name, bases, attrs)


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")
