def finiteDifference(x, y):  #Takes the finite derivative of a function
    dy = diff(y)
    dx = diff(x)
    dydx1 = zeros(y.shape, float) 
    dydx1[:-1] = dy/dx
    dydx1[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    return dydx1

def fourPtFiniteDiff(x,y): #takes the derivative for a four point
    h = .1
    dydx = zeros(y.shape, float)
    for i in range(2, len(y)-2):
        dydx[i] = (y[i - 2] - 8*y[i - 1] + 8*y[i + 1] - y[i + 2])/(12*h)
    return dydx
