# -*- coding: utf-8 -*-
from typing import List, Tuple


def min_max_sum(arr: List[int]) -> Tuple[int, int]:
    """
    >>> min_max_sum([1, 2, 3, 4, 5])
    (10, 14)
    """
    # arr.sort()
    # min_sum, max_sum = sum(arr[:-1]), sum(arr[1:])
    sum_arr = sum(arr)
    min_sum, max_sum = sum_arr - max(arr), sum_arr - min(arr)
    return min_sum, max_sum


if __name__ == '__main__':
    arr = [*map(int, input().split())]
    print(*min_max_sum(arr))
