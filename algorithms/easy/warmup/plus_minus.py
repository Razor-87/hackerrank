# -*- coding: utf-8 -*-
from typing import List, Tuple


def plus_minus(arr: List[int]) -> Tuple[float, ...]:
    """
    >>> plus_minus([0, 0, -1, 1, 1])
    (0.4, 0.2, 0.4)
    """
    len_arr = len(arr)
    # positive, negative, zeros = 0, 0, 0
    # for i in arr:
    #     if i > 0:
    #         positive += 1
    #     elif i < 0:
    #         negative += 1
    #     else:
    #         zeros += 1
    positive = len([x for x in arr if x > 0])
    negative = len([x for x in arr if x < 0])
    zeros = len([x for x in arr if x == 0])
    return (positive / len_arr,
            negative / len_arr,
            zeros / len_arr)


if __name__ == '__main__':
    import sys
    _, *arr = map(int, sys.stdin.read().split())
    print(*plus_minus(arr), sep='\n')
