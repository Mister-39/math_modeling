import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t=np.arange(-5,5,0.1)
def gg_function(func,t):
    y,g=func
    dy_dt=g
    dg_dt=-4*g-5*y
    return dy_dt,dg_dt
y0=4
dy0_dt=-1
r0=y0,dy0_dt
sol = odeint(gg_function, r0, t)
plt.plot(t, sol[:, 1],'g' , label='x')
plt.show()