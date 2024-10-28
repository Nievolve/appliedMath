import numpy as np
import matplotlib.pyplot as plt
from lib import xyPlot as xy
import sympy as sp
# Funktion för att räkna ut plot för sinus kurva
def Ctopp(t,w):
    Ut = 325  # U Topp
   
    
    return Ut * np.sin(w * t)  # Momental spänning (U(t))

# Givet
w = 100*np.pi

# Interval mellan -20 ms och 20ms
T = (2*np.pi)/w
interval = np.arange(-0.02, 0.021, 0.001)

resultat = [Ctopp(t,w) for t in interval]

for k in resultat:
    print(k)
yLabel= "Spänning"
xy.xyplot(resultat, len(resultat)+1, yLabel)


# D
currentTop = 325
targetCurrent = 230
tTarget = sp.symbols("tTarget")
eqTarget = sp.Eq(targetCurrent,currentTop*sp.sin(w*tTarget))
solve = sp.solve(eqTarget,tTarget)

print(solve[0]*10**3)
print(solve[1]*10**3)


