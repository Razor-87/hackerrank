# -*- coding: utf-8 -*-
from typing import Iterator, Set


def no_idea(n: Iterator[int], a: Set[int], b: Set[int]) -> int:
    """
    >>> no_idea((1, 5, 3), (3, 1), (5, 7))
    1
    >>> no_idea((1, 2, 3, 4, 5), (1, 3, 5, 7, 9), (2, 4, 6, 8, 10))
    1
    """
    # return sum(bool({i} & a) - bool({i} & b) for i in n)
    arr = ((i in a) - (i in b) for i in n)
    return sum(arr)


if __name__ == '__main__':
    _, n, m = (input(), map(int, input().split()),
               ({*map(int, input().split())} for _ in range(2)))
    print(no_idea(n, *m))
