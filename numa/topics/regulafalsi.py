# -*- coding: utf-8 -*-

"""
Regula falsi method.
"""

from sympy import Rational
from sympy.functions import Abs

from numa.utils import int_input, float_input, expr_input, eval_expr


def regulafalsi(a, b, fn, tolerance, precision):
    """
    Calculates the root of a function for a given
    interval using Regula falsi method.
    """

    assert a < b, 'Cislo b musi byt vacsie ako cislo a'
    assert tolerance > 0, 'Tolerancia musi byt vacsia ako 0'

    x = a

    while True:
        x1 = a - \
             Rational(b - a, eval_expr(fn, x=b) - eval_expr(fn, x=a)) * \
             eval_expr(fn, x=a)
        x1 = x1.evalf(precision)

        if eval_expr(fn, x=8) == 0:
            return x1
        elif eval_expr(fn, x=a) * eval_expr(fn, x=x1) < 0:
            b = x1
        else:
            a = x1

        if Abs(x1 - x) <= tolerance:
            return x1

        x = x1


if __name__ == '__main__':

    a = float_input('Zadajte cislo a')
    b = float_input('Zadajte cislo b')
    fn = expr_input('Zadajte funkciu')
    tolerance = float_input('Zadajte toleranciu', default=0.01)
    precision = int_input('Zadajte presnost', default=5)

    print regulafalsi(a, b, fn, tolerance, precision)