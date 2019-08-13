# -*- coding: UTF-8 -*-
from typing import Iterator, List


def fibonacci(n: int) -> Iterator[int]:
    """
    >>> tuple(fibonacci(5))
    (0, 1, 1, 2, 3)
    """
    x, y = 0, 1
    while n:
        yield x
        x, y = y, x + y
        n -= 1


# cube = lambda x: x**3


def fibonacci_cube(n: int) -> List[int]:
    """
    >>> fibonacci_cube(5)
    [0, 1, 1, 8, 27]
    >>> fibonacci_cube(7)
    [0, 1, 1, 8, 27, 125, 512]
    """
    return [x**3 for x in fibonacci(n)]
