# -*- coding: utf-8 -*-
from typing import List


def average(arr: List[int]) -> float:
    """
    >>> average([161, 182, 161, 154, 176, 170, 167, 171, 170, 174])
    169.375
    """
    arr_set = set(arr)
    return sum(arr_set) / len(arr_set)
