# -*- coding: utf-8 -*-
import re


def re_group(string: str) -> str:
    """
    >>> re_group('..12345678910111213141516171820212223')
    '1'
    """
    match = re.search(r'([a-zA-Z0-9])\1+', string)
    return match.group(1) if match else '-1'


if __name__ == '__main__':
    string = input()
    print(re_group(string))
