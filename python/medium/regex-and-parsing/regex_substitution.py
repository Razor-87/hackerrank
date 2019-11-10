# -*- coding: utf-8 -*-
import re
from typing import List


def substitution(arr: List[str]) -> List[str]:
    """
    >>> substitution(['a = 1;', 'b = input();', '',
    ... 'if a + b > 0 && a - b < 0:','    start()', 'elif a*b > 10 || a/b < 1:',
    ... '    stop()', 'print set(list(a)) | set(list(b))',
    ... '#Note do not change &&& or ||| or & or |',
    ... "#Only change those '&&' which have space on both sides.",
    ... "#Only change those '|| which have space on both sides."]
    ... ) #doctest: +NORMALIZE_WHITESPACE
    ['a = 1;', 'b = input();', '', 'if a + b > 0 and a - b < 0:',
    '    start()', 'elif a*b > 10 or a/b < 1:',
    '    stop()', 'print set(list(a)) | set(list(b))',
    '#Note do not change &&& or ||| or & or |',
    "#Only change those '&&' which have space on both sides.",
    "#Only change those '|| which have space on both sides."]
    """
    pattern = re.compile(r"(?<= )(&&|\|\|)(?= )")
    return [pattern.sub(lambda x: "and" if x.group() == "&&" else "or", row)
            for row in arr]


if __name__ == '__main__':
    arr = [input() for _ in range(int(input()))]
    print(*substitution(arr), sep='\n')
