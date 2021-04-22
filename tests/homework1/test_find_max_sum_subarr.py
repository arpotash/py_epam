import pytest

from homework1.task5.task import find_maximal_subarray_sum


class TestFindMaxSumSubArr:
    @pytest.mark.parametrize(
        "lst, length, expected_result",
        [([1, 3, -1, -3, 5, 3, 6, 7], 3, 16), ([1, 2, 3, True, 5], 2, 6)],
    )
    def test_find_sum(self, lst, length, expected_result):
        """Testing that with correct data function return right answer"""
        assert find_maximal_subarray_sum(lst, length) == expected_result

    def test_no_int_type_elements(self):
        """Testing that the presence of string elements raise TypeError"""
        with pytest.raises(TypeError):
            find_maximal_subarray_sum(["elem1", "elem2", "elem3"], 2)
