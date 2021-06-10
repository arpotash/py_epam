import os
from pathlib import Path

import pytest

from homework9.task3.task import universal_file_counter


class TestUniversalFileCounter:
    test_dir = Path(__file__).parents[0]

    def test_count_line_without_tokenizer(self):
        """Testing that function counts total amount of lines of all files in directory with
        current extension without tokenizer"""
        assert universal_file_counter(self.test_dir, "txt") == 6

    def test_count_line_with_tokenizer(self):
        """Testing that function counts total amount of tokens of all files in directory with
        current extension with tokenizer"""
        assert universal_file_counter(self.test_dir, "txt", str.split) == 6

    def test_count_line_0_files_with_current_extension(self):
        """Testing that function returns 0 when number of files with current extension equal 0"""
        assert universal_file_counter(self.test_dir, "img") == 0

    def test_count_line_not_a_directory(self):
        """Testing that function returns NotADirectoryError,
        when the first argument is not a directory"""
        with pytest.raises(NotADirectoryError) as e:
            universal_file_counter("file4.txt", "txt")
        msg_err = e.value.args[0]
        assert msg_err == "It's not a directory"
