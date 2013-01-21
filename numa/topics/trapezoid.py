# -*- coding: utf-8 -*-

"""
Numericka Integracia - Lichobeznikova metoda.
"""

from sympy import Abs
from numa import logger, float_input, int_input, expr_input, eval_expr


def trapezoid(a, b, m, fn, e):
    """
    Na intervale <a,b>, ktory sa rozdeli na m lichobeznikov, vypocita
    aproximaciu urciteho integralu funkcie fn.
    """

    assert a < b, 'Cislo b musi byt vacsie ako cislo a'
    assert e > 0, 'Presnost e musi byt vacsia ako nula'

    f = lambda x: eval_expr(fn, x=x)
    I = []
    J1 = 0
    J2 = 0
    k = 0

    # rozdelenie intervalu na m rovnako dlhych dielov
    h = (b - a) / m

    for i in range(m):
        J1 += f(a + (h * i))
        J2 += f(a + h * (i + 1))

    I.append((h / 2) * (J1 + J2))

    while True:
        J1 = 0
        J2 = 0
        m *= 2

        # skratenie intervalu na polovicu
        h /= 2

        for i in range(m):
            J1 += f(a + (h * i))
            J2 += f(a + h * (i + 1))

        I.append((h / 2) * (J1 + J2))

        logger.info('m = {0}, h = {1}, Abs(I[k] - I[k + 1]) = {2}'.format(
            m, h, I[k] - I[k + 1]))

        # skonci pri dosiahnuti presnosti
        if Abs(I[k] - I[k + 1]) <= e:
            return I[k + 1]

        k += 1


if __name__ == '__main__':
    a = float_input('Zadajte cislo a')
    b = float_input('Zadajte cislo b')
    m = int_input('Zadajte pocet delenia intervalu m')
    fn = expr_input('Zadajte funkciu fn')
    e = float_input('Zadajte presnost e', default=0.01)

    r = trapezoid(a, b, m, fn, e)

    print('Aproximacia je: {0}'.format(r))
