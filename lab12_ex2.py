import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
frames = 200
t = np.linspace(0, 5, frames)
def gg_func(a, t):
    x, v_x, y, v_y = a
    dxdt =k1
    dv_xdt =a/x
    dydt =k2
    dv_ydt =a/y
    return dxdt, dv_xdt, dydt, dv_ydt
a=10
k1=t/a
k2=t/a
x=a/2
y=a/2
v_x0=0
v_y0=0
a0=x, v_x0, y, v_y0
def solve_func(i, key):
    sol = odeint(gg_func, a0, t)
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
ani.save('lab11_ani_ex2.gif')
plt.show()

