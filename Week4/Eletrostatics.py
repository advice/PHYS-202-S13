def pointPotential(x,y,q,posx,posy):
    k=1
    Vpp = (k*q/(x**2 +(y-(posx**2+posy**2)**(1/2))**2))
    return Vpp

def dipolePotential(x,y,q,d):
    Vdp = (k*q/ (x**2 + (y-d)**2)**(1/2.)) - (k*q/ (x**2 + (y + d)**2)**(1/2.))
    return Vdp
