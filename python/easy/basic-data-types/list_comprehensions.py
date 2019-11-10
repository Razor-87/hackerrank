# -*- coding: utf-8 -*-
from typing import List


def list_comprehensions(x: int, y: int, z: int, n: int) -> List[List[int]]:
    """
    >>> list_comprehensions(1, 1, 1, 2)
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
    """
    return [[i, j, k] for i in range(x + 1) for j in range(y + 1)
            for k in range(z + 1) if ((i + j + k) != n)]


if __name__ == '__main__':
    x, y, z, n = (int(input()) for _ in range(4))
    print(list_comprehensions(x, y, z, n))
