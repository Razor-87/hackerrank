# -*- coding: utf-8 -*-


def python_evaluation(raw_str: str) -> int:
    """
    >>> python_evaluation('print(2 + 3)')
    5
    """
    return eval(raw_str)


if __name__ == '__main__':
    raw_str = input()
    python_evaluation(raw_str)
