# -*- coding: utf-8 -*-
from fractions import Fraction
from functools import reduce
from typing import List, Tuple


def product(fracs: List[Fraction]) -> Tuple[int, int]:
    """
    >>> product([Fraction(1, 2), Fraction(3, 4), Fraction(5, 3)])
    (5, 8)
    """
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator
