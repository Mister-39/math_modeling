from sympy.vector import CoordSys3D
from sympy import symbols,solve 
from sympy import sin,cos,pi,exp
N=CoordSys3D('N')
x=symbols('x')
a = 7*N.i + 2*N.j -8*N.k
b = -4*N.i + x*N.j + 9*N.k
A=a.dot(b)
solve_A=solve(A,x)
print(solve_A)