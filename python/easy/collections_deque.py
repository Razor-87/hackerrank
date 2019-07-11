# -*- coding: utf-8 -*-
from typing import Deque, List, Tuple


def collections_deque(raw_commands: Tuple[List[str], ...]) -> Deque[List[str]]:
    """
    >>> collections_deque((['append', '1'], ['append', '2'], ['append', '3'],
    ... ['appendleft', '4'], ['pop'], ['popleft']))
    deque(['1', '2'])
    """
    import collections
    deq: Deque = collections.deque()
    __ = tuple(
        getattr(deq, el[0])() if len(el) == 1 else getattr(deq, el[0])(el[1])
        for el in raw_commands)
    del __
    return deq


if __name__ == '__main__':
    import sys
    raw_commands = tuple(
        map(str.split, map(str.strip,
                           sys.stdin.readlines()[1:])))
    print(*collections_deque(raw_commands))
