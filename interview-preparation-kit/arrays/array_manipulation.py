# -*- coding: utf-8 -*-
from typing import List


def array_manipulation(n: int, queries: List[List[int]]) -> int:
    """
    >>> array_manipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]])
    200
    >>> array_manipulation(4, [[2, 3, 603], [1, 1, 286], [4, 4, 882]])
    882
    >>> array_manipulation(10, [[1, 5, 3], [4, 8, 7], [6, 9, 1]])
    10
    """
    arr = [0 for _ in range(n + 2)]
    for a, b, k in queries:
        arr[a] += k
        arr[b + 1] -= k
    answer = current = 0
    for el in arr:
        current += el
        answer = max(answer, current)
    return answer
