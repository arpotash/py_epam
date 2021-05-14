import os


def check_exist_file(path: str) -> bool:
    if not os.path.exists(path):
        raise ValueError("No such file")
    return os.path.exists(path)


def read_magic_number(path: str) -> bool:
    if check_exist_file(path):
        with open(path) as f_o:
            first_line = f_o.readline().split("\n")[0]
            return True if first_line.isdigit() and first_line in ["1", "2"] else False
