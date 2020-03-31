# -*- coding: utf-8 -*-
from typing import List, Union


def minimum_bribes(q: List[int], n: int) -> Union[int, str]:
    """
    >>> minimum_bribes([2, 1, 5, 3, 4], 5)
    3
    >>> minimum_bribes([2, 5, 1, 3, 4], 5)
    'Too chaotic'
    """
    from collections import deque
    bribes = 0
    deq, expect = deque(q), deque(range(1, n + 1))
    while deq:
        iof = expect.index(deq[0])
        if iof > 2:
            return 'Too chaotic'
        else:
            bribes += iof
            expect.remove(deq.popleft())
    return bribes
