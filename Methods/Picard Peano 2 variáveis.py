import math as m

def f1(x, y):
    return 2 * x * x - x * y - 5 * x + 1


def f2(x, y):
    return x + 3 * m.log(x) - y * y

def gx(x, y):
    return -3*m.log(x)+y*y


def gy(x, y):
    return (2*x*x-5*x+1)/x

    
def picardPeano_2(x, y, erro):
    xAnt = x + 10
    yAnt = y + 10
    while (abs(xAnt - x) > erro or abs(yAnt - y) > erro):
        xAnt = x
        yAnt = y
        x = gx(x, y)
        y = gy(xAnt, y)
        print('x: %1.7f\t y:%1.7f\t' % (x, y))
        
picardPeano_2(4, 4, 10**-5)

