# -*- coding: utf-8 -*-
from typing import Tuple


def zipped(arr: Tuple[Tuple[float, ...], ...]) -> Tuple[float, ...]:
    """
    >>> zipped(((89.0, 90.0, 78.0, 93.0, 80.0), (90.0, 91.0, 85.0, 88.0, 86.0),
    ... (91.0, 92.0, 83.0, 89.0, 90.5)))
    (90.0, 91.0, 82.0, 90.0, 85.5)
    """
    arr_zipped = zip(*arr)
    return tuple(sum(el) / len(el) for el in arr_zipped)


if __name__ == '__main__':
    import sys
    arr = tuple(tuple(map(float, lst))
                for lst in map(str.split, map(str.strip,
                                              sys.stdin.readlines()[1:])))
    print(*zipped(arr), sep='\n')
