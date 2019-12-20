# -*- coding: utf-8 -*-
from typing import List


def check_magazine(magazine: List[str], note: List[str]) -> str:
    """
    >>> check_magazine(['give', 'me', 'one', 'grand', 'today', 'night'],
    ... ['give', 'one', 'grand', 'today'])
    'Yes'
    >>> check_magazine(['two', 'times', 'three', 'is', 'not', 'four'],
    ... ['two', 'times', 'two', 'is', 'four'])
    'No'
    >>> check_magazine(['apgo', 'clm', 'w', 'lxkvg', 'mwz', 'elo', 'bg', 'elo',
    ... 'lxkvg', 'elo', 'apgo', 'apgo', 'w', 'elo', 'bg'],
    ... ['elo', 'lxkvg', 'bg', 'mwz', 'clm', 'w'])
    'Yes'
    """
    from collections import Counter
    # count_magazine = Counter(magazine)
    # count_magazine.subtract(Counter(note))
    # ans = all(val >= 0 for val in count_magazine.values())
    ans = not (Counter(note) - Counter(magazine))
    return "Yes" if ans else "No"
