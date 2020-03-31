# -*- coding: utf-8 -*-
# https://www.hackerrank.com/challenges/minimum-swaps-2/problem
from typing import List


def minimum_swaps(arr: List[int], n: int) -> int:
    """
    >>> minimum_swaps([4, 3, 1, 2], 4)
    3
    >>> minimum_swaps([1, 3, 5, 2, 4, 6, 7], 7)
    3
    """
    count = i = 0
    while i < n:
        if arr[i] != i + 1:
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
            count += 1
        else:
            i += 1
    return count
