# -*- coding: utf-8 -*-
from typing import Tuple


def tuples_hash(t: Tuple[int, ...]) -> int:
    """
    >>> tuples_hash((1, 2))
    3713081631934410656
    """
    return hash(t)


if __name__ == '__main__':
    import sys
    _, integer_list = (sys.stdin.readline(),
                       tuple(map(int,
                                 sys.stdin.readline().split())))
    print(tuples_hash(integer_list))
