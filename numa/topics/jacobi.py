# -*- coding: utf-8 -*-

"""
Jacobi method.
"""

from sympy import diff, Abs

from numa.utils import matrix_input, float_input, int_input, expr_input


def jacobi(a, b, x, accuracy):
    """
    Calculates the solutions of a system of linear
    equations using Jacobi method.
    """

    assert a.rows == b.rows == x.rows, \
    'Pocet riadkov matic "a", "b" a "c" musi byt rovnaky'

    assert b.cols == x.cols == 1,\
    'Pocet stlpcov matic "b" a "x" musi byt 1'

    x_list = x.tolist()

    while True:
        for i in range(a.rows):
            sum_a = sum_b = 0

            for j in range(i):
                sum_a += a[i, j] * x[j]

            for j in range(i + 1, a.rows):
                sum_b += a[i, j] * x[j]

            x_list[i] = 1.0 / a[i][i] * (b[i] - sum_a - sum_b)

        temp = zip(x_list, x.tolist())
        error = max([abs(item[0] - item[1]) for item in temp])

        if error <= accuracy:
            return x_list

        x = x.tolist()


if __name__ == '__main__':
    a = matrix_input('Zadajte maticu a')
    b = matrix_input('Zadajte vektor pravej strany b')
    x = matrix_input('Zadajte aproximaciu x')
    accuracy = float_input('Zadajte presnost', default=0.01)

    print jacobi(a, b, x, accuracy)