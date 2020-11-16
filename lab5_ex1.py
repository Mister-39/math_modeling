from sympy import symbols 
from sympy import sin,cos,pi,exp
from sympy import simplify,expand,factor,trigsimp
o=input
o=int(o)
p=input
p=int(p)
a=input(int(a))
x,y=symbols('x y')
ch(p)=exp(a)+exp(-a)/2
sh(p)=exp(a)-exp(-a)/2
x=a*sh(p)/ch(p)-cos(o)
y=a*sin(p)/ch(p)-cos(o)
expr=x
expr_new=y
print(x,y)