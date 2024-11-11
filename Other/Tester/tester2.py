import numpy as np
import cmath

i1 = 2.0*np.exp(1j*(np.pi/6))
i2 = 4.0*np.exp(1j*(4*np.pi/9))
i3 = i1+i2
print(f"{i3:.2g}")
i3Polar = cmath.polar(i3)


print(i3Polar)