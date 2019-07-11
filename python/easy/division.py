# -*- coding: utf-8 -*-
from typing import Tuple


def division(a: int, b: int) -> Tuple[int, float]:
    """
    >>> division(4, 3)
    (1, 1.3333333333333333)
    """
    return a // b, a / b


if __name__ == '__main__':
    a, b = int(input()), int(input())
    print(*division(a, b), sep='\n')
