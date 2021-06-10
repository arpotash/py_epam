import os

import pytest

from homework9.task1.task import merge_sorted_files


class TestMergeSortFile:

    test_data_1 = "1\n3\n5\n"
    test_data_2 = "2\n4\n6\n"
    test_data_3 = "2\n"
    test_data_4 = ""

    @pytest.fixture
    def create_first_file(self):
        """
        Function creates the file ('txt') with test data
        :return: file object
        """
        test_first_file_path = os.path.join(os.getcwd(), "test1.txt")
        with open(test_first_file_path, "w") as f_o:
            f_o.writelines(self.test_data_1)
            return f_o

    @pytest.fixture
    def create_second_file(self):
        """
        Function creates the file ('txt') with test data
        :return: file object
        """
        test_second_file_path = os.path.join(os.getcwd(), "file2.txt")
        with open(test_second_file_path, "w") as f_o:
            f_o.writelines(self.test_data_2)
            return f_o

    @pytest.fixture
    def create_file_with_little_data(self):
        """
        Function creates the file ('txt') with test data
        :return: file object
        """
        test_second_file_path = os.path.join(os.getcwd(), "file2.txt")
        with open(test_second_file_path, "w") as f_o:
            f_o.writelines(self.test_data_3)
            return f_o

    @pytest.fixture
    def create_empty_file(self):
        """
        Function creates empty file ('txt')
        :return: file object
        """
        test_second_file_path = os.path.join(os.getcwd(), "file2.txt")
        with open(test_second_file_path, "w") as f_o:
            f_o.writelines(self.test_data_4)
            return f_o

    def test_merge_2_files_data(self, create_first_file, create_second_file):
        """Testing that function merges file's with the same number of the lines of the
        data, merges that in list and returns that"""
        assert merge_sorted_files(
            [create_first_file.name, create_second_file.name]
        ) == ["1", "2", "3", "4", "5", "6"]
        os.remove(create_first_file.name)
        os.remove(create_second_file.name)

    def test_merge_2_files_data_not_equal_count_line(
        self, create_first_file, create_file_with_little_data
    ):
        """Testing that function merges file's with different number of the lines of the
        data, merges that in list and returns that"""
        assert merge_sorted_files(
            [create_first_file.name, create_file_with_little_data.name]
        ) == ["1", "2", "3", "5"]
        os.remove(create_first_file.name)
        os.remove(create_file_with_little_data.name)

    def test_merge_2_empty_files(self, create_empty_file):
        """Testing that function returns [], if both files have no any data"""
        assert (
            merge_sorted_files([create_empty_file.name, create_empty_file.name]) == []
        )

    def test_wrong_file(self):
        """Testing that function raises FileNotFoundError error, if one of the file (or both)
        doesn't exist
        """
        with pytest.raises(FileNotFoundError) as e:
            merge_sorted_files(["file4.txt", "file2.txt"])
            msg_error = e.value.args[0]
            assert msg_error == "[Errno 2] No such file or directory: 'file4.txt'"
