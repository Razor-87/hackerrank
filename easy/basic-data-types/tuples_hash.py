# -*- coding: utf-8 -*-
from typing import Tuple


def tuples_hash(t: Tuple[int, ...]) -> int:
    """
    >>> tuples_hash((1, 2))
    3713081631934410656
    """
    return hash(t)


if __name__ == '__main__':
    _, integer_list = input(), tuple(map(int, input().split()))
    print(tuples_hash(integer_list))
