# -*- coding: utf-8 -*-
from typing import List


def hourglass_sum(arrs: List[List[int]]) -> int:
    """
    >>> hourglass_sum([[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0],
    ... [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0],
    ... [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]])
    19
    """
    from itertools import islice
    inner_arrs = (arr[1:-1] for arr in arrs[1:-1])
    outer_arrs = [[
        sum(islice(arr, start, end)) for start, end in enumerate(range(3, 7))
    ] for arr in arrs]
    sum_outer_arrs = (map(sum, zip(*islice(outer_arrs, i, i + 3, 2)))
                      for i in range(4))
    ret = max(
        max(map(sum, zip(*arr))) for arr in zip(inner_arrs, sum_outer_arrs))
    return ret  # type: ignore
