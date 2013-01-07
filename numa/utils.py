# -*- coding: utf-8 -*-

from sympy import sympify, Basic, Float, Integer
from sympy.core.sympify import SympifyError


def user_input(prompt, default=None):
    if default:
        prompt = '{0} [{1}]: '.format(prompt, default)
    else:
        prompt = '{0}: '.format(prompt)
    input = raw_input(prompt)
    return default if default else input


def float_input(prompt, positive=True, default=None):
    while True:
        try:
            input = float(user_input(prompt, default))
        except ValueError:
            pass
        else:
            if (positive and input > 0.0) or not positive:
                return Float(input)


def int_input(prompt, positive=True, default=None):
    while True:
        try:
            input = int(user_input(prompt, default))
        except ValueError:
            pass
        else:
            if (positive and input > 0) or not positive:
                return Integer(input)


def expr_input(prompt):
    while True:
        try:
            input = sympify(user_input(prompt, default=None))
        except SympifyError:
            pass
        else:
            return input


def eval_expr(expr, **kwargs):
    assert isinstance(expr, Basic)
    return expr.subs(kwargs).evalf()
