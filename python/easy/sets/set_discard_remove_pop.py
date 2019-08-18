# -*- coding: utf-8 -*-
from typing import List


def set_discard_remove_pop(arr: List[str], commands: List[List[str]]) -> int:
    """
    >>> set_discard_remove_pop(['1', '2', '3', '4', '5', '6', '7', '8', '9'],
    ... [['pop'], ['remove', '9'], ['discard', '9'], ['discard', '8'],
    ... ['remove', '7'], ['pop'], ['discard', '6'], ['remove', '5'],
    ... ['pop'], ['discard', '5']])
    4
    """
    set_ = set(map(int, arr))
    fixed_commands = ('set_.{}()'.format(el[0])
                      if len(el) == 1 else 'set_.{}({})'.format(*el)
                      for el in commands)
    for el in fixed_commands:
        eval(el)
    return sum(set_)


if __name__ == '__main__':
    import sys
    _, arr, _, *commands = map(str.split, map(str.strip,
                                              sys.stdin.readlines()))
    print(set_discard_remove_pop(arr, commands))
