# -*- coding: utf-8 -*-
from typing import List


def a_very_big_sum(nums: List[int]) -> int:
    """
    >>> a_very_big_sum([1000000001, 1000000002,
    ... 1000000003, 1000000004, 1000000005])
    5000000015
    """
    ret = sum(nums)
    return ret


if __name__ == '__main__':
    _, nums = input(), [*map(int, input().split())]
    print(a_very_big_sum(nums))
