from homework2.task3.task import combinations


class TestCombination:
    def test_find_right_lists_combination(self):
        assert combinations([1, 2], [3, 4]) == [
            [1, 3],
            [1, 4],
            [2, 3],
            [2, 4],
        ]
