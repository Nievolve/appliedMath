# Räkneexempel 6.2
# En 100 μF kondensator uppladdas genom ett 100 Ω resistor från en 
# spänningskälla med polspänningen U = 100 V.

# a) Beräkna spänningen över kondensatorn vid följande tider. 
# Redovisa beräkningarna i värdetabellen nedan.
# Ledning: τ(tao) = R * C

# Tabell:
# t [s]         uc(t) [V]
# τ/2           ?
# τ             ?
# 2τ            ?
# 3τ            ?
# 5τ            ?

# b) Rita grafen till funktionen uc(t). Ange funktionens egenskaper.

# c) Rita grafen till funktionen i(t). Ange funktionens egenskaper.

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


# Bra att lägga till real=True och positive=True för att endast få ut dessa i solve variabeln.
tx = sp.symbols("tx", real=True, positive=True)

spEQ = sp.Eq(80,100*(1-(sp.exp(-100*tx))))
solve = sp.solve(spEQ)
for k in solve:
    print(k)
