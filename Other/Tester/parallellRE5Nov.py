import cmath as cm
import numpy as np


z1 = 30
z2 = complex(5,5)
z3 = complex(0,-0.5)

ztot = ((1/z1)+(1/z2)+(1/z3))**-1
#Rektangulär Form
print(f"{ztot:.2g}")


#polarForm
magnitute = abs(ztot)
print(magnitute)
rad = cm.phase(ztot)
print("Rad: ", rad)
print(np.rad2deg(rad))