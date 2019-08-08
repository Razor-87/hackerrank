# -*- coding: utf-8 -*-


def merge_the_tools(string: str, k: int) -> None:
    """
    >>> merge_the_tools('AABCAAADA', 3)
    AB
    CA
    AD
    """
    # from textwrap import wrap
    # for chunk in wrap(string, k):
    for chunk in zip(*(iter(string),) * k):
        print(*{}.fromkeys(chunk), sep='')
