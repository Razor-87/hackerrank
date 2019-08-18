# -*- coding: utf-8 -*-
import numpy
from typing import List


def arrays(arr: List[str]) -> numpy.ndarray:
    """
    >>> arrays(['1', '2', '3', '4', '-8', '-10'])
    array([-10.,  -8.,   4.,   3.,   2.,   1.])
    """
    arr.reverse()
    return numpy.array(arr, float)
