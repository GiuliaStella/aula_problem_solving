from sympy import *
import sympy as sp

x = symbols('x')

print(limit((sqrt(x + 6) - 3)/(x-3), x, 3))

print(limit((sqrt(x + 6) - 3)/(x**2 - 4*x + 3), x, 3))

f_esq = x+2
f_dir = 2*x
print('esquerda: ', sp.limit(f_esq, x, 1, dir= '-'))
print('direita: ', sp.limit(f_dir, x, 1, dir= '+'))
