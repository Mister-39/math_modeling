import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.linspace(0, 5)
def gg_func(b, t):
    x,y=b
    dxdt =k1*(a-(x+y))
    dydt =k2*(a-(x+y))
    return dxdt,  dydt
a=100
k1=5
k2=10
b=0,0
sol = odeint(gg_func,b,t)
plt.plot(t,sol, '-', color='r')
plt.show()