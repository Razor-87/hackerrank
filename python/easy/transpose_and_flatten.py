# -*- coding: utf-8 -*-
import numpy
from typing import List, Tuple


def transpose_and_flatten(lst: List[Tuple[int, ...]]
                          ) -> Tuple[numpy.ndarray, ...]:
    """
    >>> transpose_and_flatten([(1, 2), (3, 4)])
    (array([[1, 3],
           [2, 4]]), array([1, 2, 3, 4]))
    """
    arr = numpy.array(lst, int)
    return arr.transpose(), arr.flatten()


if __name__ == '__main__':
    import sys
    lst = [tuple(map(int, el.split())) for el in map(str.strip,
                                                     sys.stdin.readlines()[1:])]
    print(*transpose_and_flatten(lst), sep='\n')
