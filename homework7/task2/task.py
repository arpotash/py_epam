from copy import copy


def check_first_symbol(string):
    """
    Function checks the string for backspace at
    the beginning and cuts this symbol if there is

    :param string: first string for checking
    :return: string
    """
    while string.startswith("#"):
        string = string[1:]
    return string


def check_backspace_symbol(string):
    """
    Function checks the string. If there is a backspace after
    another symbol, symbol should be removed, after that
    all backspaces will be removed too.

    :param string: first string for checking
    :return: string
    """

    string = check_first_symbol(string)
    new_string = copy(string)
    for number, symbol in enumerate(string):
        if symbol == "#" and string[number - 1] != "#":
            new_string = string.replace(string[number - 1], "", 1)
    return new_string.replace("#", "")


def backspace_compare(first: str, second: str):
    """
    Function compare two strings between of them

    :param first: first string for comparison
    :param second: second string for comparison
    :return: boolean value
    """
    first = check_backspace_symbol(first)
    second = check_backspace_symbol(second)
    return first == second
