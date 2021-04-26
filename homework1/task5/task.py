"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    length = len(nums)
    result = 0
    for num in range(length):
        lst = []
        for update_start_num in range(num, length):
            if len(lst) == k:
                break
            lst.append(nums[update_start_num])
        result = max(result, sum(lst))
    return result
