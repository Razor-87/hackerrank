# -*- coding: utf-8 -*-
from typing import Tuple


def mod_divmod(x: int, y: int) -> Tuple[int, int, Tuple[int, ...]]:
    """
    >>> mod_divmod(177, 10)
    (17, 7, (17, 7))
    """
    divmod_xy = divmod(x, y)
    return (*divmod_xy, divmod_xy)


if __name__ == '__main__':
    x, y = (int(input()) for _ in range(2))
    print(*mod_divmod(x, y), sep='\n')
