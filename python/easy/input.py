# -*- coding: utf-8 -*-


def input_(x: int, y: int, ex: str) -> bool:
    """
    >>> input_(1, 4, 'x**3 + x**2 + x + 1')
    True
    """
    return eval(ex) == y


if __name__ == '__main__':
    (x, y), ex = map(int, input().split()), input()
    print(input_(x, y, ex))
