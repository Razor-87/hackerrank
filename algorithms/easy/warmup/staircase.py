# -*- coding: utf-8 -*-
from typing import List


def staircase(size: int) -> List[str]:
    """
    >>> staircase(4)
    ['   #', '  ##', ' ###', '####']
    """
    # ret = [f"{'#' * i:>{size}}" for i in range(1, size+1)]
    ret = [('#' * i).rjust(size) for i in range(1, size+1)]
    return ret


if __name__ == '__main__':
    print(*staircase(int(input())), sep='\n')
