import pytest

from homework3.task4.task import is_armstrong


class TestArmstrongNumber:
    @pytest.mark.parametrize("num, excepted_result", [(153, True), (10, False)])
    def test_is_armstrong_number(self, num, excepted_result):
        """Testing that with integer argument function return
        True, if number Armstrong, else return False"""
        assert is_armstrong(num) == excepted_result

    def test_error_with_no_int_argument(self):
        """Testing that with not integer argument function return
        ValueError"""
        with pytest.raises(ValueError):
            is_armstrong("num")
            is_armstrong(True)
