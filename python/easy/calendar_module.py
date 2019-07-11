# -*- coding: utf-8 -*-


def calendar_module(raw_str: str) -> str:
    """
    >>> calendar_module('08 05 2015')
    'WEDNESDAY'
    """
    import calendar
    month, day, year = map(int, raw_str.split())
    num_day = calendar.weekday(year, month, day)
    name_day = calendar.day_name[num_day].upper()
    return name_day


if __name__ == '__main__':
    import sys
    raw_str = sys.stdin.readline()
    print(calendar_module(raw_str))
