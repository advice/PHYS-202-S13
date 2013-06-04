import numpy as np
#Linear least squares fit
def LinearLeastSquaresFit(x,y):
    """Take in arrays representing (x,y) values for a set of linearly varying data and
    perform a linear least squares regression. Return the resulting slope and intercept
    parameters of the best fit line with thier uncertainties."""
    
    xavg = np.zeros(len(x),float) #<x> average
    xavg = sum(x)/len(x)
    
    yavg = np.zeros(len(y),float) #<y> average
    yavg = sum(y)/len(y)
    
    x2avg = np.zeros(len(x),float) #<x^2> average
    x2avg = sum(x**2)/len(x)
    
    xyavg = np.zeros(len(x),float) #<xy> average
    xyavg = sum(x*y)/len(x)
    
    m = (xyavg - xavg*yavg)/(x2avg-xavg**2) #slope
    b = (x2avg*yavg-xavg*xyavg)/(x2avg-xavg**2) #intercept
    
    d = np.zeros(len(x),float)
    for n in range(len(x)):
        d[n] = y[n] -(m*x[n]+b)
    
    x2 = np.zeros(len(x),float)
    for n in range(len(x)):
        x2[n] = sum(d[n]**2)
    
    
    d2avg = np.zeros(len(d),float) #<d^2> average
    d2avg = sum(x2)/float(len(x))
    
    Dm = sqrt((1/float(len(x)-2))*(d2avg/(x2avg-xavg**2))) #slope error
    Db = sqrt((1/float(len(x)-2))*((d2avg*x2avg)/(x2avg-xavg**2))) # intercept error
    print "slope=", m, "Slope Error=", Dm,"Intercept=", b, "Intercept Error=", Db
    return "slope=", m, "Slope Error=", Dm,"Intercept=", b, "Intercept Error=",Db


# Weighted Least Squares Fit
def WeightedLinearLeastSquaresFit(x,y,dy):
    
    w = 1/(dy**2)
    
    m = (sum(w)*sum(w*x*y)-sum(w*x)*sum(w*y))/(sum(w)*sum(w*x**2)-(sum(w*x))**2)
    b = (sum(w*x**2)*sum(w*y)-sum(w*x)*sum(w*x*y))/(sum(w)*sum(w*x**2)-(sum(w*x))**2)
    dm = sqrt(float(sum(w))/float(sum(w)*sum(w*x**2)-(sum(w*x))**2))
    db = sqrt(float(sum(w*x**2))/float(sum(w)*sum(w*x**2)-(sum(w*x))**2))
    
    print "slope=", m, "Slope Error=", dm,"Intercept=", b, "Intercept Error=", db
    return "slope=", m, "Slope Error=", dm,"Intercept=", b, "Intercept Error=", db
