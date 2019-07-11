# -*- coding: UTF-8 -*-
from typing import Iterator, List


def fib(n: int) -> Iterator[int]:
    """
    >>> tuple(fib(5))
    (0, 1, 1, 2, 3)
    """
    x, y = 0, 1
    while n:
        yield x
        x, y = y, x + y
        n -= 1


def fib_cube(n: int) -> List[int]:
    """
    >>> fib_cube(5)
    [0, 1, 1, 8, 27]
    >>> fib_cube(7)
    [0, 1, 1, 8, 27, 125, 512]
    """
    # return list(map(lambda x: x**3, fib(n)))
    return [x**3 for x in fib(n)]


if __name__ == '__main__':
    n = int(input())
    print(fib_cube(n))
