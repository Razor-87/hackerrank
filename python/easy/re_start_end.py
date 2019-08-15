# -*- coding: utf-8 -*-
import re


def re_start_end(s: str, k: str) -> None:
    """
    >>> re_start_end('aaadaa', 'aa')
    (0, 1)
    (1, 2)
    (4, 5)
    """
    pattern = re.compile(k)
    r = pattern.search(s)
    if not r:
        print("(-1, -1)")
    while r:
        print("({0}, {1})".format(r.start(), r.end() - 1))
        r = pattern.search(s, r.start() + 1)


if __name__ == '__main__':
    s, k = (input() for _ in range(2))
    re_start_end(s, k)
