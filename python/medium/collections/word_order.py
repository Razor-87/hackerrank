# -*- coding: utf-8 -*-
from typing import Tuple


def word_order(arr: Tuple[str, ...]) -> str:
    """
    >>> word_order(('bcdef', 'abcdefg', 'bcde', 'bcdef'))
    '3\\n2 1 1'
    """
    from collections import Counter
    d_words = Counter(arr)
    ret = f"{len(d_words)}\n{' '.join(map(str, d_words.values()))}"
    return ret


if __name__ == '__main__':
    arr = (*(input() for _ in range(int(input()))),)
    print(word_order(arr))
