# -*- coding: utf-8 -*-
from typing import Callable, List


def wrapper(f: Callable) -> Callable:
    """
    >>> sort_phone(['07895462130', '919875641230', '9195969878'])
    +91 78954 62130
    +91 91959 69878
    +91 98756 41230
    """

    def fun(lst: List[str]) -> Callable[[List[str]], list]:
        fixed_lst = (f'+91 {el[-10:-5]} {el[-5:]}' for el in lst)
        return f(fixed_lst)

    return fun


@wrapper
def sort_phone(l: List[str]) -> None:
    print(*sorted(l), sep='\n')
