# -*- coding: utf-8 -*-
from typing import Tuple


def detect_floating_point_number(arr: Tuple[str, ...]) -> None:
    """
    >>> detect_floating_point_number(('4.0O0', '-1.00', '+4.54',
    ... 'SomeRandomStuff'))
    False
    True
    True
    False
    """
    for el in arr:
        try:
            print(bool(float(el)))
        except ValueError:
            print(False)


if __name__ == '__main__':
    arr = tuple(input() for _ in range(int(input())))
    detect_floating_point_number(arr)
