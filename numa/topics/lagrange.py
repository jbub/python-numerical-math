
from sympy import Symbol


def lagrange_base(i):
    """
    Vytvori i-tu lagrangeovu bazu polynomu.
    """
    x = Symbol('x')
    x_i = Symbol('x{0}'.format(i))
    x_next = Symbol('x{0}'.format(i + 1))
    x_prev = Symbol('x{0}'.format(max(0, i - 1)))

    print x, x_i, x_next, x_prev

    numer = (x - x_prev) * (x - x_next)
    denom = (x_i - x_prev) * (x_i - x_next)


    return numer / denom


if __name__ == '__main__':
    print lagrange_base(0)