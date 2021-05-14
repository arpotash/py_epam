from homework2.task2.task import major_and_minor_elem


class TestMinMaxCount:
    def test_find_min_max(self):
        assert major_and_minor_elem([3, 2, 3]) == (3, 2)

    def test_no_min(self):
        assert major_and_minor_elem([3, 3, 3]) == (3, None)
