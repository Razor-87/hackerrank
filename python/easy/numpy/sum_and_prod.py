# -*- coding: utf-8 -*-
import numpy
from typing import List


def sum_and_prod(lst: List[List[str]]) -> int:
    """
    >>> sum_and_prod([['1', '2'], ['3', '4']])
    24
    """
    arr = numpy.array(lst, int)
    sum_arr = numpy.sum(arr, axis=0)
    product = numpy.prod(sum_arr)
    return product


if __name__ == '__main__':
    lst = [input().split() for _ in range((*map(int, input().split()),)[0])]
    print(sum_and_prod(lst))
