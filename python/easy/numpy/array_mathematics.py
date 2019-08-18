# -*- coding: utf-8 -*-
import numpy
from typing import List, Tuple


def array_mathematics(a: List[List[str]],
                      b: List[List[str]]) -> Tuple[numpy.ndarray, ...]:
    """
    >>> array_mathematics([['1', '2', '3', '4']],
    ... [['5', '6', '7', '8']]) #doctest: +NORMALIZE_WHITESPACE
    (array([[ 6,  8, 10, 12]]), array([[-4, -4, -4, -4]]),
     array([[ 5, 12, 21, 32]]), array([[0, 0, 0, 0]], dtype=int32),
     array([[1, 2, 3, 4]], dtype=int32),
     array([[    1,    64,  2187, 65536]], dtype=int32))
    """
    arr_a, arr_b = numpy.array(a, int), numpy.array(b, int)
    dict_mathematics = {
        'add': numpy.add(arr_a, arr_b),
        'subtract': numpy.subtract(arr_a, arr_b),
        'multiply': numpy.multiply(arr_a, arr_b),
        'floor_divide': numpy.floor_divide(arr_a, arr_b),
        'mod': numpy.mod(arr_a, arr_b),
        'power': numpy.power(arr_a, arr_b)
    }
    return (*dict_mathematics.values(),)


if __name__ == '__main__':
    n, _ = map(int, input().split())
    a = [input().split() for _ in range(n)]
    b = [input().split() for _ in range(n)]
    print(*array_mathematics(a, b), sep="\n")
