# -*- coding: utf-8 -*-
from typing import Tuple


def compress_the_string(n: str) -> Tuple[Tuple[int, int], ...]:
    """
    >>> compress_the_string('1222311')
    ((1, 1), (3, 2), (1, 3), (2, 1))
    """
    from itertools import groupby
    ret = (*((len((*g,)), int(k)) for k, g in groupby(n)),)
    return ret


if __name__ == '__main__':
    print(*compress_the_string(input()))
