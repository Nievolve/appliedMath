import numpy as np
import sympy as sp
# Import för tillägget
import cmath as cm

#Given information
Ie1 = 4.05 #A
b1 = 15 #grader
Ie2 = 4.78 #A
b2 = 225 #grader
GammaVinkel = 360-(b1+b2)

#Beräkningar, formel...
Ie3 =np.sqrt(Ie1**2+Ie2**2-2*Ie1*Ie2*np.cos(np.radians(GammaVinkel)))


#B3 är i tredje kvadraten och jag kan se B2 löper in där en bit och jag kan beräkna hur mycket som rör sig i tredje kvadratren.
# och vinkel Alfa tillsammans med den ger en rest på B3.
alfaRad = np.arccos((Ie2**2 + Ie3**2 - Ie1**2) / (2 * Ie2 * Ie3))
alfaGrader = np.degrees(alfaRad)

b3 = 90-(b2-180)-alfaGrader

print(f"Ie3= {Ie3:.3g} A")
print(f"B3 = {b3:.3g} grader")


# Tillägg från komplexa tal
I1topp = Ie1*np.sqrt(2)
I2topp = Ie2*np.sqrt(2)

recIe1 = complex(I1topp*np.cos(np.deg2rad(b1)), I1topp*np.sin(np.deg2rad(b1)))
print(recIe1)
recIe2 = complex(I2topp*np.cos(np.deg2rad(GammaVinkel)), I2topp*np.sin(np.deg2rad(GammaVinkel)))
print(recIe2)
recIe3 = recIe1+recIe2
print(recIe3)

Ie3Magnetute = abs(recIe3)
Ie3Argument = np.rad2deg(cm.phase(recIe3))

print(f"Itopp3 i polarform är {Ie3Magnetute:.3g} < {Ie3Argument:.3g}")

print(f"Med metoden så blir Ie3 = {Ie3Magnetute/np.sqrt(2)}")