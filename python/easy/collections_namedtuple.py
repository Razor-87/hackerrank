# -*- coding: utf-8 -*-
from typing import List


def collections_namedtuple(n: int, spreadsheet: List[str],
                           rows: List[List[str]]) -> float:
    """
    >>> collections_namedtuple(5, ['ID', 'MARKS', 'NAME', 'CLASS'],
    ... [['1', '97', 'Raymond', '7'],
    ...  ['2', '50', 'Steven', '4'],
    ...  ['3', '91', 'Adrian', '9'],
    ...  ['4', '72', 'Stewart', '5'],
    ...  ['5', '80', 'Peter', '6']])
    78.0
    """
    from collections import namedtuple
    Student = namedtuple('Student', spreadsheet)  # type: ignore
    total_marks = 0
    for row in rows:
        temp_student = Student(*row)  # type: ignore
        total_marks += int(temp_student.MARKS)  # type: ignore
    return total_marks / n


if __name__ == '__main__':
    import sys
    n = int(sys.stdin.readline())
    spreadsheet, *rows = (line.split()
                          for line in map(str.strip, sys.stdin.readlines()))
    print(collections_namedtuple(n, spreadsheet, rows))
