# -*- coding: utf-8 -*-


def find_angle(ab: float, bc: float) -> int:
    """
    >>> find_angle(10, 10)
    45
    >>> find_angle(1, 10)
    6
    """
    from math import atan2, degrees
    return round(degrees(atan2(ab, bc)))


if __name__ == '__main__':
    ab, bc = float(input()), float(input())
    print(find_angle(ab, bc), end='°')
