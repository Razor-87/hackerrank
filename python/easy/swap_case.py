# -*- coding: utf-8 -*-


def swap_case(string: str) -> str:
    """
    >>> swap_case('HackerRank.com presents "Pythonist 2".')
    'hACKERrANK.COM PRESENTS "pYTHONIST 2".'
    """
    return string.swapcase()


if __name__ == '__main__':
    string = input()
    result = swap_case(string)
    print(result)
