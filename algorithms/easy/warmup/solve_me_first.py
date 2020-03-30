# -*- coding: utf-8 -*-


def solve_me_first(a: int, b: int) -> int:
    """
    >>> solve_me_first(2, 3)
    5
    """
    ret = a + b
    return ret


if __name__ == '__main__':
    a, b = (int(input()) for _ in range(2))
    print(solve_me_first(a, b))
