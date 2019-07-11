# -*- coding: utf-8 -*-


def if_else(n: int) -> str:
    """
    >>> if_else(3)
    'Weird'
    >>> if_else(24)
    'Not Weird'
    """
    if n % 2 or 6 <= n <= 20:
        return 'Weird'
    return 'Not Weird'


if __name__ == '__main__':
    n = int(input())
    print(if_else(n))
