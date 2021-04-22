"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    d_sum = {}
    for i in a:
        for j in b:
            if i + j not in d_sum:
                d_sum[i + j] = 1
            else:
                d_sum[i + j] += 1
    count = 0
    for i in c:
        for j in d:
            second_half_sum = -1 * (i + j)
            if second_half_sum in d_sum:
                count += d_sum[second_half_sum]
    return count
