from math import sqrt 
from sympy import symbols 
from sympy import sin,cos,pi,exp
from sympy import simplify,expand,factor,trigsimp
a=symbols('a')
simp_expr=trigsimp((expr.sqrt(a)-a/(expr.sqrt(a))+1)*a-1/expr.sqrt(a))
print(simp_expt)