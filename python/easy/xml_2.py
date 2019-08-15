# -*- coding: utf-8 -*-

maxdepth = 0


def depth(elem, level) -> None:
    global maxdepth
    maxdepth = max(maxdepth, level + 1)
    for child in elem:
        depth(child, level + 1)
