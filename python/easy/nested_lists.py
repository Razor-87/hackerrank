# -*- coding: utf-8 -*-
from typing import Dict, List


def nested_lists(arr: List[str]) -> List[str]:
    """
    >>> nested_lists(['Harry', '37.21', 'Berry', '37.21', 'Tina', '37.2', 'Akriti', '41', 'Harsh', '39'])
    ['Berry', 'Harry']
    >>> nested_lists(['Test1', '52', 'Test2', '53', 'Test3', '53'])
    ['Test2', 'Test3']
    """
    arr.reverse()
    arr_zip = zip(map(float, arr[::2]), [[i] for i in arr[1::2]])
    d: Dict[float, List[str]] = {}
    for k, v in arr_zip:
        if k in d:
            d[k] += v
        else:
            d[k] = v
    return sorted(d[sorted(d)[1]])


if __name__ == '__main__':
    import sys
    _, *arr = sys.stdin.read().split()
    print(*nested_lists(arr), sep="\n")
