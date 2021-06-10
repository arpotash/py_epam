import os

import pytest

from homework8.task1.task import KeyValueStorage

FILE_PATH = os.path.join(os.getcwd(), "tests", "homework8", "file_test.txt")


class TestKeyValueStorage:

    storage = KeyValueStorage(FILE_PATH)

    def test_success_item(self):
        assert self.storage["name"] == "kek"

    def test_wrong_item(self):
        with pytest.raises(KeyError) as e:
            print(self.storage["wrong_item"])
        error_msg = e.value.args[0]
        assert error_msg == "Wrong key"

    def test_success_attribute(self):
        assert self.storage.name == "kek"

    def test_attribute_collision_case_in_class_dict(self):
        assert self.storage.__doc__ is None

    def test_attribute_collision_case_in_self_dict(self):
        assert self.storage.attr_dict_from_file == {
            "__doc__": "your_attribute",
            "last_name": "top",
            "name": "kek",
            "power": "9001",
            "song": "shadilay",
        }

    def test_wrong_attribute(self):
        with pytest.raises(AttributeError):
            return self.storage.wrong_attribute
