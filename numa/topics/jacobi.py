# -*- coding: utf-8 -*-

"""
Jacobiho methoda.
"""

from math import sqrt
from sympy.matrices.matrices import Matrix
from numa import logger, matrix_input, float_input, list_input


def iterative_form(m):
    """
    Prevedie maticu na iteracny tvar.
    """
    n = Matrix(m.rows, m.rows, lambda i, j: 0)

    for i in range(m.rows):
        for j in range(m.rows):
            n[i, j] = -1 * m[i, j] / m[i, i]

            if i == j:
                n[i, j] = 0
    return n


def row_norm(m):
    """
    Vypocita riadkovu normu matice m.
    """
    parts = []
    for row in range(m.rows):
        parts.append(sum(filter(abs, m.row(row))))
    return max(parts)


def col_norm(m):
    """
    Vypocita stlpcovu normu matice m.
    """
    parts = []
    for col in range(m.cols):
        parts.append(sum(filter(abs, m.col(col))))
    return max(parts)


def euclid_norm(m):
    """
    Vypocita euklidovu normu matice m.
    """
    sum = 0
    for r in range(m.rows):
        for c in range(m.cols):
            sum += m[r, c] ** 2
    return sqrt(sum)


def check_norms(m):
    """
    Vrati ci matica splna konvergencne kriterium. Teda ci aspon
    jedna z noriem je mensie ako jedna.
    """
    m = iterative_form(m)
    return row_norm(m) < 1 or col_norm(m) < 1 or euclid_norm(m) < 1


def list_as_float(l):
    """
    Vrati list ktoreho hodnoty prevedie na float.
    """
    return [float(i) for i in l]


def norm_error(x1, x):
    """
    Vypocita rozdiel prvej a druhej aproximacie (norma).
    """
    z = []
    for xa, xb in zip(x1, x):
        z.append(abs(xa - xb))
    return max(z)


def jacobi(a, b, x, e):
    """
    S vyuzitim Jacobiho metody vypocita sustavu linearnych rovnic.
    Matica a reprezentuje lavu stranu sustavy, matica b vektor pravej
    strany a matica x reprezentuje vektor aproximacie.

    Priklad:

    Nevyhovujuca:
    a = Matrix((
        [1,1,-3],
        [2,5,1],
        [4,-1,2],
    ))
    b = [-4,5,-12]

    Vyhovujuca:
    a = Matrix((
        [11,2,1],
        [1,10,2],
        [2,3,-8],
    ))
    b = [15,16,1]
    """

    assert a.rows == len(b) == len(x),\
    'Rozmery matice "a" a pocet prvkov vo vektoroch "b" a "x" '\
    'musi byt rovnaky'

    assert e > 0, 'Presnost e musi byt vacsia ako nula'

    assert check_norms(a), 'Matica nesplna konvergencne kriterium'

    # novy vektor aproximacie
    x1 = list(x)

    while True:
        for i in range(a.rows):
            sum_a = sum_b = 0

            for j in range(i):
                sum_a += a[i, j] * x[j]

            for j in range(i + 1, a.rows):
                sum_b += a[i, j] * x[j]

            # vypocet dalsej aproximacie
            x1[i] = (1 / a[i, i]) * (b[i] - sum_a - sum_b)

        # vypocet rozdielu prvej a druhej aproximacie (norma)
        error = norm_error(x1, x)

        logger.info('x1 = {0}\nx = {1}\nerror = {2}\n'.format(
            list_as_float(x1), list_as_float(x), float(error)))

        # skonci pri dosiahnuti presnosti
        if error <= e:
            return list_as_float(x1)

        x = list(x1)


if __name__ == '__main__':
    """
    a = matrix_input('Zadajte maticu a')
    b = list_input('Zadajte vektor pravej strany b')
    x = list_input('Zadajte vektor aproximacie x')
    e = float_input('Zadajte presnost e', default=0.01)
    """
    a = Matrix((
        [11,2,1],
        [1,10,2],
        [2,3,-8],
        ))
    b = [15,16,1]
    x = [0,0,0]
    e = 0.01

    r = jacobi(a, b, x, e)

    print('Vysledny vektor:\n{0}'.format(r))