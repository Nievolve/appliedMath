import cmath as cm
import numpy as np


z1 = complex(2,3)
z1 = complex(4,-1)


magnitute = 2
argument = 30 #grader
argumentRad = np.deg2rad(argument)
z = cm.rect(magnitute,argumentRad)

print(z)
print(f"{z.real:}")
print(f"{z.imag:.2g}")
