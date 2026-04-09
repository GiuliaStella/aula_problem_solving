#equacoes polinomiais
import sympy
from sympy import symbols,Eq, solve

x= symbols('x')

equacao = Eq (x**3 - 7*x + 6, 0)
resultado = solve(equacao,  x)
print (resultado)