import math as m

def f(x): 
    return m.sqrt(1+(2.5*m.exp(2.5*x))**2)

def trapezio(a,b,h):
    n = (b-a)/h
    natual = 1
    sum = f(a)
    while(natual < n):
        a += h
        sum += 2*f(a)
        natual += 1
    sum += f(b)
    sum *= (h/2)
    return sum

# Calculo do coeficiente de convergencia

r1 = trapezio(0, 1, 0.125)
r2 = trapezio(0, 1, 0.125/2)
r3 = trapezio(0, 1, 0.125/4)
coeficiente = (r2-r1)/(r3-r2) 
print("r1:",r1)
print("r2:",r2)
print("r3", r3)
print("coeficiente:", coeficiente)

# Calculo do erro 
erro = (r3-r2)/3

print("erro:", abs(erro))

#def trapeze_method(xi, xf, n, f):
#    h = (xf - xi) / n
#    area = f(xi) + f(xf)
#    for i in range(1, n):
#        area += 2 * f(xi + i * h)
#    area *= h / 2
#    return area