import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.linspace(0, 25,200)
def gg_func(r, t):
    y,v = r
    dydt = v
    dv_ydt = - g-(k*y)/m - 0.8*v
    return dydt, dv_ydt
m=0.5
g = 9.8
l=0.08
F=1
k=F/l
y0=-l
v0=0.5
r0=y0,v0
sol = odeint(gg_func,r0,t)
plt.plot(t,sol[:,0], '-', color='r')
plt.show()