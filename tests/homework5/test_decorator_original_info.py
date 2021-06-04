from unittest.mock import Mock

from homework5.task2.task import print_result


class TestGetOriginalInfo:
    def test_get_original_docstring_function_name(self):
        """Testing that the decorator returns original docstring and function's name"""
        func = Mock()
        func.__doc__ = "some docstring"
        func.__name__ = "custom_func"
        decorated_func = print_result(func)
        decorated_func(1, 2, 3)
        assert decorated_func.__doc__ == func.__doc__
        assert decorated_func.__name__ == func.__name__

    def custom_func(self):
        return [1, 2, 3]

    def test_get_original_func(self):
        """Testing that the decorator saves passed function in its
        attribute __original_func,which can be called"""
        decorated_func = print_result(self.custom_func)
        decorated_func()
        assert decorated_func.__dict__["__original_func"]() == [1, 2, 3]
