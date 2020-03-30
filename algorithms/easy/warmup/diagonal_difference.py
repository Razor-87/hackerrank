# -*- coding: utf-8 -*-
from typing import List


def diagonal_difference(size: int, matrix: List[List[int]]) -> int:
    """
    >>> diagonal_difference(3, [[11, 2, 4], [4, 5, 6], [10, 8, -12]])
    15
    """
    # prim_diag = sec_diag = 0
    # for i in range(size):
    #     prim_diag += matrix[i][i]
    #     sec_diag += matrix[-i-1][i]  # matrix[i][(size-1)-i]
    indexes = enumerate(range(size-1, -1, -1))
    diagonals = zip(*((matrix[i][i], matrix[i][s]) for i, s in indexes))
    prim_diag, sec_diag = map(sum, diagonals)
    ret = abs(prim_diag - sec_diag)  # type: ignore
    return ret


if __name__ == '__main__':
    size = int(input())
    matrix = [[*map(int, input().strip().split())] for _ in range(size)]
    print(diagonal_difference(size, matrix))
