# -*- coding: utf-8 -*-
import re
from typing import Tuple


def validating_UID(uids: Tuple[str, ...]) -> None:
    """
    >>> validating_UID(('B1CD102354', 'B1CDEF2354'))
    Invalid
    Valid
    """
    pattern = re.compile(
        r'^(?=(.*[A-Z]){2,})(?=(.*\d.*){3})(?=\w{10})(?!.*(\w)(.*\3)).*$')
    for uid in uids:
        matches = pattern.findall(uid)
        print('Valid' if matches else 'Invalid')


if __name__ == '__main__':
    uids = tuple(input() for _ in range(int(input())))
    validating_UID(uids)
