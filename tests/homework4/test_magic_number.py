import os

import pytest

from homework4.task1.task import check_exist_file, read_magic_number

PATH = os.path.abspath("tests/homework4/test_file.txt")


class TestMagicNumber:
    @pytest.fixture
    def create_file_magic_num(self):
        test_data = "1\n2\n"
        with open("test_file.txt", "w") as f_o:
            f_o.writelines(test_data)
            return f_o

    @pytest.fixture
    def create_file_not_magic_num(self):
        test_data = "10\n2\n"
        with open("test_file.txt", "w") as f_o:
            f_o.writelines(test_data)
            return f_o

    def test_is_created_file(self, create_file_magic_num):
        """Testing that file exists"""
        assert check_exist_file(create_file_magic_num.name)
        os.remove(create_file_magic_num.name)

    def test_positive_define_magic_number(self, create_file_magic_num):
        """Testing that on the first lane magic number"""
        assert read_magic_number(create_file_magic_num.name)
        os.remove(create_file_magic_num.name)

    def test_is_not_created_file(self, create_file_magic_num):
        """Testing that file doesn't exist"""
        with pytest.raises(FileNotFoundError):
            check_exist_file("test_file_1.txt")

    def test_negative_define_magic_number(self, create_file_not_magic_num):
        """Testing that on the first lane not magic number"""
        assert not read_magic_number(create_file_not_magic_num.name)
        os.remove(create_file_not_magic_num.name)
