# -*- coding: utf-8 -*-
import numpy
from typing import Tuple


def zeros_and_ones(shapes: Tuple[int, ...]) -> Tuple[numpy.ndarray, ...]:
    """
    >>> zeros_and_ones((3, 3, 3))
    (array([[[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]],
    <BLANKLINE>
           [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]],
    <BLANKLINE>
           [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]]), array([[[1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]],
    <BLANKLINE>
           [[1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]],
    <BLANKLINE>
           [[1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]]]))
    """
    zeros, ones = numpy.zeros(shapes, int), numpy.ones(shapes, int)
    return zeros, ones


if __name__ == '__main__':
    shapes = tuple(map(int, input().split()))
    print('{}\n{}'.format(*zeros_and_ones(shapes)))
