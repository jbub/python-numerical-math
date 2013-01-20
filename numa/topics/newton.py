# -*- coding: utf-8 -*-

"""
Newtonova metoda (metoda dotycnic).
"""

from sympy import diff, Abs
from numa import logger, float_input, expr_input, eval_expr


def newton(a, b, fn, e):
    """
    S vyuzitim Newtonovej metody vypocita koren funkcie fn na intervale <a,b>.
    """

    assert a < b, 'Cislo b musi byt vacsie ako cislo a'
    assert e > 0, 'Presnost e musi byt vacsia ako nula'

    # urci prvu a druhu derivaciu funkcie
    fn_d1 = diff(fn)
    fn_d2 = diff(fn_d1)

    logger.info('fn_d1 = {}, fn_d2 = {}'.format(fn_d1, fn_d2))

    f = lambda x: eval_expr(fn, x=x)
    fd = lambda x: eval_expr(fn_d1, x=x)
    fd2 = lambda x: eval_expr(fn_d2, x=x)

    # aspon jeden z bodov musi splnit podmienku
    # inak je potrebne upravit interval
    if f(a) * fd2(a) > 0:
        x = a
    elif f(b) * fd2(b) > 0:
        x = b
    else:
        raise ValueError('aspon jeden z bodov a alebo b musi '
                         'splnat podmienku f(x) * fd2(x) > 0')

    while True:
        # vypocet priesecnika s osou x
        x1 = x - f(x) / fd(x)

        logger.info(
            'x = {}, x1 = {}, Abs(x1 - x) = {}'.format(x, x1, Abs(x1 - x)))

        # skonci pri dosiahnuti presnosti
        if Abs(x1 - x) <= e:
            return x1

        x = x1


if __name__ == '__main__':
    a = float_input('Zadajte cislo a')
    b = float_input('Zadajte cislo b')
    fn = expr_input('Zadajte funkciu fn')
    e = float_input('Zadajte presnost e', default=0.01)

    r = newton(a, b, fn, e)

    print('Koren je: {}'.format(r))