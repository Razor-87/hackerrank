# -*- coding: utf-8 -*-
from typing import List


def is_vowel(letter: str) -> bool:
    """
    >>> is_vowel('e')
    True
    >>> is_vowel('b')
    False
    """
    return letter in {'a', 'e', 'i', 'o', 'u', 'y'}


def score_words(words: List[str]) -> int:
    """
    >>> score_words(['hacker', 'book'])
    4
    >>> score_words(['programming', 'is', 'awesome'])
    4
    """
    score = 0
    for word in words:
        score += 2 if not (sum(is_vowel(letter) for letter in word) & 1) else 1
    return score
