# -*- coding: utf-8 -*-
from typing import Tuple


def exceptions(arr: Tuple[str, ...]) -> None:
    """
    >>> exceptions(('1 0', '2 $', '3 1'))
    Error Code: integer division or modulo by zero
    Error Code: invalid literal for int() with base 10: '$'
    3
    """
    for el in arr:
        a, b = el.split()
        try:
            print(int(a) // int(b))
        except (ValueError, ZeroDivisionError) as err:
            print('Error Code:', err)


if __name__ == '__main__':
    arr = tuple(input() for _ in range(int(input())))
    exceptions(arr)
