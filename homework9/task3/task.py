import os
from pathlib import Path
from typing import Callable, Iterator, Optional


def get_count_lines(file_lst) -> Iterator:
    """
    Count total amount of lines in file
    :param file_lst: list of te files
    :return: generator, line's count
    """
    for file in file_lst:
        with open(file) as f_o:
            yield len(f_o.readlines())


def get_count_tokens(file_lst, tokenizer) -> Iterator:
    """
    Count total amount of tokens in file
    :param file_lst: list of te files
    :param tokenizer: function
    :return: generator, token's count
    """
    for file in file_lst:
        with open(file) as f_o:
            yield len(list(filter(lambda x: tokenizer(x), f_o.readlines())))


def get_file_with_extension(dir_path, file_extension):
    """
    Return list of the files with current extension
    :param dir_path Path, path to the directory
    :param file_extension: str, name of file's extension
    :return: generator, list of te files
    """
    os.chdir(dir_path)
    all_files = os.listdir(dir_path)
    for file in all_files:
        if file.endswith(file_extension):
            yield file


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    """
    Count total amount of lines or total tokens of all files in directory
    :param dir_path: Path, path to the directory
    :param file_extension: str, name of file's extension
    :param tokenizer: optional argument, function (default = None)
    :return: int, count lines(tokens, if tokenizer is not None)
    """
    if not os.path.isdir(dir_path):
        raise NotADirectoryError("It's not a directory")
    count = 0
    files_filter = list(get_file_with_extension(dir_path, file_extension))
    count += (
        sum(get_count_lines(files_filter))
        if tokenizer is None
        else sum(get_count_tokens(files_filter, tokenizer))
    )
    return count
