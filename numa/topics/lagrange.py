# -*- coding: utf-8 -*-

"""
Lagrangeov polynom.
"""

from numa import list_input
from sympy import sympify


def next_symbol_index(n, exclude, j):
    """
    Vrati index symbolu pre pouzitie v aktualnej iteracii.
    """
    choices = [x for x in range(n + 1) if x != exclude]
    return choices[j]


def lagrange_base(n, i):
    """
    Vytvori Lagrangeovu bazu n-teho stupna.
    """

    up = '(x - x{0})'
    bt = '(x{0} - x{1})'
    enume, denom = [], []

    # nalpn postupne listy citatelov a menovatelov
    for j in range(n):

        k = next_symbol_index(n, i, j)

        enume.append(up.format(k))
        denom.append(bt.format(i, k))

    # spoji listy nasobenim do stringu a prevedie do vyrazu
    d = sympify(' * '.join(enume))
    e = sympify(' * '.join(denom))

    return d / e


def lagrange(x, fx):
    pass


if __name__ == '__main__':
    x = list_input('Zadajte cislo a')
    fx = list_input('Zadajte cislo b')

    r = lagrange(x, fx)

    print('Polynom je: {0}'.format(r))