import matplotlib.pyplot as plt
import numpy as np
def circlea_plotter(R=1,title='Circle plotter'):
    x=np.linspace(-2,2,100)
    y=np.linspace(-2,2,100)
    X,Y=np.meshgrid(x,y)
    fxy=X**2+Y**2
    plt.contour(X,Y,fxy,levels=[R])
    plt.show()
circlea_plotter(3)