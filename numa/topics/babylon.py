# -*- coding: utf-8 -*-

"""
Babylonian method.
"""

from sympy import Rational, Abs

from numa.utils import float_input, int_input


def babylon(n, old_approx, accuracy):
    """
    Calculates a square root of number using Babylonian method.
    """

    assert old_approx > 0, 'Aproximacia musi byt vacsia ako nula'

    while True:
        new_approx = Rational(1, 2) * (old_approx + n / old_approx)

        if Abs(new_approx - old_approx) < accuracy:
            return new_approx

        old_approx = new_approx


if __name__ == '__main__':
    n = int_input('Zadajte cislo')
    approx = float_input('Zadajte aproximaciu')
    accuracy = float_input('Zadajte presnost', default=0.01)

    print babylon(n, approx, accuracy)
