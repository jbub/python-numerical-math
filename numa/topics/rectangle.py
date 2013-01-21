# -*- coding: utf-8 -*-

"""
Numericka Integracia - Obdlznikova metoda.
"""

from sympy import Abs
from numa import logger, float_input, int_input, expr_input, eval_expr


def rectangle(a, b, m, fn, e):
    """
    Na intervale <a,b>, ktory sa rozdeli na m obdlznikov, vypocita
    aproximaciu urciteho integralu funkcie fn.
    """

    assert a < b, 'Cislo b musi byt vacsie ako cislo a'
    assert e > 0, 'Presnost e musi byt vacsia ako nula'

    f = lambda x: eval_expr(fn, x=x)
    I = []
    J = 0
    k = 0

    # rozdelenie intervalu na m rovnako dlhych dielov
    h = (b - a) / m

    for i in range(1, m):
        J += f(((a + (i * h)) + (a + h * (i + 1))) / 2)

    I.append(h * J)

    while True:
        J = 0

        # skratenie intervalu na polovicu
        h /= 2

        for i in range(1, m):
            J += f(((a + (h * i)) + (a + h * (i + 1))) / 2)

        I.append(h * J)

        logger.info(
            'h = {0}, I[k] = {1}, I[k] - I[k + 1] = {2}'.format(h, I[k], I[k] - I[k + 1]))

        # skonci pri dosiahnuti presnosti
        if Abs(I[k] - I[k + 1]) <= e:
            return I[k]

        k += 1


if __name__ == '__main__':
    a = float_input('Zadajte cislo a')
    b = float_input('Zadajte cislo b')
    m = int_input('Zadajte pocet delenia intervalu m')
    fn = expr_input('Zadajte funkciu fn')
    e = float_input('Zadajte presnost e', default=0.01)

    print rectangle(a, b, m, fn, e)
