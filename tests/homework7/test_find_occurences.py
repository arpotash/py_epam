from homework7.task1.task import find_occurrences

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
    "fifth": "YELLOW",
}


class TestFindOccurences:
    def test_find_elem_simple_dict(self):
        """Testing finding element in simple dictionary"""
        assert find_occurrences(example_tree, "YELLOW") == 1

    def test_find_elem_in_nested_dict(self):
        """Testing finding element in nested dictionary"""
        assert find_occurrences(example_tree, "BLUE") == 2

    def test_find_elem_in_nested_dict_list(self):
        """Testing finding element in nested dictionary in list"""
        assert find_occurrences(example_tree, "simple") == 1

    def test_find_elem_in_multiply_nested_dict_in_list(self):
        """Testing finding element in multiply nested structures
        (list in dictionary, dictionary in list)"""
        assert find_occurrences(example_tree, "RED") == 6
