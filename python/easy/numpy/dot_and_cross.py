# -*- coding: utf-8 -*-
import numpy
from typing import List
numpy.set_printoptions(legacy='1.13')


def dot_and_cross(a: List[List[str]], b: List[List[str]]) -> numpy.ndarray:
    """
    >>> dot_and_cross([['1', '2'], ['3', '4']], [['1', '2'], ['3', '4']])
    array([[ 7, 10],
           [15, 22]])
    """
    arr_a, arr_b = numpy.array(a, int), numpy.array(b, int)
    matrix_dot = arr_a @ arr_b  # numpy.dot(arr_a, arr_b)
    return matrix_dot


if __name__ == '__main__':
    n = int(input())
    a = [input().split() for _ in range(n)]
    b = [input().split() for _ in range(n)]
    print(dot_and_cross(a, b))
