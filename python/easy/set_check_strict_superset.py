# -*- coding: utf-8 -*-
from typing import List


def check_strict_superset(raw_str: str, raw_arr: List[str]) -> bool:
    """
    >>> check_strict_superset('1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78',
    ... ['1 2 3 4 5\\n', '100 11 12'])
    False
    """
    superset = set(raw_str.split())
    sets = (set(el.split()) for el in map(str.strip, raw_arr))
    return all(superset > el for el in sets)


if __name__ == '__main__':
    import sys
    raw_str, raw_arr = sys.stdin.readline(), sys.stdin.readlines()[1:]
    print(check_strict_superset(raw_str, raw_arr))
