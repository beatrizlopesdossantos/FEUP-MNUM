import math as m
B = (m.sqrt(5)-1)/2
A = B**2

def f(x):
    return (x-8)**2+x**4
#Critério de paragem: |x1-x2| <= erro
#pelo gráfico do máxima, encontra se entre 0 e 4
def aurea_minimo(x1,x2,x3,x4):
    counter = 0    
    while(abs(x1-x2)>0.0001):
        x3 = x1 + A*(x2-x1)
        x4 = x1 + B*(x2-x1)
        if(counter < 3):
            print("x:" ,x1,x2,x3,x4)
            print("fx",f(x1),f(x2),f(x3),f(x4))
        if(f(x3)<f(x4)):
            x2=x4
        else:
            x1=x3
        counter += 1    
    return x1

def aurea_maximo(x1,x2):
    while(abs(x1-x2)>0.0001):
        x3 = x1 + A*(x2-x1)
        x4 = x1 + B*(x2-x1)
        if(f(x3)<f(x4)):
            x1=x3
        else:
            x2=x4
    return x1

#print(aurea_maximo(0,6))
print(aurea_minimo(0, 4, 0, 0))