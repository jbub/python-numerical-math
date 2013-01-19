# -*- coding: utf-8 -*-

"""
Newtonova metoda (metoda dotycnic).
"""

from sympy import diff, Abs
from numa.utils import float_input, expr_input, eval_expr


def newton(a, b, fn, e):
    """
    S vyuzitim Newtonovej metody vypocita koren funkcie fn na intervale <a,b>.
    """

    assert a < b, 'Cislo b musi byt vacsie ako cislo a'
    assert e > 0, 'Presnost e musi byt vacsia ako nula'

    # urci prvu a druhu derivaciu funkcie
    fn_d1 = diff(fn)
    fn_d2 = diff(fn_d1)

    f = lambda x: eval_expr(fn, x=x)
    fd = lambda x: eval_expr(fn_d1, x=x)
    fd2 = lambda x: eval_expr(fn_d2, x=x)

    if f(a) * fd2(a) > 0:
        x = a
    elif f(b) * fd2(b) > 0:
        x = b
    else:
        raise ValueError('jeden z bodov a alebo b musi '
                         'splnat podmienku f(x) * fd2(x) > 0')

    while True:
        x1 = x - f(x) / fd(x)

        # skonci pri dosiahnuti presnosti
        if Abs(x1 - x) <= e:
            return x1


if __name__ == '__main__':
    a = float_input('Zadajte cislo a')
    b = float_input('Zadajte cislo b')
    fn = expr_input('Zadajte funkciu fn')
    e = float_input('Zadajte presnost e', default=0.01)

    print newton(a, b, fn, e)