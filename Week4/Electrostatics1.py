
def pointPotential(x,y,q,posx,posy):
    k=8.9e9
    Vpp = (k*q / (x**2 + ( y- (posx**2+posy**2)**(1/2))**2)**(1/2)
    return Vpp

def dipolePotential(x,y,q,d):
    k=8.9e9
    Vdp = (k*q/(x**2 + (y-d)**2)**(1/2.)) - (k*q/ (x**2 + (y + d)**2)**(1/2.))
    return Vdp
