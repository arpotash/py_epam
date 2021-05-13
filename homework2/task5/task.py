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


def custom_range(sequence, *args):
    start, stop, step = None, None, None
    if len(args) == 1:
        start, stop, step = sequence[0], args[0], 1
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1
    elif len(args) == 3:
        start, stop, step = args[0], args[1], args[2]
    else:
        raise AttributeError("count arguments have to be from 1 to 3")
    if start in sequence and stop in sequence:
        if type(start) is str and type(stop) is str:
            start_value = ord(start)
            stop_value = ord(stop)
            result = [chr(value) for value in range(start_value, stop_value, step)]
            return result
        else:
            result = [value for value in range(start, stop, step)]
            return result
    else:
        raise ValueError("start or stop point is not suitable for this alphabet")
