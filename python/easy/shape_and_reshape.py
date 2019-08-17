# -*- coding: utf-8 -*-
import numpy
from typing import List


def shape_and_reshape(lst: List[str]) -> numpy.ndarray:
    """
    >>> shape_and_reshape(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])
    """
    arr = numpy.array(lst, int)
    return numpy.reshape(arr, (3, 3))


if __name__ == '__main__':
    lst = input().split()
    print(shape_and_reshape(lst))
