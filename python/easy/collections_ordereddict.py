# -*- coding: utf-8 -*-
from typing import Dict, Tuple


def collections_ordereddict(arr: Tuple[str, ...]) -> None:
    """
    >>> collections_ordereddict(('BANANA FRIES 12', 'POTATO CHIPS 30',
    ... 'APPLE JUICE 10', 'CANDY 5', 'APPLE JUICE 10', 'CANDY 5',
    ... 'CANDY 5', 'CANDY 5', 'POTATO CHIPS 30'))
    BANANA FRIES 12
    POTATO CHIPS 60
    APPLE JUICE 20
    CANDY 20
    """
    d: Dict[str, int] = {}
    for el in arr:
        inp = el.split()
        name, price = ' '.join(inp[:-1]), int(inp[-1])
        d[name] = d.get(name, 0) + int(price)
    for k, v in d.items():
        print(k, v)


if __name__ == '__main__':
    arr = tuple(input() for _ in range(int(input())))
    collections_ordereddict(arr)
