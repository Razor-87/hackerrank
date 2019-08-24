# -*- coding: utf-8 -*-
import re
from typing import Tuple


def hex_color_code(css_code: Tuple[str, ...]) -> None:
    """
    >>> hex_color_code(('#BED', '{', ' color: #FfFdF8; background-color:#aef;',
    ... ' font-size: 123px;', '', '}', '#Cab', '{', ' background-color: #ABC;',
    ... ' border: 2px dashed #fff;', '}'))
    #FfFdF8
    #aef
    #ABC
    #fff
    """
    pattern = re.compile(r':?.(#[0-9a-f]{6}|#[0-9a-f]{3})', re.I)
    for line in css_code:
        matches = pattern.findall(line)
        if matches:
            print(*matches, sep='\n')


if __name__ == '__main__':
    css_code = tuple(input() for _ in range(int(input())))
    hex_color_code(css_code)
