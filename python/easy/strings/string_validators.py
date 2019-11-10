# -*- coding: utf-8 -*-
from typing import Tuple


def string_validators(string: str) -> Tuple[bool, ...]:
    """
    >>> string_validators('qA2')
    (True, True, True, True, True)
    >>> string_validators('123')
    (True, False, True, False, False)
    """
    dict_methods = {
        'isalnum': (char.isalnum() for char in string),
        'isalpha': (char.isalpha() for char in string),
        'isdigit': (char.isdigit() for char in string),
        'islower': (char.islower() for char in string),
        'isupper': (char.isupper() for char in string)
    }
    return tuple(map(any, dict_methods.values()))


if __name__ == '__main__':
    string = input()
    print(*string_validators(string), sep='\n')
