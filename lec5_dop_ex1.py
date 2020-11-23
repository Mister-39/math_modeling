from sympy.vector import CoordSys3D
from sympy import symbols 
from sympy import sin,cos,pi,exp
N=CoordSys3D('N')
a = 4*N.i + 3*N.j + 8*N.k
b = -2*N.i + 8*N.j + 7*N.k
c = -5*N.i - 6*N.j + 12*N.k
a1=a.magnitude()
b1=b.magnitude()
c1=c.magnitude()
A=a.dot(b)
B=a.dot(c)
C=b.dot(c)
cos_ab=A/a1
cos_ac=B/b1
cos_bc=C/c1
print(cos_ab)
print(cos_ac)
print(cos_bc)
