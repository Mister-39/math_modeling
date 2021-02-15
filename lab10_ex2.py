import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t=np.arange(-1,1,0.1)
def gg_function(r,t):
    x,y=r
    dx_dt=3*x-2*y+np.exp(3*t)/np.exp(t)+1
    dy_dt=x-(np.exp(3*t))/np.exp(t)+1
    return dx_dt,dy_dt
x0=5
y0=-7
r0=x0,y0
sol = odeint(gg_function, r0, t)
plt.plot(t, sol[:, 1],'g' , label='x')
plt.show()