# -*- coding: utf-8 -*-
from typing import List, Tuple


def compare_triplets(a: List[int], b: List[int]) -> Tuple[int, ...]:
    """
    >>> compare_triplets((5, 6, 7), (3, 6, 10))
    (1, 1)
    """
    zip_ab = tuple(zip(a, b))
    # alice, bob = 0, 0
    # for x, y in zip_ab:
    #     if x > y:
    #         alice += 1
    #     elif x < y:
    #         bob += 1
    alice, bob = sum(a > b for a, b in zip_ab), sum(a < b for a, b in zip_ab)
    return alice, bob


if __name__ == '__main__':
    a, b = ([*map(int, input().strip().split())] for _ in range(2))
    print(*compare_triplets(a, b))
