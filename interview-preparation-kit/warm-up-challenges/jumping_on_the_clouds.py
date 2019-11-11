# -*- coding: utf-8 -*-
from typing import List


def jumping_on_clouds(arr_size: int, arr: List[int]) -> int:
    """
    >>> jumping_on_clouds(7, [0, 0, 1, 0, 0, 1, 0])
    4
    >>> jumping_on_clouds(6, [0, 0, 0, 0, 1, 0])
    3
    >>> jumping_on_clouds(6, [0, 0, 0, 1, 0, 0])
    3
    """
    jump, i = 0, 0
    while i < (arr_size - 1):
        i += 2 if ((arr_size - i) > 2) and (arr[i + 2] == 0) else 1
        jump += 1
    return jump
