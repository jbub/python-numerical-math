# -*- coding: utf-8 -*-

"""
Babylonian method.
"""

from sympy import Rational
from utils import float_input, int_input


def iterative_sqrt(n, old_approx, tolerance, precision):
    """
    Calculates a square root of number.
    """
    assert old_approx > 0, 'Aproximacia musi byt vacsia ako nula.'

    while True:
        new_approx = Rational(1, 2) * (old_approx + n / old_approx)
        new_approx = new_approx.evalf(precision)

        if abs(new_approx - old_approx) < tolerance:
            return new_approx

        old_approx = new_approx

if __name__ == '__main__':

    number = int_input('Zadajte cislo')
    approx = float_input('Zadajte aproximaciu')
    tolerance = float_input('Zadajte toleranciu', default=0.01)
    precision = int_input('Zadajte presnost', default=5)

    print iterative_sqrt(number, approx, tolerance, precision)
