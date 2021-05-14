import sys


def my_precious_logger(text: str):
    sys_stderr = sys.stderr
    sys_stdout = sys.stdout
    sys_stderr.write(text) if text.startswith("error") else sys_stdout.write(text)
