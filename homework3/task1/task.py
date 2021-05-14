def cache_function(times):
    def real_decorator(func):
        cache_key = {}

        def wrapper(*args, **kwargs):
            nonlocal cache_key
            key = (args, tuple(sorted(kwargs.items())))
            if key not in cache_key:
                cache_result = func(*args, **kwargs)
                cache_key[key] = [cache_result, 0]
            response, called = cache_key[key]
            if called > times:
                return func(*args, **kwargs)
            else:
                cache_key[key][1] += 1
                return response

        return wrapper

    return real_decorator


@cache_function(times=2)
def f():
    return input("? ")
