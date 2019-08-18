# -*- coding: utf-8 -*-


def designer_door_mat(n: int, m: int) -> None:
    """
    >>> designer_door_mat(9, 27)
    ------------.|.------------
    ---------.|..|..|.---------
    ------.|..|..|..|..|.------
    ---.|..|..|..|..|..|..|.---
    ----------WELCOME----------
    ---.|..|..|..|..|..|..|.---
    ------.|..|..|..|..|.------
    ---------.|..|..|.---------
    ------------.|.------------
    """
    pattern = '\n'.join(('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2))
    print(pattern, 'WELCOME'.center(m, '-'), pattern[::-1], sep='\n')


if __name__ == '__main__':
    n, m = map(int, input().split())
    designer_door_mat(n, m)
