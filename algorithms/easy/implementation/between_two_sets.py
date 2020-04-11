# -*- coding: utf-8 -*-
from typing import List


def get_total_x(a: List[int], b: List[int]) -> int:
    """
    >>> get_total_x([2, 4], [16, 32, 96])
    3
    """
    a_max, b_min, ret = max(a), min(b), 0
    for i in range(a_max, b_min + 1):
        a_factor = all(i % a_num == 0 for a_num in a)
        b_factor = all(b_num % i == 0 for b_num in b)
        ret += a_factor and b_factor
    return ret
