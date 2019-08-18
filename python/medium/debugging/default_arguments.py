# -*- coding: utf-8 -*-
from typing import Union


class EvenStream():
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


class OddStream():
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


def print_from_stream(n: int,
                      stream: Union[OddStream, EvenStream] = None) -> None:
    """
    >>> print_from_stream(2, OddStream())
    1
    3
    >>> print_from_stream(3)
    0
    2
    4
    >>> print_from_stream(5, OddStream())
    1
    3
    5
    7
    9
    """
    if stream is None:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())
