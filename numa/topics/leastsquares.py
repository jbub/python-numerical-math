# -*- coding: utf-8 -*-

"""
Metoda najmensich stvorcov.
"""

from numa import logger, list_input
from numa.topics.jacobi import jacobi
from sympy import Matrix


def leastsquares(x, fx):
    """
    S vyuzitim metody najmensich stvorcov urci priamku
    blizko predpisanym hodnotam.
    """

    # pocet x
    n = len(x)

    assert n == len(fx), 'Dlzka listov x a fx musi byt rovnaka'

    # suma 1 * n
    sum_1 = n

    # suma vsetkych x
    sum_x = sum(x)

    # suma vsetkych mocnin x
    sum_x2 = sum([i**2 for i in x])

    # suma vsetkych fx
    sum_fx = sum(fx)

    # suma vsetkych x * fx
    sum_x_fx = sum(xi * fxi for xi, fxi in zip(x, fx))

    logger.info(
        'sum_1 = {0}, sum_x = {1}, sum_x2 = {2}, sum_fx = {3}, sum_x_fx = {4}'
        .format(sum_1, sum_x, sum_x2, sum_fx, sum_x_fx))

    # lava strana sustavy
    a = Matrix((
        [sum_1, sum_x],
        [sum_x, sum_x2],
    ))

    # prava strana sustavy
    b = [sum_fx, sum_x_fx]

    # aproximacia riesenia pre jacobiho metodu
    x = [0, 0]

    # jacobiho metodou vypocita sustavu
    c1, c2 = jacobi(a, b, x, e=0.01)

    return '{0} + {1}x'.format(c1, c2)


if __name__ == '__main__':
    x = list_input('Zadajte zoznam hodnot x')
    fx = list_input('Zadajte zoznam funkcnych hodnot fx')

    r = leastsquares(x, fx)

    print('Priamka:\n{0}'.format(r))