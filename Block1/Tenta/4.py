import numpy as np

# Givet
a = 4.57 #m
b = 12.5 #m
gammaY = 42.5 # grader

# Beräkningar
cos = np.radians(gammaY)
c = np.sqrt(a**2+b**2-2*a*b*np.cos(cos))
area = a*b*np.sin(cos)/2



print (f"c = {c:.3g}m")
print(f"Area = {area:.3g} m2")


