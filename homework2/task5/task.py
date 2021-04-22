"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
"""

import string


def custom_range(stop, start="a", step=1, encoding=string.ascii_lowercase):
    lst_custom_for_value = []
    start_value = ord(start)
    stop_value = ord(stop)
    if step < 0:
        while stop_value > start_value:
            lst_custom_for_value.append(chr(stop_value))
            stop_value += step
    else:
        while start_value < stop_value:
            lst_custom_for_value.append(chr(start_value))
            start_value += step

    return lst_custom_for_value


print(custom_range("g"))
