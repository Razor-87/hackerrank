# -*- coding: utf-8 -*-
from typing import List, Set, Tuple


def set_mutations(arr: List[str], commands: Tuple[Tuple[str, Set[int]], ...]):
    """
    >>> set_mutations(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
    ... '12', '13', '14', '24', '52'],
    ... (('intersection_update', {1, 2, 3, 4, 5, 6, 7, 8, 9, 11}),
    ... ('update', {66, 55}), ('symmetric_difference_update',
    ... {35, 7, 22, 58, 62}), ('difference_update',
    ... {66, 35, 11, 22, 55, 58, 62})))
    38
    """
    set_ = set(map(int, arr))
    fixed_commands = ('set_.{}({})'.format(*el) for el in commands)
    for el in fixed_commands:
        eval(el)
    return sum(set_)


if __name__ == '__main__':
    import sys
    _, arr, _, *rest = map(str.split, map(str.strip,
                                          sys.stdin.readlines()))
    commands = tuple(zip((el[0] for el in rest[::2]),
                     (set(map(int, lst)) for lst in rest[1::2])))
    print(set_mutations(arr, commands))
