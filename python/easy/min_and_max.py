# -*- coding: utf-8 -*-
from typing import List


def min_and_max(inp: List[str]) -> int:
    """
    >>> min_and_max(["4 2", "2 5", "3 7", "1 3", "4 0"])
    3
    """
    mins_list = [min(map(int, tuple(s.split()))) for s in inp]
    return max(mins_list)


if __name__ == '__main__':
    import sys
    inp = sys.stdin.readlines()[1:]
    print(min_and_max(inp))
