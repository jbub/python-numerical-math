# -*- coding: utf-8 -*-

"""
Gauss Seidelova methoda.
"""

from numa import logger, matrix_input, float_input
from numa.topics.jacobi import norm_error


def gaussseidel(a, b, x, e):
    """
    S vyuzitim Gauss Seidelovej metody vypocita sustavu linearnych rovnic.
    Matica a reprezentuje lavu stranu sustavy, matica b vektor pravej
    strany a matica x reprezentuje vektor aproximacie.
    """

    assert a.rows == b.rows == x.rows,\
    'Pocet riadkov matic "a", "b" a "x" musi byt rovnaky'

    assert b.cols == x.cols == 1,\
    'Pocet stlpcov matic "b" a "x" musi byt 1'

    assert e > 0, 'Presnost e musi byt vacsia ako nula'

    # novy vektor aproximacie
    x1 = x.clone()

    while True:
        for i in range(a.rows):
            sum_a = sum_b = 0

            for j in range(i):
                sum_a = a[i, j] * x1[j, 0]

            for j in range(i + 1, a.rows):
                sum_b = a[i, j] * x[j, 0]

            # vypocet dalsej aproximacie
            x1[i, 0] = 1 / a[i, i] * (b[i, 0] - sum_a - sum_b)

        # vypocet rozdielu prvej a druhej aproximacie (norma)
        error = norm_error(x1, x)

        logger.info('x1 = {}\nx = {}\nerror = {}\n'.format(
            x1.tolist(), x.tolist(), error))

        # skonci pri dosiahnuti presnosti
        if error <= e:
            return x1

        x = x1.clone()


if __name__ == '__main__':
    a = matrix_input('Zadajte maticu a')
    b = matrix_input('Zadajte vektor pravej strany b')
    x = matrix_input('Zadajte vektor aproximacie x')
    e = float_input('Zadajte presnost e', default=0.01)

    r = gaussseidel(a, b, x, e)

    print('Vysledny vektor:\n{}'.format(r))
