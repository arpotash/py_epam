import string

import pytest

from homework2.task5.task import custom_range


class TestCustomRange:
    def test_ascii_range_arg_ascii_low_stop(self):
        assert custom_range(string.ascii_lowercase, "g") == ["a", "b", "c", "d", "e", "f"]

    def test_ascii_range_arg_ascii_low_stop_equal_start(self):
        assert custom_range(string.ascii_lowercase, "a") == []

    def test_ascii_range_arg_ascii_up_stop(self):
        assert custom_range(string.ascii_uppercase, "G") == ["A", "B", "C", "D", "E", "F"]

    def test_ascii_range_arg_ascii_up_stop_equal_start(self):
        assert custom_range(string.ascii_uppercase, "A") == []

    def test_ascii_range_arg_ascii_low_start_stop(self):
        assert custom_range(string.ascii_lowercase, "g", "p") == ["g", "h", "i", "j", "k", "l", "m", "n", "o"]

    def test_ascii_range_arg_ascii_up_start_stop(self):
        assert custom_range(string.ascii_uppercase, "G", "P") == ["G", "H", "I", "J", "K", "L", "M", "N", "O"]

    def test_ascii_range_arg_ascii_low_start_stop_equal(self):
        assert custom_range(string.ascii_lowercase, "a", "a") == []

    def test_ascii_range_arg_ascii_up_start_stop_equal(self):
        assert custom_range(string.ascii_uppercase, "A", "A") == []

    def test_ascii_range_arg_ascii_low_start_more_stop(self):
        assert custom_range(string.ascii_lowercase, "b", "a") == []

    def test_ascii_range_arg_ascii_up_start_more_stop(self):
        assert custom_range(string.ascii_uppercase, "B", "A") == []

    def test_ascii_range_arg_ascii_low_start_stop_positive_step(self):
        assert custom_range(string.ascii_lowercase, "g", "p", 2) == ['g', 'i', 'k', 'm', 'o']

    def test_ascii_range_arg_ascii_up_start_stop_positive_step(self):
        assert custom_range(string.ascii_uppercase, "G", "P", 2) == ['G', 'I', 'K', 'M', 'O']

    def test_ascii_range_arg_ascii_low_start_stop_positive_step_more_then_stop(self):
        assert custom_range(string.ascii_lowercase, "g", "p", 100) == ['g']

    def test_ascii_range_arg_ascii_up_start_stop_positive_step_more_then_stop(self):
        assert custom_range(string.ascii_uppercase, "G", "P", 100) == ['G']

    def test_ascii_range_arg_ascii_low_start_stop_negative_step(self):
        assert custom_range(string.ascii_lowercase, "p", "g", -2) == ["p", "n", "l", "j", "h"]

    def test_ascii_range_arg_ascii_up_start_stop_negative_step(self):
        assert custom_range(string.ascii_uppercase, "P", "G", -2) == ["P", "N", "L", "J", "H"]

    def test_ascii_range_wrong_arguments(self):
        with pytest.raises(ValueError) as wr_a:
            custom_range(string.ascii_lowercase, "G")
            custom_range(string.ascii_uppercase, "p", "U")
        exception_msg = wr_a.value.args[0]
        assert exception_msg == "start or stop point is not suitable for this alphabet"

    def test_ascii_range_no_encoding(self):
        with pytest.raises(TypeError) as tp_e:
            custom_range("g")
        exception_msg = tp_e.value.args[0]
        assert exception_msg == "no argument encoding"

    def test_step_0(self):
        with pytest.raises(ValueError) as e:
            custom_range(string.ascii_lowercase, 'a', 'p', 0)
            custom_range(string.ascii_lowercase, 'A', 'P', 0)
        exception_msg = e.value.args[0]
        assert exception_msg == "range() arg 3 must not be zero"
