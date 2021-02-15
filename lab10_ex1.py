import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
x=np.arange(-5,5,0.1)
def gg_function(r,x):
    y,z=r
    dy_dx=y**2*z
    dz_dx=z/x-y*z**2
    return dy_dx,dz_dx
y0=1
z0=-3
r0=y0,z0
sol = odeint(gg_function, r0, x)
plt.plot(x, sol[:, 1],'g' , label='y')
plt.show()