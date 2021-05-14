import pytest

from homework3.task3.task import make_filter


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

    def test_filter_with_keys_in_1_item(self, create_test_data):
        """Testing that if all keys are in 1 item data function return
        right answer"""
        assert make_filter(name="polly", type="bird").apply(create_test_data) == [
            {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}
        ]

    def test_filter_with_keys_in_different_items(self, create_test_data):
        """Testing that with keys, which are present in different is
        return empty list"""
        assert make_filter(name="Bill", type="bird").apply(create_test_data) == []

    def test_filter_with_1_key_in_1_item(self, create_test_data):
        """Testing that if key which is not present in both items
        return only item with this key"""
        assert make_filter(last_name="Gilbert").apply(create_test_data) == [
            {
                "name": "Bill",
                "last_name": "Gilbert",
                "occupation": "was here",
                "type": "person",
            }
        ]
