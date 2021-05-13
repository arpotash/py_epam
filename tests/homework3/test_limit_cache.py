from unittest.mock import Mock

from homework3.task1.task import cache_function


class TestCache:
    def test_limited_cache(self):
        """Testing that function return same result, when decorator
        argument will be more then calls quantity"""
        counter = 0

        @cache_function(times=2)
        def f(*args, **kwargs):
            nonlocal counter
            counter += 1
            return 20
        assert counter == 0
        f()
        assert counter == 1
        f()
        assert counter == 1
        f()
        assert counter == 1
        f()
        assert counter == 2

    def test_cache_function(self):
        """Testing that called function is cached and next calls
        this function will have the same id"""
        mock = Mock(return_value=20)
        decorated_func = cache_function(2)(mock)
        value_1 = decorated_func()
        value_2 = decorated_func()
        assert value_1 is value_2
