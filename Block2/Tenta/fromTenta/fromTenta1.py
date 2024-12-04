# Beräknar R i en krets



import sympy as sp
# Det svar du kommer få från A delen
Itopp=""
Utopp=""
Z = 17.5 #Z=Utopp/Itopp
# Given information från uppgiften(ledning)
L = 10e-3
C = 200e-6
f = 50
# Sökt information
R = sp.symbols("R")
# Beräkningar
Xl = 2*f*sp.pi*L
Xc = 1/(2*f*sp.pi*C)
spEQ = sp.Eq(Z,sp.sqrt(R**2+(Xl-Xc)**2))


solve = sp.solve(spEQ,R)
# 
print(solve)