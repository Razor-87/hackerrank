# -*- coding: utf-8 -*-
import re
from typing import Tuple


def validating_phone_numbers(arr: Tuple[str, ...]) -> None:
    """
    >>> validating_phone_numbers(('9587456281', '1252478965'))
    YES
    NO
    """
    pattern = re.compile(r'^[789]\d{9}$')
    for num in arr:
        print('YES' if pattern.match(num) else 'NO')


if __name__ == '__main__':
    arr = tuple(input() for _ in range(int(input())))
    validating_phone_numbers(arr)
