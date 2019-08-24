# -*- coding: utf-8 -*-


def is_leap(year: int) -> bool:
    """
    >>> is_leap(1990)
    False
    >>> is_leap(4)
    True
    >>> is_leap(2000)
    True
    >>> is_leap(1999)
    False
    """
    # if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    #     return True
    # return False
    import calendar
    return calendar.isleap(year)
