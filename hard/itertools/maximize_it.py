# -*- coding: utf-8 -*-
from typing import Iterator


def maximize_it(m: int, arrs: Iterator[Iterator[int]]) -> int:
    """
    >>> maximize_it(1000, [[2, 5, 4], [3, 7, 8, 9], [5, 5, 7, 8, 9, 10]])
    206
    >>> maximize_it(767, [[488512261, 423332742], [625040505, 443232774],
    ... [4553600], [92134264, 617699202, 124100179, 337650738],
    ... [778493847, 932097163],
    ... [489894997, 496724555, 693361712, 935903331, 518538304]])
    763
    """
    from itertools import product
    cartesian_product = product(*arrs)
    ret = max(sum(el**2 for el in tup) % m for tup in cartesian_product)
    return ret


if __name__ == '__main__':
    k, m = map(int, input().split())
    arrs = (map(int, input().split()[1:]) for _ in range(k))
    print(maximize_it(m, arrs))
