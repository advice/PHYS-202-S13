
def pointPotential(x,y,q,posx,posy):
    k=8.9e9
    Vpp = (k*q / (x**2 + ( y- (posx**2+posy**2)**(1/2))**2)**(1/2))
    return Vpp

def dipolePotential(x,y,q,d):
    k=8.9e9
    Vdp = (k*q/(x**2 + (y-d)**2)**(1/2.)) - (k*q/ (x**2 + (y + d)**2)**(1/2.))
    return Vdp

def pointField(x,y,q,Xq,Yq): #Defining the function
    k=8.99e9  #defining k
   
    Ex=(k*q*(x-Xq))/((x-Xq)**2+(y-Yq)**2)**(1/2.) #Writing the equations
    Ey=(k*q*(y-Yq))/((x-Xq)**2+(y-Yq)**2)**(1/2.)
    return {"Ex(x,y)":Ex, "Ey(x,y)":Ey }   #This will return my function
					   #in an easy to read manner
