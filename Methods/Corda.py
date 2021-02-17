import math as m

def f(x):
    return 2;

def fakepos(a, b, error):
    while abs(b - a) > error:
        x = (f(b) * a - f(a) * b) / (f(b) - f(a))
        if f(x) * f(a) < 0:
            b = x
        else:
            a = x

        print('f(a): {0:.10f}\t f(b): {1:.10f}\t x: {2:.10f}\t '.format(f(a), f(b), x))


falsiPosition(0.01, 1, 10**-3)