# -*- coding: utf-8 -*-
from typing import List


def any_or_all(lst: List[str]) -> bool:
    """
    >>> any_or_all(['12', '9', '61', '5', '14'])
    True
    >>> any_or_all(['81'])
    False
    """
    any_palindromic = any(x == ''.join(reversed(x)) for x in lst)
    all_positive = all(int(x) > 0 for x in lst)
    return any_palindromic and all_positive


if __name__ == '__main__':
    _, lst = input(), input().split()
    print(any_or_all(lst))
