import os


def check_exist_file(path: str) -> bool:
    if not os.path.exists(path):
        raise FileNotFoundError("No such file")
    return os.path.exists(path)


def read_magic_number(path: str) -> bool:
    if check_exist_file(path):
        with open(path) as f_o:
            first_line = f_o.readline().split("\n")[0]
            if first_line.isdigit():
                first_line = int(first_line)
            else:
                raise ValueError("element should be integer")
            return True if first_line in [1, 2] else False
