# -*- coding: utf-8 -*-
from typing import List


def lists(arr: List[List[str]]) -> List[List[int]]:
    """
    >>> lists([['insert', '0', '5'], ['insert', '1', '10'],
    ... ['insert', '0', '6'], ['print'], ['remove', '6'], ['append', '9'],
    ... ['append', '1'], ['sort'], ['print'], ['pop'], ['reverse'], ['print']])
    [[6, 5, 10], [1, 5, 9, 10], [9, 5, 1]]
    """
    lst_temp: List[int] = []
    lst_final = []
    for el in arr:
        op = el[0]
        if op == 'insert':
            lst_temp.insert(int(el[1]), int(el[2]))
        elif op == 'remove':
            lst_temp.remove(int(el[1]))
        elif op == 'append':
            lst_temp.append(int(el[1]))
        elif op == 'pop':
            lst_temp.pop()
        elif op == 'sort':
            lst_temp.sort()
        elif op == 'reverse':
            lst_temp.reverse()
        else:
            lst_final.append(list(lst_temp))
    return lst_final


if __name__ == '__main__':
    import sys
    _, *arr = map(str.split, map(str.strip, sys.stdin.readlines()))
    print(*lists(arr), sep='\n')
