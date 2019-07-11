# -*- coding: utf-8 -*-
from typing import List, Tuple


def incorrect_regex(patterns: Tuple[str, ...]) -> List[bool]:
    """
    >>> incorrect_regex([r'.*\\+', '.*+'])
    [True, False]
    """
    import re
    booleans = []
    for pattern in patterns:
        try:
            booleans.append(bool(re.compile(pattern)))
        except re.error:
            booleans.append(False)
    return booleans


if __name__ == '__main__':
    import sys
    patterns = tuple(map(str.strip, sys.stdin.readlines()[1:]))
    print(*incorrect_regex(patterns), sep='\n')
