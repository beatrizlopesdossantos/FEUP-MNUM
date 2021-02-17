import math as m 

def f(x): 
    return m.sqrt(1+(2.5*m.exp(2.5*x))**2)


def simpson(a,b,h):
    n = (b-a)/h
    natual = 1
    sum = f(a)
    while(natual <n):
        a += h
        if(natual%2==0):
            sum += 2*f(a)
        else:
            sum += 4*f(a)
        natual+=1
    sum += f(b)
    sum *= (h/3)
    return sum

# Calculo da convergencia
r1 = simpson(0, 1, 0.125)
r2 = simpson(0, 1, 0.125/2)
r3 = simpson(0, 1, 0.125/4)
coeficiente = (r2-r1)/(r3-r2)
print("r1:",r1)
print("r2:",r2)
print("r3", r3)
print("coeficiente:", coeficiente)

# Calculo do erro
erro = (r3-r2)/15
print("erro:", abs(erro)) # erros sempre em modulo 

#def simpson_method(xi, xf, n, f):
#    h = (xf - xi) / (2 * n)
#    area = f(xi) + f(xf)
#    for i in range(1, 2 * n):
#        if i % 2:
#            area += 2 * f(xi + i * h)
#        else:
#            area += 4 * f(xi + i * h)
#    area *= h / 3
#    return area

