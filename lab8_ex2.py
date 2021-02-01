import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.linspace(1,10,100)
def gg_function(m,t):
    dmdt =  -k * m*t
    return dmdt
m_0=1000
k=0.08
solve_Bi = odeint(gg_function, m_0, t)
plt.plot(t, solve_Bi[:,0], label='lenpop')
plt.xlabel()
plt.ylabel()
plt.title()
plt.legend()
plt.show()