import numpy as np

def pointPotential(x,y,q,posx,posy):
    k=8.8975517873681764e9
    Vpp = (k*q /((x-posx)**2+(y-posy)**2)**(1/2))
    return Vpp

def dipolePotential(x,y,q,d,angle):
    k=8.8975517873681764e9
    a=(d/2.)*np.cos(angle)
    b=(d/2.)*np.sin(angle)
    c1=(((x-a)**2.+(y-b)**2.)**(1/2))
    c2=(((x+a)**2.+(y+b)**2.)**(1/2))
    kq=k*q
    Vxy = kq/c1-kq/c2
    return Vxy
