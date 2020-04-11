# -*- coding: utf-8 -*-
from typing import List


def grading_students(grades: List[int]) -> List[int]:
    """
    >>> grading_students([73, 67, 38, 33])
    [75, 67, 40, 33]
    """
    def check_grade(n):
        if n < 38:
            return n
        m = n
        while m % 5:
            m += 1
        return m if (m - n) < 3 else n

    ret = [check_grade(grade) for grade in grades]
    return ret
