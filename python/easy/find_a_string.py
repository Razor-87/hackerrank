# -*- coding: utf-8 -*-


def count_substring(string: str, sub_string: str) -> int:
    """
    >>> count_substring('ABCDCDC', 'CDC')
    2
    """
    n = len(string) - len(sub_string) + 1
    return sum(chunk == sub_string
               for chunk in (string[i:i + len(sub_string)] for i in range(n)))
