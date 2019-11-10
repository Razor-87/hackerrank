# -*- coding: utf-8 -*-


def text_alignment(thickness: int, c: str = 'H') -> None:
    """
    >>> text_alignment(5) #doctest: +NORMALIZE_WHITESPACE
        H
       HHH
      HHHHH
     HHHHHHH
    HHHHHHHHH
      HHHHH               HHHHH
      HHHHH               HHHHH
      HHHHH               HHHHH
      HHHHH               HHHHH
      HHHHH               HHHHH
      HHHHH               HHHHH
      HHHHHHHHHHHHHHHHHHHHHHHHH
      HHHHHHHHHHHHHHHHHHHHHHHHH
      HHHHHHHHHHHHHHHHHHHHHHHHH
      HHHHH               HHHHH
      HHHHH               HHHHH
      HHHHH               HHHHH
      HHHHH               HHHHH
      HHHHH               HHHHH
      HHHHH               HHHHH
                        HHHHHHHHH
                         HHHHHHH
                          HHHHH
                           HHH
                            H
    """
    # Top Cone
    for i in range(thickness):
        print((c * i).rjust(thickness - 1),
              c, (c * i).ljust(thickness - 1),
              sep='')
    # Top Pillars
    for _ in range(thickness + 1):
        print((c * thickness).center(thickness * 2),
              (c * thickness).center(thickness * 6),
              sep='')
    # Middle Belt
    for _ in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))
    # Bottom Pillars
    for _ in range(thickness + 1):
        print((c * thickness).center(thickness * 2),
              (c * thickness).center(thickness * 6),
              sep='')
    # Bottom Cone
    for i in range(thickness):
        print(
            ((c * (thickness - i - 1)).rjust(thickness) + c +
             (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))


if __name__ == '__main__':
    thickness = int(input())
    text_alignment(thickness)
