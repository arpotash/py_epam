"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.
You may assume that the array is non-empty and the most common element
always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3, 2
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2, 1
"""
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    sorted_lst = sorted(inp, key=lambda elem: inp.count(elem))
    max_value = sorted_lst[-1]
    if len(set(sorted_lst)) == 1:
        min_value = None
    else:
        min_value = sorted_lst[0]
    return max_value, min_value
