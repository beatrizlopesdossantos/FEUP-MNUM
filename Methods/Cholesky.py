# NO MAXIMA: RESOLVER O SISTEMA A.x = b
# 1) [P,L,U] : get_lu_factors(lu_factor(transpose(A)))
# 2) B : transpose(L) -> matriz triangular inferior
# 3) C : transpose(U) -> matriz triangular superior
# 4) y : invert(B).matrix(b)
# 5) x : invert(C).y -> solução final