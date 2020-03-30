# -*- coding: utf-8 -*-
from typing import List


def simple_array_sum(arr: List[int]) -> int:
    """
    >>> simple_array_sum([1, 2, 3, 4, 10, 11])
    31
    >>> simple_array_sum([5])
    5
    """
    ret = sum(arr)
    return ret


if __name__ == '__main__':
    _, arr = input(), [*map(int, input().split())]
    print(simple_array_sum(arr))
