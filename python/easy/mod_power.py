# -*- coding: utf-8 -*-
from typing import Tuple


def mod_power(a: int, b: int, m: int) -> Tuple[int, ...]:
    """
    >>> mod_power(3, 4, 5)
    (81, 1)
    """
    return pow(a, b), pow(a, b, m)


if __name__ == '__main__':
    a, b, m = (int(input()) for _ in range(3))
    print(*mod_power(a, b, m), sep='\n')
