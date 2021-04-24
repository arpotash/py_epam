"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""

from typing import Callable


def cache(func: Callable) -> Callable:
    cache_key = {}

    def wrapper(*args, **kwargs):
        nonlocal cache_key
        if not cache_key.get(args, kwargs):
            response = func(*args, **kwargs)
            cache_key[args] = response
            return response
        else:
            return cache_key[args]

    return wrapper


@cache
def f(a, b):
    return (a ** b) ** 2
