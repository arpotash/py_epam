import string

import pytest

from homework2.task5.task import custom_range


class TestCustomRange:
    def test_ascii_range_arg_ascii_low_stop(self):
        assert custom_range(string.ascii_lowercase, "g") == [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
        ]

    def test_ascii_range_arg_ascii_up_stop(self):
        assert custom_range(string.ascii_uppercase, "G") == [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
        ]

    def test_ascii_range_arg_ascii_low_start_stop(self):
        assert custom_range(string.ascii_lowercase, "g", "p") == [
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
        ]

    def test_ascii_range_arg_ascii_up_start_stop(self):
        assert custom_range(string.ascii_uppercase, "G", "P") == [
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
        ]

    def test_ascii_range_arg_ascii_low_start_stop_step(self):
        assert custom_range(string.ascii_lowercase, "p", "g", -2) == [
            "p",
            "n",
            "l",
            "j",
            "h",
        ]

    def test_ascii_range_arg_ascii_up_start_stop_step(self):
        assert custom_range(string.ascii_uppercase, "P", "G", -2) == [
            "P",
            "N",
            "L",
            "J",
            "H",
        ]

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
