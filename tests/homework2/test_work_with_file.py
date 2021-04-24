import pytest

from homework2.task1.task import get_longest_diverse_words, get_rarest_char, count_non_ascii_chars, \
    get_most_common_non_ascii_char, count_punctuation_chars


class TestWorkWithFile:

    @pytest.fixture
    def create_file(self):
        u_e_word = r"\u00bb"
        u_e_word1 = r"\u00ab"
        test_data = "Jetzt hier"
        with open("test_file.txt", "w") as f_o:
            f_o.writelines(f'{u_e_word}{test_data}{u_e_word1}')
            return f_o

    def test_is_exist_file(self, create_file):
        assert create_file.name == "test_file.txt"

    def test_find_10_longest_unique_words(self, create_file):
        assert get_longest_diverse_words(create_file.name) == ['Jetzt', 'hier']

    def test_find_rarest_symbol(self, create_file):
        assert get_rarest_char(create_file.name) == '»'

    def test_calculate_count_punctuation(self, create_file):
        assert count_punctuation_chars(create_file.name) == 2

    def test_calculate_count_symbols_unicode_escape(self, create_file):
        assert count_non_ascii_chars(create_file.name) == 2

    def test_find_common_symbols_unicode_escape(self, create_file):
        assert get_most_common_non_ascii_char(create_file.name) == "»"
