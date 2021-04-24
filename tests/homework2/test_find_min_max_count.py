import pytest
from homework2.task2.task import major_and_minor_elem


class TestMinMaxCount:

    @pytest.mark.parametrize("lst, excepted_values", [([3, 2, 3], (3, 2)),
                                                      ([2, 2, 2, 2], (2, 2))])
    def test_find_min_max(self, lst, excepted_values):
        assert major_and_minor_elem(lst) == excepted_values
