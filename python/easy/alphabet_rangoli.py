# -*- coding: utf-8 -*-


def alphabet_rangoli(size: int) -> None:
    """
    >>> alphabet_rangoli(5)
    --------e--------
    ------e-d-e------
    ----e-d-c-d-e----
    --e-d-c-b-c-d-e--
    e-d-c-b-a-b-c-d-e
    --e-d-c-b-c-d-e--
    ----e-d-c-d-e----
    ------e-d-e------
    --------e--------
    """
    from string import ascii_lowercase
    alpha = list(ascii_lowercase)
    lst = []
    for i in range(size):
        s = '-'.join(alpha[i:size])
        lst.append((s[::-1]+s[1:]).center(4*size-3, '-'))
    print(*lst[:0:-1]+lst, sep='\n')
