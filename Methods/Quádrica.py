# f(x,y) -> função a minimizar
#
# df_x(x,y) -> função resultante de derivar parcialmente f(x,y) em ordem a x
#
# df_y(x,y) -> função resultante de derivar parcialmente f(x,y) em ordem a y
#
# H(x,y) -> matriz hessiana [df_xx, df_xy]
#                           [df_yx, df_yy]
#
# NO MAXIMA 1) H: invert(hessian(f))
#           2) grad: [diff(f,x),diff(f,y)]
#           3) calcular H.grad
#           4) hx(x,y) = expressão em (H.grad)[1]
#           5) hy(x,y) = expressão em (H.grad)[2]
#
# então -> xn = x - hx(x,y)
#       -> yn = y - hy(x,y)