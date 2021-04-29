def cache_function(times):
    def real_decorator(func):
        cache_key = {}

        def wrapper(*args, **kwargs):
            nonlocal cache_key
            nonlocal times
            if not cache_key.get(args, kwargs):
                cache_result = func(*args, **kwargs)
                cache_key[args] = cache_result
            while times > 0:
                times -= 1
                return cache_key[args]
            cache_key[args] = func(*args, **kwargs)
            return cache_key[args]

        return wrapper

    return real_decorator


def f():
    return input("? ")
