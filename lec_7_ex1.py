import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots() 
anim_object, = plt.plot([], [], '-', lw=2) 

xdata, ydata = [], []

def line(R, t):
    x = R*t - R*(np.sin(t))
    y = R - R*(np.cos(t))
    return x, y

edge = 100
ax.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def update(t):
    new_x, new_y = line(2, t)
    xdata.append(new_x)
    ydata.append(new_y) 
    anim_object.set_data(xdata, ydata)  
    return anim_object,

ani = FuncAnimation(fig, 
                    update, 
                    frames=np.arange(0, 8*np.pi, 0.2), 
                    interval=100
                    )           

ani.save('lec_7_ex1.gif')