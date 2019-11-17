# -*- coding: utf-8 -*-
from typing import List


def rot_left(arr: List[int], d: int) -> List[int]:
    """
    >>> rot_left([1, 2, 3, 4, 5], 4)
    [5, 1, 2, 3, 4]
    """
    from collections import deque
    ret = deque(arr)
    ret.rotate(-d)
    return [*ret]  # arr[d:] + arr[:d]
