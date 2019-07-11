# -*- coding: utf-8 -*-


def print_function(n: int) -> None:
    """
    >>> print_function(3)
    123
    """
    print(*range(1, n + 1), sep='')


if __name__ == '__main__':
    n = int(input())
    print_function(n)
