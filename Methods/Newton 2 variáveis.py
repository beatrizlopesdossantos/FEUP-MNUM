import math as m

def f1(x, y):
    return m.sin(x+y)-m.exp(x-y)
def f2(x, y):
    return m.cos(x+y)-x**2*y**2;
    
def df1x(x, y):
    return m.cos(y+x)-m.exp(x-y)

def df1y(x, y):
    return m.cos(y+x)+m.exp(x-y)

def df2x(x, y):
    return -m.sin(y+x)-2*x*y**2 
def df2y(x, y):
    return -m.sin(y+x)-2*x**2*y  

def jacobian(x, y):
    return df1x(x, y) * df2y(x, y) - df2x(x, y) * df1y(x, y)

def Newton_2(x, y, error):
    xn = x - (f1(x, y) * df2y(x, y) - f2(x, y) * df1y(x, y)) / jacobian(x, y)
    yn = y - (f2(x, y) * df1x(x, y) - f1(x, y) * df2x(x, y)) / jacobian(x, y)
    while (abs(x - xn) > error or abs(y - yn) > error):
        
        x = xn
        xn = x - (f1(x, y) * df2y(x, y) - f2(x, y) * df1y(x, y)) / jacobian(x, y)
        y = yn
        yn = y - (f2(x, y) * df1x(x, y) - f1(x, y) * df2x(x, y)) / jacobian(x, y)
        print("x is", x)
        print("y is", y)
         
Newton_2(0.5, 0.25, 0.001)