import math as m

def f(x):
    return -x+40*m.cos(m.sqrt(x))+3
    
def df(x):
    return -1 - 20*m.sin(m.sqrt(x))/(m.sqrt(x))
    
def Newton(x, error):
    xn = x - (f(x) / df(x))
    while (abs(x - xn) > error):
        x = xn
        xn = x - (f(x) / df(x))
        print(x)
        print(f(1.700))
        
        
Newton(1.7, 0.00001)



