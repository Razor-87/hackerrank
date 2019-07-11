# -*- coding: utf-8 -*-
from typing import Iterable


def sum_numbers(numbers: Iterable[int] = None) -> int:
    """
    >>> sum_numbers()
    5050
    >>> sum_numbers(numbers=None)
    5050
    >>> sum_numbers(range(1, 11))
    55
    >>> sum_numbers((1, 2, 3))
    6
    >>> sum_numbers([])
    0
    """
    if numbers is None:
        return sum(range(1, 101))
    return sum(numbers)


if __name__ == '__main__':
    print(sum_numbers())
