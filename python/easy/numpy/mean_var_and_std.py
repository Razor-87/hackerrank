# -*- coding: utf-8 -*-
import numpy
from typing import List, Tuple
numpy.set_printoptions(legacy='1.13')


def mean_var_and_std(lst: List[List[str]]
                     ) -> Tuple[numpy.ndarray, numpy.ndarray, float]:
    """
    >>> mean_var_and_std([['1', '2'], ['3', '4']])
    (array([ 1.5,  3.5]), array([ 1.,  1.]), 1.1180339887498949)
    """
    arr = numpy.array(lst, int)
    mean, var, std = numpy.mean(arr, axis=1), numpy.var(arr,
                                                        axis=0), numpy.std(arr)
    return mean, var, std


if __name__ == '__main__':
    lst = [input().split() for _ in range((*map(int, input().split()),)[0])]
    print(*mean_var_and_std(lst), sep='\n')
