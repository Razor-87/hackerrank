# -*- coding: utf-8 -*-
from typing import List


def find_the_runner_up_score(arr: List[int]) -> int:
    """
    >>> find_the_runner_up_score([2, 3, 6, 6, 5])
    5
    """
    return sorted(set(arr))[-2]


if __name__ == '__main__':
    import sys
    _, *arr = map(int, sys.stdin.read().split())
    print(find_the_runner_up_score(arr))
