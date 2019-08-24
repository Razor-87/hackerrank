# -*- coding: utf-8 -*-
import numpy
from typing import List


def linear_algebra(lst: List[List[str]]) -> float:
    """
    >>> linear_algebra([['1.1', '1.1'], ['1.1', '1.1']])
    0.0
    >>> linear_algebra([['1.1', '1.1'], ['1.1', '1.2']])
    0.11
    """
    arr = numpy.array(lst, float)
    determinant = round(numpy.linalg.det(arr), 2)
    return determinant


if __name__ == '__main__':
    lst = [input().split() for _ in range(int(input()))]
    print(linear_algebra(lst))
