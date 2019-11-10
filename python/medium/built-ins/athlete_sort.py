# -*- coding: utf-8 -*-
from typing import List


def athlete_sort(k: int, arr: List[List[int]]) -> List[List[int]]:
    """
    >>> athlete_sort(1, [[10, 2, 5], [7, 1, 0], [9, 9, 9],
    ... [1, 23, 12], [6, 5, 9]])
    [[7, 1, 0], [10, 2, 5], [6, 5, 9], [9, 9, 9], [1, 23, 12]]
    """
    arr.sort(key=lambda x: x[k])
    return arr
