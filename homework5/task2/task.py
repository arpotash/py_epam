import functools


def print_result(func):
    def original_info(*args, **kwargs):
        original_info.__doc__ = func.__doc__
        original_info.__name__ = func.__name__
        original_info.__original_func = func
        print(func)

        def wrapper(*args, **kwargs):
            """Function-wrapper which print result of an original function"""
            result = func(*args, **kwargs)
            print(result)
            return result

        return wrapper

    return original_info


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


def custom_func():
    return [1, 2, 3]


decorated_func = print_result(custom_func)
decorated_func()
print(decorated_func.__dict__["__original_func"]())
