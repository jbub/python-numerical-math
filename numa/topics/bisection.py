# -*- coding: utf-8 -*-

"""
Bisection method.
"""

from sympy import Rational

from numa.utils import float_input, expr_input, eval_expr


def bisection(a, b, fn, accuracy):
    """
    Calculates the root of a function for a given
    interval using Bisection method.
    """

    assert a < b, 'Cislo b musi byt vacsie ako cislo a'

    f = lambda x: eval_expr(fn, x=x)

    while True:
        x = Rational(1, 2) * (a + b)

        if f(x) == 0:
            return x
        elif f(a) * f(x) < 0:
            b = x
        else:
            a = x

        if b - a <= accuracy:
            return x


if __name__ == '__main__':
    a = float_input('Zadajte cislo a')
    b = float_input('Zadajte cislo b')
    fn = expr_input('Zadajte funkciu')
    accuracy = float_input('Zadajte presnost', default=0.01)

    print bisection(a, b, fn, accuracy)
