import itertools
from typing import Any


def subtree_search(tree, element, cnt):
    """
    Function finds element in the nested structures
    of the data and counts the number of matches there

    :param tree: dictionary, where will find element
    :param element: element for finding
    :param cnt: number of the matches, the default is 0
    :return: int number of matches, the default is 0
    """
    for value in itertools.chain(tree.values()):
        if isinstance(value, list) or isinstance(value, set):
            for val in value:
                if isinstance(val, dict):
                    cnt = subtree_search(val, element, cnt)
                cnt += 1 if val == element else 0
        elif isinstance(value, dict):
            cnt = subtree_search(value, element, cnt)
        else:
            cnt += 1 if value == element else 0
    return cnt


def find_occurrences(tree: dict, element: Any, count=0) -> int:
    """
    Function finds element in the dictionary and counts
    the number of matches

    :param tree: dictionary, where will find element
    :param element: element for finding
    :param count: number of the matches, the default is 0
    :return: int number of matches, the default is 0
    """
    sub_trees = {key: value for key, value in tree.items() if isinstance(value, dict)}
    for value in sub_trees.values():
        count += subtree_search(value, element, 0)
    simple_trees = [value for value in tree.values() if not isinstance(value, dict)]
    count += len(list(filter(lambda x: element in x, simple_trees)))
    return count
