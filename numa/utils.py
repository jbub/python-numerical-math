# -*- coding: utf-8 -*-

from sympy import sympify, Basic, Float, Integer, Matrix
from sympy.core.sympify import SympifyError


def user_input(prompt, default=None):
    if default:
        prompt = '{0} [{1}]: '.format(prompt, default)
    else:
        prompt = '{0}: '.format(prompt)
    input = raw_input(prompt)
    return default if default else input


def float_input(prompt, default=None):
    while True:
        try:
            input = float(user_input(prompt, default))
        except ValueError:
            pass
        else:
            return Float(input)


def int_input(prompt, default=None):
    while True:
        try:
            input = int(user_input(prompt, default))
        except ValueError:
            pass
        else:
            return Integer(input)


def expr_input(prompt):
    while True:
        try:
            input = sympify(user_input(prompt, default=None))
        except SympifyError:
            pass
        else:
            return input


def matrix_input(prompt):
    while True:
        try:
            input = user_input(prompt, default=None)
            input = eval(input)
            if isinstance(input, list):
                input = Matrix(input)
            else:
                raise ValueError
        except StandardError:
            pass
        else:
            return input


def eval_expr(expr, **kwargs):
    assert isinstance(expr, Basic)
    return expr.subs(kwargs).evalf()
