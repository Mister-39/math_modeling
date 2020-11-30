import matplotlib.pyplot as plt
import numpy as np 
def parabola_plotter(a=1,b=1,c=1, tittle='Парабола'):
    x=np.arange(-10,10,0.01)
    y=a*x**2+b*x+c
    plt.plot(x,y)
    plt.show()
parabola_plotter()

def giperbola_plotter(k=1,tittle='Гипербола'):
    x_min=-20
    x_max=20
    x=np.arange(x_min,x_max,0.01)
    y=k/x
    y=np.ma.masked_less(y,x_min)
    y=np.ma.masked_greater(y,x_max)
    plt.plot(x,y)
    plt.show()
giperbola_plotter()