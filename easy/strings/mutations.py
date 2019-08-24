# -*- coding: utf-8 -*-


def mutate_string(string: str, position: int, character: str) -> str:
    """
    >>> mutate_string('abracadabra', 5, 'k')
    'abrackdabra'
    """
    lst = list(string)
    lst[position] = character
    return ''.join(lst)
