import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 


seconds_in_year= 365*24*60*60
seconds_in_day= 24*60*60
years=1
t=np.arange(0,years*seconds_in_year,seconds_in_day)



def force(coeficient,mq,coords_a,coords_b):
    mmq=1
    for a in mq:
        mmq*=a
    a0=coords_a[0]
    a1=coords_a[1]
    b0=coords_b[0]
    b1=coords_b[1]
    return (coeficient*mmq*(a0-a1))/((a0-a1)**2+(b0-b1)**2)**(1.5)

def gg_func(s,t):
    (x1,v_x1,y1,v_y1,
     x2,v_x2,y2,v_y2,
     x3,v_x3,y3,v_y3)=s
    dxdt1=v_x1
    dv_xdt1= force(k,(q1,q2/m2),(x1,x2),(y1,y2))+force(k,(q1,q3/m3),(x1,x3),(y1,y3))+force(-G,(m2,),(x1,x2),(y1,y2))+force(-G,(m3,),(x1,x3),(y1,y3))
     
    dydt1=v_y1
    dv_ydt1= force(k,(q1,q2/m2),(y1,y2),(x1,x2))+force(k,(q1,q3/m3),(y1,y3),(x1,x3))+force(-G,(m2),(x1,x2),(y1,y2))+force(-G,(m3,),(x1,x3),(y1,y3))
    
    dxdt2=v_x2
    dv_xdt2= force(k,(q2,q1/m1),(x2,x1),(y2,y1))+force(k,(q2,q3/m3),(x2,x3),(y2,y3))+force(-G,(m1,),(x2,x1),(y2,y1))+force(-G,(m3,),(x2,x3),(y2,y3))
    
    dydt2=v_y2
    dv_ydt2= force(k,(q2,q1/m1),(y2,y1),(x2,x2))+force(k,(q2,q3/m3),(y2,y3),(x2,x3))+force(-G,(m1,),(x2,x1),(y2,y1))+force(-G,(m3,),(x2,x3),(y2,y3))
        
    dxdt3=v_x3
    dv_xdt3= force(k,(q3,q1/m1),(x3,x1),(y3,y1))+force(k,(q3,q2/m2),(x3,x2),(y3,y2))+force(-G,(m1,),(x3,x1),(y3,y1))+force(-G,(m2,),(x3,x2),(y3,y2))
             
    dydt3=v_y3
    dv_ydt3= force(k,(q3,q1/m1),(y3,y1),(x3,x1))+force(k,(q3,q2/m2),(y3,y2),(x3,x2))+force(-G,(m1,),(x3,x1),(y3,y1))+force(-G,(m2,),(x3,x2),(y3,y2))
              
    return(dxdt1,dv_xdt1,dydt1,dv_ydt1,
            dxdt2,dv_xdt2,dydt2,dv_ydt2,
            dxdt3,dv_xdt3,dydt3,dv_ydt3)

x10=-74.5*10**9
v_x10=10000 
y10=0
v_y10=0
q1=2*10**5
m1=1

x20=74.5*10**9
v_x20=10000 
y20=0
v_y20=0
q2=2*10**5
m2=1

x30=0
v_x30=0
y30=129*10**9
v_y30=0
q3=-2*10**5
m3=1


k=8.9*10**9
G=6.67*10**(-11)

s0=(x10,v_x10,y10,v_y10,
    x20,v_x20,y20,v_y20,
    x30,v_x30,y30,v_y30)

sol = odeint(gg_func,s0,t)
plt.plot(t,sol[0], '-', color='r')
plt.show()