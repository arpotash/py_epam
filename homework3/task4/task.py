from functools import reduce


def is_armstrong(number: int) -> bool:
    lst_nums = list(map(int, str(number)))
    pow_nums_lst = [pow(num, len(lst_nums)) for num in lst_nums]
    result = reduce(lambda x, y: x + y, pow_nums_lst)
    return result == number
