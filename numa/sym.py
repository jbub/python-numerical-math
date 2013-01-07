from sympy import sympify



parsed = sympify('sin(x) + 2 - 5')


print parsed.subs({'x':4}).evalf()