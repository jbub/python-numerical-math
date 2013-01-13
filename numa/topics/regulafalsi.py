# -*- coding: utf-8 -*-

"""
Regula falsi method.
"""

from sympy.functions import Abs

from numa.utils import int_input, float_input, expr_input, eval_expr


def regulafalsi(a, b, fn, accuracy, digits):
    """
    Calculates the root of a function for a given
    interval using Regula falsi method.
    """

    assert a < b, 'Cislo b musi byt vacsie ako cislo a'

    x = a
    f = lambda x: eval_expr(fn, x=x)

    while True:
        x1 = a - ((b - a) / (f(b) - f(a)) * f(a))
        x1 = x1.evalf(digits)

        if f(x1) == 0:
            return x1
        elif f(a) * f(x1) < 0:
            b = x1
        else:
            a = x1

        if Abs(x1 - x) <= accuracy:
            return x1

        x = x1


if __name__ == '__main__':

    a = float_input('Zadajte cislo a')
    b = float_input('Zadajte cislo b')
    fn = expr_input('Zadajte funkciu')
    accuracy = float_input('Zadajte presnost', default=0.01)
    digits = int_input('Zadajte pocet desatinnych miest', default=5)

    print regulafalsi(a, b, fn, accuracy, digits)