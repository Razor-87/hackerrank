# -*- coding: utf-8 -*-
from typing import Tuple


def company_logo(s: str) -> Tuple[str, ...]:
    """
    >>> company_logo('aabbbccde')
    ('b 3', 'a 2', 'c 2')
    >>> company_logo('qwertyuiopasdfghjklzxcvbnm')
    ('a 1', 'b 1', 'c 1')
    """
    from collections import Counter
    logo_counter = sorted(Counter(s).most_common(24),
                          key=lambda x: (-x[1], x))[:3]
    ret = (*(f"{el[0]} {el[1]}" for el in logo_counter),)
    return ret


if __name__ == '__main__':
    print(*company_logo(input()), sep='\n')
