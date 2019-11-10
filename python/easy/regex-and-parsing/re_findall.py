# -*- coding: utf-8 -*-
import re
from typing import List


def re_findall(raw_str: str) -> List[str]:
    """
    >>> re_findall('rabcdeefgyYhFjkIoomnpOeorteeeeet')
    ['ee', 'Ioo', 'Oeo', 'eeeee']
    """
    pattern = re.compile(
        '(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})[qwrtypsdfghjklzxcvbnm]',
        re.I)
    return pattern.findall(raw_str) or ['-1']


if __name__ == '__main__':
    raw_str = input()
    print(*re_findall(raw_str), sep='\n')
