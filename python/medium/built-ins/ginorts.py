# -*- coding: utf-8 -*-
from typing import List


def ginorts(s: str) -> List[str]:
    """
    >>> ginorts("Sorting1234")
    ['g', 'i', 'n', 'o', 'r', 't', 'S', '1', '3', '2', '4']
    """
    arr = [*s]
    arr.sort(key=lambda c: (c.isdigit(), c in '02468', c.isupper(), c))
    return arr


if __name__ == '__main__':
    print(*ginorts(input()), sep='')
