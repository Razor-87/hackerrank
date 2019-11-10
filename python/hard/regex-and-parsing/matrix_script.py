# -*- coding: utf-8 -*-
from typing import List


def matrix_script(arr: List[str]) -> str:
    """
    >>> matrix_script(['Tsi', 'h%x', 'i #', 'sM ', '$a ', '#t%', 'ir!'])
    'This is Matrix#  %!'
    """
    from itertools import chain
    from re import compile
    string = "".join(chain.from_iterable(zip(*arr)))
    pattern = compile(r"(?<=\w)([^\w]+)(?=\w)")
    return pattern.sub(' ', string)


if __name__ == '__main__':
    matrix = [input() for _ in range(int(input().split()[0]))]
    print(matrix_script(matrix))
