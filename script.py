import sympy
#preparando o ambiente:

from sympy import symbols, simplify

#DEFINIR AS VARIAVEIS:
x, y, z, a ,b, c = symbols('x y z a b c')

#  a)
expr_a = (3*x +2*y - 5) + ( 4*x - y + 8)
print(simplify(expr_a))

expr_b = (5*x**2 -x +1) - (2*x**2 + 4*x - 3)
print(simplify(expr_b))

expr_c = (7*z**2 - (3*z**2 - 5*z + 1))
print(simplify(expr_b))

expr_d = (6*a**2 - 3*b) - (2*a**2 + 5*b - 7)
print(simplify(expr_d))

expr_e = (-2*a + 5*b - 3*c) + (7*a - b + 2*c)
print(simplify(expr_e))

expr_f = (-8*x**3) * ( 4*x )
print(simplify(expr_f))

expr_g = (5*a**4*x**3) * ( 2*a*x**4)
print(simplify(expr_g))

expr_h = (12*y**5) % ( 4*y**3)
print(simplify(expr_h))

expr_i = (20*a**4*b**2) % ( -5*a*b)
print(simplify(expr_i))

expr_j = (3*x**2*y) * ( 2*x**3)
print(simplify(expr_j))



