# -*- coding: utf-8 -*-
from typing import Tuple


def polar_coordinates(raw_str: str) -> Tuple[str, ...]:
    """
    >>> polar_coordinates('1+2j')
    ('2.236', '1.107')
    >>> polar_coordinates('-1-5j')
    ('5.099', '-1.768')
    """
    import cmath
    return tuple(f'{el:.3f}' for el in cmath.polar(complex(raw_str)))


if __name__ == '__main__':
    import sys
    raw_str = sys.stdin.readline()
    print(*polar_coordinates(raw_str), sep='\n')
