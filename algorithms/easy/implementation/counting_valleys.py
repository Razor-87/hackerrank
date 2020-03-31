# -*- coding: utf-8 -*-


def counting_valleys(path: str) -> int:
    """
    >>> counting_valleys("UDDDUDUU")
    1
    >>> counting_valleys("DDUUDDUDUUUD")
    2
    >>> counting_valleys("UDUUUDUDDD")
    0
    >>> counting_valleys("DUDDDUUDUU")
    2
    """
    digit_path = ((-1, 1)[step == "U"] for step in path)
    valley, level = 0, 0
    for step in digit_path:
        if level == 0 and step == -1:
            valley += 1
        level += step
    return valley
