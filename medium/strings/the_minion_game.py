# -*- coding: utf-8 -*-


def minion_game(s: str) -> None:
    """
    >>> minion_game('BANANA')
    Stuart 12
    >>> minion_game('BANANANAAAS')
    Draw
    >>> minion_game('BAANANAS')
    Kevin 19
    """
    # import collections
    # players = collections.defaultdict(int)
    # for i in range(s_len):
    #     point = s_len - i
    #     if s[i] in vowels:
    #         players['Kevin'] += point
    #     else:
    #         players['Stuart'] += point
    # stuart, kevin = players['Stuart'], players['Kevin']
    vowels = frozenset('AEIOU')
    s_len = len(s)
    kevin = sum(i for i, c in enumerate(s[::-1], 1) if c in vowels)
    stuart = s_len * (s_len + 1) // 2 - kevin
    if stuart == kevin:
        print('Draw')
    else:
        print(f'Stuart {stuart}' if stuart > kevin else f'Kevin {kevin}')
