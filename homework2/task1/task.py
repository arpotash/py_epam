"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import re
import string
from collections import Counter
from itertools import islice
from random import choice
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path, "rb") as f_o:
        lst_count_letters = []
        for line in f_o.readlines():
            words_in_line = line.decode("unicode_escape").split()
            lst_count_letters += words_in_line
        lst_max_distinct_letter = sorted(
            lst_count_letters, reverse=True, key=lambda elem: len(set(elem))
        )
        lst = list(islice(lst_max_distinct_letter, 0, 10))
        return lst


def get_rarest_char(file_path: str) -> str:
    with open(file_path, "rb") as f_o:
        count_symbols = {}
        for line in f_o.readlines():
            words_in_line = line.decode("unicode_escape")
            for symbol in words_in_line:
                if symbol in count_symbols:
                    count_symbols[symbol] += 1
                else:
                    count_symbols[symbol] = 1
        min_value = min(count_symbols.values())
        min_keys = [key for key in count_symbols if count_symbols[key] == min_value]
        return choice(min_keys)


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, "rb") as f_o:
        count = 0
        for line in f_o.readlines():
            words_in_line = line.decode("unicode_escape")
            for symbol in words_in_line:
                count += 1 if symbol in string.punctuation else 0
        return count


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, "r") as f_o:
        result_lst = []
        text_pattern = r"\\u\d{2}\w{2}"
        for line in f_o.readlines():
            res = re.findall(text_pattern, line)
            result_lst += res
        return len(result_lst)


def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file_path, "r") as f_o:
        result_lst = []
        text_pattern = r"\\u\d{2}\w{2}"
        for line in f_o.readlines():
            res = re.findall(text_pattern, line)
            result_lst += res
            cnt = Counter(result_lst)
        max_value = max(cnt.values())
        max_key = "".join([key for key in cnt if cnt[key] == max_value])
        return max_key
