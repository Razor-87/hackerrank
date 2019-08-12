# -*- coding: utf-8 -*-


def solve(string: str) -> str:
    """
    >>> solve('chris alan')
    'Chris Alan'
    >>> solve('1 w 2 r 3g')
    '1 W 2 R 3g'
    """
    return ' '.join(char.capitalize() for char in string.split(' '))
