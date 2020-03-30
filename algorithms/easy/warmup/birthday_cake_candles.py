# -*- coding: utf-8 -*-
from typing import List


def birthday_cake_candles(arr: List[int]) -> int:
    """
    >>> birthday_cake_candles([3, 2, 1, 3])
    2
    """
    max_height = max(arr)
    ret = arr.count(max_height)
    return ret


if __name__ == '__main__':
    _, arr = input(), [*map(int, input().split())]
    print(birthday_cake_candles(arr))
