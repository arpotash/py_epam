from unittest.mock import Mock

from homework2.task4.task import cache


class TestCache:
    def test_cache_function(self):
        mock = Mock(return_value=20)
        cache_func = cache(mock)
        value_1 = cache_func()
        value_2 = cache_func()
        assert value_1 is value_2
