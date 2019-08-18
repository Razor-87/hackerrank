# -*- coding: utf-8 -*-
import numpy
from typing import List, Tuple
numpy.set_printoptions(sign=' ')


def floor_ceil_rint(lst: List[str]) -> Tuple[numpy.ndarray, ...]:
    """
    >>> floor_ceil_rint(['1.1', '2.2', '3.3', '4.4', '5.5', '6.6',
    ... '7.7', '8.8', '9.9']) #doctest: +NORMALIZE_WHITESPACE
    (array([ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.]),
     array([  2.,   3.,   4.,   5.,   6.,   7.,   8.,   9.,  10.]),
     array([  1.,   2.,   3.,   4.,   6.,   7.,   8.,   9.,  10.]))
    """
    arr = numpy.array(lst, float)
    floor, ceil, rint = numpy.floor(arr), numpy.ceil(arr), numpy.rint(arr)
    return floor, ceil, rint


if __name__ == '__main__':
    lst = input().split()
    print('{}\n{}\n{}'.format(*floor_ceil_rint(lst)))
