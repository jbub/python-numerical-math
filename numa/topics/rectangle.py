# -*- coding: utf-8 -*-

"""
Integracia - Obdlznikova metoda.
"""

from sympy import Abs

from numa.utils import float_input, int_input, expr_input, eval_expr


def rectangle(a, b, m, fn, accuracy):
    """
    Na intervale <a,b>, ktory sa rozdeli na m obdlznikov, vypocita
    aproximaciu urciteho integralu funkcie fn.
    """

    assert a < b, 'Cislo b musi byt vacsie ako cislo a'
    assert accuracy > 0, 'Presnost musi byt vacsia ako nula'

    f = lambda x: eval_expr(fn, x=x)
    h = (b - a) / m
    I = []
    J = 0
    k = 0

    for i in range(1, m):
        J += f(((a + (i * h)) + (a + h * (i + 1))) / 2)

    I.append(h * J)

    while True:
        J = 0
        h /= 2

        for i in range(1, m):
            J += f(((a + (h * i)) + (a + h * (i + 1))) / 2)

        I.append(h * J)

        if Abs(I[k] - I[k + 1]) <= accuracy:
            return I[k]

        k += 1


if __name__ == '__main__':
    a = float_input('Zadajte cislo a')
    b = float_input('Zadajte cislo b')
    m = int_input('Zadajte pocet delenia intervalu m')
    fn = expr_input('Zadajte funkciu')
    accuracy = float_input('Zadajte presnost', default=0.01)

    print rectangle(a, b, m, fn, accuracy)
