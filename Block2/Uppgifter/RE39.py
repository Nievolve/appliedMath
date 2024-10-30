# Beräkna den kapacitiva reaktansen för en kondensator
#       Givet:
# - Kapacitans C = 4.5 mF = 4.5 * 10**-3 F
# - Frekvens f = 50 Hz
# - Spänning i nätet är 230 V, 50 Hz enfas
#       Sök:
# - Kapacitiv reaktans Xc

import numpy as np
def Xc(C,f,U):
    return 1/(2*np.pi*f*C)
#Given
C = 4.5*10**-3 #Farad [F]
f = 50 # Hz
U = 230 #V

print(f"{Xc(C,f,U):.2g}")