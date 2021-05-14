import time

import pytest

from homework3.task2.task import distribution_pool, slow_calculate


class TestSlowCalculate:
    @pytest.fixture
    def get_start_time(self):
        start = time.time()
        return start

    def test_get_sum_nums_from_0_to_499(self, get_start_time):
        """Testing get sum of 500 elements with time limit less then 1 minute"""
        result = distribution_pool()
        time_end = time.time() - get_start_time
        assert result == 1024259
        assert time_end <= 60

    def test_get_1_elem(self):
        """Testing get 1 element"""
        assert slow_calculate(1) == 1996
