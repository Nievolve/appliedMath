import cmath as cm
import numpy as np
from lib import recToPolForm as rp


x = complex(2,3)
print(x)
print(rp.recToPol(x))

#polarForm
magnitute = abs(x)
print(magnitute)
argument = np.rad2deg(np.atan(x.imag/x.real))
print(argument)


print(f"{rp.polToRec(magnitute,argument):.1g}")

"""
magnitute = 2
argument = 30 #grader
argumentRad = np.deg2rad(argument)
z = cm.rect(magnitute,argumentRad)

print(z)
print(z.real)
print(z.imag)
"""