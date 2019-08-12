# -*- coding: utf-8 -*-
from typing import Optional


def say_hello_world(phrase: Optional[str] = 'Hello, World!') -> None:
    """
    >>> say_hello_world()
    Hello, World!
    >>> say_hello_world('Hello!')
    Hello!
    """
    print(phrase)


if __name__ == '__main__':
    say_hello_world()
