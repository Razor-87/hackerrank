# -*- coding: utf-8 -*-
import textwrap


def wrap(string: str, max_width: int) -> str:
    """
    >>> wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4)
    'ABCD\\nEFGH\\nIJKL\\nIMNO\\nQRST\\nUVWX\\nYZ'
    """
    return textwrap.fill(string, width=max_width)
