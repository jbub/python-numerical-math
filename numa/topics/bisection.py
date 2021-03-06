# -*- coding: utf-8 -*-

"""
Metoda bisekcie (polenie intervalu).
"""

from numa import logger, float_input, expr_input, eval_expr


def bisection(a, b, fn, e):
    """
    S vyuzitim metody Bisekcie vypocita koren funkcie fn na intervale <a,b>.
    """

    assert a < b, 'Cislo b musi byt vacsie ako cislo a'
    assert e > 0, 'Presnost e musi byt vacsia ako nula'

    f = lambda x: eval_expr(fn, x=x)

    while True:
        # stred intervalu <a,b>
        x = 0.5 * (a + b)

        logger.info('a = {0}, b = {1}, x = {2}'.format(a, b, x))

        # skonci ak je stred intervalu
        # korenom funkcie inak uprav interval
        if f(x) == 0:
            return x
        elif f(a) * f(x) < 0:
            b = x
        else:
            a = x

        # skonci pri dosiahnuti presnosti
        if b - a <= e:
            return x


if __name__ == '__main__':
    a = float_input('Zadajte cislo a')
    b = float_input('Zadajte cislo b')
    fn = expr_input('Zadajte funkciu fn')
    e = float_input('Zadajte presnost e', default=0.01)

    r = bisection(a, b, fn, e)

    print('Koren je: {0}'.format(r))