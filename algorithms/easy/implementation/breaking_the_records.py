# -*- coding: utf-8 -*-
from typing import List, Tuple


def breaking_records(scores: List[int]) -> Tuple[int, int]:
    """
    >>> breaking_records([10, 5, 20, 20, 4, 5, 2, 25, 1])
    (2, 4)
    >>> breaking_records([3, 4, 21, 36, 10, 28, 35, 5, 24, 42])
    (4, 0)
    """
    maxs = mins = 0
    _max_min = {scores[0]}
    for score in scores[1:]:
        if score not in _max_min:
            max_score, min_score = max(_max_min), min(_max_min)
            maxs += max_score < score
            mins += score < min_score
            _max_min = {max(max_score, score), min(min_score, score)}
    return maxs, mins
