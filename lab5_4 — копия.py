from sympy import symbols 
from sympy import sin,cos,pi,exp
from sympy import Eq,solve,solveset,linsolve,nonlinsolve

x,y,z=symbols ( 'x y z')
expr=x**2-2
solve_expr=solve(expr,x)
print(solve_expr)