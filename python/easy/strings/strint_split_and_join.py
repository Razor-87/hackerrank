# -*- coding: utf-8 -*-


def split_and_join(line: str) -> str:
    """
    >>> split_and_join('this is a string')
    'this-is-a-string'

    """
    return "-".join(line.split())
