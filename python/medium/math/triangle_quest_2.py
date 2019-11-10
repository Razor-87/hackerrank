# -*- coding: utf-8 -*-


def triangle_quest_2(n: int) -> None:
    """
    >>> triangle_quest_2(5)
    1
    121
    12321
    1234321
    123454321
    """
    for i in range(1, n + 1):
        print(((10**i - 1) // 9)**2)


if __name__ == '__main__':
    triangle_quest_2(int(input()))
