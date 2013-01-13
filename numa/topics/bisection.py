# -*- coding: utf-8 -*-

"""
Bisection method.
"""

from sympy import Rational

from numa.utils import int_input, float_input, expr_input, eval_expr


def bisection(a, b, fn, tolerance, precision):
    """
    Calculates the root of a function for a given
    interval using Bisection method.
    """

    assert a < b, 'Cislo b musi byt vacsie ako cislo a'
    assert tolerance > 0, 'Tolerancia musi byt vacsia ako 0'

    while True:
        x = Rational(1, 2) * (a + b)
        x = x.evalf(precision)

        if eval_expr(fn, x=x) == 0:
            return x

        if eval_expr(fn, x=a) * eval_expr(fn, x=a) < 0:
            b = x
        else:
            a = x

        if b - a <= tolerance:
            return x


if __name__ == '__main__':

    a = float_input('Zadajte cislo a')
    b = float_input('Zadajte cislo b')
    fn = expr_input('Zadajte funkciu')
    tolerance = float_input('Zadajte toleranciu', default=0.01)
    precision = int_input('Zadajte presnost', default=5)

    print bisection(a, b, fn, tolerance, precision)
