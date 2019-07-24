# -*- coding: utf-8 -*-
from typing import List, Set


def binary_xor_sets(arr: List[str]) -> Set[str]:
    """
    >>> binary_xor_sets(['0', '2', '1', '0', '1', '1'])
    {'2'}
    """
    return set(arr[0::2]) ^ set(arr[1::2])


def the_captains_room(arr: List[str]) -> Set[str]:
    """
    >>> the_captains_room(
    ... ['1', '2', '3', '6', '5', '4', '4', '2', '5', '3', '6', '1', '6', '5',
    ... '3', '2', '4', '1', '2', '5', '1', '4', '3', '6', '8', '4', '3', '1',
    ... '5', '6', '2'])
    {'8'}
    """
    fast_return = binary_xor_sets(arr)
    if len(fast_return) == 1:
        return fast_return
    arr.sort()
    return binary_xor_sets(arr)


# def the_captains_room(n: int, arr: list) -> set:
#     if n < len(set(arr))**0.5:
#         arr.sort()
#     return set(arr[0::2]) ^ set(arr[1::2])


if __name__ == '__main__':
    import sys
    _, arr = sys.stdin.readline(), sys.stdin.readline().split()
    print(*the_captains_room(arr))
