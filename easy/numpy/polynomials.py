# -*- coding: utf-8 -*-
import numpy
from typing import List


def polynomials(p: List[float], x: int) -> float:
    """
    >>> polynomials([1.1, 2.0, 3.0], 0)
    3.0
    """
    polyval = numpy.polyval(p, x)
    return polyval


if __name__ == '__main__':
    p, x = [*map(float, input().split())], int(input())
    print(polynomials(p, x))
