import pytest

from homework3.task3.task import Filter, make_filter


class TestFilterObjects:
    @pytest.fixture
    def create_test_data(self):
        sample_data = [
            {
                "name": "Bill",
                "last_name": "Gilbert",
                "occupation": "was here",
                "type": "person",
            },
            {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
        ]
        return sample_data

    def test_fail_with_arguments_in_1_element(self, create_test_data):
        """Testing that if all keys are in 1 element data function return
        wrong answer, should return this element"""
        assert make_filter(name="polly", type="bird").apply(create_test_data) != [
            {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}
        ]

    def test_fail_with_no_elem_key_by_both_elem(self, create_test_data):
        """Testing that with key, which is not present in both elements
        return wrong answer, should return element with this key"""
        with pytest.raises(KeyError):
            make_filter(kind="parrot").apply(create_test_data)
