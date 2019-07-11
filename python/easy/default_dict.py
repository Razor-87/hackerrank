# -*- coding: utf-8 -*-
from typing import DefaultDict, List


def default_dict(n: int, arr: List[str]) -> List[str]:
    """
    >>> default_dict(5, ['a', 'a', 'b', 'a', 'b', 'a', 'b'])
    ['1 2 4', '3 5']
    >>> default_dict(1, ['s', 't'])
    ['-1']
    """
    from collections import defaultdict
    d: DefaultDict = defaultdict(list)
    arr.insert(0, '')
    for i in range(1, len(arr[:n])+1):
        d[arr[i]].append(i)
    return [' '.join(map(str, lst))
            for lst in [d[i] if i in d else [-1] for i in arr[n+1:]]]


if __name__ == '__main__':
    import sys
    n, _, *arr = sys.stdin.read().split()
    print(*default_dict(int(n), arr), sep='\n')
