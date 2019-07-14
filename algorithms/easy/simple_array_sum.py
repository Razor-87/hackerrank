# -*- coding: utf-8 -*-
from typing import Tuple


def simple_array_sum(arr: Tuple[int, ...]) -> int:
    """
    >>> simple_array_sum((1, 2, 3, 4, 10, 11))
    31
    >>> simple_array_sum((5,))
    5
    """
    return sum(arr)


if __name__ == '__main__':
    import sys
    _, arr = sys.stdin.readline(), tuple(map(int, sys.stdin.readline().split()))
    print(simple_array_sum(arr))
