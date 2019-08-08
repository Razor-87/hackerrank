# -*- coding: utf-8 -*-


def time_delta(t1: str, t2: str, fmt='%a %d %b %Y %X %z') -> int:
    """
    >>> time_delta('Sun 10 May 2015 13:54:36 -0700',
    ... 'Sun 10 May 2015 13:54:36 -0000')
    25200
    >>> time_delta('Sat 02 May 2015 19:54:36 +0530',
    ... 'Fri 01 May 2015 13:54:36 -0000')
    88200
    >>> time_delta('Wed 12 May 2269 23:22:15 -0500',
    ... 'Tue 05 Oct 2269 02:12:07 -0200')
    12527392
    """
    from datetime import datetime
    dt1, dt2 = datetime.strptime(t1, fmt), datetime.strptime(t2, fmt)
    delta = dt1 - dt2
    return abs(int(delta.total_seconds()))
