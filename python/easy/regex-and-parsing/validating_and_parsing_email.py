# -*- coding: utf-8 -*-
import re
import email.utils
from typing import Tuple


def validating_and_parsing_email(arr: Tuple[str, ...]) -> None:
    """
    >>> validating_and_parsing_email(('DEXTER <dexter@hotmail.com>',
    ... 'VIRUS <virus!@variable.:p>'))
    DEXTER <dexter@hotmail.com>
    """
    pattern = re.compile(r'[a-z][\w._-]*@[a-z]+\.[a-z]{1,3}$', re.I)
    for addr in arr:
        if pattern.match(email.utils.parseaddr(addr)[1]):
            print(addr)


if __name__ == '__main__':
    arr = tuple(input() for _ in range(int(input())))
    validating_and_parsing_email(arr)
