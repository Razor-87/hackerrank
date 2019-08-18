# -*- coding: utf-8 -*-
from typing import List


def itertools_combinations(string: str, n: int) -> List[str]:
    """
    >>> itertools_combinations('HACK', 2)
    ['A', 'C', 'H', 'K', 'AC', 'AH', 'AK', 'CH', 'CK', 'HK']
    >>> itertools_combinations('ABCD', 3) #doctest: +NORMALIZE_WHITESPACE
    ['A', 'B', 'C', 'D', 'AB', 'AC', 'AD', 'BC',
     'BD', 'CD', 'ABC', 'ABD', 'ACD', 'BCD']
    """
    import itertools
    rang = range(1, n+1)
    return sorted((''.join(tup) for i in rang
                   for tup in itertools.combinations(sorted(string), i)),
                  key=lambda x: (len(x), x))


def itertools_combinations_with_repl(string: str, n: int) -> List[str]:
    """
    >>> itertools_combinations_with_repl('HACK', 2)
    ['AA', 'AC', 'AH', 'AK', 'CC', 'CH', 'CK', 'HH', 'HK', 'KK']
    """
    import itertools
    return sorted(''.join(tup)
                  for tup in itertools.combinations_with_replacement(
                      sorted(string), n))


def itertools_permutations(string: str, n: int) -> List[str]:
    """
    >>> itertools_permutations('HACK', 2)
    ['AC', 'AH', 'AK', 'CA', 'CH', 'CK', 'HA', 'HC', 'HK', 'KA', 'KC', 'KH']
    """
    import itertools
    return sorted(''.join(tup)
                  for tup in itertools.permutations(string, n))


if __name__ == '__main__':
    import sys
    inp = sys.stdin.read().split()
    print(*itertools_combinations(inp[0], int(inp[1])), sep='\n')
    # print(*itertools_combinations_with_repl(inp[0], int(inp[1])), sep='\n')
    # print(*itertools_permutations(inp[0], int(inp[1])), sep='\n')
