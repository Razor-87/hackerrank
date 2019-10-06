# -*- coding: utf-8 -*-
from typing import List


def iterables_and_iterators(n: int, arr: List[str], k: int) -> float:
    """
    >>> iterables_and_iterators(4, ['a', 'a', 'c', 'd'], 2)
    0.833333333333
    >>> iterables_and_iterators(9,
    ... ['a', 'b', 'c', 'a', 'd', 'b', 'z', 'e', 'o'], 4)
    0.722222222222
    """
    from itertools import permutations
    from math import factorial
    ret = sum('a' in p for p in permutations(arr, k))
    return round(ret / (factorial(n) // factorial(n - k)), 12)


if __name__ == '__main__':
    n, arr, k = int(input()), input().split(), int(input())
    print(iterables_and_iterators(n, arr, k))
