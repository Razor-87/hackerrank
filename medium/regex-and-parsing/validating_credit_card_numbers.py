# -*- coding: utf-8 -*-
import re
from typing import List


def validator(arr: List[str]) -> List[str]:
    """
    >>> validator(['4123456789123456', '5123-4567-8912-3456',
    ... '61234-567-8912-3456', '4123356789123456',
    ... '5133-3367-8912-3456', '5123 - 3567 - 8912 - 3456'])
    ['Valid', 'Valid', 'Invalid', 'Valid', 'Invalid', 'Invalid']
    """
    pattern = re.compile(r"^(?!.*(\d)(-?\1){3})[456]\d{3}(?:-?\d{4}){3}$")
    return ["Valid" if pattern.match(row.strip()) else "Invalid"
            for row in arr]


if __name__ == '__main__':
    arr = [input() for _ in range(int(input()))]
    print(*validator(arr), sep='\n')
