import math as m

def f(x):
    return x**3-10*m.sin(x)+2.8

def bissec(a, b, error):
    count = 1
    while abs(a - b) > error and count < 3:
        mid = (a+b)/2
        if f(a)*f(mid) < 0:
            b = mid;
        else:
            a = mid;
        count += 1
        print('f(a): {0:.10f}\t f(b): {1:.10f}\t mid: {2:.10f}\t ' .format(f(a),f(b),mid))

        
bissec(1.5, 4.2, 10**-4)