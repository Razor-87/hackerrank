# -*- coding: utf-8 -*-
from typing import List


def finding_the_percentage(n: int, arr: List[str], query_name: str) -> str:
    """
    >>> finding_the_percentage(3, ['Krishna 67 68 69', 'Arjun 70 98 63',
    ... 'Malika 52 56 60'], 'Malika')
    '56.00'
    >>> finding_the_percentage(2, ['Harsh 25 26.5 28', 'Anurag 26 28 30'],
    ... 'Harsh')
    '26.50'
    """
    student_marks = {}
    for i in range(n):
        name, *line = arr[i].split()
        scores = list(map(float, line))
        student_marks[name] = sum(scores)/len(scores)
    return '{:.2f}'.format(student_marks[query_name])


if __name__ == '__main__':
    import sys
    n, *arr, query_name = map(str.strip, sys.stdin.readlines())
    print(finding_the_percentage(int(n), arr, query_name))
