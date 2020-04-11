# -*- coding: utf-8 -*-


def kangaroo(x1: int, v1: int, x2: int, v2: int) -> str:
    """
    >>> kangaroo(0, 2, 5, 3)
    'NO'
    >>> kangaroo(0, 3, 4, 2)
    'YES'
    >>> kangaroo(14, 4, 98, 2)
    'YES'
    >>> kangaroo(21, 6, 47, 3)
    'NO'
    """
    # if v1 > v2:
    #     i = 0
    #     while i <= x2:
    #         i += 1
    #         if (x1 + v1 * i) == (x2 + v2 * i):
    #             return 'YES'
    # return 'NO'
    ret = 'YES' if (v1 > v2) and (not (x2 - x1) % (v2 - v1)) else 'NO'
    return ret
