# -*- coding: utf-8 -*-
from typing import Iterable, Tuple


def piling_up(arr: Iterable) -> Tuple[str, ...]:
    """
    >>> piling_up(((4, 3, 2, 1, 3, 4), (1, 3, 2)))
    ('Yes', 'No')
    """
    ret = (*(('Yes' if (sum((el[j] - el[j + 1])
                        for j in range(len(el) // 2)) >= 0) or
                       ((len(el) <= 3) and ((el[0] >= el[1]) or
                        (el[-1] >= el[-2]))) else 'No')
             for el in arr),)
    return ret


if __name__ == '__main__':
    import sys
    arr = (tuple(map(int, row.split()))
           for row in map(str.strip, sys.stdin.readlines()[2::2]))
    print(*piling_up(arr), sep='\n')
