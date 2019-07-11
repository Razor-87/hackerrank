# -*- coding: utf-8 -*-
from typing import List, Tuple


def check_subest(raw_arr: List[str]) -> Tuple[bool, ...]:
    """
    >>> check_subest(
    ... ['1 2 3 5 6\\n', '9 8 5 6 3 2 1 4 7\\n', '2\\n', '3 6 5 4 1\\n',
    ... '1 2 3 5 6 8 9\\n', '9 8 2'])
    (True, False, False)
    """
    arr = [set(el.split()) for el in map(str.strip, raw_arr)]
    sets = zip(arr[::2], arr[1::2])
    return tuple(el[0] < el[1] for el in sets)


if __name__ == '__main__':
    import sys
    raw_arr = sys.stdin.readlines()[2::2]
    print(*check_subest(raw_arr), sep='\n')
