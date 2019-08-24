# -*- coding: utf-8 -*-
import numpy
numpy.set_printoptions(legacy='1.13')


def eye_and_identity(n: int, m: int) -> numpy.ndarray:
    """
    >>> eye_and_identity(3, 3)
    array([[ 1.,  0.,  0.],
           [ 0.,  1.,  0.],
           [ 0.,  0.,  1.]])
    """
    matrix = numpy.eye(n, m,)
    return matrix


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(eye_and_identity(n, m))
