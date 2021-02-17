def gradient_method(x, y, h, iterations):
    
    for i in range(iterations):
        xn = x
        yn = y
        xn = x - h * gradiente(x, y)
        yn = y - h * gradiente(x, y)
        if f(xn, yn) < f(x, y):
            h *= 2
            x = xn
            y = yn
        else:
            h /= 2
       print("no. iteration: {} -> x = {} y = {} f(x,y) = {} ".format(i, x, y, f(x, y)))
