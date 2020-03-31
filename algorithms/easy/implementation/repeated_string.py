# -*- coding: utf-8 -*-


def repeated_string(string: str, n: int, char: str = "a") -> int:
    """
    >>> repeated_string("aba", 10)
    7
    >>> repeated_string("a", 1000000000000)
    1000000000000
    """
    string_size = len(string)
    if string_size == 1:
        return n if string == char else 0
    whole, remainder = divmod(n, string_size)
    char_count = string.count(char), string[:remainder].count(char)
    ret = (whole * char_count[0]) + char_count[1]
    return ret
