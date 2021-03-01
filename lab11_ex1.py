import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
frames = 200
t = np.linspace(0, 5, frames)
def gg_func(r, t):
    y, v = r
    dydt = v
    dv_ydt = - g-(n*(v**2))
    return dydt, dv_ydt
m=0.5
g = 9.8
v = 20
n=0.1
y0=5
r0=y0,v
def solve_func(i, key):
    sol = odeint(gg_func, r0, t)
    if key == 'point':
    
        y = sol[i, 0]
    else:
        y = sol[:i, 0]
    return 0,y
fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')
def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)
edge = 100
ax.set_xlim(-5,edge)
ax.set_ylim(-5, edge)
ani.save('lab11_ani_ex1.gif')
plt.show()
