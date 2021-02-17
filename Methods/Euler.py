PRECISION = 10e-10


def euler_method(x0, y0, x, h, df):
    while abs(x - x0) > PRECISION:
        y0 += df(x0, y0) * h
        x0 += h
    return y0
print(euler(5,3,3,0.4))



Calculando o erro
h = 0.5

r1y, r1z= Euler(0,0,1,0.1,h)
r2y= Euler(0,1,1,0.1,h/2)
r3y= Euler(0,1,1,0.1,h/4)
print("y1:",r1z)
print("y2:",r2y)
print("y3:",r3y)
quociente = (r2y - r1y)/(r3y-r2y)           #o passo é adequado, quociente igual a 2(ou quase)
erro = (r3y-r2y)
print("quociente", quociente) 
print("erro:", erro)

  