import numpy as np
from lib import complexConv as cc

#Given information
U = 230
f = 200
R1 = 180
L = 321e-3
R2 = 220
C = 235e-6

#Beräkningar
Xl = 2*np.pi*f*L
Xc = 1/(2*np.pi*f*C)
z1 = complex(R1,Xl)
z2 = complex(R2,Xc)
i2 = complex(U/z2)
#
zTot = ((1/z1)+(1/z2))**-1
#
komplexImpedansPolarForm = cc.recToPol(zTot)
i2PolarForm = cc.recToPol(i2)


# Presentation
# A
print("A: ")
print(f"Komplexa impedansen = {komplexImpedansPolarForm[0]:.3g} < {komplexImpedansPolarForm[1]:.3g} grader")
# B
print("B: ")
print(f"Den komplexa strömmen I2 = {i2PolarForm[0]:.3g} < {i2PolarForm[1]:.3g}")