import os

import pytest

from homework4.task1.task import check_exist_file, read_magic_number


class TestMagicNumber:
    @pytest.fixture
    def create_file_not_magic_num(self, tmp_path):
        test_file_path = os.path.join(tmp_path, "test_file.txt")
        test_data = "1\n2\n"
        with open(test_file_path, "w") as f_o:
            f_o.writelines(test_data)
            return test_file_path

    @pytest.fixture
    def create_file_magic_num(self, tmp_path):
        test_file_path = os.path.join(tmp_path, "test_file_1.txt")
        test_data = "10\n2\n"
        with open(test_file_path, "w") as f_o:
            f_o.writelines(test_data)
            return test_file_path

    def test_is_created_file(self, create_file_magic_num):
        """Testing that file exists"""
        assert check_exist_file(create_file_magic_num)

    def test_positive_define_magic_number(self, create_file_magic_num):
        """Testing that on the first lane magic number"""
        assert read_magic_number(create_file_magic_num)

    def test_is_not_created_file(self):
        """Testing that file doesn't exist"""
        with pytest.raises(FileNotFoundError):
            check_exist_file("test_hide_file.txt")

    def test_negative_define_magic_number(self, create_file_not_magic_num):
        """Testing that on the first lane not magic number"""
        assert not read_magic_number(create_file_not_magic_num)
