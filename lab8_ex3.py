import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.linspace(1,10,100)
def gg_function(v,t):
    dvdt= v**2*y/m+a_0
    return dvdt
    
v_0=0
a_0=10
y=-3
m=70
solve_Bi = odeint(gg_function, v_0, t)
plt.plot(t, solve_Bi[:,0], label='lenpop')
plt.xlabel()
plt.ylabel()
plt.title()
plt.legend()
plt.show() 