# -*- coding: utf-8 -*-
from typing import List, Tuple


def plus_minus(arr: List[int]) -> Tuple[float, ...]:
    """
    >>> plus_minus([0, 0, -1, 1, 1])
    (0.4, 0.2, 0.4)
    """
    # positive, negative, zeros = 0, 0, 0
    # for i in arr:
    #     if i > 0:
    #         positive += 1
    #     elif i < 0:
    #         negative += 1
    #     else:
    #         zeros += 1
    len_arr = len(arr)
    positive = sum(x > 0 for x in arr)
    negative = sum(x < 0 for x in arr)
    zeros = len_arr - (positive + negative)
    ret = (positive / len_arr, negative / len_arr, zeros / len_arr)
    return ret


if __name__ == '__main__':
    _, arr = input(), [*map(int, input().split())]
    print(*plus_minus(arr), sep='\n')
