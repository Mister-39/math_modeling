import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t=np.arange(-5,5,0.1)
def gg_function(func,t):
    y,g=func
    dy_dt=g
    dg_dt=np.sin(t)+np.cos(t)
    return dy_dt,dg_dt
y0=3
dy0_dt=0
r0=y0,dy0_dt
sol = odeint(gg_function, r0, t)
plt.plot(sol[:,0], sol[:, 1],'b' , label='x')
plt.plot(sol[:, 1], sol[:, 0],'r' , label='x')
plt.plot(t, sol[:, 1],'g' , label='x')
plt.show()