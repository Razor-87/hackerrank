# -*- coding: utf-8 -*-
from typing import List


def collections_counter(sizes: List[str], customers: List[List[str]]) -> int:
    """
    >>> collections_counter(['2', '3', '4', '5', '6', '8', '7', '6', '5', '18'],
    ... [['6', '55'], ['6', '45'], ['6', '55'], ['4', '40'], ['18', '60'],
    ... ['10', '50']])
    200
    """
    from collections import Counter
    sizes_count = Counter(sizes)
    temp = []
    for cust in customers:
        if cust[0] in sizes and sizes_count[cust[0]] > 0:
            temp.append(cust[1])
            sizes_count[cust[0]] -= 1
    return sum(map(int, temp))


if __name__ == '__main__':
    import sys
    _, sizes, _, *customers = map(str.split,
                                  map(str.strip, sys.stdin.readlines()))
    print(collections_counter(sizes, customers))
