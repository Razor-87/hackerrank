# -*- coding: utf-8 -*-
from typing import List


def set_union(arr_1: List[str], arr_2: List[str]) -> int:
    """
    >>> set_union(['1', '2', '3', '4', '5', '6', '7', '8', '9'],
    ... ['10', '1', '2', '3', '11', '21', '55', '6', '8'])
    13
    """
    return len(set(arr_1) | set(arr_2))


def set_intersection(arr_1: List[str], arr_2: List[str]) -> int:
    """
    >>> set_intersection(['1', '2', '3', '4', '5', '6', '7', '8', '9'],
    ... ['10', '1', '2', '3', '11', '21', '55', '6', '8'])
    5
    """
    return len(set(arr_1) & set(arr_2))


def set_difference(arr_1: List[str], arr_2: List[str]) -> int:
    """
    >>> set_difference(['1', '2', '3', '4', '5', '6', '7', '8', '9'],
    ... ['10', '1', '2', '3', '11', '21', '55', '6', '8'])
    4
    """
    return len(set(arr_1) - set(arr_2))


def set_symmetric_difference(arr_1: List[str], arr_2: List[str]) -> int:
    """
    >>> set_symmetric_difference(['1', '2', '3', '4', '5', '6', '7', '8', '9'],
    ... ['10', '1', '2', '3', '11', '21', '55', '6', '8'])
    8
    """
    return len(set(arr_1) ^ set(arr_2))


def set_symmetric_difference_sort(arr_1: List[str],
                                  arr_2: List[str]) -> List[int]:
    """
    >>> set_symmetric_difference_sort(['2', '4', '5', '9',],
    ... ['2', '4', '11', '12'])
    [5, 9, 11, 12]
    """
    return sorted(map(int, set(arr_1) ^ set(arr_2)))


if __name__ == '__main__':
    import sys
    _, arr_1, _, arr_2 = map(str.split, map(str.strip, sys.stdin.readlines()))
    print(set_union(arr_1, arr_2))
    # print(set_intersection(arr_1, arr_2))
    # print(set_difference(arr_1, arr_2))
    # print(set_symmetric_difference(arr_1, arr_2))
    # print(*set_symmetric_difference(arr_1, arr_2), sep='\n')
