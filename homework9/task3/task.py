import os
from pathlib import Path
from typing import Callable, Optional


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
    os.chdir(dir_path)
    all_files = os.listdir(dir_path)
    files_filter = list(filter(lambda x: x.endswith(file_extension), all_files))
    for file in files_filter:
        with open(file) as f_o:
            count += (
                len(f_o.readlines())
                if tokenizer is None
                else len(list(filter(lambda x: tokenizer(x), f_o.readlines())))
            )
    return count
