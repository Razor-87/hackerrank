# -*- coding: utf-8 -*-
from typing import List


def alphabet_rangoli(size: int) -> List[str]:
    """
    >>> alphabet_rangoli(5)
    ['--------e--------', '------e-d-e------', '----e-d-c-d-e----', '--e-d-c-b-c-d-e--', 'e-d-c-b-a-b-c-d-e', '--e-d-c-b-c-d-e--', '----e-d-c-d-e----', '------e-d-e------', '--------e--------']
    """
    from string import ascii_lowercase
    alpha = list(ascii_lowercase)
    lst = []
    for i in range(size):
        s = '-'.join(alpha[i:size])
        lst.append((s[::-1]+s[1:]).center(4*size-3, '-'))
    return lst[:0:-1]+lst


if __name__ == '__main__':
    n = int(input())
    print(*alphabet_rangoli(n), sep='\n')
