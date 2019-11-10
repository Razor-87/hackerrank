# -*- coding: utf-8 -*-
import re


def fun(s: str) -> bool:
    """
    >>> fun("lara@hackerrank.com")
    True
    >>> fun("britts_54@hackerrank.com")
    True
    >>> fun("harsh@gmail")
    False
    >>> fun("its@gmail.com1")
    False
    >>> fun("daniyal@gmail.coma")
    False
    >>> fun("learn.point@learningpoint.net")
    False
    """
    pattern = re.compile(r"^[\w-]{1,}@[a-zA-Z0-9]{1,}\.\w{1,3}$")
    return bool(pattern.match(s))
