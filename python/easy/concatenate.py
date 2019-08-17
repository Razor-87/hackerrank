# -*- coding: utf-8 -*-
import numpy
from typing import List


def concatenate(a: List[List[str]], b: List[List[str]]) -> numpy.ndarray:
    """
    >>> concatenate([['1', '2'], ['1', '2'], ['1', '2'], ['1', '2']],
    ... [['3', '4'], ['3', '4'], ['3', '4']])
    array([[1, 2],
           [1, 2],
           [1, 2],
           [1, 2],
           [3, 4],
           [3, 4],
           [3, 4]])
    """
    arr_a, arr_b = numpy.array(a, int), numpy.array(b, int)
    return numpy.concatenate((arr_a, arr_b), axis=0)


if __name__ == '__main__':
    n, m, _ = map(int, input().split())
    a = [input().split() for _ in range(n)]
    b = [input().split() for _ in range(m)]
    print(concatenate(a, b))
