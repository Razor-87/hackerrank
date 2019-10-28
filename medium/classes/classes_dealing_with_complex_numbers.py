# -*- coding: utf-8 -*-
from __future__ import annotations


class Complex:
    """
    >>> x, y = Complex(2, 1), Complex(5, 6)
    >>> print(*(x+y, x-y, x*y, x/y, x.mod(), y.mod()), sep='\\n')
    7.00+7.00i
    -3.00-5.00i
    4.00+17.00i
    0.26-0.11i
    2.24+0.00i
    7.81+0.00i
    """

    def __init__(self, real: float, imag: float) -> None:
        self.real = real
        self.imag = imag

    def __add__(self, other: Complex) -> Complex:
        real_sum = self.real + other.real
        imag_sum = self.imag + other.imag
        return Complex(real_sum, imag_sum)

    def __sub__(self, other: Complex) -> Complex:
        real_diff = self.real - other.real
        imag_diff = self.imag - other.imag
        return Complex(real_diff, imag_diff)

    def __mul__(self, other: Complex) -> Complex:
        real_prod = (self.real * other.real - self.imag * other.imag)
        imag_prod = (self.real * other.imag + self.imag * other.real)
        return Complex(real_prod, imag_prod)

    def __truediv__(self, other: Complex) -> Complex:
        conjugate = Complex(other.real, -1 * other.imag)
        return (self * conjugate * Complex(1.0 / (other.mod().real)**2, 0))

    def mod(self) -> Complex:
        return Complex(((self.real**2 + self.imag**2)**0.5), 0)

    def __str__(self) -> str:
        return f"{self.real:.2f}{self.imag:+.2f}i"
