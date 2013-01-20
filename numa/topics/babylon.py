# -*- coding: utf-8 -*-

"""
Babylonska metoda.
"""

from sympy import Abs
from numa import logger, float_input, int_input


def babylon(n, x0, e):
    """
    S vyuzitim Babylonskej metody vypocita odmocninu cisla n.
    """

    assert n > 0, 'Cislo n musi byt vacsie ako nula'
    assert x0 > 0, 'Pociatocna hodnota x0 musi byt vacsia ako nula'
    assert e > 0, 'Presnost e musi byt vacsia ako nula'

    while True:
        # nova aproximacia je priemerom hodnot x0 a n / x0
        x = 0.5 * (x0 + n / x0)

        logger.info(
            'x = {}, x0 = {}, Abs(x - x0) = {}'.format(x, x0, Abs(x - x0)))

        # skonci ak je dosiahnuta pozadovana presnost
        if Abs(x - x0) < e:
            return x

        x0 = x


if __name__ == '__main__':
    n = int_input('Zadajte cislo n')
    x0 = float_input('Zadajte pociatocnu hodnotu x0')
    e = float_input('Zadajte presnost e', default=0.01)

    r = babylon(n, x0, e)

    print('Odmocnina je: {}'.format(r))
