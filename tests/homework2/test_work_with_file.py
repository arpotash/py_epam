import os

import pytest

from homework2.task1 import task


class TestWorkWithFile:

    @pytest.fixture
    def create_file(self, tmp_path):
        file_path = os.path.join(tmp_path, 'test_file.txt')
        u_e_word = r"\u00bb"
        u_e_word1 = r"\u00ab"
        test_data = "Jetzt-\nderisqse hier"
        with open(file_path, "w") as f_o:
            f_o.writelines(f"{u_e_word}{test_data}{u_e_word1}")
            return file_path

    def test_is_exist_file(self, create_file):
        assert os.path.isfile(create_file)

    def test_find_10_longest_unique_words(self, create_file):
        assert task.get_longest_diverse_words(create_file) == [
            "Jetztderisqse",
            "hier",
        ]

    def test_find_rarest_symbol(self, create_file):
        assert task.get_rarest_char(create_file) == "»"

    def test_calculate_count_punctuation(self, create_file):
        assert task.count_punctuation_chars(create_file) == 3

    def test_calculate_count_symbols_unicode_escape(self, create_file):
        assert task.count_non_ascii_chars(create_file) == 2

    def test_find_common_symbols_unicode_escape(self, create_file):
        assert task.get_most_common_non_ascii_char(create_file) == "»"
