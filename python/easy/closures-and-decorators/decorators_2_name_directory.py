# -*- coding: utf-8 -*-
from typing import Callable, Generator, List


def person_lister(f: Callable) -> Callable:
    """
    >>> print(*name_format([['Mike', 'Thomson', '20', 'M'],
    ... ['Robert', 'Bustle', '32', 'M'],
    ... ['Andria', 'Bustle', '30', 'F']]), sep='\\n')
    Mr. Mike Thomson
    Ms. Andria Bustle
    Mr. Robert Bustle
    """

    def inner(people: List[List[str]]) -> Generator:
        # return map(f, sorted(people, key=lambda l: int(l[2])))
        return (f(per) for per in sorted(people, key=lambda l: int(l[2])))

    return inner


@person_lister
def name_format(person):
    return ("Mr. "
            if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
