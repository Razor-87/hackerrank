# -*- coding: utf-8 -*-


def triangle_quest(n: int) -> None:
    """
    >>> triangle_quest(6)
    1
    22
    333
    4444
    55555
    """
    for i in range(1, n):
        # print((1, 22, 333, 4444, 55555, 666666, 7777777, 88888888,
        #        999999999)[i - 1])
        print(i * (10**i // 9))


if __name__ == '__main__':
    triangle_quest(int(input()))
