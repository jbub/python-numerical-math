# -*- coding: utf-8 -*-

"""
Lagrangeov interpolacny polynom.
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


def evaluate_base(base, n, x):
    """
    Dosadi hodnoty x do bazy.
    """
    values = {}

    for i, value in enumerate(x):
        values['x{0}'.format(i)] = value

    return base.subs(values).evalf()


def lagrange(x, fx):
    """
    Vypocita Lagrangeov interpolacny polynom.
    """

    # pocet x
    n = len(x)

    # casti polynomu
    poly = []

    assert n == len(fx), 'Dlzka listov x a fx musi byt rovnaka'

    for i in range(n):
        # zostroji bazu
        base = lagrange_base(n - 1, i)

        # dosadi do bazy hodnoty x
        base_eval = evaluate_base(base, n, x)

        # prida cast polynomu
        poly.append(str(fx[i]) + ' * ' + str(base_eval))

    return ' + '.join(poly)


if __name__ == '__main__':
    x = list_input('Zadajte zoznam hodnot x')
    fx = list_input('Zadajte zoznam funkcnych hodnot fx')

    r = lagrange(x, fx)

    print('Polynom je:\n{0}'.format(r))