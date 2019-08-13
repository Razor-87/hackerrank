# -*- coding: utf-8 -*-


def sum_pows(a: int, b: int, c: int, d: int) -> int:
    """
    >>> sum_pows(9, 29, 7, 27)
    4710194409608608369201743232
    """
    return a**b + c**d


if __name__ == '__main__':
    a, b, c, d = (int(input()) for _ in range(4))
    print(sum_pows(a, b, c, d))
