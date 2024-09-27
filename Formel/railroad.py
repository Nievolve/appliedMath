import math

# Räkneexempel 1.15

# Formler
# volymmassa = meter/Volym
# materialmassa = massa/längdenhet
#V=A*L samband av massa i relation med area till längd i rätblock
#R =alfa*L/A Resitivitet i ledningen, alfa är materialtypen
def Rl(rå,L,A):
    Rl=rå*L/A
    print(Rl)
    return Rl
def Area(V,L):
    A=V/L
    print(A)
    return A
def volym(m,densitet):
    V=m/densitet
    print(V)
    
    return V
def m(vikt,L):
    m=vikt*L
    return m


L = 15 #meter
vikt = 50 #per meter
rs = 0.15*10**-6
densitet = 7.8*10**3 #kg/m**3


RL1 = Rl(rs,L,Area(volym(m(vikt,L),densitet),L))
print(f"{RL1:.2g}")
