# -*- coding: utf-8 -*-
from typing import Tuple


def arithmetic_operators(a: int, b: int) -> Tuple[int, ...]:
    """
    >>> arithmetic_operators(3, 2)
    (5, 1, 6)
    """
    return a + b, a - b, a * b


if __name__ == '__main__':
    a, b = int(input()), int(input())
    print(*arithmetic_operators(a, b), sep='\n')
