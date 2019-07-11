# -*- coding: utf-8 -*-


def say_hello_world(phrase: str = 'Hello, World!') -> None:
    """
    >>> say_hello_world()
    Hello, World!
    """
    print(phrase)


if __name__ == '__main__':
    say_hello_world()
