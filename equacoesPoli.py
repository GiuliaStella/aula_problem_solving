#equacoes polinomiais
import sympy
from sympy import symbols,Eq, solve

x= symbols('x')

equacao= Eq( 6*x, 2*x + 16)
resultado = solve(equacao, x)
print(resultado)

equacao = Eq (x**2 + 3*x - 28, 0)
resultado = solve(equacao,  x)
print (resultado)

equacao = Eq (4*x**2 - 8*x + 7, 0)
resultado = solve(equacao,  x)
print (resultado)

equacao = Eq (x**2 - 8*x + 16, 0)
resultado = solve(equacao,  x)
print (resultado)

equacao = Eq (4*x**2 - 6*x + 7, 0)
resultado = solve(equacao,  x)
print (resultado)
