# -*- coding: utf-8 -*-

"""
pr2.py -- Bisection method.
(c) 2012 Juraj Bubniak. BSD License.
"""

from __future__ import division
import math

__author__ = 'Juraj Bubniak'
__license__ = 'BSD'


def fn(x):
    """
    Calculates the value for given x.
    """
    return x + math.sin(x) - 2


def bisect(a, b, tolerance, precision=6):
    """
    Calculates the root of a function for a given interval.
    """
    assert a < b
    assert tolerance > 0

    while True:
        x = round(0.5 * (a + b), precision)

        if fn(x) == 0:
            return x

        if fn(a) * fn(x) < 0:
            b = x
        else:
            a = x

        if b - a <= tolerance:
            return x

if __name__ == '__main__':
    print bisect(1.1, 1.2, 0.01)
