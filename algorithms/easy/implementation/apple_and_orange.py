# -*- coding: utf-8 -*-
from typing import List, Tuple


def count_apples_and_oranges(s: int, t: int, a: int, b: int,
                             apples: List[int],
                             oranges: List[int]) -> Tuple[int, int]:
    """
    >>> count_apples_and_oranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])
    (1, 1)
    """
    count_apples = sum((s <= (a + apple) <= t) for apple in apples)
    count_oranges = sum((s <= (b + orange) <= t) for orange in oranges)
    return count_apples, count_oranges
