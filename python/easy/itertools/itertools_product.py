# -*- coding: utf-8 -*-
from typing import Tuple


def itertools_product(arr_1: Tuple[int, ...],
                      arr_2: Tuple[int, ...]) -> Tuple[Tuple[int, ...], ...]:
    """
    >>> itertools_product((1, 2), (3, 4))
    ((1, 3), (1, 4), (2, 3), (2, 4))
    """
    import itertools
    return tuple(itertools.product(arr_1, arr_2))


if __name__ == '__main__':
    import sys
    arr = (tuple(map(int, lst))
           for lst in map(str.split, sys.stdin.readlines()))
    print(*itertools_product(*arr))
