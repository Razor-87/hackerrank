# -*- coding: utf-8 -*-
from typing import List


def min_and_max(lst: List[List[str]]) -> int:
    """
    >>> min_and_max([['2', '5'], ['3', '7'], ['1', '3'], ['4', '0']])
    3
    """
    max_of_mins = max(min(map(int, el)) for el in lst)
    return max_of_mins


if __name__ == '__main__':
    lst = [input().split() for _ in range((*map(int, input().split()),)[0])]
    print(min_and_max(lst))
