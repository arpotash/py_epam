"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    result = False
    if len(data) < 3:
        raise Exception("the length of the sequence have to be at least 3")
    length = len(data) - 2
    for elem in range(length):
        result = False
        if data[elem] + data[elem + 1] == data[elem + 2]:
            result = True
    return result
