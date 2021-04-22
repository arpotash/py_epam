import pytest

from homework1.task2.task import check_fibonacci


class TestCheckFibonachi:
    @pytest.mark.parametrize(
        "lst, expected_result",
        [([1, 1, 2], True), ([-1, -1, -2, -3], True), ([10, 20, 30, 50], True)],
    )
    def test_positive_case(self, lst, expected_result):
        """Testing that actual sequence of fibonachi return True"""
        assert check_fibonacci(lst) == expected_result

    @pytest.mark.parametrize(
        "lst, expected_result", [([1, 1, 3], False), ([-1, 0, 1], False)]
    )
    def test_negative_case(self, lst, expected_result):
        """Testing that not actual sequence of fibonachi return False"""
        assert check_fibonacci(lst) == expected_result

    def test_length_less_3(self):
        """Testing that sequence with length less than 3 return IndexError"""
        with pytest.raises(IndexError):
            check_fibonacci([1, 2])
