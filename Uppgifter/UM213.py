import sympy as sp

U1 = 60 #V
alfa1 = 20 #grader
U2 = 40 #V
alfa2 = 50 #grader

B = 180- (alfa2-alfa1)
print(B)
U3 = sp.symbols("U3")
eqU3= sp.Eq(U3, sp.sqrt(U1**2+U2**2-2*U1*U2*sp.cos(sp.rad(B))))
sol = sp.solve(eqU3, U3)
print(f"U3 = {sol[0].evalf(2)} V")