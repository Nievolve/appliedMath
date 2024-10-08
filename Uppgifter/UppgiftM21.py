import numpy as np
#Beräkna Z
#Beräkna R
# Rita impedansTriangel


#Given
Xl=90 #ohm

f=50 #Hz
Ueff = 48 #V
Ie = 0.1 #A
Z = Ueff/Ie

R = np.sqrt(Z**2-Xl**2)

print(f"{Z:.3g}....{R:.2g}")