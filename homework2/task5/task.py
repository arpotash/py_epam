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


def custom_range(encoding, *args):
    if encoding not in [string.ascii_lowercase, string.ascii_uppercase]:
        raise TypeError("no argument encoding")
    start, stop, step = None, None, None
    if len(args) == 1:
        start = "a".lower() if encoding == string.ascii_lowercase else "a".upper()
        stop, step = args[0], 1
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1
    elif len(args) == 3:
        start, stop, step = args[0], args[1], args[2]
    if start in encoding and stop in encoding:
        start_value = ord(start)
        stop_value = ord(stop)
        result = [chr(value) for value in range(start_value, stop_value, step)]
        return result
    else:
        raise ValueError("start or stop point is not suitable for this alphabet")
