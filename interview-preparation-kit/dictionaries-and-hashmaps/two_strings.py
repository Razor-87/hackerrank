# -*- coding: utf-8 -*-


def two_strings(s1: str, s2: str) -> str:
    """
    >>> two_strings("hello", "world")
    'YES'
    >>> two_strings("hi", "world")
    'NO'
    """
    intersection = {*s1} & {*s2}
    return "YES" if intersection else "NO"
