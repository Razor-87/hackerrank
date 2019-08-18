# -*- coding: utf-8 -*-
import numpy
from typing import List, Tuple


def inner_and_outer(a: List[str], b: List[str]) -> Tuple[numpy.ndarray, ...]:
    """
    >>> inner_and_outer(['0', '1'], ['2', '3'])
    (3, array([[0, 0],
           [2, 3]]))
    """
    arr_a, arr_b = numpy.array(a, int), numpy.array(b, int)
    inner, outer = numpy.inner(arr_a, arr_b), numpy.outer(arr_a, arr_b)
    return inner, outer


if __name__ == '__main__':
    a, b = (input().split() for _ in range(2))
    print(*inner_and_outer(a, b), sep='\n')
