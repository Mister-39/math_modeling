import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
frames = 365
seconds_in_year = 365 * 24 * 60 * 60
years = 1
t = np.linspace(0, years*seconds_in_year, frames)
def move_func(s, t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3, y3, v_y3,
     x4, v_x4, y4, v_y4,
     x5, v_x5, y5, v_y5,
     x6, v_x6, y6, v_y6,
     x7, v_x7, y7, v_y7,
     x8, v_x8, y8, v_y8)= s

    dxdt1 = v_x1
    dv_xdt1 = - G * m * x1 / (x1**2 + y1**2)**1.5
    dydt1 = v_y1
    dv_ydt1 = - G * m * y1 / (x1**2 + y1**2)**1.5

    dxdt2 = v_x2
    dv_xdt2 = - G * m * x2 / (x2**2 + y2**2)**1.5
    dydt2 = v_y2
    dv_ydt2 = - G * m * y1 / (x2**2 + y2**2)**1.5

    dxdt3 = v_x3
    dv_xdt3 = - G * m * x3 / (x3**2 + y3**2)**1.5
    dydt3 = v_y3
    dv_ydt3 = - G * m * y3 / (x3**2 + y3**2)**1.5

    dxdt4 = v_x4
    dv_xdt4 = - G * m * x4 / (x4**2 + y4**2)**1.5
    dydt4 = v_y4
    dv_ydt4 = - G * m * y4 / (x4**2 + y4**2)**1.5
    
    dxdt5 = v_x5
    dv_xdt5 = - G * m * x5 / (x5**2 + y5**2)**1.5
    dydt5 = v_y5
    dv_ydt5 = - G * m * y5 / (x5**2 + y5**2)**1.5
    
    dxdt6 = v_x6
    dv_xdt6 = - G * m * x6 / (x6**2 + y6**2)**1.5
    dydt6 = v_y6
    dv_ydt6 = - G * m * y6 / (x6**2 + y6**2)**1.5
    
    dxdt7 = v_x7
    dv_xdt7 = - G * m * x7 / (x7**2 + y7**2)**1.5
    dydt7 = v_y7
    dv_ydt7 = - G * m * y7 / (x7**2 + y7**2)**1.5
    
    dxdt8 = v_x8
    dv_xdt8 = - G * m * x8 / (x8**2 + y8**2)**1.5
    dydt8 = v_y8
    dv_ydt8 = - G * m * y8 / (x8**2 + y8**2)**1.5
    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2,
            dxdt3, dv_xdt3, dydt3, dv_ydt3,
            dxdt4, dv_xdt4, dydt4, dv_ydt4,
            dxdt5, dv_xdt5, dydt5, dv_ydt5,
            dxdt6, dv_xdt6, dydt6, dv_ydt6,
            dxdt7, dv_xdt7, dydt7, dv_ydt7,
            dxdt8, dv_xdt8, dydt8, dv_ydt8)

G = 6.67 * 10**(-11)
m = 1.98 * 10**(30)

x10 = 0
v_x10 = -47360
y10 = 0.387 * 149 * 10**9
v_y10 = 0

x20 = 0
v_x20 =35000
y20 = 0.387 * 149 * 10**9
v_y20 = 0

x30 = 149 * 10**9
v_x30 = 0
y30 = 0
v_y30 = 30000

x40 = 0
v_x40 = -47360
y40 = 0.387 * 149 * 10**9
v_y40 = 0

x50 = 0
v_x50 = -47360
y50 = 0.387 * 149 * 10**9
v_y50 = 0

x60 = 0
v_x60 = -47360
y60 = 0.387 * 149 * 10**9
v_y60 = 0

x70 = 0
v_x70 = -47360
y70 = 0.387 * 149 * 10**9
v_y70 = 0

x80 = 0
v_x80 = -47360
y80 = 0.387 * 149 * 10**9
v_y80 = 0

s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80)    