# -*- coding: utf-8 -*-
from typing import List


def loops(n: int) -> List[int]:
    """
    >>> loops(5)
    [0, 1, 4, 9, 16]
    """
    return [x**2 for x in range(n)]


if __name__ == '__main__':
    n = int(input())
    print(*loops(n), sep='\n')
