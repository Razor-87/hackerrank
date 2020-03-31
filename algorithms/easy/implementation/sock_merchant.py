# -*- coding: utf-8 -*-
from typing import Iterable


def sock_merchant(arr: Iterable[int]) -> int:
    """
    >>> sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20])
    3
    >>> sock_merchant([6, 5, 2, 3, 5, 2, 2, 1, 1, 5, 1, 3, 3, 3, 5])
    6
    """
    from collections import Counter
    count = Counter(arr).values()
    ret = sum(n // 2 for n in count)
    return ret
