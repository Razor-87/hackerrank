# -*- coding: utf-8 -*-
from typing import Tuple


def set_add(arr: Tuple[str, ...]) -> int:
    """
    >>> set_add(('UK', 'China', 'USA', 'France', 'New Zealand', 'UK', 'France'))
    5
    """
    return len(set(arr))


if __name__ == '__main__':
    arr = tuple(input() for _ in range(int(input())))
    print(set_add(arr))
