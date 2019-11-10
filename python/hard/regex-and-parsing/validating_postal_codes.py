# -*- coding: utf-8 -*-
import re

regex_integer_in_range = r"^[1-9][\d]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"


def test_validator(p: str) -> bool:
    """
    >>> test_validator("110000")
    False
    >>> test_validator("137370")
    False
    >>> test_validator("101201")
    True
    """
    return bool(re.match(
        regex_integer_in_range,
        p)) and len(re.findall(regex_alternating_repetitive_digit_pair, p)) < 2
