# -*- coding: utf-8 -*-


def time_conversion(raw_time: str) -> str:
    """
    >>> time_conversion('07:05:45PM')
    '19:05:45'
    >>> time_conversion('12:40:22AM')
    '00:40:22'
    >>> time_conversion('12:45:54PM')
    '12:45:54'
    """
    time, time_format = raw_time[:-2], raw_time[-2:]
    hours, mins_secs, start_twelve = time[:2], time[2:], time.startswith('12')
    # if time_format == 'AM':
    #     return f"00{mins_secs}" if start_twelve else time
    # return time if start_twelve else f"{int(hours) + 12}{mins_secs}"
    if time_format == 'AM' and start_twelve:
        return f"00{mins_secs}"
    elif time_format == 'PM' and not start_twelve:
        return f"{int(hours) + 12}{mins_secs}"
    return time


if __name__ == '__main__':
    print(time_conversion(input()))
