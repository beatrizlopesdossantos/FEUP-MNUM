import math as m

def g(x): 
	return m.exp(x)-5	#apenas a raiz positiva

def f(x): 
	return m.exp(x)-x-5

def picardPeano(x, max_iter):
	for i in range(max_iter):
		x = g(x)
		print(x)


picardPeano(3,10)