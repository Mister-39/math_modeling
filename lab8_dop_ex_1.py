import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
x=np.arange(0,h-R,100)
def gg_function(v,x):
    r=R+h-x
    dvdx=G*M/(v*r**2)
    return dvdx
v_0=0.0001
G=6.67*10**(-11)
M=5.97*10**(24)
h=30000000
R=6300000
solve_Bi = odeint(gg_function,v_0,x )
plt.plot(x,solve_Bi[:,0], label='lenpop')
plt.xlabel()
plt.ylabel()
plt.title()
plt.legend()
plt.show()
