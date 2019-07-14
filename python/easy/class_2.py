# -*- coding: utf-8 -*-
from __future__ import annotations


class Points():
    """
    >>> a, b, c, d = (Points(0.0, 4.0, 5.0), Points(1.0, 7.0, 6.0),
    ... Points(0.0, 5.0, 9.0), Points(1.0, 7.0, 2.0))
    >>> x, y = (b - a).cross(c - b), (c - b).cross(d - c)
    >>> import math; angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))
    >>> print(f"{math.degrees(angle):.2f}")
    8.19
    """

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no: Points) -> Points:
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no: Points) -> float:
        return self.x*no.x + self.y*no.y + self.z*no.z

    def cross(self, no: Points) -> Points:
        return Points(self.y*no.z - self.z*no.y,
                      self.z*no.x - self.x*no.z,
                      self.x*no.y - self.y*no.x)

    def absolute(self) -> float:
        return pow((self.x**2 + self.y**2 + self.z**2), 0.5)
