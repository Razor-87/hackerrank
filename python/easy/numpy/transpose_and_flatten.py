# -*- coding: utf-8 -*-
import numpy
from typing import List, Tuple


def transpose_and_flatten(lst: List[List[str]]) -> Tuple[numpy.ndarray, ...]:
    """
    >>> transpose_and_flatten([['1', '2'], ['3', '4']])
    (array([[1, 3],
           [2, 4]]), array([1, 2, 3, 4]))
    """
    arr = numpy.array(lst, int)
    transpose, flatten = arr.transpose(), arr.flatten()
    return transpose, flatten


if __name__ == '__main__':
    lst = [input().split() for _ in range((*map(int, input().split()),)[0])]
    print(*transpose_and_flatten(lst), sep='\n')
