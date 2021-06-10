import itertools
from typing import Iterator


def merge_sorted_files(file_list) -> Iterator:
    """
    Function merges file data
    :param file_list: list of files
    :return: list of merged data
    """
    file_1, file_2 = file_list
    with open(file_1) as f1_obj, open(file_2) as f2_obj:
        content_1, content_2 = f1_obj.readlines(), f2_obj.readlines()
        lst_result = list(itertools.zip_longest(content_1, content_2))
    final_lst = [
        line.rstrip()
        for line in itertools.chain.from_iterable(lst_result)
        if line is not None
    ]
    return final_lst
