# -*- coding: utf-8 -*-

"""
Gauss Seidelova methoda.
"""

from numa import logger, matrix_input, list_input, float_input
from numa.topics.jacobi import norm_error, list_as_float, check_norms


def gaussseidel(a, b, x, e):
    """
    S vyuzitim Gauss Seidelovej metody vypocita sustavu linearnych rovnic.
    Matica a reprezentuje lavu stranu sustavy, matica b vektor pravej
    strany a matica x reprezentuje vektor aproximacie.
    """

    assert a.rows == b.rows == len(b) == len(x), \
    'Rozmery matice "a" a pocet prvkov vo vektoroch "b" a "x" ' \
    'musi byt rovnaky'

    assert e > 0, 'Presnost e musi byt vacsia ako nula'

    assert check_norms(a), 'Matica nesplna konvergencne kriterium'

    # novy vektor aproximacie
    x1 = list(x)

    while True:
        for i in range(a.rows):
            sum_a = sum_b = 0

            for j in range(i):
                sum_a = a[i, j] * x1[j]

            for j in range(i + 1, a.rows):
                sum_b = a[i, j] * x[j]

            # vypocet dalsej aproximacie
            x1[i] = (1 / a[i, i]) * (b[i] - sum_a - sum_b)

        # vypocet rozdielu prvej a druhej aproximacie (norma)
        error = norm_error(x1, x)

        logger.info('x1 = {0}\nx = {1}\nerror = {2}\n'.format(
            list_as_float(x1), list_as_float(x), error))

        # skonci pri dosiahnuti presnosti
        if error <= e:
            return x1

        x = list(x1)


if __name__ == '__main__':
    a = matrix_input('Zadajte maticu a')
    b = list_input('Zadajte vektor pravej strany b')
    x = list_input('Zadajte vektor aproximacie x')
    e = float_input('Zadajte presnost e', default=0.01)

    r = gaussseidel(a, b, x, e)

    print('Vysledny vektor:\n{0}'.format(r))
